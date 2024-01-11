<template>
    <div>
      <h2>Add Paste</h2>
      <form @submit.prevent="addPaste">
        <textarea v-model="content"></textarea>
        <button type="submit">Add</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        content: ''
      }
    },
    methods: {
      addPaste() {
        axios.post('/api/pastes', { content: this.content })
          .then(() => {
            this.$router.push('/');
          });
      }
    }
  }
  </script>
  