<template>
  <div class="min-h-screen">
    <Navbar />
    
    <!-- 主要内容区域 -->
    <main class="flex-1 flex items-center justify-center px-4 py-8 pt-28">
      <div class="max-w-4xl mx-auto w-full">
        <div class="text-center text-white">
          <h1 class="text-5xl lg:text-6xl font-bold mb-6 bg-gradient-to-r from-cute-pink to-cute-purple bg-clip-text drop-shadow-lg">
            {{ $t('home.title') }}
          </h1>
          <p class="text-lg lg:text-xl mb-8 text-cute-blue max-w-2xl mx-auto drop-shadow-sm">
            {{ $t('home.desc') }}
          </p>
          
          <!-- 按钮区域 -->
          <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4 mb-12">
            <button class="bg-gradient-to-r from-cute-pink to-cute-purple text-white px-8 py-3 rounded-xl hover:from-cute-purple hover:to-cute-pink transition-all duration-200 font-medium text-lg shadow-lg hover:shadow-xl transform hover:scale-105">
              {{ $t('home.start') }}
            </button>
            <button class="border-2 border-cute-pink text-cute-pink px-8 py-3 rounded-xl hover:bg-cute-pink hover:text-white transition-all duration-200 font-medium text-lg shadow-lg hover:shadow-xl transform hover:scale-105">
              {{ $t('home.more') }}
            </button>
          </div>
          
          <!-- Live2D角色区域 -->
          <div class="mt-8">
            <Live2DCharacter />
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import Navbar from './Navbar.vue'
import Live2DCharacter from './Live2DCharacter.vue'
</script>

<style scoped>
/* 组件特定样式 */
</style> 