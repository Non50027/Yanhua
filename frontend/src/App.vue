<template>
    <div>
      <BNavbar toggleable="lg">
        <BNavbarBrand href="/">
          <img src="http://localhost:8000/static/image15.png" alt="Logo">
        </BNavbarBrand>


        <BCollapse id="nav-collapse" is-nav>
          <BNavbarNav>
            <BNavItem href="/member" @click="test= !test">
              <router-link to="/member" class="custom-link">
                {{memberData.display_name? memberData.display_name: memberData.name}}
              </router-link>
            </BNavItem>
            <BNavItem v-for="(items, index) in optionsData.Navigation" :key="index" :href="items.link" >
              <router-link :to="items.link" class="custom-link">
                {{items.name}}
              </router-link>
            </BNavItem>
          </BNavbarNav>
        </BCollapse>
        <BDropdown   v-if="!isLogin" no-caret class="ms-auto" >
          <template #button-content>
            <BButton  class="ms-auto">戴上命名牌</BButton>
          </template>
          <login @login-success="isMember"></login>
        </BDropdown>
        <BNavbarToggle target="nav-collapse"></BNavbarToggle>
      </BNavbar>
        <!-- <member v-if="isLogin" :data='memberData' /> -->

      <router-view />
      <home v-if='test'/>
    </div>
  
</template>

<script setup>
import { ref, reactive, onUpdated, onMounted } from 'vue'
import axios from "axios"

const test= ref(true)
const isLogin = ref(!!sessionStorage.getItem('name'))
const memberData= reactive({})
const optionsData= reactive({})

const getAllData= ()=>{
  axios.get('http://localhost:8000/options/get')
  .then(response=> {{
    Object.assign(optionsData, response.data)
    console.log('Options:', optionsData)
  }})
  .catch(error=> {
    console.log(error)
  })
  const name= sessionStorage.getItem('name')
  if (name=== null){return}
  axios.get(`http://localhost:8000/member/data/?name=${name}`)
  .then(response=> {{
    Object.assign(memberData, response.data)
  }})
  .catch(error=> {
    console.log(error)
  })
}
onUpdated(()=>{
  getAllData()
  
})
onMounted(()=>{
  getAllData()
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

<style scoped>
.custom-link {
  text-decoration: none; /* 移除底線 */
  color: #440000; 
}

.custom-link:hover {
  color: #9b6498; /* 可以設置懸停時的顏色 */
}
</style>>