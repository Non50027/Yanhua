import { createRouter, createWebHistory } from 'vue-router'
import member from './member/member.vue'
import activityShow from './activity/show.vue'
import activityCreate from './activity/create/create.vue'
import activityDetailed from './activity/detailed.vue'
import shopShow from './shop/show.vue'
import shopAddProduct from './shop/add/add.vue'
import ProductDetailed from './shop/detailed.vue'
import create from './order/create.vue'
import get from './order/get.vue'
import yanhua from './components/yanhua.vue'
import done from './components/done.vue'
import huh from './components/huh.vue'
import tto from './components/tto.vue'
import admin from './admin/admin-index.vue'
import admin_order from './admin/order-management.vue'
import admin_member from './admin/member-management.vue'
import sound from './components/sound.vue'
import error from './components/error.vue'

const routes = [
    { 
        path: '/member/:name?/:uidb64?/:token?',
        component: member,
        props: true
    },
    { 
        path: '/shop',
        children:[
            { 
                path: 'show',
                name: 'showAllProducts',
                component: shopShow,
            },
            { 
                path: 'add',
                name: 'editProducts',
                component: shopAddProduct,
            },
            { 
                path: 'detailed',
                name: 'detailedPage',
                component: ProductDetailed,
            },
        ]
    },
    { 
        path: '/order',
        children:[
            { 
                path: 'get',
                name: 'orderGet',
                component: get,
            },
            { 
                path: 'create',
                name: 'orderCreate',
                component: create,
            }
        ]
    },
    { 
        path: '/activity',
        children:[
            { 
                path: 'show',
                name: 'activityShow',
                component: activityShow,
            },
            { 
                path: 'create',
                name: 'activityCreate',
                component: activityCreate,
            },
            { 
                path: 'detailed',
                name: 'activityDetailedPage',
                component: activityDetailed,
            },
        ]
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
        path: '/sound',
        component: sound,
    },
    { 
        path: '/huh',
        component: huh,
    },
    { 
        path: '/tto',
        component: tto,
    },
    { 
        path: '/admin',
        name: 'admin-index',
        component: admin,
        children:[
            { 
                path: 'member',
                name: 'admin-member',
                component: admin_member,
            },
            { 
                path: 'order',
                name: 'admin-order',
                component: admin_order,
            },
        ]
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
