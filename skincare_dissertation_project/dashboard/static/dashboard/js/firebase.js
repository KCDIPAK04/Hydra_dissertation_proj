// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAfMz4Dxs58ukCbFfkc8B7piGb9wMnUQI4",
  authDomain: "hydra-skincare.firebaseapp.com",
  projectId: "hydra-skincare",
  storageBucket: "hydra-skincare.firebasestorage.app",
  messagingSenderId: "584477765167",
  appId: "1:584477765167:web:38b28e09c18d2ee35320da",
  measurementId: "G-5YPCR501QC"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Messaging instance
const messaging = firebase.messaging();