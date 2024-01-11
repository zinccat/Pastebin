<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input type="text" v-model="username" placeholder="Username" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Register</button>
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
      register() {
        axios.post('/api/register', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push('/login');
        })
        .catch(error => {
          console.error(error);
          alert('Registration failed!');
        });
      }
    }
  }
  </script>
  