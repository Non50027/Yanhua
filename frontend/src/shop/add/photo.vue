<template>
    <BForm @submit.prevent="submitForm" >
        <img :src='data.icon' class="icon img-thumbnail" :alt="data.display_name? data.display_name: data.name">
        <div class="input-group mt-3">
            <input class="form-control" type="file" @change="onFileChange">
            <BButton pill type="submit" :disabled="!selectedFile.file">更新資料</BButton>
        </div>
    </BForm>
</template>

<script setup>
import axios from "axios"
import { getMemberData } from "../../services/getData";
import { ref, reactive, computed, onUpdated, onMounted, onBeforeMount } from 'vue'
const data= reactive({})
onBeforeMount(async ()=>{
    Object.assign(data, await getMemberData(sessionStorage.getItem('name')))
});
// 上傳圖片
const selectedFile = reactive({
    file: null,
    name: null,
})
const onFileChange = (event) => {
    selectedFile.file = event.target.files[0]
    selectedFile.name = event.target.files[0].name
}
const submitForm= ()=>{

    const tempForm= new FormData()
    
    tempForm.append('name', sessionStorage.getItem('name'));
    tempForm.append('icon', selectedFile.file)

    selectedFile.file= null
    selectedFile.name= null
    
    axios.put(`${import.meta.env.VITE_BACKEND}/member/edit_data/`, tempForm, {
        headers: {
        'Content-Type': 'multipart/form-data',
        },
    })
    .then(response => {
        alert(response.data.message);
        console.log('Response:', response.data)
        location.reload()
    })
    .catch(error => {
        // 處理錯誤
        alert('錯誤')
        console.log(error.response.data.error)
        
    });
}
</script>

<style scoped>
.icon {
    max-width: 200px;
    max-height: 200px;
    width: auto;
    height: auto;
}

</style>