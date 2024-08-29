<template>
    <div v-if="switchShow">
        <BButton class="mb-3 cart-button" pill @click.stop="isShopCart= !isShopCart" >購物車</BButton>
        <cart v-if="isShopCart" class="levitated-windows" :items="shopCartItems" ref="shopCartRef" />
    </div>
    <div>        
        <BButton pill class="mb-3" v-if="(memberData.name && (memberData.role != 'member'))" @click="switchShow= !switchShow">{{switchShow?'新商品':'取消'}}</BButton>
        <add v-if="!switchShow" />
    </div>
    <BContainer v-if="switchShow">
        <BRow>
            <BCol v-for="(item, index) in shopData" :key="index">
                <BCard no-body class="mb-5 my-card" tag="article" border-variant="success">
                    <BCardImg :src="item.icon" :alt="item.name"/>
                    <BCardBody>
                        <BCardTitle class="title">{{ item.name }}</BCardTitle>
                        <BCardText class="context">{{ item.introduction }}</BCardText>
                        <BCardText class="context price">{{ `$ ${item.price}` }}</BCardText>
                        <BRow>
                            <BCol><BCardText class="context">{{ `剩餘數量:${item.count}` }}</BCardText></BCol>
                            <BCol><BButton pill @click="addShopCartItems(item)">加購物車</BButton></BCol>
                        </BRow>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>
    </BContainer>
</template>

<script setup>
import { ref, reactive, onBeforeUnmount, onMounted, onBeforeMount } from 'vue'
import add from './add/add.vue'
import cart from './cart.vue'
import axios from "axios"
import { getMemberData } from '../services/getData';
const switchShow = ref(true)
const memberData = reactive({})
const isShopCart= ref(false)
const shopCartRef = ref(null);
const handleClickOutside = (event) => {
    if (shopCartRef.value && !shopCartRef.value.$el.contains(event.target)) {
        isShopCart.value = false
    }
};
// 載入前執行
onBeforeMount(async()=>{
    document.addEventListener('click', handleClickOutside);
    if (!sessionStorage.getItem('name')){return}
    Object.assign(memberData, await getMemberData(sessionStorage.getItem('name')))
})
// 卸載前執行
onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside);
});
// 取得所有商品資料
const shopData= reactive({});
(()=>{
    
    axios.get(`${import.meta.env.VITE_BACKEND}/shop/get/`)
    .then(response=> {{
        // console.log('shop', response.data)
        Object.assign(shopData, response.data)
    }})
    .catch(error=> {
        alert(error.response.data.error)
        console.log('error', error)
    })
})();
const shopCartItems= reactive([])
const addShopCartItems= (item)=>{
    let index= shopCartItems.findIndex(element=> element.name===item.name)
    if(index===-1){
        item.num=1
        shopCartItems.push(item)
    }else{
        shopCartItems[index].num++
    }
    // console.log('list', shopCartItems)
}
</script>

<style scoped>
.levitated-windows{
    width: 500px;
    position: fixed;
    border-radius: 15px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    z-index: 1001;
    outline: none; /* 確保元素沒有默認的focus樣式 */
}
.cart-button {
    position: fixed;
    right: 5%;
    bottom: 15%;
    z-index: 1000;
}
.my-card{
    width: 300px;
    height: 500px;
}
</style>