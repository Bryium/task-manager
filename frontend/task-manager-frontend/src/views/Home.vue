<template>
  <div class="container">
    <h1>Welcome to Task Manager</h1>
    <LoginForm />
  </div>
</template>

<script lang="ts" setup>
import LoginForm from "../components/LoginForm.vue";
</script>

<style scoped>
.container {
  max-width: 500px;
  margin: auto;
  padding: 2rem;
  text-align: center;
}
</style>
