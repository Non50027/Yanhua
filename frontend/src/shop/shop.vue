<template>
    <div v-if="switchShow">
        <BButton class="mb-3 cart-button" pill @click.stop="isShopCart= !isShopCart" >購物車</BButton>
        <cart v-if="isShopCart" class="levitated-windows shopping-cart" :items="shopCartItems" ref="windowsRef" />
    </div>
    <div>        
        <BButton pill class="mb-3" v-if="(memberData.name && (memberData.role != 'member'))" @click="switchShow= !switchShow">{{switchShow?'新商品':'取消'}}</BButton>
        <add v-if="!switchShow" />
    </div>
    <BContainer v-if="switchShow">
        <BRow>
            <BCol v-for="(item, index) in shopData" :key="index">
                <BCard no-body class="mb-5 my-card" tag="article" border-variant="success" @click.stop="showDetailed(item)">
                    <BCardImg :src="item.icon" :alt="item.name"/>
                    <BCardBody>
                        <BCardTitle class="title">{{ item.name }}</BCardTitle>
                        <BCardText class="context">{{ item.introduction }}</BCardText>
                        <BCardText class="context price">{{ `$ ${item.price}` }}</BCardText>
                        <BRow>
                            <BCol><BCardText class="context">{{ `剩餘數量:${item.count}` }}</BCardText></BCol>
                            <BCol><BButton pill @click.stop="addShopCartItems(item)">加購物車</BButton></BCol>
                        </BRow>
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>
        <detailed v-if="selectedItem" class="levitated-windows detailed-windows" :data="selectedItem" ref="detailedRef" @close="closeDetailed" />
    </BContainer>
</template>

<script setup>
import { ref, reactive, onBeforeUnmount, onMounted, onBeforeMount } from 'vue'
import add from './add/add.vue'
import cart from './cart.vue'
import detailed from './detailed.vue'
import axios from "axios"
import { getMemberData } from '../services/getData';
const switchShow = ref(true)
const memberData = reactive({})
const isShopCart= ref(false)
const windowsRef = ref(null);
const detailedRef = ref(null);
const handleClickOutside = async(event) => {
    if (windowsRef.value && !windowsRef.value.$el.contains(event.target)) {
        isShopCart.value = false
    }
    if (detailedRef.value && detailedRef.value.$el && !detailedRef.value.$el.contains(event.target)) {
        closeDetailed();
    }
};
const selectedItem = ref(null);
// 顯示商品詳細資訊
const showDetailed = (item) => {
    selectedItem.value = item;
};
// 關閉商品詳細資訊
const closeDetailed = () => {
    selectedItem.value = null;
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
const shopData= reactive([]);
(()=>{
    axios.get(`${import.meta.env.VITE_BACKEND}/shop/get/`)
    .then(response=> {{
        // console.log('shop', response.data)
        Object.assign(shopData, response.data)
        shopData.forEach(item => {
            item.show= false;
        });
    }})
    .catch(error=> {
        alert(error.response)
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
    position: fixed;
    border-radius: 15px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    outline: none;
}
.shopping-cart{
    width: 500px;
    z-index: 1002;
}
.detailed-windows{
    width: 80%;
    z-index: 1001;
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