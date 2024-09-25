<template>
    <div>
      <BRow align-h="center">
        <BCol md="9">
          <navbar :optionsData="optionsData" :memberData="memberData" />
        </BCol>
        <BCol md="12">
          <home />
        </BCol>
      </BRow>
    
    </div>
  
</template>

<script setup>
import { ref, reactive, onBeforeMount  } from 'vue'
import axios from "axios"
import navbar from './control/navbar.vue'
import { getMemberData } from './services/getData';
const memberData= reactive({})  // 會員資料
const optionsData= reactive({}) // 設定檔
onBeforeMount (async ()=>{
  // 取得會員資料
  if (sessionStorage.getItem('name')){
    Object.assign (memberData, await getMemberData(sessionStorage.getItem('name')))
  }
});
// 取得設定檔
(()=>{
  axios.get(`${import.meta.env.VITE_BACKEND}/options/get`)
  .then(response => {
    Object.assign(optionsData, response.data)
  })
  .catch(error => {
    console.log(error)
  })
})();

</script>

<style>
.levitated-windows {
  position: fixed;
  border-radius: 15px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 1001;
  outline: none; /* 確保元素沒有默認的focus樣式 */
}
</style>