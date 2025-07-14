<template>
  <div class="task-form">
    <h3>Assign New Task</h3>
    <form @submit.prevent="submitTask">
      <input v-model="title" placeholder="Task title" required />
      <textarea v-model="description" placeholder="Description"></textarea>
      <input v-model="deadline" type="date" required />
      <input
        v-model.number="userId"
        type="number"
        placeholder="User ID"
        required
      />
      <button type="submit">Assign</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { showToast } from "../utils/toast";

const title = ref("");
const description = ref("");
const deadline = ref("");
const userId = ref(1);

const submitTask = async () => {
  const res = await fetch("http://127.0.0.1:5000/api/tasks/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: title.value,
      description: description.value,
      deadline: deadline.value,
      user_id: userId.value,
    }),
  });

  if (res.ok) {
    showToast("Task assigned and user notified");
    title.value = "";
    description.value = "";
    deadline.value = "";
  } else {
    const err = await res.json();
    showToast(`Failed: ${err.error}`, "error");
  }
};
</script>

<style scoped>
.task-form {
  background-color: #fff;
  padding: 2rem;
  border-radius: 10px;
  margin-top: 2rem;
}
input,
textarea {
  width: 100%;
  margin: 0.5rem 0;
  padding: 0.75rem;
}
button {
  background: #27ae60;
  color: white;
  border: none;
  padding: 0.75rem;
  cursor: pointer;
  width: 100%;
}
button:hover {
  background-color: #219150;
}
</style>
