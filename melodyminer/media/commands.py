# coding: utf-8

import asyncio
import hashlib
import logging
import sys
from pathlib import Path
from typing import TYPE_CHECKING, List

from tqdm import tqdm

from melodyminer.media.models import Audio

if TYPE_CHECKING:
    from argparse import Namespace


log = logging.getLogger(__name__)


async def import_(args: 'Namespace') -> int:
    paths: List[Path] = args.paths

    log.info('%s files will be imported', len(paths))
    has_conflict = False
    has_exception = False

    for path in paths:
        try:
            path = path.expanduser().resolve(strict=True)

            log.info('Importing %s', path)
            log.info('Calculating MD5 checksum')

            hasher = hashlib.md5()

            with path.open('rb') as f:
                with tqdm(total=path.stat().st_size, file=sys.stdout, unit='b', unit_scale=True) as t:
                    for chunk in iter(lambda: f.read(65535), b''):
                        hasher.update(chunk)
                        t.update(len(chunk))

                        # await asyncio.sleep(0)

            file_hash = hasher.hexdigest()
            log.info('Checksum: %s', file_hash)

            audio = await Audio.get(file_hash)
            if not audio:
                media_dir = Path(__file__).parent.parent.parent / 'media'
                audio_dir = media_dir / file_hash[:2] / file_hash[2:4]
                audio_path = audio_dir / path.name

                log.info('Audio file will be copied into %s', audio_path)
                audio_dir.mkdir(exist_ok=True, parents=True)

                with path.open('rb') as input_file, audio_path.open('wb') as output_file:
                    with tqdm(total=path.stat().st_size, file=sys.stdout, unit='b', unit_scale=True) as t:
                        for chunk in iter(lambda: input_file.read(65535), b''):
                            output_file.write(chunk)
                            t.update(len(chunk))

                            # await asyncio.sleep(0)

                audio = await Audio.create(
                    id=file_hash,
                    title=path.name,
                    path=str(audio_path)
                )

                log.info('Audio #%s has been created. Title: %s', audio.id, audio.title)

            else:
                log.error('File has already been imported. Title: %s', audio.title)
                has_conflict = True

        except Exception as e:
            log.exception('Import failure')
            has_exception = True

    return has_exception << 1 | has_conflict << 0
