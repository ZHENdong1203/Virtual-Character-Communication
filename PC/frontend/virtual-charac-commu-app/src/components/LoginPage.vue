<template>
  <div class="min-h-screen bg-gradient-to-b from-cute-blue to-cute-purple">
    <!-- 导航栏 -->
    <Navbar />

    <!-- 页面主体内容 -->
    <div class="flex items-center justify-center px-4 py-20">
      <div class="w-full max-w-md bg-white/10 backdrop-blur-md p-8 rounded-3xl shadow-2xl border border-white/20">
        <!-- 页面标题 -->
        <div class="text-center mb-6">
          <h1 class="text-white text-3xl font-bold bg-gradient-to-r from-cute-pink to-cute-purple bg-clip-text drop-shadow-lg">
            {{ $t('login.loginAniTalk') }}
          </h1>
        </div>

        <!-- Live2D 登录组件 -->
        <Live2DLogin />

        <!-- 登录表单 -->
        <form @submit.prevent="handleLogin" class="space-y-6 mt-6">
          <input
            v-model="username"
            type="text"
            :placeholder="$t('login.username')"
            required
            class="w-full px-4 py-3 rounded-2xl bg-white/10 border border-white/30 text-white placeholder-white/60 shadow-inner focus:outline-none focus:ring-2 focus:ring-cute-pink"
          />

          <input
            v-model="password"
            type="password"
            :placeholder="$t('login.password')"
            required
            class="w-full px-4 py-3 rounded-2xl bg-white/10 border border-white/30 text-white placeholder-white/60 shadow-inner focus:outline-none focus:ring-2 focus:ring-cute-pink"
          />

          <label class="flex items-center text-white text-sm">
            <input
              type="checkbox"
              v-model="rememberMe"
              class="mr-2 rounded border-gray-300 text-cute-pink focus:ring-cute-pink"
            />
            {{ $t('login.rememberMe') }}
          </label>

          <button
            type="submit"
            class="w-full py-3 rounded-2xl bg-gradient-to-r from-cute-pink to-cute-purple text-white font-bold shadow-[0_0_16px_4px_rgba(255,105,180,0.4)] hover:shadow-[0_0_32px_8px_rgba(255,105,180,0.6)] transition-all duration-200 transform hover:scale-105"
          >
            {{ $t('login.submit') }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import Live2DLogin from './Live2DLogin.vue'
import Navbar from './Navbar.vue' 

const username = ref('')
const password = ref('')
const rememberMe = ref(false)
const router = useRouter()

const handleLogin = async () => {
  try {
    const response = await axios.post('http://localhost:5000/login', {
      username: username.value,
      password: password.value,
      remember: rememberMe.value
    }, {
      withCredentials: true
    })

    if (response.data.success) {
      alert('登录成功！')
      router.push('/')
    } else {
      alert('登录失败：' + response.data.message)
    }
  } catch (error) {
    alert('登录请求出错')
    console.error(error)
  }
}
</script>
