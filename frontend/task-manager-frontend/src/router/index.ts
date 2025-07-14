import { createRouter, createWebHistory } from "vue-router";
import AdminDashboard from "../views/AdminDashboard.vue";
import UserDashboard from "../views/UserDashboard.vue";

const routes = [
  { path: "/admin", component: AdminDashboard },
  { path: "/user", component: UserDashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
