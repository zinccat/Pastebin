import Vue from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import AddPaste from '../components/AddPaste.vue'
import ViewPaste from '../components/ViewPaste.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/add',
      name: 'AddPaste',
      component: AddPaste
    },
    {
      path: '/view/:id',
      name: 'ViewPaste',
      component: ViewPaste
    }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
