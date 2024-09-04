<template>
    <div class="title mb-3">烟花蹦蹦蹦 ch.YanHua</div>
    <div v-for="(value, index) in baseData" :key="index">
        <p>{{ value[0] }}：{{ value[1] }}</p>
    </div>
    <div class="mb-3" v-html="introduction"></div>
    <div v-for="(value, index) in tagsData" :key="index">
        <p>{{ value[0] }} <BBadge pill variant="dark">{{value[1]}}</BBadge></p>
    </div>
</template>

<script setup>
import { ref, reactive, onUpdated, onMounted, onBeforeMount } from 'vue'
const props= defineProps({
    optionsData: Object,
    memberData: Object,
})
const baseData= props.optionsData['personal_data']['base']
const introduction= props.optionsData['personal_data']['Introduction'].replace(/\n/g, '<br>')
const tagsData= props.optionsData['personal_data']['Tags']
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
