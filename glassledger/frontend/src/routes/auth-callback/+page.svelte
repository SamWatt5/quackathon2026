<script>
    import { onMount } from "svelte";
    import { auth, signInWithGoogle } from "$lib/firebase";
    import { browser } from "$app/environment";

    let status = $state("Signing you in...");

    onMount(async () => {
        if (!browser) return;

        if (!auth.currentUser) {
            await signInWithGoogle();
        }

        auth.onAuthStateChanged(async (firebaseUser) => {
            if (!firebaseUser) return;

            const token = await firebaseUser.getIdToken();

            window.postMessage(
                {
                    type: "GL_AUTH",
                    token,
                    user: {
                        uid: firebaseUser.uid,
                        name: firebaseUser.displayName,
                        email: firebaseUser.email,
                    },
                },
                "*",
            );

            status = "Signed in! You can close this tab.";
        });
    });
</script>

<h1>{status}</h1>
