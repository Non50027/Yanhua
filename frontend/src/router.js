import { createRouter, createWebHistory } from 'vue-router'
import member from './member/member.vue'

const routes = [
    { 
        path: '/member/:name?/:uidb64?/:token?',
        component: member,
        props: true
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
