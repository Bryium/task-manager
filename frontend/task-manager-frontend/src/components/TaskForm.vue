<template>
  <form @submit.prevent="assignTask">
    <input v-model="title" placeholder="Title" />
    <textarea v-model="description" placeholder="Description" />
    <input v-model="deadline" type="date" />
    <input v-model.number="userId" type="number" placeholder="User ID" />
    <button type="submit">Assign</button>
  </form>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { showToast } from "../utils/toast";

const title = ref("");
const description = ref("");
const deadline = ref("");
const userId = ref(1);

const assignTask = async () => {
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
    showToast("Task assigned");
    title.value = "";
    description.value = "";
    deadline.value = "";
  } else {
    showToast("Failed to assign task", "error");
  }
};
</script>
