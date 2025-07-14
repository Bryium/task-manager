<template>
  <div class="login-container">
    <h2>Welcome to Task Manager</h2>
    <p>Please continue as your appropriate role</p>

    <div class="role-buttons">
      <button @click="handleAdmin" class="role-btn admin">
        Continue as Admin
      </button>
      <button @click="handleUser" class="role-btn user">
        Continue as User
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useRouter } from "vue-router";
import { showToast } from "../utils/toast";

const router = useRouter();

const handleAdmin = () => {
  showToast("Welcome Admin");
  router.push("/admin");
};

const handleUser = () => {
  showToast("Welcome User");
  router.push("/user");
};
</script>

<style scoped>
.login-container {
  background-color: #fff;
  padding: 2.5rem;
  border-radius: 16px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
  margin: 5rem auto;
}

.login-container h2 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #111827;
}

.login-container p {
  color: #6b7280;
  font-size: 0.95rem;
  margin-bottom: 2rem;
}

.role-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.role-btn {
  padding: 0.8rem;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.role-btn.admin {
  background-color: #10b981;
  color: white;
}

.role-btn.admin:hover {
  background-color: #059669;
}

.role-btn.user {
  background-color: #3b82f6;
  color: white;
}

.role-btn.user:hover {
  background-color: #2563eb;
}

/* Responsive Styling */
@media screen and (max-width: 480px) {
  .login-container {
    padding: 1.5rem;
    margin: 2rem 1rem;
  }

  .login-container h2 {
    font-size: 1.5rem;
  }

  .role-btn {
    font-size: 0.95rem;
    padding: 0.7rem;
  }
}
</style>
