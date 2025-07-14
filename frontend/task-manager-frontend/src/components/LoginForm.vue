<template>
  <div class="login-container">
    <h2>Login</h2>
    <p>Enter your correct details to access iMarketAfrica</p>
    <form class="login-form" @submit.prevent="login">
      <div class="input-group">
        <span class="icon">📧</span>
        <input v-model="email" type="email" placeholder="Enter email address" required />
      </div>
      <div class="input-group">
        <span class="icon">🔒</span>
        <input v-model="password" type="password" placeholder="Enter password" required />
      </div>
      <div class="forgot-password">
        <router-link to="/reset-password">Forgot Password?</router-link>
      </div>
      <button type="submit" class="login-btn">Login</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { showToast } from '../utils/toast'

const email = ref('')
const password = ref('')

const login = async () => {
  try {
    const res = await fetch('http://127.0.0.1:5000/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email.value, password: password.value }),
    })

    const data = await res.json()

    if (!res.ok || !data.success) {
      throw new Error(data.message || 'Login failed')
    }

    showToast('Login successful')
    // Optionally: store token or navigate
    // router.push('/dashboard') if using Vue Router
  } catch (err: any) {
    showToast(err.message, 'error')
  }
}
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
  margin-bottom: 1.5rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.input-group {
  display: flex;
  align-items: center;
  background-color: #f9fafb;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  padding: 0.6rem 0.75rem;
}

.input-group .icon {
  margin-right: 0.6rem;
  color: #6b7280;
  font-size: 1.1rem;
}

.input-group input {
  border: none;
  outline: none;
  width: 100%;
  background: transparent;
  font-size: 1rem;
  color: #111827;
}

.login-btn {
  padding: 0.8rem;
  background-color: #3b82f6;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s ease;
}

.login-btn:hover {
  background-color: #2563eb;
}

.forgot-password {
  margin-top: -0.5rem;
  text-align: right;
  font-size: 0.9rem;
}

.forgot-password a {
  text-decoration: none;
  color: #3b82f6;
}

.forgot-password a:hover {
  text-decoration: underline;
}
</style>
