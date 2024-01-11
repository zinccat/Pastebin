<template>
    <div>
      <h1>Pastebin</h1>
      <div v-for="paste in pastes" :key="paste.id">
        <p>{{ paste.content }}</p>
        <router-link :to="'/view/' + paste.id">View</router-link>
        <button @click="deletePaste(paste.id)">Delete</button>
      </div>
      <router-link to="/add">Add New Paste</router-link>
      <p v-if="message" class="message">{{ message }}</p>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        pastes: [],
        message: '',
        error: ''
      }
    },
    created() {
      axios.get('/api/pastes')
        .then(response => {
          this.pastes = response.data;
        });
    },
    
    methods: {
      deletePaste(id) {
        this.message = '';
        this.error = '';
        axios.delete('/api/pastes/' + id, {
        headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      })
          .then(() => {
            this.pastes = this.pastes.filter(paste => paste.id !== id);
          })
        .catch(error => {
            this.error = error.response.data.msg || 'An error occurred while deleting the paste';
        });
      }
    }
  }
  </script>
  
<style>
.error {
  color: red;
}
.message {
  color: green;
}
</style>
