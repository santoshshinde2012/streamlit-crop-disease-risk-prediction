import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import AppDev from "./AppDev.tsx";
import { isDev } from "./helper.ts";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>{isDev() ? <AppDev /> : <App />}</React.StrictMode>,
);
