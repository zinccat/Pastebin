import { setupAxios } from './plugins/axios';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App);
setupAxios(app);
app.use(router);
app.mount('#app');