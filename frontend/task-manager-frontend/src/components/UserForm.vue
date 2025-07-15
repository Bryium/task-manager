<template>
  <div class="header">
    <h3></h3>
    <button class="back-button" @click="$router.back()">← Back</button>
  </div>

  <div class="user-form">
    <h3>Manage Users</h3>

    <form @submit.prevent="addUser" class="add-user-form">
      <input v-model="name" type="text" placeholder="Enter name" required />
      <input v-model="userId" type="text" placeholder="Enter ID" required />
      <input v-model="email" type="email" placeholder="Enter email" required />
      <button type="submit">Add User</button>
    </form>

    <ul class="user-list">
      <li v-for="(user, index) in users" :key="user.id" class="user-card">
        <div class="user-item">
          <span>
            <strong>{{ user.name }}</strong> (ID: {{ user.id }})<br />
            <small>Email: {{ user.email }}</small>
          </span>
          <div class="actions">
            <button @click="editUser(index)">Edit</button>
            <button @click="deleteUser(user.id)">Delete</button>
          </div>
        </div>

        <div v-if="editingIndex === index" class="edit-section">
          <input v-model="editName" placeholder="New name" />
          <input v-model="editEmail" placeholder="New email" />
          <button @click="saveUser(user.id)">Save</button>
          <button @click="cancelEdit">Cancel</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import Toastify from "toastify-js";
import "toastify-js/src/toastify.css";

const API_URL = "https://task-manager-v4al.onrender.com/api/users";
const users = ref<{ name: string; id: string; email: string }[]>([]);
const name = ref("");
const userId = ref("");
const email = ref("");

const editingIndex = ref<number | null>(null);
const editName = ref("");
const editEmail = ref("");
// eslint-disable-next-line @typescript-eslint/no-unused-vars
let currentEditId = "";

// Toast utility
const showToast = (message: string, type: "success" | "error") => {
  Toastify({
    text: message,
    duration: 3000,
    close: true,
    gravity: "top",
    position: "right",
    backgroundColor: type === "success" ? "#28a745" : "#dc3545",
  }).showToast();
};

// Fetch users from API
const fetchUsers = async () => {
  try {
    const response = await axios.get(API_URL);
    users.value = response.data;
  } catch (error) {
    showToast("Failed to fetch users", "error");
    console.error(error);
  }
};

onMounted(fetchUsers);

// Add new user
const addUser = async () => {
  try {
    await axios.post(API_URL, {
      name: name.value,
      id: userId.value,
      email: email.value,
    });
    showToast("User added successfully", "success");
    name.value = "";
    userId.value = "";
    email.value = "";
    await fetchUsers();
  } catch (error) {
    showToast("Error adding user", "error");
    console.error(error);
  }
};

// Delete user
const deleteUser = async (id: string) => {
  try {
    await axios.delete(`${API_URL}/${id}`);
    showToast("User deleted successfully", "success");
    await fetchUsers();
  } catch (error) {
    showToast("Error deleting user", "error");
    console.error(error);
  }
};

// Start editing
const editUser = (index: number) => {
  editingIndex.value = index;
  editName.value = users.value[index].name;
  editEmail.value = users.value[index].email;
  currentEditId = users.value[index].id;
};

// Save edited user
const saveUser = async (id: string) => {
  try {
    await axios.put(`${API_URL}/${id}`, {
      name: editName.value,
      email: editEmail.value,
    });
    showToast("User updated successfully", "success");
    await fetchUsers();
    cancelEdit();
  } catch (error) {
    showToast("Error updating user", "error");
    console.error(error);
  }
};

// Cancel editing
const cancelEdit = () => {
  editingIndex.value = null;
  editName.value = "";
  editEmail.value = "";
  currentEditId = "";
};
</script>

<style scoped>
.user-form {
  margin-bottom: 2rem;
  padding: 1rem;
  background: #f9f9f9;
  border-radius: 8px;
}
.user-form h3 {
  margin-bottom: 1rem;
}
.add-user-form {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}
.add-user-form input,
.edit-section input {
  padding: 0.4rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.add-user-form button,
.edit-section button,
.user-item button {
  padding: 0.4rem 0.8rem;
  background-color: #007bff;
  border: none;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}
.user-list {
  list-style: none;
  padding: 0;
}
.user-card {
  background: #ffffff;
  border: 1px solid #ddd;
  border-radius: 6px;
  margin-bottom: 1rem;
  padding: 1rem;
}
.user-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.actions button {
  margin-left: 0.5rem;
  background-color: #28a745;
}
.actions button:last-child {
  background-color: #dc3545;
}
.edit-section {
  margin-top: 0.5rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
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
