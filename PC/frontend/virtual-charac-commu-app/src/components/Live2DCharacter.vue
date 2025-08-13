<template>
  <div ref="live2dContainer" class="live2d-container"></div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import * as PIXI from 'pixi.js'
import { Live2DModel } from 'pixi-live2d-display'

const live2dContainer = ref(null)

onMounted(async () => {
  const app = new PIXI.Application({
    width: 1000,
    height: 700,
    transparent: true, 
    backgroundColor: 0x000000
  })

  live2dContainer.value.appendChild(app.view)

  const model = await Live2DModel.from(
    'https://cdn.jsdelivr.net/gh/Eikanya/Live2d-model/%E5%B4%A9%E5%9D%8F%E5%AD%A6%E5%9B%AD2/Nina/model.json'
  )

  model.anchor.set(0.5)
  model.scale.set(0.5)
  model.x = app.view.width / 2 - 50
  model.y = app.view.height / 2

  model.interactive = false
  model.interactiveChildren = false

  app.stage.addChild(model)

  app.ticker.add(() => {
    model.update(app.ticker.deltaMS)
  })
})
</script>

<style scoped>
.live2d-container {
  width: 1000px;
  height: 700px;
  position: relative;
  background: hsla(0, 0%, 0%, 0);
}
</style>
