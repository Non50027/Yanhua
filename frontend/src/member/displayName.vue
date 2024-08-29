<template>
    <BForm class="mt-3" @submit.prevent="submitForm">
        <div class="input-group">
            <span class="input-group-text">暱稱</span>
            <BFormInput type="text" class="form-control" v-model="tempData.value" :disabled="tempData.show" />
            <BButton v-if="tempData.show" @click="tempData.show= !tempData.show" >修改</BButton>
            <BButton v-if="!tempData.show" type="submit" >確定</BButton>
        </div>
    </BForm>
</template>

<script setup>
import axios from "axios"
import { reactive, onBeforeMount } from 'vue'
import { getMemberData } from "../services/getData";
const tempData = reactive({
    value: '', 
    show:true
});
const data= reactive({})
onBeforeMount(async ()=>{
    Object.assign(data, await getMemberData(sessionStorage.getItem('name')))
    tempData.value= data.display_name
});
const submitForm = () => {
    tempData.show= true
    
    const tempForm = new FormData();
    
    tempForm.append('name', sessionStorage.getItem('name'));
    tempForm.append('display_name', tempData.value|| '')
    
    axios.put(`${import.meta.env.VITE_BACKEND}/member/edit_data/`, tempForm)
    .then(response => {
        alert(response.data.message);
        console.log('Response:', response.data)
        // location.reload()
    })
    .catch(error => {
        // 處理錯誤
        alert('錯誤')
        console.log(error.response.data.error)
    });
};

</script>

<style scoped>

</style>