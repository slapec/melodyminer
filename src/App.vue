<template>
    <div id="app">
        <playlist
                id="playlist-main"
                :api="'/api/v1/media/audio/'"
                @select="play"
        />
        <player
                id="player-main"
                :media="currentMedia"
        />
    </div>
</template>

<script>
  import Playlist from '@/components/Playlist.vue';
  import Player from '@/components/Player.vue';

  export default {
    components: {
      Playlist,
      Player
    },
    data(){
      return {
        currentMedia: null
      }
    },
    methods: {
      play(media){
        this.currentMedia = media;
      }
    }
  };
</script>

<style lang="scss">
    html, body {
        padding: 0;
        margin: 0;
    }

    #app {
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        overflow: hidden;
        box-sizing: border-box;
        display: flex;
        background: #e3e3e3;
        flex-direction: column;
    }

    #playlist-main {
        flex-grow: 1;
        overflow: auto;
    }

    #player-main {
        border-top: 2px solid black;
        flex-shrink: 0;
    }
</style>
