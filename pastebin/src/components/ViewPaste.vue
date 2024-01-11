<template>
    <div>
      <h2>View Paste</h2>
      <p>{{ paste.content }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        paste: {}
      }
    },
    created() {
      const id = this.$route.params.id;
      axios.get('/api/pastes/' + id)
        .then(response => {
          this.paste = response.data;
        });
    }
  }
  </script>
  