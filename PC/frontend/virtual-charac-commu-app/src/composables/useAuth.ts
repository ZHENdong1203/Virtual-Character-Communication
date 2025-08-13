// src/composables/useAuth.ts
import { ref, onMounted } from 'vue'
import axios from 'axios'

const isLoggedIn = ref(false)
const userInfo = ref<{ userId: number; username: string; avatarUrl: string } | null>(null)

const fetchUser = async () => {
  try {
    const res = await axios.get('http://localhost:5000/me', {
      withCredentials: true
    })
    isLoggedIn.value = res.data.loggedIn
    userInfo.value = {
      username: res.data.username,
      avatarUrl: res.data.avatarUrl,
      userId: res.data.userId
    }
  } catch {
    isLoggedIn.value = false
    userInfo.value = null
  }
}

onMounted(fetchUser)

export function useAuth() {
  return {
    isLoggedIn,
    userInfo,
    fetchUser
  }
}
