import { createRouter, createWebHistory } from 'vue-router'
import member from './member/member.vue'
import shop from './shop/shop.vue'
import cart from './shop/cart.vue'
import add from './shop/add/add.vue'
import create from './order/create.vue'
import get from './order/get.vue'
import go from './activity/go.vue'
import yanhua from './components/yanhua.vue'
import done from './components/done.vue'
import huh from './components/huh.vue'
import tto from './components/tto.vue'
import error from './components/error.vue'

const routes = [
    { 
        path: '/member/:name?/:uidb64?/:token?',
        component: member,
        props: true
    },
    { 
        path: '/shop',
        component: shop,
        children:[
            { 
                path: 'add',
                component: add,
            },
            { 
                path: 'cart',
                component: cart,
                params:{}
            }
        ]
    },
    { 
        path: '/order',
        name: 'order',
        component: create,
        // children:[
        //     { 
        //         path: 'get/:id',
        //         component: get,
        //         props: true
        //     }
        // ]
    },
    { 
        path: '/go',
        component: go,
    },
    { 
        path: '/yanhua',
        component: yanhua,
    },
    { 
        path: '/done',
        component: done,
    },
    { 
        path: '/huh',
        component: huh,
    },
    { 
        path: '/tto',
        component: tto,
    },
    // { 
    //     path: '/:pathMatch(.*)*',
    //     component: error,
    // },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
