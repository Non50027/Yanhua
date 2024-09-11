<template>
    <BContainer>
        <BRow>
            <BCol>
                <img :src='data.icon' class="icon img-thumbnail">
            </BCol>
            <BCol>
                <div>
                    <label >商品名稱<br>{{ data.name }}</label>
                </div>
                <div>
                    <label >商品簡介<br>{{ data.introduction }}</label>
                </div>
                <div>
                    <label >價格<br>{{ data.price }}</label>
                </div>
            </BCol>
        </BRow>
        <div>
            <label >商品詳細<br>{{ data.description }}</label>
        </div>
        <BRow>
            <BCol>
                <label >庫存數量<br>{{ data.stock }}</label>
            </BCol>
            <BCol>
                <label >開始販售日期<br>{{ data.date }}</label><br>
            </BCol>
        </BRow>
        {{ data.photos }} 
    </BContainer>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref, reactive, computed, onUpdated, onMounted, onBeforeMount } from 'vue'
const props= defineProps({
    data: {
        type: Object,
        default: ()=>{
            let route= useRoute()
            return JSON.parse(decodeURIComponent(route.query.data))
        }
    }
})
// 載入前執行
onBeforeMount(()=>{
    console.log(props.data)
});
// 載入後執行
onMounted(()=>{

});
// 資料更新後執行
onUpdated(()=>{

});

</script>

<style scoped>
/* 自訂表單內容樣式 */
.icon {
    max-width: 500px;
    max-height: 500px;
    width: auto;
    height: auto;
}
</style>