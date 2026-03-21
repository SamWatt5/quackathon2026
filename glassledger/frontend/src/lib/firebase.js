import { initializeApp, getApps } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut, connectAuthEmulator } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { browser } from "$app/environment";

const firebaseConfig = {
    apiKey: "AIzaSyCghBdqOBhf7Sf-V9F-UyWSRd_CjWd12lY",
    authDomain: "glass-ledger.firebaseapp.com",
    projectId: "glass-ledger",
    storageBucket: "glass-ledger.firebasestorage.app",
    messagingSenderId: "322578464441",
    appId: "1:322578464441:web:240b28501f7a24bc422568",
    measurementId: "G-5HV4QJQVWD",
};

const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApps()[0];

export const auth = getAuth(app);
export const db = getFirestore(app);
export const googleProvider = new GoogleAuthProvider();

if (browser) {
    auth.useDeviceLanguage();
}

export async function signInWithGoogle() {
    if (!browser) return;
    try {
        const result = await signInWithPopup(auth, googleProvider);
        console.log("Signed in:", result.user.displayName);
        return result.user;
    } catch (e) {
        console.error("Sign in error:", e.code, e.message);
    }
}

export async function logOut() {
    await signOut(auth);
}
