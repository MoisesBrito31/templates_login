<template>
    <div>
        
    <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand href="#">
      <img class="mr-3" src="../assets/logo.png" width="120" height="40">
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item><router-link to="/">Home</router-link></b-nav-item>
        <b-nav-item><router-link to="/user/profile">Usuario</router-link></b-nav-item>
        <b-nav-item><router-link to="/user/login">Login</router-link></b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto mr-2" v-if="logado">
        <b-nav-item-dropdown right>
          <template #button-content>
            <em>
              Olá {{usuario}}
              <b-avatar badge="5" badge-variant="danger" :text="inicial" :src="avatar"></b-avatar>
            </em>
          </template>
          <div>
             <b-button @click="logout" variant="primary">sair</b-button>
          </div>
        </b-nav-item-dropdown>
      </b-navbar-nav>

    </b-collapse>
  </b-navbar>
    
</div>
</template>

<script>
export default {
    name:'mainmenu',
    created(){
      setInterval(()=>{
        this.logado = this.getCookie('userid')!=null
        this.usuario = this.getCookie('userid'),
        this.inicial = this.getCookie('inicial')
        this.avatar = `${this.$host}/media/${this.getCookie('avatar')}`
      },1000)
    },
    methods:{
      logout(){
        this.apagaCookies()
        document.location.href = '/#/user/login'
        this.logado=false
      },
      getImgUrl(pet,ext) {
        var images = ''
        if (ext =='png'){
            images = require.context('../assets/', false, /\.png$/)
            return images('./' + pet + ".png")
          }else if(ext=='jpg'){
             images = require.context('../assets/', false, /\.jpg$/)
              return images('./' + pet + ".jpg")
          }else{
            images = require.context('../assets/', false, /\.bmp$/)
              return images('./' + pet + ".bmp")
          }
        },
    },
    data(){
      return{
        logado: this.getCookie('sessionid')!=null,
        usuario: '',
        inicial: '',
        avatar: '', 
      }
    },
    computed:{
    },
    props:{
    },
}
</script>