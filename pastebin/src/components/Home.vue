<template>
    <div>
      <h1>Pastebin</h1>
      <div v-for="paste in pastes" :key="paste.id">
        <p>{{ paste.content }}</p>
        <router-link :to="'/view/' + paste.id">View</router-link>
        <button @click="deletePaste(paste.id)">Delete</button>
      </div>
      <router-link to="/add">Add New Paste</router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        pastes: []
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
        axios.delete('/api/pastes/' + id)
          .then(() => {
            this.pastes = this.pastes.filter(paste => paste.id !== id);
          });
      }
    }
  }
  </script>
  