<template>
  <div id="app">
    <mainmenu></mainmenu>
    <b-container fluid>
      <router-view/>
    </b-container>
  </div>
</template>

<script>
import mainmenu from '@/components/main_menu.vue'
export default {
  components:{
    mainmenu
  }
}
</script>


