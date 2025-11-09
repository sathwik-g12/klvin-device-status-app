const API = "http://localhost:5000";

const companySelect = document.getElementById("companySelect");
const devicesContainer = document.getElementById("devicesContainer");
const searchInput = document.getElementById("searchInput");
const sortSelect = document.getElementById("sortSelect");
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");

let devices = [];

// Apply saved theme
if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark");
    themeIcon.classList.replace("fa-moon", "fa-sun");
}

// Theme Toggle
themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    const dark = document.body.classList.contains("dark");

    if (dark) {
        themeIcon.classList.replace("fa-moon", "fa-sun");
        localStorage.setItem("theme", "dark");
    } else {
        themeIcon.classList.replace("fa-sun", "fa-moon");
        localStorage.setItem("theme", "light");
    }
});

// Load Companies
async function loadCompanies() {
    const res = await fetch(`${API}/companies`);
    const data = await res.json();
    companySelect.innerHTML = data.companies.map(c => `<option value="${c.id}">${c.name}</option>`).join("");
    loadDevices(companySelect.value);
}

// Load Devices
async function loadDevices(companyId) {
    const res = await fetch(`${API}/devices/${companyId}`);
    const data = await res.json();
    devices = data.devices;
    renderDevices();
}

function renderDevices() {
    let filtered = devices.filter(d =>
        d.name.toLowerCase().includes(searchInput.value.toLowerCase())
    );

    if (sortSelect.value === "online") {
        filtered.sort((a, b) => a.status === "online" ? -1 : 1);
    } else if (sortSelect.value === "alpha") {
        filtered.sort((a, b) => a.name.localeCompare(b.name));
    }

    devicesContainer.innerHTML = filtered.map(d => `
        <div class="card">
            <div class="status-circle status-${d.status}"></div>
            <div class="device-info">
                <strong>${d.name}</strong><br>
                <small>${d.last_reading || "No Data"}</small>
            </div>
        </div>
    `).join("");
}

companySelect.addEventListener("change", () => loadDevices(companySelect.value));
searchInput.addEventListener("input", renderDevices);
sortSelect.addEventListener("change", renderDevices);

// Refresh every 8 sec
setInterval(() => loadDevices(companySelect.value), 8000);

// Init
loadCompanies();
