<template>
    <div class="title">聊天室迷因</div>
    <div v-for="(value, index) in memeData['content']" :key="index">
        <img :src="value.imgUrl" alt="meme image">
        <p>{{ value.title }} <BBadge pill variant="dark">{{ value.tag }}</BBadge></p>
        <p>{{value.value}}</p>
    </div>
    <div class="title">精華迷因</div>
    <div v-for="(value, index) in memeData['video']" :key="index">
        <a :href="value.videoUrl"><img :src="value.iconUrl" alt="meme image"></a>
        <p>{{ value.title }} <BBadge pill variant="dark">{{ value.tag }}</BBadge></p>
        <p></p>
    </div>
</template>

<script setup>
import { ref, reactive, onUpdated, onMounted, onBeforeMount } from 'vue'
const props= defineProps({
    optionsData: Object,
    memberData: Object,
})
const memeData= props.optionsData['meme']
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
