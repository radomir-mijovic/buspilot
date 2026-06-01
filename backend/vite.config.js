import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
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
          navbar: path.resolve(__dirname, "./assets/pages/navbar.jsx"),
          navlinks: path.resolve(__dirname, "./assets/pages/navlinks.jsx"),
        },
        output: {
          entryFileNames: `js/[name]-bundle.js`,
        },
      },
    },
  };
});
