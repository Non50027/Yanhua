<template>
  <div>

    <div>
      {{message}}
    </div>

    <div>
      <button @click= "change(1)">type1</button>
      <button @click= "change(2)">type2</button>
      <button @click= "change(3)">type3</button>
      
    </div>

    <div class= 'type1' v-if= 'view== 1'>
      
      <home></home>
      {{ test }}
    </div>

    <div class= 'type2' v-else-if= 'view== 2'>

      <input type="text" v-model="text">
      <p>{{text}}</p>
    </div>

    <div v-else>no view</div>

  </div>
  
</template>

<script setup>
import axios from "axios"
import { ref, onMounted } from 'vue'
import home from './components/home.vue'
const test= '烟花'
const text = ref('蹦蹦蹦')
const view= ref(1)
const change= (num)=> {
  view.value= num
}

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
.type1 {
  border: 2px rgb(235, 155, 235) solid;
}
.type2 {
  border: 2px rgb(109, 243, 214) solid;
}
</style>>

