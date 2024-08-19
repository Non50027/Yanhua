<template>
    <div class="container mt-5">
        <h2 class="mb-4">{{data.display_name? data.display_name: data.name}}</h2>
        <BForm @submit.prevent="submitImageForm">
            <img :src='data.icon' class="icon img-thumbnail" :alt="data.display_name? data.display_name: data.name">
            <div class="input-group mt-3" :key="selectedFile">
                <input class="form-control" type="file" @change="onFileChange" placeholder="讓我看看你的長相">
                <BButton type="submit" :disabled="!selectedFile.file">更新資料</BButton>
            </div>
        </BForm>

        <BForm v-for="(data, index) in formData" :key="index" class="mt-3" @submit.prevent="submitForm">
            <div class="input-group" :label="data.key">
                <span class="input-group-text">{{ data.key }}</span>
                <input :type="data.type" class="form-control" v-model="data.value" :id="data.id" :disabled="data.show"/>
                <BButton v-if="data.show" @click="data.show= !data.show">修改</BButton>
                <BButton v-if="!data.show" type="submit">確定</BButton>
            </div>
        </BForm>
        <div class="mt-3 mb-3">
            <label >成為小羊的那天：{{formatTime()}}</label>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, onBeforeMount, onUpdated } from 'vue'
import { useRoute } from 'vue-router'
import axios from "axios"
// 初始化資料
const data= reactive({})
const formData = reactive({
    display_name: {'key':'暱稱', 'value':'', 'show':true, 'id':'display_name', 'type':'text'},
    email: {'key':'信箱', 'value':'', 'show':true, 'id':'email', 'type':'email'},
    tel: {'key':'電話', 'value':'', 'show':true, 'id':'tel', 'type':'text'},
    address: {'key':'地址', 'value':'', 'show':true, 'id':'address', 'type':'text'},
})
const getMemberData= (name)=>{
    axios.get(`http://localhost:8000/member/data/?name=${name}`)
    .then(response=> {{
        Object.assign(data, response.data)
        formData.display_name.value= data.display_name
        formData.email.value= data.email
        formData.tel.value= data.tel
        formData.address.value= data.address
    }})
    .catch(error=> {
        console.log(error)
    })
}
onBeforeMount(()=>{
    verificationEmail()
})
onUpdated(()=>{
    getMemberData(sessionStorage.getItem("name"))
})
// 信箱驗證
const verificationEmail= ()=>{
    const route= useRoute()
    if (route.params.name== ''){
        getMemberData(sessionStorage.getItem("name"))
        return
    }else{
        sessionStorage.setItem("name", route.params.name)
        getMemberData(route.params.name)
    }
    const uidb64= route.params.uidb64
    const token= route.params.token
    
    axios.get(`http://localhost:8000/member/verification/${uidb64}/${token}`)
    .then(response=> {{
        alert(response.data.message)
    }})
    .catch(error=> {
        alert(error.response.data.error)
        console.log('error', error)
    })
}
// 格式化時間
const formatTime= ()=>{
    const date = new Date(data.created_at)
    // 格式化時間為"年-月-日 小時:分鐘:秒"
    const year = date.getFullYear()
    const month = String(date.getMonth() + 1).padStart(2, "0")
    const day = String(date.getDate()).padStart(2, "0")
    // const hours = String(date.getHours()).padStart(2, "0")
    // const minutes = String(date.getMinutes()).padStart(2, "0")
    // const seconds = String(date.getSeconds()).padStart(2, "0")

    // return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
    return `${year}-${month}-${day}`
}
// 上傳圖片
const selectedFile = reactive({
    file: null,
    name: null,
})
const onFileChange = (event) => {
    selectedFile.file = event.target.files[0]
    selectedFile.name = event.target.files[0].name
}
// 完成表單
const putForm= (tempForm)=>{
    axios.put('http://localhost:8000/member/edit_data/', tempForm, {
        headers: {
        'Content-Type': 'multipart/form-data',
        },
    })
    .then(response => {
        alert(response.data.message);
        console.log(response.data)
    })
    .catch(error => {
        // 處理錯誤
        if (Object.keys(error.response.data.error)[0]== 'tel'){
            alert('電話欄位不超過12碼')
        }else{
            alert('錯誤')
            console.log(error.response.data.error)
        }
    });
}
const submitImageForm= ()=>{
    console.log(sessionStorage.getItem('name'))
    const tempImageForm= new FormData()
    
    tempImageForm.append('name', sessionStorage.getItem('name'));
    tempImageForm.append('icon', selectedFile.file)

    selectedFile.file= null
    selectedFile.name= null
    
    putForm(tempImageForm)
}
const submitForm = () => {
    const tempForm = new FormData();

    
    tempForm.append('name', sessionStorage.getItem('name'));
    tempForm.append('display_name', formData.display_name.value|| '')
    tempForm.append('email', formData.email.value|| '')
    tempForm.append('tel', formData.tel.value|| '')
    tempForm.append('address', formData.address.value|| '')

    if(formData.email.value!= data.email){
        tempForm.append('verification', false)
        // 寄送驗證信件
        console.log('temp', formData.email.value)
        axios.post('http://localhost:8000/member/verification/', tempForm)
        .then(response => {
            alert(response.data.message);
            console.log(response.data)
        })
        .catch(error => {
            alert('錯誤')
            console.log(error.response.data.error)
        });
    }

    formData.display_name.show= true
    formData.tel.show= true
    formData.address.show= true
    
    putForm(tempForm);
};
</script>

<style scoped>
.icon {
    max-width: 200px;
    max-height: 200px;
    width: auto;
    height: auto;
}
</style>