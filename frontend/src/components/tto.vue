<template>
    <div>
        <BButton pill class="mb-3" v-if="(memberData.name && (memberData.role != 'member'))" @click="switchShow= !switchShow">{{switchShow?'編輯模式':'退出'}}</BButton>
        <div v-for="(value, index) in ttoData" :key="index">
            <p>{{ value.title }} <BBadge pill variant="dark">{{ value.tag }}</BBadge></p>
            <p>{{value.value}}</p>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, onUpdated, onMounted, onBeforeMount } from 'vue'
const props= defineProps({
    optionsData: Object,
    memberData: Object,
})
const ttoData= props.optionsData['Derivative_work']
const switchShow= ref(true)
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

<style scoped>

</style>