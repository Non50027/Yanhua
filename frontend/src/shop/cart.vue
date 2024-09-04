<template>
    <div tabindex="0">
        <BContainer >
            <BRow class="justify-content-md-center">
                <BCol md="1" />
                <BCol md="4">商品名稱</BCol>
                <BCol class="text-end">單價</BCol>
                <BCol class="text-center">數量</BCol>
                <BCol class="text-end">總金額</BCol>
            </BRow>
            <BRow v-for="(item, index) in items" :key="index">
                <BCol md="1"><BButton pill size="sm" variant="outline-danger" @click.stop="deleteItem(item)">-</BButton></BCol>
                <BCol md="4">{{ item.name }}</BCol>
                <BCol class="text-end">{{ item.price }}</BCol>
                <BCol><BFormInput class="text-end" type="number" v-model="item.num"/></BCol>
                <BCol class="text-end">{{ item.price*item.num }}</BCol>
            </BRow>
            <BRow align-v="end" >
                <BCol md="8"></BCol>
                <BCol><BLink :to="{name: 'orderCreate', query: {list: encodeURIComponent(JSON.stringify(rawItems()))}}" ><BButton size="sm" @click.stop>確定</BButton></BLink></BCol>
                <BCol class="total-price">${{ total }}</BCol>
            </BRow>
        </BContainer>
    </div>
</template>

<script setup>
import { toRaw } from 'vue';
import create from '../order/create.vue'
import { ref, reactive, computed, onUpdated, onMounted, onBeforeMount } from 'vue'
// 接收商品資料
const props= defineProps({
    items:{type: Array}
})
const rawItems= ()=>{
    return toRaw(props.items)
}
// 刪除購物車內物品
const deleteItem= (item)=>{
    let index= props.items.findIndex(element=> element.name===item.name)
    props.items.splice(index, 1)
}
// 計算總金額
const total= computed(()=>{
    return props.items.reduce((total, item)=> total+item.price*item.num, 0)
})
// 確認結帳
const onOrder= ref(false)
onMounted(()=>{
    
})
</script>
<style scoped>
.total-price{
    font-weight: bold;
    margin-top: 20px;
    text-align: right;
    color:rgb(255, 0, 0)
}
</style>