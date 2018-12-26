<template>
  <div id="app">
    <!--<div id="nav">-->
      <!--<router-link to="/">Home</router-link> |-->
      <!--<router-link to="/about">About</router-link>-->
    <!--</div>-->
    <!--<router-view/>-->
    <h1>{{ title }}</h1>
    <audio v-if="file" :src="file" autoplay controls style="width: 100%"></audio>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        title: '',
        file: null
      }
    },
    async mounted(){
      const tracks = await fetch('/api/v1/media/audio/').then(r => r.json());
      this.title = tracks[0].title;
      this.file = tracks[0].url;
    }
  }
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
