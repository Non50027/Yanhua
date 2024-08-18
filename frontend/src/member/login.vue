<template>
    <!-- <div v-if="!isLogin">     -->
    <div >    
        <h2>{{isRegistered? "創建我的命名牌":"尋找我的命名牌"}}</h2>
        <form @submit.prevent="submitForm">
            <div>
                <label for="name">帳號：</label>
                <input type="text" v-model="formData.name" name="name" required />
                <p v-if="errors.name">{{ errors.name }}</p>
            </div>
            <div v-if="isRegistered">
                <label for="email">電子郵件：</label>
                <input type="email" v-model="formData.email" name="email" required/>
                <p v-if="errors.email">{{ errors.email }}</p>
            </div>
            <div>
                <label for="password">密碼：</label>
                <input type="password" v-model="formData.password" name="password" required />
            </div>
            <div v-if="isRegistered">
                <label for="rePassword">再次輸入密碼：</label>
                <input type="password" v-model="formData.rePassword" name="rePassword" required/>
            </div>
            <p v-if="errors.password">{{ errors.password }}</p>
            <button type="submit" >提交</button>
        </form>
        <button @click='isRegistered= !isRegistered'>{{isRegistered ? '已經有了' : '成為小羊'}}</button>
        {{message}}
    </div>
</template>

<script setup>
import { ref, reactive, onUpdated } from 'vue'
import axios from 'axios'
import cookies from 'vue-cookies'
// 控制登入&註冊表單切換
const isRegistered= ref(false)
// 定義表單數據
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
// 父組件監聽事件
const emit = defineEmits(['login-success'])

// 表單提交處理函數
const submitForm = () => {
    // 初始化
    errors.name= null;
    errors.email= null;
    errors.password= null;
    let url= 'http://localhost:8000/member/'
    // 註冊
    if (isRegistered.value){
        url+= 'register/'
        if (formData.password!== formData.rePassword) {
            errors.password = '密碼不符';
            return;
        }
    // 登入
    }else{
        url+= 'login/'
    }
    // 通用判斷
    if (!/^[A-Za-z0-9_]{8,}$/.test(formData.name)){
        errors.name= '帳號至少需要 8 位且只能包含大小寫字母數字和底線'
        return
    }
    if (!/^[A-Za-z0-9_]{8,}$/.test(formData.password)){
        errors.password= '密碼至少需要 8 位且只能包含大小寫字母數字和底線'
        return
    }
    // 提交表單
    axios.post(url, formData)
    .then(response => {
        console.log('成功提交：', response.data)
        alert(`歡迎 ${response.data.message}`)
        // 儲存小羊的名子
        message.value= response.data.message
        // 設置 session 為小羊名子
        sessionStorage.setItem('name', formData.name)
        // 回應父組件
        emit('login-success')
    })
    .catch(error => {
        // 檢查回應中的錯誤信息
        if (Object.keys(error.response.data.error)[0]=='name') {
            errors.name = error.response.data.error.name[0];
        } if (Object.keys(error.response.data.error)[0]=='email') {
            errors.email = error.response.data.error.email[0];
        } else {
            errors.password = '發生錯誤';
        }
    })
}

</script>

<style scoped>

</style>>