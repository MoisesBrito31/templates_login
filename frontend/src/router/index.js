import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/',name: 'Home', component: Home, meta:{'auth': true} },
  { 
    path: '/user/login',name: 'LoginView', 
    component: () => import('../views/LoginView.vue'),
    meta:{'auth': false}
  },
  {
    path:'/user/profile',name: 'UserView',
    component: () => import('../views/UserView.vue'),
    meta:{'auth': true}
  },
]

const router = new VueRouter({
  routes
})

router.beforeEach((to,from,next)=>{
  var logado = getCookie('userid')
  console.log(logado) 
  if(to.meta.auth && logado==null){
    next('/user/login')
  }else{
    next()
  }
})

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

export default router
