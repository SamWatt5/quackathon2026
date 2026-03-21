const API_URL = "http://127.0.0.1:5000/api";
const FRONTEND_PERSON_URL = "http://127.0.0.1:5173/person";

chrome.storage.local.set({ "gl-mode": "all" }).then(() => {
    console.log("Value is set");
});

const style = document.createElement("style");
style.textContent = `
    .gl-highlight {
        background: rgba(255,200,0,0.3);
        border-bottom: 2px solid gold;
        cursor:pointer;
    }
    .gl-a {
        color:inherit;
        text-decoration: inherit;
        cursor: inherit;
    }
`;
document.head.appendChild(style);

async function getNamesFromAPI() {
    const { mode } = await chrome.storage.local.get("gl-mode");
    const endpoint = mode === "subscribed" ? "/watchlist" : "/explore";
    const res = await fetch(`${API_URL}${endpoint}`);
    const data = await res.json();
    return data.map((p) => ({ id: p.id, name: p.name, transparency_score: p.transparency_score }));
}

async function scanForNames() {
    console.log("Scanning for names...");

    const people = await getNamesFromAPI();
    // console.log(names);

    const elements = document.querySelectorAll("p, h1, h2, h3, li, span");
    elements.forEach((element) => {
        people.forEach((person) => {
            if (element.innerText.toLowerCase().includes(person.name.toLowerCase())) {
                // console.log(`found ${person} in `, element);
                highlightName(element, person);
            }
        });
    });
}

function highlightName(el, person) {
    const regex = new RegExp(`(${person.name})`, "gi");
    el.innerHTML = el.innerHTML.replace(regex, `<span class="gl-highlight" data-id="${person.id}">$1</span>`);

    // now find the span we just created and attach the listener
    el.querySelectorAll(".gl-highlight").forEach((span) => {
        span.addEventListener("click", async (e) => {
            e.stopPropagation();
            const id = span.dataset.id;
            const res = await fetch(`${API_URL}/person/${id}`);
            const data = await res.json();
            showCard(data, e.clientX, e.clientY);
        });
    });
}

function showCard(person, x, y) {
    document.getElementById("gl-card")?.remove();

    const initials = person.name
        .split(" ")
        .map((n) => n[0])
        .join("");
    const scoreColor = person.transparency_score < 40 ? "#c0392b" : person.transparency_score < 70 ? "#e67e22" : "#27ae60";

    const txRows = person.transactions
        .slice(0, 3)
        .map((tx) => {
            const amount = tx.amount < 0 ? `-£${Math.abs(tx.amount / 100).toLocaleString()}` : `+£${(tx.amount / 100).toLocaleString()}`;
            const amountColor = tx.amount < 0 ? "#c0392b" : "#27ae60";
            const desc = tx.description.replace("Donation — ", "").replace("Speaking fee — ", "").replace("Expenses — ", "");
            return `<div style="display:flex;justify-content:space-between;align-items:center;font-size:12px;padding:6px 8px;background:#f8f8f8;border-radius:6px;">
            <span style="color:#333;flex:1;margin-right:8px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${desc}</span>
            <span style="color:${amountColor};font-weight:600;white-space:nowrap;">${amount}</span>
        </div>`;
        })
        .join("");

    const topFlag = person.flags?.[0];
    const flagHTML = topFlag
        ? `
        <div style="background:#fff5f5;border:1px solid #fcc;border-radius:8px;padding:8px 10px;margin-bottom:12px;">
            <div style="font-size:10px;font-weight:600;color:#c0392b;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:3px;">Conflict flagged</div>
            <div style="font-size:11px;color:#555;line-height:1.4;">${topFlag.summary}</div>
        </div>`
        : "";

    // keep card on screen
    const cardWidth = 300;
    const left = x + cardWidth > window.innerWidth ? x - cardWidth - 10 : x + 10;
    const top = Math.min(y, window.innerHeight - 500);

    const card = document.createElement("div");
    card.id = "gl-card";
    card.style.cssText = `
        position:fixed;top:${top}px;left:${left}px;z-index:2147483647;
        width:${cardWidth}px;background:#fff;border-radius:12px;
        overflow:hidden;font-family:system-ui,sans-serif;
        border:1px solid rgba(0,0,0,0.12);
        box-shadow:0 8px 32px rgba(0,0,0,0.18);
    `;

    card.innerHTML = `
        <div style="background:#1a1a2e;padding:12px 14px;display:flex;align-items:center;justify-content:space-between;">
            <div style="display:flex;align-items:center;gap:8px;">
                <div style="width:24px;height:24px;background:#e63946;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:#fff;">GL</div>
                <span style="color:#fff;font-size:13px;font-weight:500;">Glass Ledger</span>
            </div>
            <button id="gl-close" style="background:none;border:none;color:rgba(255,255,255,0.5);font-size:16px;cursor:pointer;padding:0;line-height:1;">&#x2715;</button>
        </div>
        <div style="padding:14px;">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
                <div style="width:40px;height:40px;border-radius:50%;background:#fde8e8;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;color:#c0392b;flex-shrink:0;">${initials}</div>
                <div>
                    <div style="font-size:15px;font-weight:600;color:#111;">${person.name}</div>
                    <div style="font-size:11px;color:#888;margin-top:1px;">${person.role}</div>
                </div>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px;">
                <div style="background:#f8f8f8;border-radius:8px;padding:8px 10px;">
                    <div style="font-size:10px;color:#888;margin-bottom:2px;">Transparency</div>
                    <div style="font-size:18px;font-weight:700;color:${scoreColor};">${person.transparency_score}<span style="font-size:11px;font-weight:400;color:#aaa;">/100</span></div>
                </div>
                <div style="background:#f8f8f8;border-radius:8px;padding:8px 10px;">
                    <div style="font-size:10px;color:#888;margin-bottom:2px;">Flags</div>
                    <div style="font-size:18px;font-weight:700;color:${scoreColor};">${person.flags?.length ?? 0}<span style="font-size:11px;font-weight:400;color:#aaa;"> issues</span></div>
                </div>
            </div>
            <div style="margin-bottom:12px;">
                <div style="font-size:11px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:6px;">Recent transactions</div>
                <div style="display:flex;flex-direction:column;gap:5px;">${txRows}</div>
            </div>
            ${flagHTML}
            <a href="${FRONTEND_PERSON_URL}/${person.id}" target="_blank" style="display:block;text-align:center;background:#1a1a2e;color:#fff;padding:9px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;">View full profile →</a>
        </div>
    `;

    document.body.appendChild(card);
    document.getElementById("gl-close").addEventListener("click", () => card.remove());
    document.addEventListener(
        "click",
        (e) => {
            if (!card.contains(e.target)) card.remove();
        },
        { once: true },
    );
}

scanForNames();
