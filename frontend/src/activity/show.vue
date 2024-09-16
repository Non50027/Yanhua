<template>
    <BContainer>
        <BLink v-if="isAdmin" to="create"><BButton pill class="mb-3">新活動</BButton></BLink>
        <div v-for="(data, index) in allActivityData" :key="index">
            {{ data }}
        </div>
    </BContainer>
</template>

<script setup>
import axios from "axios"
import { ref, reactive, onUpdated, onMounted, onBeforeMount } from 'vue'
const props= defineProps({
    options: Object,
    memberData: Object
})
const isAdmin= (sessionStorage.getItem('name') && (props.memberData.role != 'member'))   // 判斷登入者為管理員
// 取得所有活動資料
const allActivityData= reactive([]);
(()=>{
    axios.get(`${import.meta.env.VITE_BACKEND}/activity/get/`)
    .then(response=> {{
        // console.log('shop', response.data)
        Object.assign(allActivityData, response.data)
        allActivityData.forEach(item => {
            item.show= false;
        });
    }})
    .catch(error=> {
        alert(error.response)
        console.log('error', error)
    })
})();
// 載入前執行
onBeforeMount(()=>{

})
// 載入後執行
onMounted(()=>{

})
// 資料更新後執行
onUpdated(()=>{

})

</script>
