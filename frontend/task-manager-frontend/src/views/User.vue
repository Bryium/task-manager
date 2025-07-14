<template>
  <div class="user">
    <h2>User Dashboard</h2>
    <UserDashboard />
  </div>
</template>

<script lang="ts" setup>
import UserDashboard from "../components/UserDashboard.vue";
</script>

<style scoped>
.user {
  max-width: 700px;
  margin: auto;
  padding: 2rem;
}
</style>
