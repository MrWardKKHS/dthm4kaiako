import { defineConfig } from 'vite'
import { viteStaticCopy } from 'vite-plugin-static-copy'
import path from 'path'

export default defineConfig({
    base: '/static',
    build: {
        outDir: path.resolve(__dirname, 'build'),
        emptyOutDir: true,
        manifest: true,
        manifestFileName: 'manifest.json',
        rollupOptions: {
          input: {
            'website.js': path.resolve(__dirname, 'static/js/website.js'),
            'ara-ako-dashboard.js': path.resolve(__dirname, 'static/js/ara-ako-dashboard.js'),
            'faq.js': path.resolve(__dirname, 'static/js/faq.js'),
            'google-maps.js': path.resolve(__dirname, 'static/js/google-maps.js'),
            'poet.js': path.resolve(__dirname, 'static/js/poet.js'),
            'resource-search.js': path.resolve(__dirname, 'static/js/resource-search.js'),
            'learning-area-cards.js': path.resolve(__dirname, 'static/js/learning-area-cards.js'),
            'tenz-ct-puzzle.js': path.resolve(__dirname, 'static/js/secret_pages/tenz-ct-puzzle.js'),
            'vite-test.js': path.resolve(__dirname, 'static/js/vite-test.js'),

          }
        },
    },
    plugins: [
        viteStaticCopy({
            targets: [
                { src: path.resolve(__dirname, 'static/img/**/*'), dest: 'img' },
                { src: path.resolve(__dirname, 'static/svg/**/*'), dest: 'svg' },
            ]
        })
    ],
    css: {
        preprocessorOptions: {
            scss: {
                includePaths: [
                    path.resolve(__dirname, '../node_modules/bootstrap/scss'),
                    path.resolve(__dirname, './static/scss'),
                ]
            }
        }
    },
    server: {
        host: true,
        port: 5173,
        strictPort: true
    }
})
