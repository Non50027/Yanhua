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
                        <label >活動名稱</label>
                        <BFormInput type="text" v-model="data.title" required />
                    </div>
                    <div>
                        <label >活動地點</label>
                        <BFormInput type="text" v-model="data.address" required />
                    </div>
                    <div>
                        <label >活動網址</label>
                        <BFormInput type="text" v-model="data.url" required />
                    </div>
                </BCol>
            </BRow>
            <BRow class="mb-3">
                <label >活動詳細</label>
                <BFormTextarea v-model="data.description" rows="5" max-rows="10"></BFormTextarea>
            </BRow>
            <BRow class="mb-3">
                <BCol>
                    <label >活動開始日期</label>
                    <BFormInput type="date" v-model="data.start_date" />
                </BCol>
                <BCol>
                    <label >活動結束日期</label>
                    <BFormInput type="date" v-model="data.stop_date" />
                </BCol>
            </BRow>
            <label >活動照片</label>
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
const iconUrl= `${import.meta.env.VITE_STATIC}/product_icon.png`
const data= reactive({
    image: null,
    title: '',
    address: '',
    start_date: null,
    stop_date: null,
    description: '',
    url: '',
});
// 上傳圖片
const onFileChange = (event) => {
    data.image = event.target.files[0]
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
    axios.post(`${import.meta.env.VITE_BACKEND}/activity/add/`, data, {
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