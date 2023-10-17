import { createRouter, createWebHistory } from 'vue-router'
import ProcessingQueue from "@/views/ProcessingQueue.vue";
import DBKeyWorkflow from "@/views/DBKeyWorkflow.vue";

const routes = [
    {
        path: '/',
        name: 'ProcessingQueue',
        component: ProcessingQueue
    },
    {
        path: '/workflow/:reportid',
        name:'Workflow',
        component: DBKeyWorkflow
    }
]
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})
export default router