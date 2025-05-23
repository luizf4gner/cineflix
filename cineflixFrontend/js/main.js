const toggle = document.getElementById("toggle-theme");
toggle.onclick = () => {
    document.body.classList.toggle("dark-mode");
    toggle.textContext = document.body.classList.contains("dark-mode") ? "Light Mode" : "Dark Mode";
};