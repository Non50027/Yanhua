<template>
    <BNavbar fixed="top" toggleable="lg" class="my-navbar">
        <BNavbarBrand to="/">
            <img class="logo" :src=logoImg alt="Logo">
        </BNavbarBrand>
        
        <BCollapse id="nav-collapse" is-nav v-model="onSwitch">
            <BNavbarNav>
                <BNavItem v-if="isLogin" to="/member" @click="onSwitch= !onSwitch">
                    {{ memberData.display_name ? memberData.display_name : memberData.name }}
                </BNavItem>
                <BNavItem v-for="(item, index) in optionsData.Navigation" :key="index" :[isHref(item.link)]="item.link" @click="onSwitch= !onSwitch">
                    {{item.name}}
                </BNavItem>
                <BNavItem v-if="isAdmin" to="/admin" @click="onSwitch= !onSwitch">管理</BNavItem>
            </BNavbarNav>
        </BCollapse>
        <BButton pill v-if="!isLogin" @click.stop="onLogin= !onLogin" class="ms-auto">
            {{onLogin?'取消':'戴上命名牌'}}
        </BButton>
        <login v-if="onLogin" class="levitated-windows" ref="loginRef"/>
        <BNavbarToggle target="nav-collapse" />
    </BNavbar>
    <div class="router-content"><router-view :optionsData="optionsData" :memberData="memberData"/></div>
</template>

<script setup>
import { ref, onBeforeMount, onBeforeUnmount } from 'vue'
// 父組件傳來的資料
const props= defineProps({
    optionsData: Object,
    memberData: Object,
})
const isLogin = ref(!!sessionStorage.getItem('name'))   // 檢查登入狀態
const isAdmin= (isLogin && (props.memberData.role != 'member'))   // 判斷登入者為管理員
const loginRef= ref(null)
const logoImg= `${import.meta.env.VITE_STATIC}/image15.png`
// const isLogin= ref(false)
const handleClickOutside = (event) => {
    if (loginRef.value && !loginRef.value.$el.contains(event.target)) {
        onLogin.value = false
    }
};
// 控制登入表單的顯示
const onLogin= ref(false)
// 切換選單的收起
const onSwitch= ref(false)
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
  padding-top: 150px; /* 根據導航欄的高度調整 */
}
.logo {
    width: 172px;
}
</style>