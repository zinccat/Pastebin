<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
      <button @click="logout">Logout</button>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios';

export default {
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

<style>
/* Add your CSS styling here */
</style>
