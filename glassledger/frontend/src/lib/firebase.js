import { initializeApp, getApps } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut, connectAuthEmulator } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { PUBLIC_FIREBASE_API_KEY, PUBLIC_FIREBASE_AUTH_DOMAIN, PUBLIC_FIREBASE_PROJECT_ID, PUBLIC_FIREBASE_STORAGE_BUCKET, PUBLIC_FIREBASE_MESSAGING_SENDER_ID, PUBLIC_FIREBASE_APP_ID } from "$env/static/public";
import { browser } from "$app/environment";

const firebaseConfig = {
    apiKey: PUBLIC_FIREBASE_API_KEY,
    authDomain: PUBLIC_FIREBASE_AUTH_DOMAIN,
    projectId: PUBLIC_FIREBASE_PROJECT_ID,
    storageBucket: PUBLIC_FIREBASE_STORAGE_BUCKET,
    messagingSenderId: PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
    appId: PUBLIC_FIREBASE_APP_ID,
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
