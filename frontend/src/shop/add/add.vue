<template>
    <div>
        <BForm @submit.prevent="submitForm">
            <BRow>
                <BCol>
                    <img :src='iconUrl' class="icon img-thumbnail">
                    <label>封面</label>
                    <input class="form-control" type="file" @change="onFileChange">
                    <b-form-file v-model="data.icon" class="mt-3" plain></b-form-file>
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
            <div>
                <label >商品詳細</label>
                <BFormTextarea v-model="data.description" rows="5" max-rows="10"></BFormTextarea>
            </div>
            <BRow>
                <BCol>
                    <label >庫存數量</label>
                    <BFormInput type="number" v-model="data.stock" required />
                </BCol>
                <BCol>
                    <label >開始販售日期</label><br>
                    <input type="date" v-model="data.date" />
                </BCol>
            </BRow>
            <BButton pill type="submit">提交</BButton>
        </BForm>
    </div>
</template>

<script setup>
import { ref, reactive, onUpdated, onMounted, onBeforeMount } from 'vue'
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

})
// 載入後執行
onMounted(()=>{

})
// 資料更新後執行
onUpdated(()=>{

})
// 表單提交處理函數
const submitForm = () => {
    let tempForm= new FormData();
    
    if(data.icon){
        tempForm.append('icon', data.icon);
    }
    
    data.forEach((item) => {
        tempForm.append(item.DBkey, item.value);
    });
    // 提交表單
    axios.post(`${import.meta.env.VITE_BACKEND}/shop/add/`, tempForm, {
        headers: {
        'Content-Type': 'multipart/form-data',
        },
    })
    .then(response => {
        location.reload()
        console.log('成功提交：', response.data)
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