<template>
  <div id="app">
    <navigation-bar></navigation-bar>
    <router-view/>
  </div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    NavigationBar
  },
  methods: {
    logout() {
      axios.post('/api/logout')
        .then(() => {
          this.$router.push('/login');
        })
        .catch(error => {
          console.error(error);
          alert('Logout failed!');
        });
    }
  }
}
</script>