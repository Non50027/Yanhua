<template>
    <div >
      <div v-if="!isLoggedIn">
        <button @click='buttonLogin= !buttonLogin'>註冊</button>
        <register v-if="buttonLogin" :isLogin='buttonLogin' @login-success="handleLoginSuccess"></register>
      </div>
      <home />


      <!-- <input type="text" v-model= 'msg'>
      <br>
      <test :msg= 'msg' @update= 'updateHandler'></test> -->

    </div>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import home from './components/home.vue'
import register from './member/register.vue'

const buttonLogin = ref(false)
const isLoggedIn = ref(!!sessionStorage.getItem('name'))

const handleLoginSuccess = () => {
    isLoggedIn.value = !!sessionStorage.getItem('name')
}
// 傳送到子組件
// const msg= ref('')

// 從子組件接收
// const updateHandler= (data)=>{
//   console.log(data)
// }



</script>

<style>

</style>>

