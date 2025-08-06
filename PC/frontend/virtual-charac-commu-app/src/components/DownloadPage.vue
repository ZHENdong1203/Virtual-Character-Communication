<template>
  <div class="min-h-screen">
    <Navbar />
    
    <!-- 下载页面内容 -->
    <main class="flex-1 flex items-center justify-center py-16 pt-28">
      <div class="max-w-4xl mx-auto px-4">
        <div class="text-center mb-12">
          <h1 class="text-white text-5xl font-bold mb-6 bg-gradient-to-r from-cute-pink to-cute-purple bg-clip-text drop-shadow-lg">
            {{ $t('download.title') }}
          </h1>
          <p class="text-white text-xl text-cute-blue max-w-2xl mx-auto drop-shadow-sm">
            {{ $t('download.desc') }}
          </p>
        </div>

        <!-- 下载选项 -->
        <div class="grid md:grid-cols-2 gap-8">
          <!-- PC客户端 -->
          <div class="bg-transparent backdrop-blur-md rounded-2xl p-8 border border-cute-pink/50 shadow-2xl hover:shadow-2xl transition-all duration-300 transform hover:scale-105">
            <div class="text-center">
              <div class="w-20 h-20 bg-gradient-to-r from-cute-blue to-cute-mint rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-lg">
                <span class="text-3xl">💻</span>
              </div>
              <h2 class="text-2xl font-bold text-white mb-4">{{ $t('download.pc') }}</h2>
              <p class="text-white mb-6" style="white-space: pre-line;">
                {{ $t('download.pcDesc') }}
              </p>
              <div class="space-y-3 mb-6">
                <div class="flex items-center justify-center space-x-2 text-cute-yellow">
                  <span>✨</span>
                  <span class='text-white'>{{ $t('download.hd') }}</span>
                </div>
                <div class="flex items-center justify-center space-x-2 text-cute-yellow">
                  <span>🧩</span>
                  <span class='text-white'>{{ $t('download.plugin') }}</span>
                </div>
                <div class="flex items-center justify-center space-x-2 text-cute-yellow">
                  <span>💾</span>
                  <span class='text-white'>{{ $t('download.storage') }}</span>
                </div>
              </div>
              <button 
                @click="downloadPC"
                class="w-full bg-gradient-to-r from-cute-blue to-cute-mint text-white px-8 py-4 rounded-2xl border-2 border-white font-bold text-lg shadow-[0_0_16px_4px_rgba(0,255,255,0.5)] hover:from-cute-mint hover:to-cute-blue hover:shadow-[0_0_32px_8px_rgba(0,255,255,0.7)] hover:border-cute-mint transition-all duration-200 transform hover:scale-110"
              >
                {{ $t('download.downloadPC') }}
              </button>
            </div>
          </div>

          <!-- 安卓APP -->
          <div class="bg-transparent backdrop-blur-md rounded-2xl p-8 border border-cute-pink/50 shadow-2xl hover:shadow-2xl transition-all duration-300 transform hover:scale-105">
            <div class="text-center">
              <div class="w-20 h-20 bg-gradient-to-r from-cute-yellow to-cute-pink rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-lg">
                <span class="text-3xl">📱</span>
              </div>
              <h2 class="text-2xl font-bold text-white mb-4">{{ $t('download.android') }}</h2>
              <p class="text-white mb-6" style="white-space: pre-line;">
                {{ $t('download.androidDesc') }}
              </p>
              <div class="space-y-3 mb-6">
                <div class="flex items-center justify-center space-x-2 text-cute-yellow">
                  <span>🚀</span>
                  <span class='text-white'>{{ $t('download.fast') }}</span>
                </div>
                <div class="flex items-center justify-center space-x-2 text-cute-yellow">
                  <span>🖼️</span>
                  <span class='text-white'>{{ $t('download.widget') }}</span>
                </div>
                <div class="flex items-center justify-center space-x-2 text-cute-yellow">
                  <span>☁️</span>
                  <span class='text-white'>{{ $t('download.cloud') }}</span>
                </div>
              </div>
              <button 
                @click="downloadAndroid"
                class="w-full bg-gradient-to-r from-cute-yellow to-cute-pink text-white px-8 py-4 rounded-2xl border-2 border-white font-bold text-lg shadow-[0_0_16px_4px_rgba(255,192,203,0.5)] hover:from-cute-pink hover:to-cute-yellow hover:shadow-[0_0_32px_8px_rgba(255,192,203,0.7)] hover:border-cute-pink transition-all duration-200 transform hover:scale-110"
              >
                {{ $t('download.downloadAndroid') }}
              </button>
            </div>
          </div>
        </div>

        <!-- 系统要求 -->
        <div class="mt-12 bg-transparent backdrop-blur-md rounded-2xl p-8 border border-cute-pink/40 shadow-xl">
          <h3 class="text-2xl font-bold text-white mb-6 text-center">{{ $t('download.sysreq') }}</h3>
          <div class="grid md:grid-cols-2 gap-8">
            <div>
              <h4 class="text-lg font-semibold text-white mb-3">{{ $t('download.pcReq') }}</h4>
              <ul class="space-y-2 text-white">
                <li>• {{ $t('download.win') }}</li>
                <li>• {{ $t('download.mac') }}</li>
                <li>• {{ $t('download.ram4') }}</li>
                <li>• {{ $t('download.disk2') }}</li>
              </ul>
            </div>
            <div>
              <h4 class="text-lg font-semibold text-white mb-3">{{ $t('download.androidReq') }}</h4>
              <ul class="space-y-2 text-white">
                <li>• {{ $t('download.andver') }}</li>
                <li>• {{ $t('download.ram2') }}</li>
                <li>• {{ $t('download.disk500') }}</li>
                <li>• {{ $t('download.net') }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import Navbar from './Navbar.vue'

const downloadPC = () => {
  // 这里可以添加实际的下载逻辑
  alert('开始下载 PC 客户端...\n\n注意：这是一个演示版本，实际下载功能需要配置真实的下载链接。')
}

const downloadAndroid = () => {
  // 这里可以添加实际的下载逻辑
  alert('开始下载安卓 APP...\n\n注意：这是一个演示版本，实际下载功能需要配置真实的下载链接。')
}
</script>

<style scoped>
/* 组件特定样式 */
</style> 