import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

//export default defineConfig({
//  base: "/static/", // This should match Django's settings.STATIC_URL
//  build: {
//    // Where Vite will save its output files.
//    // This should be something in your settings.STATICFILES_DIRS
//    outDir: path.resolve(__dirname, "./static"),
//    emptyOutDir: false, // Preserve the outDir to not clobber Django's other files.
//    manifest: "manifest.json",
//    rollupOptions: {
//      input: {
//        invoices: path.resolve(__dirname, "./assets/pages/finance.jsx"),
//        index: path.resolve(__dirname, "./assets/pages/index.jsx"),
//      },
//      output: {
//        // Output JS bundles to js/ directory with -bundle suffix
//        entryFileNames: `js/[name]-bundle.js`,
//      },
//    },
//  },
//});
//
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  const djangoOrigin = env.DJANGO_ORIGIN || "http://localhost:8001";
  const viteHost = env.VITE_HOST || "localhost";
  const vitePort = Number(env.VITE_PORT || 5173);

  return {
    plugins: [react()],
    base: "/static/",
    server: {
      host: viteHost,
      port: vitePort,
      strictPort: true,
      origin: `http://${viteHost}:${vitePort}`,
      cors: true,
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
    },
    build: {
      outDir: path.resolve(__dirname, "./static"),
      emptyOutDir: false,
      manifest: "manifest.json",
      rollupOptions: {
        input: {
          finance: path.resolve(__dirname, "./assets/pages/finance.jsx"),
          index: path.resolve(__dirname, "./assets/pages/index.jsx"),
        },
        output: {
          entryFileNames: `js/[name]-bundle.js`,
        },
      },
    },
  };
});
