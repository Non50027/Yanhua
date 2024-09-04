<template>
    <BContainer>
        <BRow>
            <BCol sm="12" md="6">
                <b-input-group prepend="編號" class="mb-3">
                    <BFormInput v-model="orderData.id" disabled></BFormInput>
                </b-input-group>
            </BCol>
            <BCol sm="7" md="6">
                <b-input-group prepend="日期" class="mb-3">
                    <BFormInput v-model="orderData.created_at" disabled></BFormInput>
                </b-input-group>
            </BCol>
            <BCol sm="5" md="4">
                <b-input-group prepend="狀態" class="mb-3">
                    <BFormInput v-model="orderData.status" disabled></BFormInput>
                </b-input-group>
            </BCol>
            <BCol sm="7" md="4">
                <b-input-group prepend="收件人" class="mb-3">
                    <BFormInput v-model="orderData.addressee" disabled></BFormInput>
                </b-input-group>
            </BCol>
            <BCol sm="5" md="4">
                <b-input-group prepend="金額" class="mb-3">
                    <BFormInput v-model="orderData.total_amount" disabled></BFormInput>
                </b-input-group>
            </BCol>
            <b-input-group prepend="地址" class="mb-3">
                <BFormInput v-model="orderData.address" disabled></BFormInput>
            </b-input-group>
            <b-input-group prepend="電話" class="mb-3">
                <BFormInput v-model="orderData.tel" disabled></BFormInput>
            </b-input-group>
        </BRow>
        <BTable bordered striped hover :items="orderItemsTable" ></BTable>
    </BContainer>
</template>

<script setup>
import { useRoute } from 'vue-router';
import axios from "axios"
import { ref, reactive, computed, onUpdated, onMounted, onBeforeMount } from 'vue'
// 載入前執行
onBeforeMount(()=>{
    // 接收URL參數
    let route= useRoute()
    let orderId= route.query.orderId
    getOrder(orderId)
});
// 載入後執行
onMounted(()=>{
    
});
// 資料更新後執行
onUpdated(()=>{
    
});
// 宣告訂單變數
const orderData= reactive({})
const orderItemsTable= reactive([])
// 取得訂單資料資料
const getOrder= (id)=>{
    axios.get(`${import.meta.env.VITE_BACKEND}/order/get/?id=${id}`)
    .then(response=> {{
        // console.log('shop', response.data)
        Object.assign(orderData, response.data)
        orderData.created_at= formatTime(orderData.created_at)
        orderData.items.forEach((item)=>{
            orderItemsTable.push({
                商品名: item.product.name,
                單價: item.product.price,
                數量: item.count,
                金額: item.price,
            })
        })
    }})
    .catch(error=> {
        alert(error.response.data.error)
        console.log('error', error)
    })
}
// 格式化時間
const formatTime= (time)=>{
    const date = new Date(time)
    // 格式化時間為"年-月-日 小時:分鐘:秒"
    const year = date.getFullYear()
    const month = String(date.getMonth() + 1).padStart(2, "0")
    const day = String(date.getDate()).padStart(2, "0")
    const hours = String(date.getHours()).padStart(2, "0")
    const minutes = String(date.getMinutes()).padStart(2, "0")
    const seconds = String(date.getSeconds()).padStart(2, "0")

    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
}
</script>

<style scoped>

</style>