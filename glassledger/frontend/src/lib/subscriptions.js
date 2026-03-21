import { db, auth } from "$lib/firebase";
import { doc, setDoc, deleteDoc, collection, getDocs } from "firebase/firestore";

export async function subscribe(personId) {
    const uid = auth.currentUser?.uid;
    if (!uid) return;
    await setDoc(doc(db, "users", uid, "subscriptions", String(personId)), { personId });
}

export async function unsubscribe(personId) {
    const uid = auth.currentUser?.uid;
    if (!uid) return;
    await deleteDoc(doc(db, "users", uid, "subscriptions", String(personId)));
}

export async function getSubscriptions() {
    const uid = auth.currentUser?.uid;
    if (!uid) return [];
    const snapshot = await getDocs(collection(db, "users", uid, "subscriptions"));
    return snapshot.docs.map((d) => d.data().personId);
}
