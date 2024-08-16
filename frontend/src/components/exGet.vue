<template>

    <div>
        {{message}}
    </div>
    
</template>

<script setup>
import axios from "axios"
import { ref, onMounted } from 'vue'

const message= ref('123')

onMounted(() => {
    axios.get('http://127.0.0.1:8000/member/hello/')
    .then(response => {
      message.value = response.data.message;  // 正確地更新 message 的值
    })
    .catch(error => {
        console.error('There was an error!', error);
    });
})

</script>

<style scoped>

</style>