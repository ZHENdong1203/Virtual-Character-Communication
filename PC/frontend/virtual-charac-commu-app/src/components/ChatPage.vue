<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />

    <main class="flex-1 flex flex-col pt-20 pb-28 px-4">
      <div class="flex-1 flex gap-4">
        <!-- 左侧 Live2D -->
        <div class="w-2/5 bg-transparent backdrop-blur-md rounded-2xl border border-cute-pink/50 shadow-2xl flex items-center justify-center">
          <div class="w-full h-full flex items-center justify-center">
            <div ref="live2dContainer" class="live2d-container"></div>
          </div>
        </div>

        <!-- 右侧聊天记录 -->
        <div class="flex-1 bg-transparent backdrop-blur-md rounded-2xl border border-cute-pink/50 shadow-2xl flex flex-col">
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
                {{ msg.text }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </main>

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
           transform hover:scale-110
           "
  >
    发送
  </button>
  <button
    @click="startVoiceInput"
    class="px-4 py-3 rounded-2xl border-2 border-white font-bold text-lg
           bg-gradient-to-r from-cute-blue to-cute-mint text-white
           transition-all duration-200
           transform hover:scale-110
           "
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

// 聊天记录
const messages = ref([
  { sender: 'bot', text: '你好，我是你的虚拟角色！' }
])
const inputText = ref('')
const isSending = ref(false)
const live2dContainer = ref(null)

// Live2D 模型引用
let live2dModel = null
let motionGroups = []

// 发送消息
const sendMessage = async () => {
  if (!inputText.value.trim() || isSending.value) return

  const userMsg = inputText.value
  messages.value.push({ sender: 'user', text: userMsg })
  inputText.value = ''
  isSending.value = true

  try {
    const res = await axios.post('http://127.0.0.1:5000/chat', {
      message: userMsg
    })
    const reply = res.data.reply
    messages.value.push({ sender: 'bot', text: reply })

    // GPT 回复时随机触发一个动作
    if (live2dModel && motionGroups.length > 0) {
      const randomGroup = motionGroups[Math.floor(Math.random() * motionGroups.length)]
      live2dModel.motion(randomGroup)
    }

  } catch (err) {
    messages.value.push({ sender: 'bot', text: '❌ 服务器连接失败，请稍后重试' })
    console.error(err)
  } finally {
    isSending.value = false
  }
}

const startVoiceInput = () => {
  alert('语音输入功能开发中...')
}

onMounted(async () => {
  const app = new PIXI.Application({
    width: 1200,
    height: 700,
    transparent: true
  })

  live2dContainer.value.appendChild(app.view)

  live2dModel = await Live2DModel.from(
    'https://cdn.jsdelivr.net/gh/Eikanya/Live2d-model/%E5%B0%91%E5%A5%B3%E5%89%8D%E7%BA%BF%20girls%20Frontline/live2dnew/88type_1809/normal/normal.model3.json'
  )

  live2dModel.anchor.set(0.5, 0.5)
  live2dModel.scale.set(0.15)
  live2dModel.x = app.view.width / 2
  live2dModel.y = app.view.height / 2

  app.stage.addChild(live2dModel)

  live2dModel.interactive = false
  live2dModel.interactiveChildren = false

  live2dModel.motion("", 5);

  // 读取模型动作分组
  if (live2dModel.internalModel?.motionManager) {
    motionGroups = Object.keys(live2dModel.internalModel.motionManager.definitions)
    console.log('可用动作组:', motionGroups)
  }

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
  width: 1200px;
  height: 700px;
  position: relative;
  background: transparent;
}
</style>
