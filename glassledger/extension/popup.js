const modeToggle = document.getElementById("mode-toggle");
const enableToggle = document.getElementById("enabled-toggle");
const modeDesc = document.getElementById("mode-desc");
const enabledDesc = document.getElementById("enabled-desc");

chrome.storage.local.get(["gl-mode", "gl-enabled"], (res) => {
    modeToggle.checked = res["gl-mode"] === "subscribed";
    enableToggle.checked = res["gl-enabled"] !== false;
    updateLabels();
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

function updateLabels() {
    modeDesc.textContent = modeToggle.checked ? "Subscribed names only" : "Highlighting all names";
    enabledDesc.textContent = enableToggle.checked ? "Active on all pages" : "Highlighting paused";
}
