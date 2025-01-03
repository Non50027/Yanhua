<template>
    <div>
        <b-form @submit.prevent="submitForm" class="input-group">
            <input type="file" class="form-control" @change="onFile">
            <input type="text" :v-bind="selectedFile.description">
            <b-button type="submit">上傳</b-button>
        </b-form>
        <!-- <div v-for="(item, index) in soundData" :key="index">
            <b-button >{{ item.name }}</b-button>
        </div> -->
        <div class="accordion" role="tablist">
            <div v-for="(item, index) in soundData" :key="index">
                <div>
                    <b-button v-b-toggle.collapse-1>{{ item.name }}</b-button>
                </div>
                <b-collapse id="collapse-1" accordion="my-accordion" role="tabpanel" visible>
                        <b-card>list[button]</b-card>
                </b-collapse>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, computed, onUpdated, onMounted, onBeforeMount } from 'vue'

const soundData= reactive({})
// 取得所有音效檔案資料
(()=>{
    axios.get('https://napi.yanhua.com.tw/sound/all-sound')
    .then(response => {
        Object.assign(soundData, response.data)
    })
    .catch(error => {
        console.log(error)
    })
})();
// 用來儲存上傳檔案資料
const selectedFile = reactive({
    file: null,
    name: null,
    description: null,
})
// 上傳的檔案存入 selectedFile
const onFile = (event) => {
    selectedFile.file = event.target.files[0]
    selectedFile.name = event.target.files[0].name
}
// 提交表單
const submitForm= ()=>{

const tempForm= new FormData()

tempForm.append('icon', selectedFile.file);
tempForm.append('name', selectedFile.name);
tempForm.append('description', selectedFile.description);

selectedFile.file= null
selectedFile.name= null
selectedFile.description= null

axios.post(`https://napi.yanhua.com.tw/sound/upload/`, {
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

</style>