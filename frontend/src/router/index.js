import { createWebHistory, createRouter } from 'vue-router'

import Login from "../pages/Login.vue";
import Main from "../pages/Main.vue";
import Settings from "../pages/Settings.vue";
import Users from "../pages/Users.vue";
import Grades from "../pages/Grades.vue";


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/login', component: Login, name: 'login-page' },
        { path: '/', component: Main, name: 'main-page' },
        { path: '/settings', component: Settings, name: 'settings-page' },
        { path: '/users', component: Users, name: 'users-page' },
        { path: '/grades', component: Grades, name: 'grades-page' },
    ]
})

export default router