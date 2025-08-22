<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />
    <div class="flex flex-1 overflow-hidden pt-20 pb-28">
      <!-- 左侧侧边栏 -->
      <div
        :class="[
          'relative z-40 bg-transparent backdrop-blur-md border-r border-cute-pink/50 shadow-2xl transition-all duration-300',
          isSidebarOpen ? 'w-64' : 'w-16'
        ]"
      >
        <!-- 展开状态 -->
        <div v-if="isSidebarOpen" class="h-full flex flex-col">
          <!-- 顶部操作 -->
          <div class="flex items-center justify-between p-4 border-b border-cute-pink/30">
            <span class="text-lg font-bold text-white">聊天列表</span>
            <button
              @click="isSidebarOpen = false"
              class="p-2 rounded-full bg-cute-pink text-white hover:scale-110 transition-transform"
            >
              ❌
            </button>
            <span
              class="absolute left-full ml-2 top-1/2 -translate-y-1/2
                     bg-black/80 text-white text-sm px-2 py-1 rounded opacity-0 group-hover:opacity-100
                     whitespace-nowrap transition-opacity"
            >
              关闭列表
            </span>
          </div>

          <!-- 新建聊天 -->
          <div class="p-4">
            <button
              @click="createNewChat"
              class="w-full py-2 rounded-xl border-2 border-white bg-cute-blue text-white font-bold hover:scale-105 transition-transform"
            >
              新建聊天
            </button>
          </div>

          <!-- 历史聊天列表 -->
          <div class="flex-1 overflow-y-auto p-2 space-y-2">
            <div
              v-for="chat in chatHistory"
              :key="chat.id"
              class="group relative p-2 rounded-lg cursor-pointer transition-colors flex justify-between items-center"
              :class="chat.id === currentChatId
                ? 'bg-cute-pink text-white'
                : 'bg-white/10 text-white hover:bg-cute-purple/40'"
            >
              <!-- 点击切换聊天 -->
              <div @click="switchChat(chat.id)" class="flex-1 truncate">
                {{ chat.title }}
              </div>

              <!-- 三点按钮（仅 hover 时显示） -->
              <div class="opacity-0 group-hover:opacity-100 transition-opacity">
                <button
                  @click="toggleMenu(chat.id)"
                  class="p-1 rounded hover:bg-white/20"
                >
                  ⋮
                </button>
              </div>

              <!-- 下拉菜单 -->
              <div
                v-if="menuChatId === chat.id"
                class="absolute right-2 top-full mt-1 bg-black/80 text-white rounded-lg shadow-lg z-50 w-28"
              >
                <div
                  @click="renameChat(chat.id)"
                  class="px-3 py-2 hover:bg-white/20 cursor-pointer rounded-t-lg"
                >
                  重命名
                </div>
                <div
                  @click="deleteChat(chat.id)"
                  class="px-3 py-2 hover:bg-white/20 cursor-pointer rounded-b-lg text-red-400"
                >
                  删除
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- 收起状态 -->
        <div v-else class="flex flex-col items-center py-4 gap-6">
          <!-- 打开列表按钮 -->
          <div class="relative group">
            <button
              @click="isSidebarOpen = true"
              class="p-2 rounded-full bg-cute-pink text-white hover:scale-110 transition-transform"
            >
              📂
            </button>
            <span
              class="absolute left-full ml-2 top-1/2 -translate-y-1/2
                     bg-black/80 text-white text-sm px-2 py-1 rounded opacity-0 group-hover:opacity-100
                     whitespace-nowrap transition-opacity"
            >
              打开列表
            </span>
          </div>

          <!-- 新建聊天按钮 -->
          <div class="relative group">
            <button
              @click="createNewChat"
              class="p-2 rounded-full bg-cute-blue text-white hover:scale-110 transition-transform"
            >
              ✨
            </button>
            <span
              class="absolute left-full ml-2 top-1/2 -translate-y-1/2
                     bg-black/80 text-white text-sm px-2 py-1 rounded opacity-0 group-hover:opacity-100
                     whitespace-nowrap transition-opacity"
            >
              新建聊天
            </span>
          </div>
        </div>
      </div>

      <!-- 右侧内容 -->
      <main class="relative z-0 flex-1 flex flex-col px-4 overflow-hidden">
        <div class="flex-1 flex flex-col lg:flex-row gap-4">
          <!-- 左侧 Live2D -->
          <div
            class="lg:w-2/5 w-full h-80 lg:h-auto bg-transparent backdrop-blur-md rounded-2xl
                  border border-cute-pink/50 shadow-2xl flex items-center justify-center"
          >
            <div ref="live2dContainer" class="live2d-container w-full h-full"></div>
          </div>

          <!-- 右侧聊天记录 -->
          <div
            class="flex-1 bg-transparent backdrop-blur-md rounded-2xl border border-cute-pink/50 shadow-2xl flex flex-col"
          >
            <div class="flex-1 overflow-y-auto p-4 space-y-4">
              <div
                v-for="(msg, index) in messages"
                :key="index"
                :class="msg.sender === 'user' ? 'text-right' : 'text-left'"
              >
                <span
                  :class="msg.sender === 'user'
                    ? 'bg-cute-purple text-white px-4 py-2 rounded-2xl inline-block'
                    : 'bg-cute-pink text-white px-4 py-2 rounded-2xl inline-block'"
                >
                  {{ msg.textKey ? $t(msg.textKey) : msg.text }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </main>

    </div>

    <!-- 输入栏 -->
    <div
      class="fixed bottom-0 left-0 w-full bg-transparent backdrop-blur-md border-t border-cute-pink/50 p-4 flex items-center gap-2"
    >
      <input
        v-model="inputText"
        type="text"
        placeholder="输入消息..."
        class="flex-1 px-4 py-3 rounded-xl border border-white bg-white/10 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-cute-pink"
        @keyup.enter="sendMessage"
      />
      <button
        @click="sendMessage"
        class="px-4 py-3 rounded-2xl border-2 border-white font-bold text-lg
             bg-gradient-to-r from-cute-blue to-cute-mint text-white
             transition-all duration-200
             transform hover:scale-110"
      >
        发送
      </button>
      <button
        @click="startVoiceInput"
        class="px-4 py-3 rounded-2xl border-2 border-white font-bold text-lg
             bg-gradient-to-r from-cute-blue to-cute-mint text-white
             transition-all duration-200
             transform hover:scale-110"
      >
        语音输入
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Navbar from './Navbar.vue'
import axios from 'axios'
import * as PIXI from 'pixi.js'
import { Live2DModel } from 'pixi-live2d-display'

// 聊天相关
const messages = ref([{ sender: 'bot', textKey: 'chat.welcome' }])
const inputText = ref('')
const isSending = ref(false)
const live2dContainer = ref(null)

// 侧边栏 & 历史聊天
const isSidebarOpen = ref(false)
const chatHistory = ref([
  { id: 1, title: '聊天 1', messages: [{ sender: 'bot', textKey: 'chat.welcome' }] }
])
const currentChatId = ref(1)

const createNewChat = () => {
  const newId = chatHistory.value.length + 1
  chatHistory.value.push({
    id: newId,
    title: `聊天 ${newId}`,
    messages: [{ sender: 'bot', textKey: 'chat.welcome' }]
  })
  switchChat(newId)
}

const switchChat = (id) => {
  currentChatId.value = id
  const chat = chatHistory.value.find((c) => c.id === id)
  messages.value = chat ? [...chat.messages] : []
}


// Live2D 模型引用
let live2dModel = null
let totalLength = 0

const getRandomInt = (length) => {
  return Math.floor(Math.random() * length) + 1
}

// 发送消息
const sendMessage = async () => {
  if (!inputText.value.trim() || isSending.value) return

  const userMsg = inputText.value
  messages.value.push({ sender: 'user', text: userMsg })
  inputText.value = ''
  isSending.value = true

  try {
    const res = await axios.post('http://127.0.0.1:5000/chat/get-gpt-reply', {
      message: userMsg
    })
    const reply = res.data.reply
    messages.value.push({ sender: 'bot', text: reply })

    const motionIndex = getRandomInt(totalLength)
    live2dModel.motion('idle_click', motionIndex)
  } catch (err) {
    messages.value.push({ sender: 'bot', text: '❌ 服务器连接失败，请稍后重试' })
  } finally {
    isSending.value = false
  }

  // 保存到当前聊天记录
  const chat = chatHistory.value.find((c) => c.id === currentChatId.value)
  if (chat) chat.messages = [...messages.value]
}

const startVoiceInput = () => {
  alert('语音输入功能开发中...')
}

onMounted(async () => {
  const app = new PIXI.Application({
    resizeTo: live2dContainer.value,
    transparent: true
  })

  live2dContainer.value.appendChild(app.view)

  live2dModel = await Live2DModel.from(
    'https://cdn.jsdelivr.net/gh/Eikanya/Live2d-model/%E6%96%B9%E8%88%9F%E6%8C%87%E4%BB%A4/l_143200301/model.json'
  )

  live2dModel.anchor.set(0.5, 0.5)
  live2dModel.scale.set(0.18)
  live2dModel.x = app.view.width / 2
  live2dModel.y = app.view.height / 2

  app.stage.addChild(live2dModel)

  live2dModel.interactive = false
  live2dModel.interactiveChildren = false

  // 动作分组
  if (live2dModel.internalModel?.motionManager) {
    const motions = live2dModel.internalModel.motionManager.definitions
    totalLength = Object.values(motions).reduce(
      (sum, group) => sum + group.length,
      0
    )
  }

  live2dModel.motion('idle', 0)

  app.ticker.add(() => {
    live2dModel.update(app.ticker.deltaMS)
  })
})
</script>


<style scoped>
::-webkit-scrollbar {
  width: 6px;
}
::-webkit-scrollbar-thumb {
  background: rgba(255, 192, 203, 0.6);
  border-radius: 3px;
}
.live2d-container {
  width: 100%;
  height: 100%;
  position: relative;
  background: transparent;
}
</style>
