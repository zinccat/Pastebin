<template>
  <div class="container">
    <h2>View Paste</h2>
    <div v-if="paste.content" class="paste-item">
      <p class="paste-content">{{ paste.content }}</p>
      <div class="actions">
        <!-- <router-link :to="'/edit/' + paste.id" class="edit-link">Edit</router-link> -->
        <button @click="deletePaste(paste.id)" class="delete-button">Delete</button>
        <button @click="copyPasteContent(paste.content)" class="copy-button">Copy</button>
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
      paste: {},
      message: '',
      error: ''
    }
  },
  created() {
    const id = this.$route.params.id;
    axios.get('/api/pastes/' + id)
      .then(response => {
        this.paste = response.data;
      })
      .catch(error => {
        this.error = 'An error occurred while fetching the paste.';
      });
  },
  methods: {
    deletePaste(id) {
      axios.delete('/api/pastes/' + id)
        .then(() => {
          this.$router.push('/');
        })
        .catch(error => {
          this.error = 'An error occurred while deleting the paste.';
        });
    },
    copyPasteContent(content) {
      navigator.clipboard.writeText(content)
        .then(() => {
          this.message = 'Copied to clipboard!';
        })
        .catch(err => {
          console.error('Failed to copy text: ', err);
        });
    }
  }
}
</script>

<style>
/* General Container Styles */
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

/* Titles and Headings */
.title,
h2 {
  text-align: center;
  color: #333;
}

/* Paste List and Individual Paste Item Styles */
.paste-list,
.paste-item {
  margin-top: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 8px;
}

/* Content of the Paste */
.paste-content {
  white-space: pre-wrap;
  word-wrap: break-word;
}

/* Button and Link Styles */
.actions,
.current-user {
  margin-top: 10px;
  text-align: center;
}

.view-link,
.edit-link,
.delete-button,
.copy-button,
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
  display: inline-block;
}

.view-link:hover,
.edit-link:hover,
.delete-button:hover,
.copy-button:hover,
.add-link:hover {
  background-color: #0056b3;
}

/* Error and Message Display */
.error,
.message {
  color: red;
  text-align: center;
  margin-top: 10px;
}

.message {
  color: green;
}

/* Logged-in User Display */
.current-user {
  font-size: 16px;
  margin-bottom: 20px;
}

/* Logout Link Style */
.current-user a {
  color: #007bff;
  text-decoration: none;
}

.current-user a:hover {
  text-decoration: underline;
}
</style>