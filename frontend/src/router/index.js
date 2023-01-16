import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/LoginView.vue'
import Profile from '../views/UserView.vue'

Vue.use(VueRouter)

const routes = [
  { 
	path: '/',
	name: 'Home',
	component: Home, 
	meta:{'auth': true}
  },
  { 
    path: '/user/login',name: 'LoginView', 
    component: Login,
    meta:{'auth': false}
  },
  {
    path:'/user/profile',name: 'UserView',
    component: Profile,
    meta:{'auth': true}
  },
]

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes
})

router.beforeEach((to,from,next)=>{
  var logado = getCookie('logado')
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
