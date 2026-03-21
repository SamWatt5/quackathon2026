<script>
    import { onMount } from "svelte";
    import { user, loading } from "$lib/stores/auth";
    import { signInWithGoogle, logOut, auth } from "$lib/firebase";
    import { getRedirectResult } from "firebase/auth";
    import { browser } from "$app/environment";

    onMount(async () => {
        if (!browser) return;
        try {
            const result = await getRedirectResult(auth);
            if (result?.user) {
                console.log("Redirect result user:", result.user.displayName);
                user.set(result.user);
            }
        } catch (e) {
            console.error("Redirect error:", e);
        }
    });
</script>

{#if $loading}
    <p>Loading...</p>
{:else if $user}
    <h1>Your account</h1>
    <p>{$user.displayName}</p>
    <p>{$user.email}</p>
    <button on:click={logOut}>Sign out</button>
{:else}
    <h1>Sign in</h1>
    <button on:click={signInWithGoogle}>Sign in with Google</button>
{/if}
