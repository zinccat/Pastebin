<template>
  <div class="container">
    <h1 class="title">Pastebin</h1>
    <h4 v-if="currentUsername" class="current-user">
      Logged in as: <strong>{{ currentUsername }}</strong> (<router-link to="/login" @click="logout">Logout</router-link>)
    </h4>

    <router-link to="/add" class="add-link">Add New Paste</router-link>
    <div class="paste-list">
      <div v-for="paste in pastes" :key="paste.id" class="paste-item">
        <p class="paste-content">{{ paste.content }}</p>
        <div class="actions">
          <router-link :to="'/view/' + paste.id" class="view-link">View</router-link>
          <button @click="deletePaste(paste.id)" class="delete-button">Delete</button>
          <button @click="copyPasteContent(paste.content)" class="delete-button">Copy</button>
        </div>
      </div>
    </div>
    <p v-if="message" class="message">{{ message }}</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>
  
<script>
import axios from 'axios';
import { getAuthHeader } from '../utils.js';

export default {
  data() {
    return {
      pastes: [],
      message: '',
      error: '',
      currentUsername: ''
    }
  },
  created() {
    axios.get('/api/pastes', {
      headers: {
        'Authorization': getAuthHeader()
      }
    })
      .then(response => {
        this.pastes = response.data;
      })
      .catch(error => {
        this.error = 'An error occurred while fetching the pastes.';
      });

    axios.get('/api/username', {
      headers: {
        'Authorization': getAuthHeader()
      }
    })
      .then(response => {
        this.currentUsername = response.data.username;
      })
      .catch(error => {
        this.error = '';
      });
  },

  methods: {
    logout() {
      // Remove the token from local storage
      localStorage.removeItem('token');

      // Remove the Authorization header
      delete axios.defaults.headers.common['Authorization'];
    },
    deletePaste(id) {
      this.message = '';
      this.error = '';
      axios.delete('/api/pastes/' + id, {
        headers: {
          'Authorization': getAuthHeader()
        }
      })
        .then(() => {
          this.pastes = this.pastes.filter(paste => paste.id !== id);
        })
        .catch(error => {
          this.error = "Permission denied"; //error.response.data.msg || 'An error occurred while deleting the paste';
        });
    },
    copyPasteContent(content) {
      if (navigator.clipboard) { // Modern async clipboard API
        navigator.clipboard.writeText(content).then(() => {
          this.message = "Content copied to clipboard";
        }).catch(err => {
          console.error('Could not copy text: ', err);
          this.error = "Failed to copy";
        });
      } else { // Fallback for older browsers
        // Create a temporary textarea element
        const textArea = document.createElement('textarea');
        textArea.value = content;

        // Avoid scrolling to bottom
        textArea.style.top = "0";
        textArea.style.left = "0";
        textArea.style.position = "fixed";

        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
          document.execCommand('copy');
          this.message = "Content copied to clipboard";
        } catch (err) {
          console.error('Fallback: Could not copy text: ', err);
          this.error = "Failed to copy";
        }

        document.body.removeChild(textArea);
      }
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

.view-link,
.delete-button,
.add-link {
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

.view-link:hover,
.delete-button:hover,
.add-link:hover {
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
  