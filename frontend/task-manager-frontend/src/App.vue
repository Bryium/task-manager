<template>
  <div>
    <h1 style="text-align: center;">Task Manager Dashboard</h1>
    <TaskFormComponent />
    <TaskListComponent />
    <UserManagementComponent />
  </div>
</template>

<script>
import TaskFormComponent from './components/TaskFormComponent.vue';
import TaskListComponent from './components/TaskListComponent.vue';
import UserManagementComponent from './components/UserManagementComponent.vue';

export default {
  components: {
    TaskFormComponent,
    TaskListComponent,
    UserManagementComponent,
  },
};
</script>
