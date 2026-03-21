const modeToggle = document.getElementById("mode-toggle");
const enableToggle = document.getElementById("enabled-toggle");
const modeDesc = document.getElementById("mode-desc");
const enabledDesc = document.getElementById("enabled-desc");
const signInBtn = document.getElementById("sign-in-btn");
const signOutBtn = document.getElementById("sign-out-btn");
const userInfo = document.getElementById("user-info");
const userName = document.getElementById("user-name");

chrome.storage.local.get(["gl-mode", "gl-enabled", "gl-user"], (res) => {
    modeToggle.checked = res["gl-mode"] === "subscribed";
    enableToggle.checked = res["gl-enabled"] !== false;
    updateLabels();
    updateUser(res["gl-user"]);
});

modeToggle.addEventListener("change", () => {
    const mode = modeToggle.checked ? "subscribed" : "all";
    chrome.storage.local.set({ "gl-mode": mode });
    updateLabels();
});

enableToggle.addEventListener("change", () => {
    chrome.storage.local.set({ "gl-enabled": enableToggle.checked });
    updateLabels();
});

signInBtn.addEventListener("click", () => {
    chrome.tabs.create({ url: "http://localhost:5173/auth-callback" });
});

signOutBtn.addEventListener("click", () => {
    chrome.storage.local.remove(["gl-token", "gl-user", "gl-subscriptions"]);
    updateUser(null);
});

function updateUser(user) {
    if (user) {
        userName.textContent = user.name;
        userInfo.style.display = "block";
        signInBtn.style.display = "none";
    } else {
        userInfo.style.display = "none";
        signInBtn.style.display = "block";
    }
}

function updateLabels() {
    modeDesc.textContent = modeToggle.checked ? "Subscribed names only" : "Highlighting all names";
    enabledDesc.textContent = enableToggle.checked ? "Active on all pages" : "Highlighting paused";
}
