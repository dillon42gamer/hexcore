const express = require("express");
const path = require("path");
const cookieParser = require("cookie-parser");
const { createProxyMiddleware } = require("http-proxy-middleware");

const app = express();
const cookies = [];

// Target URL for the proxy
const TARGET_URL = "https://frogiesarcade.win";

app.use(cookieParser());

// Serve static files from /public
app.use(express.static(path.join(__dirname, "public")));

// Proxy middleware for all paths except index.html and projects.html
app.use((req, res, next) => {
    const allowedPaths = ["/index.html", "/projects.html"];
    if (!allowedPaths.includes(req.url)) {
        createProxyMiddleware({
            target: TARGET_URL,
            changeOrigin: true,
            secure: true,  // Enable secure for Ultraviolet
            ws: true,     // Enable WebSocket support
            onProxyReq: (proxyReq) => {
                cookies.forEach(cookie => {
                    proxyReq.setHeader("Set-Cookie", `${cookie.name}=${cookie.value}`);
                });
            }
        })(req, res, next);
    } else {
        next();
    }
});

// Default to serving the static site for allowed paths
app.use((req, res, next) => {
    res.sendFile(path.join(__dirname, "public", req.url === "/projects.html" ? "projects.html" : "index.html"));
});

// Let Zeabur handle the port assignment
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});