<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button type="submit">Login</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    login() {
      axios.post('/api/login', {
        username: this.username,
        password: this.password
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        localStorage.setItem('token', response.data.token);
        this.$router.push('/');
      })
      .catch(error => {
        this.error = error.response.data.error || 'Login failed!';
      }
      );
      axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`;
    }
  }
}
</script>

<style>
.error {
  color: red;
}
</style>
