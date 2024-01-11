<template>
  <div class="container">
    <h2 class="title">Register</h2>
    <form @submit.prevent="register" class="register-form">
      <input type="text" v-model="username" placeholder="Username" class="input-field"/>
      <input type="password" v-model="password" placeholder="Password" class="input-field"/>
      <button type="submit" class="submit-button">Register</button>
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
      register() {
        axios.post('/api/register', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push('/login');
        })
        .catch(error => {
          this.error = error.response.data.error || 'Registration failed!';
        }
        );
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

.register-form {
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
</style>