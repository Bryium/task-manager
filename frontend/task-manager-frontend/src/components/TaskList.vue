<template>
  <div>
    <h3>My Tasks</h3>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <strong>{{ task.title }}</strong>
        <div class="progress-bar">
          <div :class="task.status.toLowerCase()" class="bar">
            {{ task.status }}
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue";

const tasks = ref<any[]>([]);

const fetchTasks = async () => {
  const userId = 1; // Change to actual user ID after login logic
  const res = await fetch(`http://127.0.0.1:5000/api/tasks/user/${userId}`);
  const data = await res.json();
  tasks.value = data;
};

onMounted(fetchTasks);
</script>

<style scoped>
.progress-bar {
  background: #eee;
  height: 20px;
  margin-top: 5px;
}
.bar {
  height: 100%;
  text-align: center;
  color: white;
}
.pending {
  background-color: gray;
  width: 33%;
}
.in\ progress {
  background-color: orange;
  width: 66%;
}
.completed {
  background-color: green;
  width: 100%;
}
</style>
