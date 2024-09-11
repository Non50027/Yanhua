<template>
    <BForm class="mt-3" @submit.prevent="submitForm">
        <div class="input-group">
            <span class="input-group-text">信箱</span>
            <input 
            type="email" 
            class="form-control" 
            v-model="tempData.value" 
            :state="formatEmailState(tempData)"
            :placeholder="data.email"
            :disabled="tempData.show"/>
            <b-input-group-text><strong :class="data.verification? 'text-success': 'text-danger'">{{ data.verification? '已驗證': '未驗證' }}</strong></b-input-group-text>
            <b-form-invalid-feedback >
                無效的電子郵件地址
            </b-form-invalid-feedback>
            <BButton v-if="tempData.show" @click="tempData.show=!tempData.show" >修改</BButton>
            <BButton v-if="!tempData.show" type="submit" >確定</BButton>
        </div>
    </BForm>
</template>

<script setup>
import axios from "axios"
import { reactive, onBeforeMount } from 'vue'
import { verificationEmail } from "../services/verificationEmail"
// 傳入的資料
defineProps(['data'])
// 用來儲存表單內容
const tempData = reactive({
    value: '', 
    show:true, // 控制按鈕的狀態
    verification: false
});
 // 判斷 email 格式
const formatEmailState= (email)=>{
    return email==''? null: (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)?  true: false)
};
// 提交表單
const submitForm = () => {
    // 重製按鈕顯示
    tempData.show= true
    // 未修改就直接跳出
    if (!tempData.value){return}

    const tempForm = new FormData();
    
    tempForm.append('name', sessionStorage.getItem('name'));
    tempForm.append('email', tempData.value|| '')
    tempForm.append('verification', false)

    axios.put(`${import.meta.env.VITE_BACKEND}/member/edit_data/`, tempForm)
    .then(response => {
        alert(response.data.message);
        // 寄送驗證信
        verificationEmail(data.name)
        console.log('Response:', response.data)
        location.reload()
    })
    .catch(error => {
        alert('錯誤')
        console.log(error.response.data.error)
    });
};

</script>

<style scoped>

</style>