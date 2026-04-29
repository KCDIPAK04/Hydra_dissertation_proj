
// Register Service Worker (ONLY HERE)
if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/firebase-messaging-sw.js")
    .then((reg) => {
        console.log("SW registered:", reg.scope);
    })
    .catch((err) => console.log("SW error:", err));
}

// GLOBAL FUNCTION (VERY IMPORTANT)
window.enableNotifications = async function () {

    const permission = await Notification.requestPermission();

    if (permission !== "granted") {
        console.log("Permission denied");
        return;
    }

    try {
        // Wait for SW
        const registration = await navigator.serviceWorker.ready;

        console.log("SW READY:", registration);

        // IMPORTANT: pass SW explicitly
        const token = await messaging.getToken({
    vapidKey: "BNtd_9yUqLMttllzvn2wbyJpp7r9wE-xAdhaK9vknzizJax4843AB2KBt8VfRJ4YpbZRDgALzf3Pl4QhejUh5FM",
    serviceWorkerRegistration: registration
});

        console.log("FCM TOKEN:", token);

        const response = await fetch("/save-token/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({ token })
        });

        console.log("Saved:", await response.json());

    } catch (err) {
        console.log("Token error:", err);
    }
};
// CSRF helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        const cookies = document.cookie.split(";");
        for (let c of cookies) {
            c = c.trim();
            if (c.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(c.split("=")[1]);
            }
        }
    }
    return cookieValue;
}