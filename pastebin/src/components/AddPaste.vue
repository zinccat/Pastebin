<template>
  <div class="container">
    <h2 class="title">Add Paste</h2>
    <form @submit.prevent="addPaste" class="paste-form">
      <textarea v-model="content" placeholder="Enter your paste content here" class="textarea"></textarea>
      <button type="submit" class="submit-button">Add</button>
    </form>
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
      content: '',
      message: '',
      error: ''
    };
  },
  methods: {
    addPaste() {
      if (!this.content) {
        this.error = 'Content cannot be empty';
        return;
      }
      this.error = '';
      this.message = '';

      axios.post('/api/pastes', { content: this.content }, {
        headers: {
        'Authorization': getAuthHeader()
        }
      })
        .then(response => {
          this.message = 'Paste added successfully, redirecting to view paste...';
          this.content = ''; // Clear the textarea after successful submission
          setTimeout(() => {
            this.$router.push('/view/' + response.data.id);
          }, 1000);
        })
        .catch(error => {
          this.error = "Error" //error.response.data.msg || 'An error occurred while adding the paste';
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

.paste-form {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.textarea {
  width: 100%;
  min-height: 150px;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
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

.message {
  color: green;
  text-align: center;
  margin-top: 10px;
}
</style>