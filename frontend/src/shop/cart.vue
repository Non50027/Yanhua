<template>
    <div tabindex="0">
        <BContainer>
            <div>
                <BRow class="justify-content-md-center">
                    <BCol class="d-none d-sm-block"/>
                    <BCol >商品</BCol>
                    <BCol class="text-end">單價</BCol>
                    <BCol class="text-center">數量</BCol>
                    <BCol class="text-end d-none d-sm-block">總金額</BCol>
                </BRow>
                <BRow class="justify-content-md-center" v-for="(item, index) in shoppingCartItems" :key="index">
                    <BCol class="d-none d-sm-block"><BButton pill size="sm" variant="outline-danger" @click.stop="deleteItem(item)">-</BButton></BCol>
                    <BCol >{{ item.name }}</BCol>
                    <BCol class="text-end">{{ item.price }}</BCol>
                    <BCol ><BFormInput class="text-end" type="number" v-model="item.num"/></BCol>
                    <BCol class="text-end d-none d-sm-block">{{ item.price*item.num }}</BCol>
                </BRow>
            </div>
            <BRow align-v="end" >
                <BCol md="8"></BCol>
                <BCol><BLink to="/order/create" ><BButton size="sm" @click.stop>確定</BButton></BLink></BCol>
                <BCol class="total-price">${{ total }}</BCol>
            </BRow>
        </BContainer>
    </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
const shoppingCartItems= reactive(JSON.parse(sessionStorage.getItem('shoppingCartItems'))|| [])  // 購物車
// 刪除購物車內物品
const deleteItem= (item)=>{
    let index= shoppingCartItems.findIndex(element=> element.name===item.name)
    shoppingCartItems.splice(index, 1)
    sessionStorage.setItem('shoppingCartItems', JSON.stringify(shoppingCartItems))
}
// 計算總金額
const total= computed(()=>{
    return shoppingCartItems.reduce((total, item)=> total+item.price*item.num, 0)
})
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