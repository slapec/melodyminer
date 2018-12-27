<template>
    <div class="player">
        <div class="now-playing">
            Now playing: {{ media ? media.title : 'nothing' }}
        </div>
        <audio
            autoplay
            controls
            controlslist="nodownload"
            @timeupdate="progress"
            :src="media ? media.url : null"
        ></audio>
    </div>
</template>

<script>
    export default {
      props: ['media'],
      methods: {
        progress(e){
          console.log('Audio progress', e.target.currentTime);
        }
      }
    }
</script>

<style lang="scss" scoped>
    .player {
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        background: rgba(0, 0, 0, 0.1);
        padding: 4px;

        audio {
            width: 100%;
        }
    }

    .now-playing {
        text-align: center;
    }
</style>