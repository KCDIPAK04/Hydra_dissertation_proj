importScripts("https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging-compat.js");

firebase.initializeApp({
  apiKey: "AIzaSyAfMz4Dxs58ukCbFfkc8B7piGb9wMnUQI4",
  authDomain: "hydra-skincare.firebaseapp.com",
  projectId: "hydra-skincare",
  messagingSenderId: "584477765167",
  appId: "1:584477765167:web:38b28e09c18d2ee35320da"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log("Background message:", payload);

    self.registration.showNotification(payload.notification.title, {
        body: payload.notification.body,
        icon: "/static/dashboard/images/icon.png"
    });
});