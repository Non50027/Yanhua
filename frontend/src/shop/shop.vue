<template>
    <BContainer>
        <div v-if="switchShow">
            <BButton class="mb-3 cart-button" pill @click.stop="isShopCart= !isShopCart" >購物車</BButton>
            <cart v-if="isShopCart" class="levitated-windows shopping-cart" :items="shopCartItems" ref="windowsRef" />
        </div>
        <div>        
            <BLink to="add">
                <BButton pill class="mb-3" v-if="(memberData.name && (memberData.role != 'member'))" @click="switchShow= !switchShow">{{switchShow?'新商品':'取消'}}</BButton>
            </BLink>
        </div>
        <b-input-group prepend="查詢訂單" class="mb-3">
            <BFormInput v-model="orderId"></BFormInput>
            <BLink :to="{ name: 'orderGet', query: { orderId: orderId } }"><BButton>搜尋</BButton></BLink>
        </b-input-group>
        <BRow v-if="switchShow" >
            <BCol v-for="(item, index) in shopData" :key="index" cols="12" md="6" xl="4">
                <BCard no-body class="mb-5 my-card" :class="onWindows" tag="article" border-variant="success" @click.stop="showDetailed(item)">
                    <BCardImg class="h-50" :src="item.icon" :alt="item.name"/>
                    <BCardBody class="h-25">
                        <BCardTitle class="title">{{ item.name }}</BCardTitle>
                        <BCardText class="context">{{ item.introduction }}</BCardText>
                        <BCardText class="context price">{{ `$ ${item.price}` }}</BCardText>
                        <BRow>
                            <BCol><BCardText class="context">{{ `剩餘數量:${item.count}` }}</BCardText></BCol>
                            <BCol class="d-md-none">
                                <BLink :to="{name: 'detailedPage', query:{data: encodeURIComponent(JSON.stringify(rawDetailedData(item)))}}">
                                    <BButton pill @click.stop>查看詳情</BButton>
                                </BLink>
                            </BCol>
                            <BCol><BButton pill @click.stop="addShopCartItems(item)">加購物車</BButton></BCol>
                        </BRow>
                    </BCardBody>
                    <template v-if="(memberData.name && (memberData.role != 'member'))" v-slot:footer>
                        <BRow>
                            <BCol>
                                <BLink :to="{name: 'editProducts', query:{detailedData: encodeURIComponent(JSON.stringify(rawDetailedData(item)))}}">
                                    <BButton pill @click.stop>編輯</BButton>
                                </BLink>
                            </BCol>
                            <BCol><BButton pill @click.stop>刪除</BButton></BCol>
                        </BRow>
                    </template>
                </BCard>
            </BCol>
        </BRow>
        <detailed v-if="selectedItem" class="levitated-windows detailed-windows d-none d-md-block" :data="selectedItem" ref="detailedRef" @close="closeDetailed" />
        
    </BContainer>
</template>

<script setup>
import { ref, reactive, computed, onBeforeUnmount, onMounted, onBeforeMount } from 'vue'
import add from './add/add.vue'
import cart from './cart.vue'
import detailed from './detailed.vue'
import axios from "axios"
import { getMemberData } from '../services/getData';
import { toRaw } from 'vue';
const orderId= ref('')
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
const rawDetailedData= (data)=>{
    return toRaw(data)
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
// 儲存設備銀幕寬度
const windowWidth = ref(window.innerWidth);
const handleResize = () => {
    windowWidth.value = window.innerWidth;
};
const onWindows= computed(()=> {
    if(windowWidth.value < 768){
        return 'small-card'
    }else{
        return 'normal-card'
    }
});
// 載入前執行
onBeforeMount(async()=>{
    window.addEventListener('resize', handleResize);
    document.addEventListener('click', handleClickOutside);
    if (!sessionStorage.getItem('name')){return}
    Object.assign(memberData, await getMemberData(sessionStorage.getItem('name')))
});
// 卸載前執行
onBeforeUnmount(() => {
    window.removeEventListener('resize', handleResize);
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
const shopCartItems= reactive(JSON.parse(sessionStorage.getItem('shopCart'))|| [])
const addShopCartItems= (item)=>{
    let index= shopCartItems.findIndex(element=> element.name===item.name)
    if(index===-1){
        item.num=1
        shopCartItems.push(item)
    }else{
        shopCartItems[index].num++
    }
    sessionStorage.setItem('shopCart', JSON.stringify(shopCartItems))
    // console.log('list', shopCartItems)
}
</script>

<style scoped>
.levitated-windows{
    position: fixed;
    border-radius: 15px;
    top: 50%;
    left: 50%;
    transform: translate(-50%);
    background-color: white;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    outline: none;
}
.detailed-windows{
    top: 275px;
    width: 80%;
    z-index: 1001;
}
.shopping-cart{
    width: 500px;
    z-index: 1002;
}
.cart-button {
    position: fixed;
    right: 5%;
    bottom: 15%;
    z-index: 1000;
}
.my-card{
    transition: all 0.3s ease;
}
/* 小螢幕時的卡片尺寸 */
.small-card {
    width: 360px;
}

/* 中等螢幕時的卡片尺寸 */
.normal-card {
    width: 270px;
    height: 500px;
}
</style>