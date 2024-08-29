<template>
    <BForm class="mt-3" @submit.prevent="submitForm">
        <div class="input-group">
            <span class="input-group-text">信箱</span>
            <input 
            type="email" 
            class="form-control" 
            v-model="tempData.value" 
            :state="formatEmailState(tempData)"
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
import { ref, reactive, onBeforeMount } from 'vue'
import { getMemberData } from "../services/getData";
import { verificationEmail } from "../services/verificationEmail"
const tempData = reactive({
    value: '', 
    show:true,
    verification: false
});
const data= reactive({})
onBeforeMount(async()=>{
    Object.assign(data, await getMemberData(sessionStorage.getItem('name')))
    tempData.value= data.email
    tempData.verification = data.verification
});
 // 判斷 email 格式
const formatEmailState= (email)=>{
    return email==''? null: (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)?  true: false)
};
const submitForm = () => {
    tempData.show= true
    let temp= false

    const tempForm = new FormData();
    
    tempForm.append('name', sessionStorage.getItem('name'));
    tempForm.append('email', tempData.value|| '')
    
    if(tempData.value!= data.email){
        tempForm.append('verification', false)
        temp= true
    }
    axios.put(`${import.meta.env.VITE_BACKEND}/member/edit_data/`, tempForm)
    .then(response => {
        alert(response.data.message);
        if(temp){
            verificationEmail(data.name)
            temp= false
        }
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