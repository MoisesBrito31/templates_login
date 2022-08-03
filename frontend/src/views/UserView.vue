<template>
    <div>
        tela de view do usuario
        <userview></userview>
    </div>
</template>

<script>
import userview from '@/components/user/view.vue'
export default {
    name: 'UserView',
    components:{
        userview
    }
}
</script>