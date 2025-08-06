<template>
  <nav class="bg-white/15 backdrop-blur-md border-b border-cute-pink/30 shadow-lg">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- 左侧：图标和名字 -->
        <div class="flex items-center space-x-4">
          <div class="flex items-center space-x-2">
            <div class="w-8 h-8 bg-gradient-to-r from-cute-pink to-cute-purple rounded-xl flex items-center justify-center shadow-md">
              <span class="text-white font-bold text-sm">A</span>
            </div>
            <span class="text-cute-pink font-bold text-xl drop-shadow-sm">ANiTalk</span>
          </div>
          
          <!-- 导航链接 -->
          <div class="hidden md:flex items-center space-x-8 ml-8">
            <router-link to="/" class="text-white drop-shadow font-medium hover:text-cute-pink transition-colors duration-200 shadow-lg hover:shadow-xl transform hover:scale-105">
              {{ $t('navbar.home') }}
            </router-link>
            <router-link to="/download" class="text-white drop-shadow font-medium hover:text-cute-pink transition-colors duration-200 shadow-lg hover:shadow-xl transform hover:scale-105">
              {{ $t('navbar.download') }}
            </router-link>
          </div>
        </div>

        <!-- 右侧：语言选择器和登录注册按钮 -->
        <div class="flex items-center space-x-4">
          <router-link to="/login" class="text-white drop-shadow font-medium hover:text-cute-pink transition-colors duration-200 shadow-lg hover:shadow-xl transform hover:scale-105">
            {{ $t('navbar.login') }}
          </router-link>

          <router-link to="/register" class="bg-gradient-to-r from-cute-pink to-cute-purple text-white font-bold px-6 py-2 rounded-xl hover:from-cute-purple hover:to-cute-pink transition-all duration-200 shadow-md hover:shadow-lg transform hover:scale-105">
            {{ $t('navbar.register') }}
          </router-link>

          <!-- 语言下拉框 -->
          <div class="relative language-dropdown">
            <button 
              @click="toggleLanguageDropdown"
              class="flex items-center space-x-2 text-white drop-shadow font-medium px-3 py-2 rounded-lg hover:text-cute-pink hover:bg-white/10 transition-colors duration-200"
            >
              <span class="text-lg">{{ getCurrentLanguageFlag() }}</span>
              <span class="hidden sm:inline">{{ getCurrentLanguageName() }}</span>
              <svg 
                class="w-4 h-4 transition-transform duration-200" 
                :class="{ 'rotate-180': isLanguageDropdownOpen }"
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>
            
            <!-- 语言下拉菜单 -->
            <div 
              v-if="isLanguageDropdownOpen"
              class="absolute right-0 mt-2 w-48 bg-white/95 backdrop-blur-md rounded-xl shadow-lg border border-cute-pink/20 z-50"
            >
              <div class="py-2">
                <button 
                  v-for="lang in languages" 
                  :key="lang.code"
                  @click="selectLanguage(lang.code)"
                  class="w-full flex items-center space-x-3 px-4 py-3 text-left hover:bg-cute-pink/10 transition-colors duration-200"
                  :class="{ 'bg-cute-pink/20 text-cute-purple': currentLanguage === lang.code }"
                >
                  <span class="text-lg">{{ lang.flag }}</span>
                  <span class="font-medium">{{ lang.name }}</span>
                  <span class="text-sm text-gray-500">{{ lang.nativeName }}</span>
                </button>
              </div>
            </div>
          </div>

          <div v-if="isLoggedIn" class="relative user-dropdown">
          <button @click="toggleUserDropdown" class="w-10 h-10 rounded-full overflow-hidden border-2 border-white">
            <img :src="userInfo?.avatarUrl" alt="avatar" class="w-full h-full rounded-full" />
          </button>

          <div v-if="isUserDropdownOpen" class="absolute right-0 mt-2 w-48 bg-white/95 backdrop-blur-md rounded-xl shadow-lg border border-cute-pink/20 z-50">
            <div class="py-2">
              <router-link to="/profile" class="block px-4 py-3 hover:bg-cute-pink/10 transition-colors duration-200 text-cute-purple font-medium">
                用户中心
              </router-link>
              <button @click="logout" class="w-full text-left px-4 py-3 hover:bg-cute-pink/10 transition-colors duration-200 text-red-500 font-medium">
                退出登录
              </button>
            </div>
          </div>
        </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useAuth } from '../composables/useAuth'
import axios from 'axios'

const { isLoggedIn, userInfo, fetchUser } = useAuth()

const isUserDropdownOpen = ref(false)

const toggleUserDropdown = () => {
  isUserDropdownOpen.value = !isUserDropdownOpen.value
  if (isUserDropdownOpen.value) {
    isLanguageDropdownOpen.value = false  // 关闭语言下拉
  }
}

// 语言配置
const languages = [
  { code: 'zh', name: '中文', nativeName: '中文', flag: '🇨🇳' },
  { code: 'en', name: 'English', nativeName: 'English', flag: '🇺🇸' },
  { code: 'ja', name: '日本語', nativeName: '日本語', flag: '🇯🇵' }
]

// 响应式状态
const { locale } = useI18n({ useScope: 'global' })
const currentLanguage = ref(locale.value)
const isLanguageDropdownOpen = ref(false)



// 获取当前语言名称
const getCurrentLanguageName = () => {
  const lang = languages.find(l => l.code === currentLanguage.value)
  return lang ? lang.name : '中文'
}

// 获取当前语言国旗
const getCurrentLanguageFlag = () => {
  const lang = languages.find(l => l.code === currentLanguage.value)
  return lang ? lang.flag : '🇨🇳'
}

// 切换语言下拉框
const toggleLanguageDropdown = () => {
  isLanguageDropdownOpen.value = !isLanguageDropdownOpen.value
  if (isLanguageDropdownOpen.value) {
    isUserDropdownOpen.value = false  // 关闭用户头像下拉
  }
}

// 选择语言
const selectLanguage = (langCode: string) => {
  currentLanguage.value = langCode
  locale.value = langCode
  isLanguageDropdownOpen.value = false
  // 这里可以添加语言切换的逻辑
  // 例如：触发全局事件、更新i18n配置等
  console.log(`Language changed to: ${langCode}`)
}

// 点击外部关闭语言和用户头像下拉框
const handleClickOutside = (event: Event) => {
  const target = event.target as HTMLElement
  // 如果点击区域不在任意下拉容器内，关闭所有下拉框
  if (
    !target.closest('.language-dropdown') &&
    !target.closest('.user-dropdown')
  ) {
    isLanguageDropdownOpen.value = false
    isUserDropdownOpen.value = false
  }
}

const logout = async () => {
  await axios.post('http://localhost:5000/logout', {}, { withCredentials: true })
  await fetchUser()
}

// 生命周期钩子
onMounted(() => {
  fetchUser()
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
/* 组件特定样式 */
</style> 