<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Username" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login() {
        axios.post('/api/login', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push('/');
        })
        .catch(error => {
          console.error(error);
          alert('Login failed!');
        });
      }
    }
  }
  </script>
  