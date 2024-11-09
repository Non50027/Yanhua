<template>
    <b-table :items="member_all_data" :fields="fields">
        <template #cell(verification)="data">
            {{ data.item.verification ? '已驗證' : '未驗證'}}
        </template>
        <template #cell(created_at)="data">
            {{ formatDate(data.item.created_at) }}
        </template>
        <template #cell(order)="data">
            <b-button variant="primary" @click="handleOrder(data.item)">
            查看訂單
            </b-button>
        </template>
    </b-table>
</template>

<script setup>
import axios from "axios";
import dayjs from 'dayjs';
import { ref, reactive, computed, onUpdated, onMounted, onBeforeMount } from 'vue'
const member_all_data= reactive([])
const fields = ref([
  { key: 'name', label: '帳號' },
  { key: 'display_name', label: '名稱' },
  { key: 'email', label: 'Email' },
  { key: 'verification', label: '驗證' },
  { key: 'address', label: '地址' },
  { key: 'tel', label: '電話' },
  { key: 'created_at', label: '建立日期' },
  { key: 'role', label: '角色' },
  { key: 'order', label: '訂單操作' }  // 訂單按鈕欄位
]);
// 載入前執行
onBeforeMount(()=>{
    axios.get(`${import.meta.env.VITE_BACKEND}/member/all-data`)
    .then(response=>{
        console.log(response.data)
        Object.assign(member_all_data, response.data)
    })
    .catch(error=>{
        console.log(error)
    })
});
// 處理訂單按鈕點擊事件
const handleOrder = (item) => {
  console.log('查看訂單：', item.order);
  // 這裡可以加入處理訂單的邏輯，比如跳轉到訂單詳情頁
};
// 使用 dayjs 格式化日期和時間
const formatDate = (dateString) => {
  return dayjs(dateString).format('YYYY-MM-DD HH:mm');
};
// 載入後執行
onMounted(()=>{

});
// 資料更新後執行
onUpdated(()=>{

});

</script>

<style scoped>

</style>