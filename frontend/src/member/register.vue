<template>
    <div v-if="!isLogin">    
        <h2>成為小羊</h2>
        <form @submit.prevent="submitForm">
            <div>
                <label for="name">帳號：</label>
                <input type="text" v-model="formData.name" name="name" required />
                <p v-if="errors.name">{{ errors.name }}</p>
            </div>
            <div>
                <label for="email">電子郵件：</label>
                <input type="email" v-model="formData.email" name="email" required />
                <p v-if="errors.email">{{ errors.email }}</p>
            </div>
            <div>
                <label for="password">密碼：</label>
                <input type="password" v-model="formData.password" name="password" required />
            </div>
            <div>
                <label for="rePassword">再次輸入密碼：</label>
                <input type="password" v-model="formData.rePassword" name="rePassword" required />
                <p v-if="errors.password">{{ errors.password }}</p>
            </div>
            <button type="submit" >提交</button>
        </form>
        {{message}}
    </div>
</template>

<script setup>
import { ref, reactive, onUpdated } from 'vue'
import axios from 'axios'
import cookies from 'vue-cookies'

// 定義響應式的表單數據
const formData = reactive({
    name: '',
    email: '',
    password: '',
    rePassword: ''
})

// 成功訊息
const message= ref('')

//錯誤訊息
const errors = reactive({
    name: null,
    email: null,
    password: null,
})
const emit = defineEmits(['login-success'])

// 表單提交處理函數
const submitForm = () => {
    errors.name= null;
    errors.email= null;
    errors.password= null;
    
    if (formData.password!== formData.rePassword) {
        errors.password = '密碼不符';
        return;
    }

    if (!/^[A-Za-z_]{8,}$/.test(formData.name)){
        errors.name= '帳號至少需要 8 位且只能包含大小寫字母和底線'
        return
    }
    if (!/^[A-Za-z_]{8,}$/.test(formData.password)){
        errors.password= '密碼至少需要 8 位且只能包含大小寫字母和底線'
        return
    }

    axios.post('http://127.0.0.1:8000/member/register/', formData)
    .then(response => {
        console.log('成功提交：', response.data)
        message.value= response.data.message
        sessionStorage.setItem('name', formData.name)
        emit('login-success')
    })
    .catch(error => {
      // 檢查回應中的錯誤信息
        if (Object.keys(error.response.data.error)[0]=='name') {
            errors.name = error.response.data.error.name[0];
        }if (Object.keys(error.response.data.error)[0]=='email') {
            errors.email = error.response.data.error.email[0];
        } else {
            console.log(error.response.data.error)
            errors.password = '發生未知錯誤';
        }
    })
}

</script>

<style scoped>

</style>>