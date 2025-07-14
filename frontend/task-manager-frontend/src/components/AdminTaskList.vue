<template>
  <div class="task-list">
    <h3>Tasks Assigned by Admin</h3>
    <table v-if="tasks.length">
      <thead>
        <tr>
          <th>Task Name</th>
          <th>Assigned To</th>
          <th>Email</th>
          <th>Deadline</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in tasks" :key="task.id">
          <td>{{ task.title }}</td>
          <td>{{ task.user.name }}</td>
          <td>{{ task.user.email }}</td>
          <td>{{ formatDate(task.deadline) }}</td>
          <td :class="statusClass(task.status)">{{ task.status }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>No tasks found.</p>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue";
import axios from "axios";

// ✅ Define the task interface
interface Task {
  id: number;
  title: string;
  deadline: string;
  status: string;
  user: {
    name: string;
    email: string;
  };
}

// ✅ Assign the correct type to the ref
const tasks = ref([] as Task[]);

const fetchTasks = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:5000/api/tasks/");
    tasks.value = response.data;
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }
};

const formatDate = (dateStr: string) => {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
};

const statusClass = (status: string) => {
  switch (status) {
    case "Pending":
      return "status status-pending";
    case "In Progress":
      return "status status-progress";
    case "Completed":
      return "status status-completed";
    default:
      return "status";
  }
};

onMounted(fetchTasks);
</script>

<style scoped>
.task-list {
  margin-top: 2rem;
  overflow-x: auto;
}

/* Make table container scrollable on smaller screens */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
  min-width: 600px;
}

th,
td {
  padding: 0.75rem;
  border: 1px solid #ddd;
  text-align: left;
}

/* Status cell styling */
.status {
  font-weight: bold;
  padding: 0.5rem;
  border-radius: 5px;
  text-align: center;
}

.status-pending {
  background-color: #fff3cd;
  color: #856404;
}

.status-progress {
  background-color: #cce5ff;
  color: #004085;
}

.status-completed {
  background-color: #d4edda;
  color: #155724;
}

/* Responsive adjustments */
@media screen and (max-width: 768px) {
  table {
    display: block;
    overflow-x: auto;
  }

  .task-list {
    padding: 0 1rem;
  }

  th,
  td {
    white-space: nowrap;
  }
}
</style>
