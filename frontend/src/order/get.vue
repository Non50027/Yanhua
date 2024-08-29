<template>
{{ getOrder('202408293aae216') }}
</template>

<script setup>
import axios from "axios"
import { ref, reactive, computed, onUpdated, onMounted, onBeforeMount } from 'vue'
// 載入前執行
onBeforeMount(()=>{

});
// 載入後執行
onMounted(()=>{

});
// 資料更新後執行
onUpdated(()=>{

});
// 取得所有商品資料
const getOrder= (id)=>{
    axios.get(`${import.meta.env.VITE_BACKEND}/order/get/?id=${id}`)
    .then(response=> {{
        // console.log('shop', response.data)
        Object.assign(orderData, response.data)
    }})
    .catch(error=> {
        alert(error.response.data.error)
        console.log('error', error)
    })
}
</script>

<style scoped>

</style>