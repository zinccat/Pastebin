<template>
  <div>
    <h1>Create Paste</h1>
    <form @submit="createPaste">
      <textarea v-model="pasteContent" rows="5"></textarea>
      <button type="submit">Create Paste</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      pasteContent: '',
    };
  },
  methods: {
    createPaste() {
      axios
        .post('/api/pastes', { content: this.pasteContent })
        .then(response => {
          // Handle success
          console.log(response.data);
        })
        .catch(error => {
          // Handle error
          console.error(error);
        });
    },
  },
};
</script>

<style>
/* Add your CSS styles here */
</style>
