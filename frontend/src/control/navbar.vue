<template>
    <BNavbar fixed="top" toggleable="lg" class="my-navbar">
        <BNavbarBrand href="/">
            <img src="http://localhost:8000/static/image15.png" alt="Logo">
        </BNavbarBrand>
        
        <BCollapse id="nav-collapse" is-nav v-model="onSwitch">
            <BNavbarNav>
                <BNavItem v-if="isLogin" to="/member" @click="onSwitch= !onSwitch">
                    {{ memberName }}
                </BNavItem>
                <BNavItem v-for="(item, index) in data.Navigation" :key="index" :[isHref(item.link)]="item.link" @click="onSwitch= !onSwitch">
                    {{item.name}}
                </BNavItem>
            </BNavbarNav>
        </BCollapse>
        <BButton pill v-if="!isLogin" @click.stop="onLogin= !onLogin" class="ms-auto">
            {{onLogin?'取消':'戴上命名牌'}}
        </BButton>
        <login v-if="onLogin" class="levitated-windows" ref="loginRef"/>
        <BNavbarToggle target="nav-collapse" />
    </BNavbar>
    <div class="router-content"><router-view /></div>
</template>

<script setup>
import { ref, onBeforeMount, onBeforeUnmount } from 'vue'
const loginRef= ref(null)
// const isLogin= ref(false)
const handleClickOutside = (event) => {
    if (loginRef.value && !loginRef.value.$el.contains(event.target)) {
        onLogin.value = false
    }
};
const onLogin= ref(false)
const onSwitch= ref(false)
// 父組件傳來的資料
defineProps({
    data: Object,
    memberName: String,
})
// 檢查登入狀態
const isLogin = ref(!!sessionStorage.getItem('name'))
// 判斷是否為外部連結
const isHref = (url) => {
    if(url.startsWith('http://') || url.startsWith('https://')){
        return 'href'
    }else{
        return 'to'
    };
};
// 載入前執行
onBeforeMount(async()=>{
    document.addEventListener('click', handleClickOutside);
})
// 卸載前執行
onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside);
});
</script>

<style scoped>
.my-navbar {
    background: #fff4fe;
}
.router-content {
  padding-top: 220px; /* 根據導航欄的高度調整 */
}
</style>