<template>
  <div class="min-h-screen">
    <Navbar />

    <main class="flex-1 flex items-center justify-center py-16 pt-28">
      <div class="w-full max-w-xl bg-transparent backdrop-blur-md rounded-2xl p-8 border border-cute-pink/50 shadow-2xl">
        <h1 class="text-white text-4xl font-bold text-center mb-8 bg-gradient-to-r from-cute-pink to-cute-purple bg-clip-text drop-shadow-lg">
          {{ $t('profile.title') }}
        </h1>

        <!-- 页面内容切换动画 -->
        <transition name="fade-scale" mode="out-in">
          <!-- 用户信息 -->
          <div v-if="activeTab === ''" key="info" class="flex flex-col items-center space-y-4">
            <img
              :src="userInfo?.avatarUrl"
              alt="用户头像"
              class="w-28 h-28 rounded-full border-4 border-white shadow-lg object-cover"
            />
            <p class="text-white text-lg font-semibold">{{ $t('profile.welcome') }}, {{ userInfo?.username }}</p>

            <div class="flex space-x-4 mt-6">
                <button
                @click="activeTab = 'username'"
                class="bg-gradient-to-r from-cute-blue to-cute-mint text-white px-4 py-2 rounded-xl border-2 border-white font-bold text-lg shadow-[0_0_16px_4px_rgba(0,255,255,0.5)] hover:from-cute-mint hover:to-cute-blue hover:shadow-[0_0_32px_8px_rgba(0,255,255,0.7)] hover:border-cute-mint transition-all duration-200 transform hover:scale-105"
              >
                {{ $t('profile.changeUsername') }}
              </button>
              <button
                @click="activeTab = 'avatar'"
                class="bg-gradient-to-r from-cute-pink to-cute-purple text-white px-4 py-2 rounded-xl border-2 border-white font-bold text-lg shadow-[0_0_16px_4px_rgba(255,0,255,0.3)] hover:from-cute-purple hover:to-cute-pink hover:shadow-[0_0_32px_8px_rgba(255,0,255,0.6)] hover:border-cute-pink transition-all duration-200 transform hover:scale-105"
              >
                {{ $t('profile.changeAvatar') }}
              </button>
              <button
                @click="activeTab = 'password'"
                class="bg-gradient-to-r from-cute-yellow to-cute-pink text-white px-4 py-2 rounded-xl border-2 border-white font-bold text-lg shadow-[0_0_16px_4px_rgba(255,192,203,0.5)] hover:from-cute-pink hover:to-cute-yellow hover:shadow-[0_0_32px_8px_rgba(255,192,203,0.7)] hover:border-cute-pink transition-all duration-200 transform hover:scale-105"
              >
                {{ $t('profile.changePassword') }}
              </button>
            </div>
          </div>

          <!-- 修改用户名 -->
          <form v-else-if="activeTab === 'username'" key="username" @submit.prevent="submitUsernameChange" class="space-y-6">
            <h2 class="text-white text-xl font-bold mb-4">{{ $t('profile.changeUsername') }}</h2>

            <input
              v-model="passwordForm.username"
              type="text"
              :placeholder="$t('register.username')"
              class="w-full px-4 py-3 rounded-xl border border-white bg-white/10 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-cute-pink"
              required
            />

            <div class="flex space-x-4">
              <button
                type="submit"
                class="flex-1 bg-gradient-to-r from-cute-pink to-cute-purple text-white px-4 py-2 rounded-xl border-2 border-white font-bold shadow-md hover:scale-105 transition"
              >
                {{ $t('profile.confirmChange') }}
              </button>
              <button
                type="button"
                @click="activeTab = ''"
                class="flex-1 bg-gray-500 text-white px-4 py-2 rounded-xl hover:scale-105 transition"
              >
                {{ $t('profile.back') }}
              </button>
            </div>
          </form>

          <!-- 修改头像表单 -->
          <div v-else-if="activeTab === 'avatar'" key="avatar" class="space-y-6">
            <h2 class="text-white text-xl font-bold mb-4">{{ $t('profile.changeAvatar') }}</h2>
            <div class="flex flex-col items-center space-y-4">
              <img
                :src="userInfo?.avatarUrl"
                alt="用户头像"
                class="w-28 h-28 rounded-full border-4 border-white shadow-lg object-cover"
              />
              
            </div>
            <div class="flex flex-col space-y-4">
                <button
                @click="showAvatarPicker = true"
                class="flex-1 bg-gradient-to-r from-cute-pink to-cute-purple text-white px-4 py-2 rounded-xl border-2 border-white font-bold shadow-md hover:scale-105 transition"
                >
                {{ $t('profile.selectNewAvatar') }}
                </button>
              <button
                @click="activeTab = ''"
                class="flex-1 bg-gray-500 text-white px-4 py-2 rounded-xl hover:scale-105 transition"
              >
                {{ $t('profile.back') }}
              </button>
            </div>

            <!-- 弹窗选择头像 -->
            <div
                v-if="showAvatarPicker"
                class="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
            >
                <div class="bg-white rounded-xl p-6 w-96 space-y-4">
                <h3 class="text-lg font-bold text-gray-800">{{ $t('profile.chooseAvatar') }}</h3>
                
                <div class="grid grid-cols-3 gap-3">
                    <img
                    v-for="avatar in avatarList"
                    :key="avatar"
                    :src="avatar"
                    class="w-20 h-20 rounded-full border-2 border-transparent hover:border-cute-pink cursor-pointer transition"
                    @click="selectAvatar(avatar)"
                    />
                </div>

                <button
                    @click="showAvatarPicker = false"
                    class="w-full bg-gray-400 text-white py-2 rounded-lg hover:scale-105 transition"
                >
                    {{ $t('profile.cancel') }}
                </button>
                </div>
                </div>
          </div>

          <!-- 修改密码表单 -->
          <form v-else-if="activeTab === 'password'" key="password" @submit.prevent="submitPasswordChange" class="space-y-6">
            <h2 class="text-white text-xl font-bold mb-4">{{ $t('profile.changePassword') }}</h2>

            <input
              v-model="passwordForm.newPassword"
              type="password"
              :placeholder="$t('profile.newPassword')"
              class="w-full px-4 py-3 rounded-xl border border-white bg-white/10 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-cute-pink"
              required
            />

            <input
              v-model="passwordForm.confirmPassword"
              type="password"
              :placeholder="$t('profile.confirmPassword')"
              class="w-full px-4 py-3 rounded-xl border border-white bg-white/10 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-cute-pink"
              required
            />

            <div class="flex space-x-4">
              <button
                type="submit"
                class="flex-1 bg-gradient-to-r from-cute-pink to-cute-purple text-white px-4 py-2 rounded-xl border-2 border-white font-bold shadow-md hover:scale-105 transition"
              >
                {{ $t('profile.confirmChange') }}
              </button>
              <button
                type="button"
                @click="activeTab = ''"
                class="flex-1 bg-gray-500 text-white px-4 py-2 rounded-xl hover:scale-105 transition"
              >
                {{ $t('profile.back') }}
              </button>
            </div>
          </form>
        </transition>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import Navbar from './Navbar.vue'
import { useAuth } from '../composables/useAuth'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()

const { userInfo, fetchUser } = useAuth()

const activeTab = ref('')

const passwordForm = ref({
  username: '',
  newPassword: '',
  confirmPassword: ''
})

const submitUsernameChange = async () => {
  if (passwordForm.value.username == '') {
    alert('用户名不能为空！')
    return
  }

  const res = await fetch('http://localhost:5000/change-username', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({userName: passwordForm.value.username, 
        userId: userInfo.value?.userId})
  })
  const result = await res.json()
  if (result.success) {
    alert('用户名修改成功！')
    fetchUser()
    passwordForm.value.username = ''
    activeTab.value = ''
  } else {
    alert('修改失败：' + result.message)
  }
}

const submitPasswordChange = async () => {
  if (passwordForm.value.newPassword !== passwordForm.value.confirmPassword) {
    alert('两次新密码不一致')
    return
  }

  const res = await fetch('http://localhost:5000/change-password', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({
        confirmPassword: passwordForm.value.confirmPassword, 
        userId: userInfo.value?.userId})
  })
  const result = await res.json()
  if (result.success) {
    alert('密码修改成功！需要重新登陆')
    passwordForm.value.newPassword = ''
    passwordForm.value.confirmPassword = ''
    await axios.post('http://localhost:5000/logout', {}, { withCredentials: true })
    await fetchUser()
    router.push('/login')
  } else {
    alert('修改失败：' + result.message)
  }
}

const showAvatarPicker = ref(false)
const avatarList = ref<string[]>([])

// 生成 Dicebear 头像列表
const generateAvatars = () => {
  const styles = ['icons', 'shapes', 'thumbs', 'bottts-neutral', 'fun-emoji']
  avatarList.value = Array.from({ length: 9 }, () => {
    const style = styles[Math.floor(Math.random() * styles.length)]
    const seed = Math.random().toString(36).substring(2, 10)
    return `https://api.dicebear.com/9.x/${style}/svg?seed=${seed}`
  })
}

// 选择头像并保存到后端
const selectAvatar = async (url: string) => {
  const res = await fetch('http://localhost:5000/change-avatar', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ avatarUrl: url,
        userId: userInfo.value?.userId
     })
  })
  const result = await res.json()
  if (result.success) {
    alert('头像修改成功！')
    fetchUser()
    showAvatarPicker.value = false
    activeTab.value = ''
  } else {
    alert('修改失败：' + result.message)
  }
}

// 打开选择器时自动生成头像
watch(showAvatarPicker, (val) => {
  if (val) generateAvatars()
})

onMounted(() => {
  fetchUser()
})
</script>

<style scoped>
.fade-scale-enter-active,
.fade-scale-leave-active {
  transition: all 0.3s ease;
}
.fade-scale-enter-from {
  opacity: 0;
  transform: scale(0.95);
}
.fade-scale-enter-to {
  opacity: 1;
  transform: scale(1);
}
.fade-scale-leave-from {
  opacity: 1;
  transform: scale(1);
}
.fade-scale-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
</style>
