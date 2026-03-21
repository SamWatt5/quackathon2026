import { writable } from "svelte/store";
import { browser } from "$app/environment";
import { auth } from "$lib/firebase";
import { onAuthStateChanged } from "firebase/auth";

export const user = writable(null);
export const loading = writable(true);

if (browser) {
    onAuthStateChanged(auth, (firebaseUser) => {
        user.set(firebaseUser);
        loading.set(false);
    });
} else {
    loading.set(false);
}
