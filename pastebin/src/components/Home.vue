<template>
    <div class="container">
      <h1 class="title">Pastebin</h1>
      <router-link to="/add" class="add-link">Add New Paste</router-link>
      <div class="paste-list">
        <div v-for="paste in pastes" :key="paste.id" class="paste-item">
          <p class="paste-content">{{ paste.content }}</p>
          <div class="actions">
            <router-link :to="'/view/' + paste.id" class="view-link">View</router-link>
            <button @click="deletePaste(paste.id)" class="delete-button">Delete</button>
          </div>
        </div>
      </div>
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
            this.error = "Permission denied"; //error.response.data.msg || 'An error occurred while deleting the paste';
        });
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
  
  .paste-list {
    margin-top: 20px;
  }
  
  .paste-item {
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 8px;
  }
  
  .paste-content {
    white-space: pre-wrap;
    word-wrap: break-word;
  }
  
  .actions {
    margin-top: 10px;
  }
  
  .view-link, .delete-button, .add-link {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    text-decoration: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    margin-right: 10px;
  }
  
  .view-link:hover, .delete-button:hover, .add-link:hover {
    background-color: #0056b3;
  }
  
  .error {
    color: red;
    text-align: center;
    margin-top: 10px;
  }
  
  .message {
    color: green;
    text-align: center;
    margin-top: 10px;
  }
  </style>
  