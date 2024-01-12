import { createRouter, createWebHashHistory } from 'vue-router'

// Lazy load components
const Home = () => import('../components/Home.vue')
const Login = () => import('../components/Login.vue')
const Register = () => import('../components/Register.vue')
const AddPaste = () => import('../components/AddPaste.vue')
const ViewPaste = () => import('../components/ViewPaste.vue')

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: { title: 'Pastebin' } // Add meta title for each route
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { title: 'Login' }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: { title: 'Register' }
  },
  {
    path: '/add',
    name: 'AddPaste',
    component: AddPaste,
    meta: { title: 'Add New Paste' }
  },
  {
    path: '/view/:id',
    name: 'ViewPaste',
    component: ViewPaste,
    meta: { title: 'View Paste' }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// Optional: Update document title based on route meta title
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Default Title';
  next();
});

export default router;
