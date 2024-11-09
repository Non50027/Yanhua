<template>
    <div>
        <b-button-group>
            <b-link  to="/admin/order"><b-button>訂單管理</b-button></b-link>
            <b-link to="/admin/member"><b-button>會員管理</b-button></b-link>
        </b-button-group>
    </div>
    <div class="router-content"><router-view /></div>
    
</template>

<script setup>
import { ref, reactive, onUpdated, onMounted, onBeforeMount } from 'vue'
const props= defineProps({
    optionsData: Object,
    memberData: Object,
})
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
