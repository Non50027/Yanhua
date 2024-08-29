<template>
    <BTable striped hover :items="table" ></BTable>
    <p class="total-price">$ {{ total }}</p>
    <login v-if="!isLogin" />
    <div v-if="isLogin">
        <BForm @submit.prevent="submitForm">
            <BRow>
                <BCol>
                    <label>收件人</label>
                    <BFormInput type="text" v-model="tempFormData.name" />
                </BCol>
                <BCol>
                    <label>信箱</label>
                    <BFormInput type="text" v-model="tempFormData.email" disabled/>
                </BCol>
            </BRow>
            <label>電話</label>
            <BFormInput type="text" v-model="tempFormData.tel"/>
            <label>地址</label>
            <BFormInput type="text" v-model="tempFormData.address"/>
            <BButton type="submit">確認結帳</BButton>
        </BForm>
    </div>
</template>

<script setup>
import axios from 'axios'
import { toRaw } from 'vue';
import login from '../member/login.vue'
import { getMemberData } from '../services/getData';
import { useRoute } from 'vue-router';
import { ref, reactive, computed, onUpdated, onMounted, onBeforeMount } from 'vue'
// 接收URL參數
const route= useRoute()
const data= reactive(route.query.list ? JSON.parse(route.query.list) : [])
// 判斷登入
const isLogin= ref(sessionStorage.getItem('name'))
// 會員資料
const memberData= reactive({})
// 宣告表單
const tempFormData= reactive({})
// 宣告表格
const table= reactive([])
// 載入前執行
onBeforeMount(async()=>{
    // 響應式表單資料
    if (isLogin){
        Object.assign(memberData, await getMemberData(sessionStorage.getItem('name')))
        tempFormData.name= memberData.display_name
        tempFormData.email= memberData.email
        tempFormData.tel= memberData.tel
        tempFormData.address= memberData.address
    }
    // 製作表格
    data.forEach((item)=>{
        table.push({
            商品名: item.name,
            數量: item.num,
            單價: item.price,
            金額: item.price * item.num
        })
    })
});
// 計算總金額
const total= computed(()=>{
    return data.reduce((total, item)=> total+item.price*item.num, 0)
})
// 表單提交
const submitForm = () => {
    // 判斷信箱驗證
    if (!memberData.verification){
        alert('請先驗證信箱');
        return;
    }
    // 宣告表單
    let tempForm= new FormData();
    // 宣告商品名列表
    let items_name=[]
    data.forEach((item)=>{
        items_name.push(item.name)
    })
    // 宣告商品數量列表
    let items_count=[]
    data.forEach((item)=>{
        items_count.push(item.num)
    })
    
    tempForm.append('member', memberData.name);
    tempForm.append('addressee', tempFormData.name);
    tempForm.append('tel', tempFormData.tel);
    tempForm.append('address', tempFormData.address);
    tempForm.append('total_amount', total.value);
    tempForm.append('items_name', items_name);
    tempForm.append('items_count', items_count);

    // 提交表單
    axios.post(`${import.meta.env.VITE_BACKEND}/order/add/`, tempForm)
    .then(response => {
        location.reload()
        alert(response.data['message'])
        console.log('成功提交：', response.data['data'])
        location.href = '/shop'
    })
    .catch(error => {
        console.log(error.response.data.error)
    })
}

</script>

<style scoped>
.total-price{
    font-weight: bold;
    margin-top: 20px;
    text-align: right;
    color:rgb(255, 0, 0)
}

</style>