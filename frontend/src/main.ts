import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap"; // Esto incluye el JS para botones, modales, etc.
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
