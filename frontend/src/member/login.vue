<template>
    <div>
        <BForm @submit.prevent="submitForm" @click.stop class="floating-form p-4">
            <h3 >{{isRegistered? "創建命名牌":"尋找命名牌"}}</h3>
            <div>
                <label for="name">帳號：</label>
                <BFormInput type="text" v-model="formData.name" name="name" required />
                <p v-if="errors.name" class="text-danger">{{ errors.name }}</p>
            </div>
            <div v-if="isRegistered">
                <label for="email">電子郵件：</label>
                <BFormInput type="email" v-model="formData.email" name="email" required/>
                <p v-if="errors.email" class="text-danger">{{ errors.email }}</p>
            </div>
            <div>
                <label for="password">密碼：</label>
                <BFormInput type="password" v-model="formData.password" name="password" required />
            </div>
            <div v-if="isRegistered">
                <label for="rePassword">再次輸入密碼：</label>
                <BFormInput type="password" v-model="formData.rePassword" name="rePassword" required/>
            </div>
            <p v-if="errors.password" class="text-danger">{{ errors.password }}</p>
            <BButton type="submit" >提交</BButton>
            <BButton @click.stop='isRegistered= !isRegistered' variant="link">{{isRegistered ? '已經有命名牌了' : '成為小羊'}}</BButton>
        </BForm>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
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
    // 通用判斷
    if (!/^[A-Za-z0-9_]{8,}$/.test(formData.name)){
        errors.name= '帳號至少需要 8 位且只能包含大小寫字母數字和底線'
        return
    }
    if (!/^[A-Za-z0-9_]{8,}$/.test(formData.password)){
        errors.password= '密碼至少需要 8 位且只能包含大小寫字母數字和底線'
        return
    }
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
        // 寄送驗證信件
        axios.post('http://localhost:8000/member/verification/', formData)
        .then(response => {
            alert(response.data.message);
            console.log(response.data)
        })
        .catch(error => {
            alert('錯誤')
            console.log(error.response.data.error)
        });
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
                console.log(error.response.data.error)
            }
        }
    })
}

</script>

<style scoped>
/* 自訂表單內容樣式 */
.floating-form {
  width: 300px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
  position: absolute; /* 絕對定位相對於按鈕 */
  top: -10px; /* 懸浮在按鈕下方 */
  right: 20px; /* 距離螢幕右邊界 10px */
  transform: translateY(10px); /* 稍微下移，使其看起來更自然 */
  z-index: 1000;
  padding: 20px;
  border: none;
}

.text-danger {
  color: red;
}
</style>>