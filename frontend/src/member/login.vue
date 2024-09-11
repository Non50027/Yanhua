<template>
    <div>
        <BForm @submit.prevent="submitForm" @click.stop class="floating-form p-4">
            <h3 >{{isRegistered? "創建命名牌":"尋找命名牌"}}</h3>
            <div>
                <label for="name">帳號：</label>
                <BFormInput 
                    type="text" 
                    v-model="formData.name" 
                    name="name" 
                    :state="formatState(formData.name)"
                    pattern="^[A-Za-z0-9_]{8,}$" 
                    title="至少 8 位且只能包含大小寫字母、數字和底線" 
                    required />
                <b-form-invalid-feedback >
                    至少 8 位且只能包含大小寫字母數字和底線
                </b-form-invalid-feedback>
                <p v-if="errors.name" class="text-danger">{{ errors.name }}</p>
            </div>
            <div v-if="isRegistered">
                <label for="email">電子郵件：</label>
                <BFormInput 
                    type="email" 
                    v-model="formData.email" 
                    name="email" 
                    :state="formatEmailState(formData.email)"
                    required/>
                <b-form-invalid-feedback >
                    無效的電子郵件地址
                </b-form-invalid-feedback>
                <p v-if="errors.email" class="text-danger">{{ errors.email }}</p>
            </div>
            <div>
                <label for="password">密碼：</label>
                <BFormInput 
                    type="password" 
                    v-model="formData.password" 
                    name="password" 
                    :state="formatState(formData.password)" 
                    pattern="^[A-Za-z0-9_]{8,}$" 
                    title="至少 8 位且只能包含大小寫字母、數字和底線" 
                    required />
                <b-form-invalid-feedback >
                    至少 8 位且只能包含大小寫字母數字和底線
                </b-form-invalid-feedback>
            </div>
            <!-- :pattern="formData.password=== formData.rePassword" -->
            <div v-if="isRegistered">
                <label for="rePassword">再次輸入密碼：</label>
                <BFormInput 
                    type="password" 
                    v-model="formData.rePassword" 
                    name="rePassword"
                    required/>
            </div>
            <p v-if="errors.password" class="text-danger">{{ errors.password }}</p>
            <BButton pill type="submit" >提交</BButton>
            <BButton pill @click.stop='isRegistered= !isRegistered' variant="link">{{isRegistered ? '已經有命名牌了' : '成為小羊'}}</BButton>
        </BForm>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import axios from 'axios'
import { verificationEmail } from '../services/verificationEmail';
// 控制登入&註冊表單切換
const isRegistered= ref(false)
// 定義表單數據
const formData = reactive({
    name: '',
    email: '',
    password: '',
    rePassword: ''
})
//錯誤訊息
const errors = reactive({
    name: null,
    email: null,
    password: null,
})
// 判斷帳號密碼格式
const formatState= (value)=>{
    return value==''? null: (/^[A-Za-z0-9_]{8,}$/.test(value)? true: false)
}
 // 判斷 email 格式
const formatEmailState= (email)=>{
    return email==''? null: (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)?  true: false)
}
// 表單提交處理函數
const submitForm = () => {
    // 初始化
    errors.name= null;
    errors.email= null;
    errors.password= null;
    let url= `${import.meta.env.VITE_BACKEND}/member/`
    // 註冊
    if (isRegistered.value){
        // 驗證兩次密碼
        if (formData.password != formData.rePassword) {
            errors.password= '兩次密碼不一樣'
            return
        }
        url+= 'register/'
    // 登入
    }else{
        url+= 'login/'
    }
    // 提交表單
    axios.post(url, formData)
    .then(response => {
        console.log('成功提交：', response.data)
        // 設置 session
        sessionStorage.setItem('name', response.data.data.name)
        console.log('name', sessionStorage.getItem('name'))
        alert(`歡迎 ${response.data.message}`)
        // 寄送驗證信件
        if (isRegistered.value){verificationEmail(response.data.data.name)}
        location.reload()
    })
    .catch(error => {
        // 檢查回應中的錯誤信息
        if (Object.keys(error.response.data.error)[0]=='name') {
            errors.name = error.response.data.error.name[0];
        } if (Object.keys(error.response.data.error)[0]=='email') {
            errors.email = error.response.data.error.email[0];
        } else {
            if(error.response.data.error=='密碼不正確'){
                errors.password = '密碼不正確';
            }else{
                errors.password = '錯誤';
                console.log('error', error.response.data.error)
            }
        }
    })
}

</script>

<style scoped>
/* 自訂表單內容樣式 */
.text-danger {
    color: red;
}
</style>