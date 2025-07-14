import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "toastify-js/src/toastify.css";

createApp(App).use(router).mount("#app");
