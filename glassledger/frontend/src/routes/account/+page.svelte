<script>
    import { onMount } from "svelte";
    import { user, loading } from "$lib/stores/auth";
    import { signInWithGoogle, logOut } from "$lib/firebase";
    import { getSubscriptions } from "$lib/subscriptions";
    import { browser } from "$app/environment";

    let people = $state([]);

    $effect(() => {
        if ($user) {
            loadSubscriptions();
        }
    });

    async function loadSubscriptions() {
        const ids = await getSubscriptions();
        if (ids.length === 0) return;
        const res = await fetch("http://localhost:5000/api/explore");
        const all = await res.json();
        people = all.filter((p) => ids.includes(p.id));
    }
</script>

{#if $loading}
    <p>Loading...</p>
{:else if $user}
    <h1>Your account</h1>
    <p>{$user.displayName}</p>
    <p>{$user.email}</p>
    <button on:click={logOut}>Sign out</button>

    <h2>Subscribed politicians</h2>
    {#if people.length === 0}
        <p>You have not subscribed to anyone yet.</p>
    {:else}
        {#each people as person}
            <div>
                <a href="/person/{person.id}">{person.name}</a>
                <span>{person.role}</span>
            </div>
        {/each}
    {/if}
{:else}
    <h1>Sign in</h1>
    <button on:click={signInWithGoogle}>Sign in with Google</button>
{/if}
