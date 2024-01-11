<template>
  <div>
    <h2>Add Paste</h2>
    <form @submit.prevent="addPaste">
      <textarea v-model="content" placeholder="Enter your paste content here"></textarea>
      <button type="submit">Add</button>
    </form>
    <p v-if="message" class="message">{{ message }}</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

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
        'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      })
        .then(response => {
          this.message = 'Paste added successfully';
          this.content = ''; // Clear the textarea after successful submission
        })
        .catch(error => {
          this.error = error.response.data.msg || 'An error occurred while adding the paste';
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
