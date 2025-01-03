<template>
    <div>
        <h1>done</h1>
        <div v-for="(value, index) in optionsData['done']" :key="index">
            <a :href="value.link">
                <img :src="value.imgUrl" alt="link">
                <p>{{ value.name }}</p>
            </a>
        </div>
    </div>
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
