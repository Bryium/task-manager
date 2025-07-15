<template>
  <div class="task-list">
    <h3>My Tasks</h3>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <div class="task-header">
          <strong>{{ task.title }}</strong>
          <span>{{ task.deadline }}</span>
        </div>

        <div class="progress-bar">
          <div :class="['bar', statusClass(task.status)]">
            {{ task.status || "Unknown" }}
          </div>
        </div>

        <label>
          Update Status:
          <select v-model="task.status" @change="updateTaskStatus(task)">
            <option value="Pending">Pending</option>
            <option value="In Progress">In Progress</option>
            <option value="Completed">Completed</option>
          </select>
        </label>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch } from "vue";

const props = defineProps<{
  userId: string;
}>();

const tasks = ref<any[]>([]);

const fetchTasks = async () => {
  try {
    const res = await fetch(
      `https://task-manager-v4al.onrender.com/api/tasks/user/${props.userId}`
    );
    const data = await res.json();
    tasks.value = data;
  } catch (err) {
    console.error("Failed to fetch tasks:", err);
  }
};

onMounted(fetchTasks);
watch(() => props.userId, fetchTasks); // refetch if userId changes

const updateTaskStatus = async (task: any) => {
  try {
    const res = await fetch(
      `https://task-manager-v4al.onrender.com/api/tasks/${task.id}`,
      {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status: task.status }),
      }
    );

    if (!res.ok) {
      throw new Error("Failed to update task");
    }

    console.log(`Task ${task.id} updated to status: ${task.status}`);
  } catch (err) {
    console.error("Error updating task status:", err);
  }
};

const statusClass = (status: string | null | undefined): string => {
  if (!status) return "unknown";
  return status.toLowerCase().replace(" ", "-");
};
</script>

<style scoped>
.task-list {
  background: white;
  padding: 2rem;
  border-radius: 10px;
}
.task-header {
  display: flex;
  justify-content: space-between;
  font-size: 1rem;
}
.progress-bar {
  background: #eee;
  height: 20px;
  border-radius: 5px;
  margin: 0.5rem 0 0.5rem;
}
.bar {
  height: 100%;
  color: white;
  text-align: center;
  padding: 0 10px;
  line-height: 20px;
  border-radius: 5px;
}

/* Status-specific styles */
.pending {
  background: gray;
  width: 33%;
}
.in-progress {
  background: orange;
  width: 66%;
}
.completed {
  background: green;
  width: 100%;
}
.unknown {
  background: red;
  width: 20%;
}

select {
  margin-bottom: 1.5rem;
  padding: 0.3rem;
  border-radius: 5px;
  border: 1px solid #ccc;
}
</style>
