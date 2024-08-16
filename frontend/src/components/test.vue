<template>
    <dir>
        <p>msgCount: {{ msgCount}}</p>
        <!-- {{data}} -->
    </dir>
</template>

<script setup>
import { computed } from '@vue//reactivity'
import { watch } from 'vue'

// 接收父組件參數的方法
const data= defineProps({
    msg: {
        type: String,
        default: '123',
    }
})
// 使用父組件參數
const msgCount= computed(()=>{
    return data.msg.length
})

// 傳送到父組件
const emits= defineEmits(['update'])

watch( msgCount, (newValue)=>{
    emits('update', newValue)
})

</script>

<style scoped>

</style>