<template>
  <div id="stage">
    <div id="inner">
      <div id="cover" :style="{ bottom: coverBottom }">
        <div id="text" v-html="text"></div>
        <div id="detail"></div>
        <div id="handle" @click="toggleCover"></div>
      </div>
      <canvas id="live2d" width="800" height="800" class="w-72 h-72 mx-auto cursor-grab active:cursor-grabbing" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Cubism2Model } from '../live2d/build/index.js'

const coverBottom = ref('10%')
const text = ref(`<span style="color: rgba(255, 105, 180, 0.6);">MIMI</span><span style="color: white;">POWERED</span>`.repeat(10))

let state = 0
let loading = false
let model
let modelId = 1
let modelTexturesId = 0

const setState = newState => {
  state = newState
  coverBottom.value = newState === 0 ? '10%' : newState === 1 ? '20%' : '80%'
}

const loadModel = async () => {
  const modelSettingPath = `https://live2d.fghrsh.net/api/get/?id=${modelId}-${modelTexturesId}`
  const response = await fetch(modelSettingPath)
  const modelSetting = await response.json()

  if (!model?.gl) {
    model = new Cubism2Model()
    await model.init('live2d', modelSettingPath, modelSetting)
  } else {
    await model.changeModelWithJSON(modelSettingPath, modelSetting)
  }

  setState(2)
}


const toggleCover = () => setState(state === 2 ? 1 : 2)


onMounted(() => {

  loadModel()

  const passInput = document.querySelector('input[type=password]')
  passInput?.addEventListener('focus', () => state === 2 && setState(1))
  passInput?.addEventListener('blur', () => state === 1 && setState(2))
})
</script>
<style scoped>
#stage {
	position: relative;
}
#stage img {
	width: 100%;
	margin-bottom: 20px;
	border-radius: 20px;
}
#stage button {
	position: absolute;
	padding: 0;
}
#inner {
	position: relative;
	background-color: #99999900;
	clip-path: circle(120px at center);
}
#cover {
	position: absolute;
	background-color: #181717;
	width: 100%;
	height: 100%;
	bottom: 0;
	transition: all 1s;
	box-shadow: 0 0 0 5px rgba(0, 0, 0, .1);
	overflow: hidden;
}
#text {
	position: absolute;
	font-size: 2em;
	opacity: 0.4;
	font-weight: bold;
	word-wrap: break-word;
	max-width: 100%;
}
#detail {
	position: absolute;
	background: rgba(255, 255, 255, .1);
	width: 100%;
	height: 10px;
	bottom: 0;
}
#handle {
	position: absolute;
	background: #ccc;
	bottom: -2px;
	box-shadow: 0 1px 0 1px rgba(0, 0, 0, .1);
	height: 8px;
	left: 50%;
	margin-left: -15px;
	width: 30px;
	cursor: pointer;
}
</style>