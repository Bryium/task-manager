// src/store/auth.ts
import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null as null | { id: number; name: string; is_admin: boolean },
  }),
  actions: {
    setUser(user: { id: number; name: string; is_admin: boolean }) {
      this.user = user;
    },
    logout() {
      this.user = null;
    },
  },
});
