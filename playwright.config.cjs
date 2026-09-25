const {defineConfig} = require('@playwright/test');
module.exports=defineConfig({
  testDir:'tests/browser', timeout:30000, retries:0, workers:1,
  use:{baseURL:'http://127.0.0.1:8765', browserName:'chromium', headless:true,
    launchOptions:process.env.CHROMIUM_PATH?{executablePath:process.env.CHROMIUM_PATH}:{}},
  webServer:{command:'python -m http.server 8765 --bind 127.0.0.1 --directory site',url:'http://127.0.0.1:8765',reuseExistingServer:!process.env.CI},
  reporter:[['list']], outputDir:'.qa/playwright'
});
