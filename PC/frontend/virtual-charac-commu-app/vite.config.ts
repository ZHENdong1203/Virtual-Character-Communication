import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

const base = process.env.VITE_BASE

export default defineConfig({
  plugins: [vue(), tailwindcss()],
  base: base,
  resolve: {
    alias: {
      crypto: 'crypto-browserify'
    }
  },
  optimizeDeps: {
    include: ['crypto-browserify']
  }
})