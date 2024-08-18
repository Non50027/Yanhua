<template>
    <div>
        <h2>{{data.display_name? data.display_name: data.name}}</h2>
        <form @submit.prevent="submitForm">
            <div>
                <img :src='data.icon' class="icon" :alt="data.display_name? data.display_name: data.name">
                <input type="file" @change="onFileChange" />
            </div>
            <div>
                <label >暱稱：</label>
                <input type="text" v-model="displayName" />
            </div>
            <div>
                <label >電話：</label>
                <input type="text" v-model="tel" />
            </div>
            <div>
                <label >地址：</label>
                <input type="text" v-model="address" />
            </div>
            <div>
                <label >成為小羊的那天：{{formatTime()}}</label>
            </div>
            <button type="submit">更新資料</button>
        </form>
    </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from "axios"
// 父組件傳進來的會員資料
const props= defineProps({
    data:{
        type: Object,
    }
})
// 初始化表單資料
const name= sessionStorage.getItem('name')
const displayName= ref(props.data.display_name)
const tel= ref(props.data.tel)
const address= ref(props.data.address)
// 格式化時間
const formatTime= ()=>{
    const date = new Date(props.data.created_at)
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
const selectedFile = ref(null)

const onFileChange = (event) => {
    selectedFile.value = event.target.files[0]
}
// 完成表單
const submitForm = () => {
    const formData = new FormData();

    formData.append('name', name);
    formData.append('display_name', displayName.value)
    formData.append('tel', tel.value)
    formData.append('address', address.value)

    if (selectedFile.value) {
        formData.append('icon', selectedFile.value)
    }
    axios.put('http://localhost:8000/member/edit_data/', formData, {
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
        alert(error.message)
        console.log(error.message)
    });
};
onMounted(()=>{
    axios.get(`http://localhost:8000/member/data/?name=${name}`)
    .then(response=> {{
        console.log(sessionStorage.getItem('name'))
        Object.assign(props.data, response.data)
        console.log(response.data)
    }})
    .catch(error=> {
        console.log(error)
    })
})
</script>

<style scoped>
.icon {
    max-width: 200px;
    max-height: 200px;
    width: auto;
    height: auto;
}
</style>