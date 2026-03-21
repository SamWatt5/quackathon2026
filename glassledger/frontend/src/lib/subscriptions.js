import { db, auth } from "$lib/firebase";
import { doc, setDoc, deleteDoc, collection, getDocs } from "firebase/firestore";

/**
 * @param {any} personId
 */
export async function subscribe(personId) {
    const uid = auth.currentUser?.uid;
    if (!uid) return;
    await setDoc(doc(db, "users", uid, "subscriptions", String(personId)), { personId });
}

/**
 * @param {any} personId
 */
export async function unsubscribe(personId) {
    const uid = auth.currentUser?.uid;
    if (!uid) return;
    await deleteDoc(doc(db, "users", uid, "subscriptions", String(personId)));
}

export async function getSubscriptions() {
    const uid = auth.currentUser?.uid;
    if (!uid) return [];
    const snapshot = await getDocs(collection(db, "users", uid, "subscriptions"));
    return snapshot.docs.map((doc) => doc.data().personId);
}
