const { app, BrowserWindow } = require("electron");

app.whenReady().then(() => {
  // create a window
  const myWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
      app.quit();
    }
  });

  // load a webpage
  myWindow.loadFile("index.html");
});
