<template>
  <div class="container">
    <h2 class="title">Login</h2>
    <form @submit.prevent="login" class="login-form">
      <input type="text" v-model="username" placeholder="Username" class="input-field"/>
      <input type="password" v-model="password" placeholder="Password" class="input-field"/>
      <button type="submit" class="submit-button">Login</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { getAuthHeader } from '../utils.js';

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
      axios.defaults.headers.common['Authorization'] = getAuthHeader();
    }
  }
}
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  text-align: center;
  color: #333;
}

.login-form {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input-field {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.submit-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.submit-button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  text-align: center;
  margin-top: 10px;
}
</style>