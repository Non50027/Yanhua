<template>

    <BButton class="mb-3 cart-button" pill @click.stop="shopCartButton= true" >購物車</BButton>
    <cart v-if="shopCartButton" class="levitated-windows" :class="setShoppingCartSize" ref="shoppingCartRef" />

    <BContainer>
        <BLink v-if="isAdmin" to="add"><BButton pill class="mb-3">新商品</BButton></BLink>

        <b-input-group prepend="查詢訂單" class="mb-3">
            <BFormInput v-model="findOrderId"></BFormInput>
            <BLink :to="{ name: 'orderGet', query: { orderId: findOrderId } }"><BButton>搜尋</BButton></BLink>
        </b-input-group>

        <BRow>
            <BCol v-for="(item, index) in allProductsData" :key="index" cols="12" md="6" xl="4">
                <BCard no-body class="mb-5 my-card" :class="setCardSize" tag="article" border-variant="success" @click.stop="showDetailed(item)">
                    <BCardImg class="h-50" :src="item.icon" :alt="item.name"/>
                    <BCardBody class="h-25">
                        <BCardTitle class="title">{{ item.name }}</BCardTitle>
                        <BCardText class="context">{{ item.introduction }}</BCardText>
                        <BCardText class="context price">{{ `$ ${item.price}` }}</BCardText>
                        <BRow>
                            <BCol><BCardText class="context">{{ `剩餘數量:${item.count}` }}</BCardText></BCol>
                            <BCol class="d-md-none">
                                <BLink :to="{name: 'detailedPage', query:detailedPageQuery(item)}">
                                    <BButton pill @click.stop>查看詳情</BButton>
                                </BLink>
                            </BCol>
                            <BCol><BButton pill @click.stop="addShoppingCartItems(item)">加購物車</BButton></BCol>
                        </BRow>
                    </BCardBody>
                    <template v-if="isAdmin" v-slot:footer>
                        <BRow>
                            <BCol><BLink :to="{name: 'editProducts', query: editProductQuery(item)}">
                                <BButton pill @click.stop>編輯</BButton>
                            </BLink></BCol>
                            <BCol><BButton pill @click.stop>刪除</BButton></BCol>
                        </BRow>
                    </template>
                </BCard>
            </BCol>
        </BRow>
        <detailed v-if="selectedItem" class="levitated-windows detailed-windows d-none d-md-block" :data="selectedItem" ref="detailedPageRef" @close="closeDetailed" />
    </BContainer>
</template>

<script setup>
import { ref, reactive, computed, onBeforeUnmount, onBeforeMount } from 'vue'
import cart from './cart.vue'
import detailed from './detailed.vue'
import axios from "axios"
import { toRaw } from 'vue';
// 父組件傳進來的資料
const props= defineProps({
    optionsData: Object,
    memberData: Object,
})
// 取得所有商品資料
const allProductsData= reactive([]);
(()=>{
    axios.get(`${import.meta.env.VITE_BACKEND}/shop/get/`)
    .then(response=> {{
        // console.log('shop', response.data)
        Object.assign(allProductsData, response.data)
        allProductsData.forEach(item => {
            item.show= false;
        });
    }})
    .catch(error=> {
        alert(error.response)
        console.log('error', error)
    })
})();
// 載入前執行
onBeforeMount(()=>{
    window.addEventListener('resize', handleResize);
    document.addEventListener('click', handleClickOutside);
});
const isAdmin= (sessionStorage.getItem('name') && (props.memberData.role != 'member'))   // 判斷登入者為管理員
const findOrderId= ref('')  // 要搜尋的訂單 ID
const jsonToUrl= (data)=>{return encodeURIComponent(JSON.stringify(toRaw(data)))} // 物件轉 Url 參數格式
const editProductQuery= (item)=>{return {detailedData: jsonToUrl(item)}}   // 編輯商品參數
const detailedPageQuery= (item)=>{return {data: jsonToUrl(item)}}   // 詳細資料參數
const shopCartButton= ref(false)    // 顯示購物車按鈕
const shoppingCartRef = ref(null)   // 購物車標籤元素
const detailedPageRef = ref(null)   // 詳細資料頁標籤元素
// 處理元素的點擊事件
const handleClickOutside = async(event) => {
    // 點到購物車以外就關閉購物車
    if (shoppingCartRef.value && !shoppingCartRef.value.$el.contains(event.target)) {
        shopCartButton.value = false
    }
    // 點到詳細資料頁以外就關閉詳細資料頁
    if (detailedPageRef.value && detailedPageRef.value.$el && !detailedPageRef.value.$el.contains(event.target)) {
        closeDetailed();
    }
};
const selectedItem = ref(null)  // 儲存點擊的商品詳細資訊
const showDetailed = (item) => {selectedItem.value = item}  // 顯示商品詳細資訊
const closeDetailed = () => {selectedItem.value = null} // 關閉商品詳細資訊
const onWindowWidth = ref(window.innerWidth)    // 儲存設備銀幕寬度
const handleResize = () => {onWindowWidth.value = window.innerWidth}// 偵測畫面的尺寸...判斷使用設備
// 根據銀幕寬度改變購物車懸浮窗大小
const setShoppingCartSize= computed(()=>{
    if(onWindowWidth.value < 768){
        return 'w-100'
    }else{
        return 'shopping-cart'
    };
})
// 根據銀幕寬度改變商品卡片格式
const setCardSize= computed(()=> {
    if(onWindowWidth.value < 768){
        return 'small-card'
    }else{
        return 'normal-card'
    }
});
const shoppingCartItems= reactive(JSON.parse(sessionStorage.getItem('shoppingCartItems'))|| [])  // 購物車
// 加入到購物車
const addShoppingCartItems= (item)=>{
    let index= shoppingCartItems.findIndex(element=> element.name===item.name)
    if(index===-1){
        item.num=1
        shoppingCartItems.push(item)
    }else{
        shoppingCartItems[index].num++
    }
    sessionStorage.setItem('shoppingCartItems', JSON.stringify(shoppingCartItems))
}
// 卸載前執行
onBeforeUnmount(() => {
    window.removeEventListener('resize', handleResize)
    document.removeEventListener('click', handleClickOutside);
});
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
    width: 700px;
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