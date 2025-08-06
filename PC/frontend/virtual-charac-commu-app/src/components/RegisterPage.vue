<template>
  <div class="min-h-screen">
    <Navbar />

    <main class="flex-1 flex items-center justify-center py-16 pt-28">
      <div class="w-full max-w-xl bg-transparent backdrop-blur-md rounded-2xl p-8 border border-cute-pink/50 shadow-2xl">
        <h1 class="text-white text-4xl font-bold text-center mb-8 bg-gradient-to-r from-cute-pink to-cute-purple bg-clip-text drop-shadow-lg">
          {{ $t('register.title') }}
        </h1>

        <form @submit.prevent="submitRegister" class="space-y-6">
          <!-- 用户名 -->
          <input
            v-model="form.username"
            type="text"
            :placeholder="$t('register.username')"
            class="w-full px-4 py-3 rounded-xl border border-white bg-white/10 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-cute-pink"
            required
          />

          <!-- 密码 -->
          <input
            v-model="form.password"
            type="password"
            :placeholder="$t('register.password')"
            class="w-full px-4 py-3 rounded-xl border border-white bg-white/10 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-cute-pink"
            required
          />

          <!-- 确认密码 -->
          <input
            v-model="form.confirmPassword"
            type="password"
            :placeholder="$t('register.confirmPassword')"
            class="w-full px-4 py-3 rounded-xl border border-white bg-white/10 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-cute-pink"
            required
          />

          <!-- 验证码 -->
          <div class="flex items-center space-x-4">
            <input
              v-model="form.captcha"
              type="text"
              :placeholder="$t('register.captcha')"
              class="flex-1 px-4 py-3 rounded-xl border border-white bg-white/10 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-cute-pink"
              required
            />
            <img
              :src="captchaUrl"
              @click="refreshCaptcha"
              class="w-24 h-10 rounded-lg border border-white cursor-pointer"
              alt="验证码"
            />
          </div>

          <!-- 协议勾选 -->
          <label class="flex items-center space-x-2 text-white">
            <input v-model="form.agreed" type="checkbox" class="form-checkbox text-cute-pink" required />
            <span>{{ $t('register.agree') }} <a href="#" class="underline hover:text-cute-pink">{{ $t('register.protocol') }}</a></span>
          </label>

          <!-- 注册按钮 -->
          <button
            type="submit"
            class="w-full bg-gradient-to-r from-cute-pink to-cute-purple text-white px-6 py-3 rounded-2xl border-2 border-white font-bold text-lg shadow-[0_0_16px_4px_rgba(255,0,255,0.3)] hover:from-cute-purple hover:to-cute-pink hover:shadow-[0_0_32px_8px_rgba(255,0,255,0.6)] hover:border-cute-pink transition-all duration-200 transform hover:scale-105"
          >
            {{ $t('register.submit') }}
          </button>
        </form>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Navbar from './Navbar.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref({
  username: '',
  password: '',
  confirmPassword: '',
  captcha: '',
  agreed: false,
})

const captchaUrl = ref('http://localhost:5000/captcha?' + Math.random())
const refreshCaptcha = () => {
  captchaUrl.value = 'http://localhost:5000/captcha?' + Math.random()
}

const submitRegister = async () => {
  if (form.value.password !== form.value.confirmPassword) {
    alert('两次密码不一致')
    refreshCaptcha()
    return
  }

  const res = await fetch('http://localhost:5000/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify(form.value)
  })
  const result = await res.json()
  if (result.success) {
    alert('注册成功！')
    router.push('/login')
  } else {
    alert('注册失败：' + result.message)
    refreshCaptcha()
  }
}
</script>
