<template>
    <div class="playlist">
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="media in mediaList"
                    :class="{playing: media.isPlaying}"
                    @click="play(media)"
                >
                    <td>{{ media.title }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
  export default {
    props: ['api'],
    data(){
      return {
        mediaList: []
      }
    },
    async mounted(){
      console.log('Fetching', this.api);

      this.mediaList = (await fetch(this.api).then(r => r.json())).map(media => {
        media.isPlaying = false;

        return media;
      });

      console.log('Fetched %s objects', this.mediaList.length);
    },
    methods: {
      play(media){
        this.mediaList.forEach(m => {
          m.isPlaying = m === media;
        });

        this.$emit('select', media);
      }
    }
  }
</script>

<style lang="scss" scoped>
    .playlist {
        display: flex;
        flex-direction: column;

        table {
            padding: 0;
            box-sizing: border-box;
            border-collapse: collapse;
            flex-grow: 1;
            table-layout: fixed;
            width: 100%;

            thead {
                position: sticky;
                top: 0;
                z-index: 999;

                tr {
                    th {
                        position: sticky;
                        top: 0;
                        z-index: 999;
                        background: #ccc;
                    }
                }
            }

            tbody {
                tr {
                    cursor: pointer;

                    &:hover {
                        background: rgba(0, 0, 0, 0.1);
                    }

                    &.playing {
                        background: rgba(100, 147, 49, 0.5);
                    }
                }
            }
        }
    }
</style>