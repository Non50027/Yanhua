<template>
    <div>
        <BForm @submit.prevent="submitForm">
            <BRow class="mb-3">
                <BCol>
                    <img :src='iconUrl' class="icon img-thumbnail">
                    <label>封面</label>
                    <input class="form-control" type="file" @change="onFileChange">
                </BCol>
                <BCol>
                    <div>
                        <label >商品名稱</label>
                        <BFormInput type="text" v-model="data.name" required />
                    </div>
                    <div>
                        <label >商品簡介</label>
                        <BFormTextarea v-model="data.introduction" rows="3" max-rows="6"></BFormTextarea>
                    </div>
                    <div>
                        <label >價格</label>
                        <BFormInput type="number" v-model="data.price" required />
                    </div>
                </BCol>
            </BRow>
            <BRow class="mb-3">
                <label >商品詳細</label>
                <BFormTextarea v-model="data.description" rows="5" max-rows="10"></BFormTextarea>
            </BRow>
            <BRow class="mb-3">
                <BCol>
                    <label >庫存數量</label>
                    <BFormInput type="number" v-model="data.stock" required />
                </BCol>
                <BCol>
                    <label >開始販售日期</label>
                    <BFormInput type="date" v-model="data.date" />
                </BCol>
            </BRow>
            <label >商品美照</label>
            <photo />
            <BButton pill type="submit">提交</BButton>
        </BForm>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref, reactive, onUpdated, onMounted, onBeforeMount } from 'vue'
import photo from './photo.vue'
import axios from 'axios'
const isToday= ref(true)
const iconUrl= `${import.meta.env.VITE_BACKEND}/static/product_photo/default_icon.png`
const data= reactive({
    icon: null,
    name: '',
    date: null,
    introduction: '',
    price: '',
    description: '',
});
// 上傳圖片
const onFileChange = (event) => {
    data.icon = event.target.files[0]
}
// 載入前執行
onBeforeMount(()=>{
    let route= useRoute() 
    if (route.query.detailedData!=undefined){
        Object.assign(data, JSON.parse(decodeURIComponent(route.query.detailedData)))
    }
})
// 載入後執行
onMounted(()=>{

})
// 資料更新後執行
onUpdated(()=>{

})
// 表單提交處理函數
const submitForm = () => {

    // 提交表單
    axios.post(`${import.meta.env.VITE_BACKEND}/shop/add/`, data, {
        headers: {
        'Content-Type': 'multipart/form-data',
        },
    })
    .then(response => {
        console.log('成功提交：', response.data)

        location.href= '/shop/show'
    })
    .catch(error => {
        console.log(error.response.data.error)
    })
}
</script>

<style>
/* 自訂表單內容樣式 */
.icon {
    max-width: 200px;
    max-height: 200px;
    width: auto;
    height: auto;
}
</style>