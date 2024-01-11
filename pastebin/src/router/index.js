import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import AddPaste from '../components/AddPaste.vue'
import ViewPaste from '../components/ViewPaste.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: Home },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/add', component: AddPaste },
    { path: '/view/:id', component: ViewPaste }
  ]
})
