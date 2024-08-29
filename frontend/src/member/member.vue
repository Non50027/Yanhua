<template>
    <div class="container mt-5">
        <div class="mt-3 mb-3">
            <h2>{{data.display_name? data.display_name: data.name}}</h2>
            <label v-if="!data.verification">信箱未驗證</label>
        </div>
        <iconForm :data="data" />
        <displayNameForm :data="data" />
        <emailForm :data="data" />
        
        <div class="mt-3 mb-3">
            <label >成為小羊的那天：{{formatTime()}}</label>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, onBeforeMount, onUpdated } from 'vue'
import { useRoute } from 'vue-router'
import axios from "axios"
import { getMemberData } from '../services/getData'
import iconForm from './icon.vue'
import displayNameForm from './displayName.vue'
import emailForm from './email.vue'
// 初始化資料
const data= reactive({})
const props= defineProps(['name', 'uidb64', 'token'])
onBeforeMount(async ()=>{
    // 取得會員資料
    Object.assign(data, await getMemberData(sessionStorage.getItem('name')||props.name))
});
// 信箱驗證進入點
(()=>{
    if (!props.name){return}

    sessionStorage.setItem('name', props.name)
    
    axios.get(`${import.meta.env.VITE_BACKEND}/verification/${props.uidb64}/${props.token}`)
    .then(response=> {{
        alert(response.data.message)
        location.href = '/member'
    }})
    .catch(error=> {
        alert(error.response.data.error)
        console.log('error', error)
    })
})();
// 格式化時間
const formatTime= ()=>{
    const date = new Date(data.created_at)
    // 格式化時間為"年-月-日 小時:分鐘:秒"
    const year = date.getFullYear()
    const month = String(date.getMonth() + 1).padStart(2, "0")
    const day = String(date.getDate()).padStart(2, "0")
    // const hours = String(date.getHours()).padStart(2, "0")
    // const minutes = String(date.getMinutes()).padStart(2, "0")
    // const seconds = String(date.getSeconds()).padStart(2, "0")

    // return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
    return `${year}-${month}-${day}`
}
</script>

<style scoped>
</style>