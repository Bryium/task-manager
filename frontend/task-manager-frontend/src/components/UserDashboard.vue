<template>
  <div class="header">
    <h3></h3>
    <button class="back-button" @click="$router.back()">← Back</button>
  </div>
  <div class="container">
    <!-- Login Screen -->
    <div v-if="!isAuthenticated" class="login-box">
      <h2>Welcome Back 👋</h2>
      <p>Please log in to view your tasks</p>
      <input
        v-model="email"
        type="email"
        placeholder="Email address"
        required
      />
      <input v-model="userId" type="text" placeholder="User ID" required />
      <button @click="loginUser">Login</button>
    </div>

    <!-- Task List Screen -->
    <div v-else class="task-box">
      <TaskList :user-id="userId" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import TaskList from "../components/TaskList.vue";
import Toastify from "toastify-js";
import "toastify-js/src/toastify.css";

const email = ref("");
const userId = ref("");
const isAuthenticated = ref(false);

async function loginUser() {
  if (!email.value || !userId.value) {
    Toastify({
      text: "Please enter both ID and Email!",
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#f44336",
    }).showToast();
    return;
  }

  try {
    const res = await fetch("http://127.0.0.1:5000/api/users/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email: email.value,
        user_id: userId.value,
      }),
    });

    const data = await res.json();

    if (res.ok) {
      isAuthenticated.value = true;
      Toastify({
        text: data.message || "Login successful!",
        duration: 3000,
        close: true,
        gravity: "top",
        position: "right",
        backgroundColor: "#4CAF50",
      }).showToast();
    } else {
      throw new Error(data.error || "Login failed");
    }
  } catch (error: any) {
    Toastify({
      text: error.message,
      duration: 3000,
      close: true,
      gravity: "top",
      position: "right",
      backgroundColor: "#f44336",
    }).showToast();
  }
}
</script>

<style scoped>
/* Base container */
.container {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  min-height: 100vh;
  padding: 1rem;
}

/* Login box */
.login-box {
  background-color: white;
  padding: 2rem 2.5rem;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.login-box h2 {
  margin-bottom: 0.5rem;
  color: #333;
}

.login-box p {
  margin-bottom: 1.5rem;
  color: #666;
}

.login-box input {
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
}

.login-box button {
  width: 100%;
  padding: 0.75rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

.login-box button:hover {
  background-color: #45a049;
}

/* Task display box (after login) */
.task-box {
  width: 100%;
  max-width: 700px;
  padding: 2rem;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.back-button {
  background-color: #6c757d;
  color: #fff;
  border: none;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  cursor: pointer;
}
.back-button:hover {
  background-color: #5a6268;
}
</style>
