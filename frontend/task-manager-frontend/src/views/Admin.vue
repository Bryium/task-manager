<template>
  <div class="admin">
    <h2>Admin Dashboard</h2>

    <UserForm />
    <TaskForm />
    <AdminTaskList />
  </div>
</template>

<script lang="ts" setup>
import TaskForm from "../components/TaskForm.vue";
import UserForm from "../components/UserForm.vue";
import AdminTaskList from "../components/AdminTaskList.vue";
</script>

<style scoped>
.admin {
  max-width: 700px;
  margin: auto;
  padding: 2rem;
}
</style>
