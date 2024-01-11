<template>
    <nav class="navbar">
      <router-link to="/" class="nav-link">Home</router-link>
      <router-link to="/login" class="nav-link">Login</router-link>
      <router-link to="/register" class="nav-link">Register</router-link>
      <router-link to="/add" class="nav-link">Add Paste</router-link>
      <router-link to="/" class="nav-link" @click="logout">Logout</router-link>
    </nav>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'NavigationBar',
    data() {
      return {
        isLoggedIn: false
      };
    },
    created() {
      this.isLoggedIn = !!localStorage.getItem('token');
    },
    methods: {
      logout() {
        // Remove the token from local storage
        localStorage.removeItem('token');

        // Remove the Authorization header
        delete axios.defaults.headers.common['Authorization'];
      }
    }
  }
</script>

  
  <style>
  .navbar {
    background-color: #0056b3;
    overflow: hidden;
    display: flex;
    justify-content: center;
  }
  
  .nav-link {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    margin: 0 10px;
  }
  
  .nav-link:hover {
    background-color: #ddd;
    color: black;
  }
  </style>
  