import { defineConfig } from 'vite'
import { viteStaticCopy } from 'vite-plugin-static-copy'
import path from 'path'

export default defineConfig({
    root: path.resolve(__dirname, 'static'),
    base: 'static',
    build: {
        outDir: path.resolve(__dirname, 'build'),
        emptyOutDir: true,
        mainfest: true,
    },
    rollupOptions: {
      input: {
        'website.js': path.resolve(__dirname, 'static/js/website.js'),
        'ara-ako-dashboard.js': path.resolve(__dirname, 'static/js/ara-ako-dashboard.js'),
        'faq.js': path.resolve(__dirname, 'static/js/faq.js'),
        'google-maps.js': path.resolve(__dirname, 'static/js/google-maps.js'),
        'poet.js': path.resolve(__dirname, 'static/js/poet.js'),
        'resource-search.js': path.resolve(__dirname, 'static/js/resource-search.js'),
              'learning-area-cards.js': path.resolve(__dirname, 'static/js/learning-area-cards.js'),
      }
    },
    plugins: [
        viteStaticCopy({
            targets: [
                { src: 'img/**/*', dest: 'img' },
                { src: 'svg/**/*', dest: 'svg' },
                { src: 'files/**/*', dest: 'files' },
            ]
        })
    ],
    css: {
        preprocessorOptions: {
            scss: {
                includePaths: [
                    path.resolve(__dirname, 'node_modules/bootstrap/scss'),
                    path.resolve(__dirname, 'static/scss'),
                ]
            }
        }
    },
    server: {
        host: true,
        port: 5173,
    }
})
