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
import login from '../member/login.vue'
import { getMemberData } from '../services/getData';
import { ref, reactive, computed, onBeforeMount } from 'vue'
const isLogin= ref(sessionStorage.getItem('name'))  // 判斷登入
const memberData= reactive({})  // 會員資料
// const props= defineProps({
//     memberData:Object,
//     optionsData:Object
// })
const tempFormData= reactive({})    // 宣告表單
const table= reactive([])   // 宣告表格
const shoppingCartItems= reactive(JSON.parse(sessionStorage.getItem('shoppingCartItems'))|| [])  // 購物車
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
    shoppingCartItems.forEach((item)=>{
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
    return shoppingCartItems.reduce((total, item)=> total+item.price*item.num, 0)
})
// 表單提交
const submitForm = () => {
    // 判斷信箱驗證
    if (!memberData.verification){
        alert('請先驗證信箱');
        return;
    }
    // 構建要提交的資料
    const orderData = {
        member: memberData,
        addressee: tempFormData.name,
        tel: tempFormData.tel,
        address: tempFormData.address,
        total_amount: total.value,
        items: data.map(item => ({
            product: item,
            count: item.num
        }))
    };
    // 提交表單
    axios.post(`${import.meta.env.VITE_BACKEND}/order/add/`, orderData)
    .then(response => {
        location.reload()
        alert(response.data['message'])
        location.href = '/shop'
        console.log('成功提交：', response.data['data'])
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