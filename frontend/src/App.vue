<template>
    <div>
      <div>
        <button @click='showForm= !showForm'>{{isLogin? (showForm? (memberData.display_name? memberData.display_name: memberData.name): "返回"): (showForm? "不想戴":"戴上命名牌")}}</button>
        <login v-if="showForm && !isLogin" @login-success="isMember"></login>
        <member v-if="!showForm && isLogin" :data='memberData' />
      </div>
      <home />
    </div>

</template>

<script setup>
import { ref, reactive, onUpdated } from 'vue'
import axios from "axios"

const showForm = ref(false)
const isLogin = ref(!!sessionStorage.getItem('name'))
const memberData= reactive({})

onUpdated(()=>{
  const name= sessionStorage.getItem('name')
  axios.get(`http://localhost:8000/member/data/?name=${name}`)
  .then(response=> {{
    Object.assign(memberData, response.data)
  }})
  .catch(error=> {
    console.log(error)
  })
})

const isMember= ()=>{
  isLogin.value = !isLogin.value
  const name= sessionStorage.getItem('name')
  axios.get(`http://localhost:8000/member/data/?name=${name}`)
  .then(response=> {{
    Object.assign(memberData, response.data)
  }})
  .catch(error=> {
    console.log(error)
  })
}

</script>

<style>

</style>>

