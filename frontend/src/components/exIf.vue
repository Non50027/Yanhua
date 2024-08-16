<template>
    <div>
        <!-- 
        if 方法會選擇性的生成節點
        還有另一種 show 方法能夠先行生成所有節點
        之後利用 css 設置隱藏 
        -->

        <div>
            <button @click= "change(1)">type1</button>
            <button @click= "change(2)">type2</button>
            <button @click= "change(3)">type3</button>
        
        </div>

        <div class= 'type1' v-if= 'view== 1'>
            {{ test }}
        </div>

        <div class= 'type2' v-else-if= 'view== 2'>
            <input type="text" v-model="text">
            <p>{{text}}</p>
        </div>

        <div v-else>
            no view
        </div>

    </div>    

</template>

<script setup>
import { ref, onMounted } from 'vue'

const test= '烟花'
const text = ref('蹦蹦蹦')
const view= ref(1)
const change= (num)=> {
    view.value= num 
}

</script>

<style scoped>
.type1 {
    border: 2px rgb(235, 155, 235) solid;
}
.type2 {
    border: 2px rgb(109, 243, 214) solid;
}
</style>>

