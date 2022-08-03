<template>
    <div class="mt-4 pt-4">
        <div class="m-auto card col-sm-5 mb-5 p-3">
            <img :src="logo" width="200px"/>
            <login caminho="/user/login/" @logou="logou"></login>
        </div>
    </div>
</template>

<script>
import login from '@/components/login.vue'
export default {
    name:"LoginView",
    components:{
        login,
    },
    computed:{
        logo(){
            return this.getImgUrl("logo","png")
        }
    },
    methods:{
        logou(){
            document.location.href='/'
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
    }
}
</script>

<style>
body{
    /*background-image: url('https://picsum.photos/1024/480/?image=43');
    background-repeat: no-repeat;
    background-size:100%;
    background-size: cover;*/
}
</style>