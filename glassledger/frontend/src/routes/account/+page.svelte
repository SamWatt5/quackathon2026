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

<header id="top">
    <nav class="sticky-top navbar navbar-expand-lg navbar-light mt-0" style="border-bottom: 2px solid; margin-top: 5px; width: 100%;" aria-label="Main navigation for Glass Ledger">
        <div class="container-fluid mx-1 mx-md-4">
            <a class="navbar-brand d-flex justify-content-center align-items-center" href="/" aria-label="Go to Glass Ledger home page">
                <h2 class="mb-0"><span>Glass</span> <span class="text-primary-red">Ledger</span></h2>
            </a>

            <button class="navbar-toggler collapsed d-flex d-lg-none flex-column justify-content-around" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="toggler-icon top-bar"></span>
                <span class="toggler-icon middle-bar"></span>
                <span class="toggler-icon bottom-bar"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarContent">
                <ul class="navbar-nav ms-auto fs-4 justify-content-center align-items-center">
                    <li class="nav-item">
                        <a class="nav-link" href="../">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/">Account</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</header>
<main>
    <div class="log-in-container">
        <section class="log-in">
            <div class="log-in-col">
                {#if $loading}
                    <p>Loading...</p>
                {:else if $user}
                    <h1>Your account</h1>
                    <p>{$user.displayName}</p>
                    <p>{$user.email}</p>
                    <button class="btn btn-subscribed text-decoration-none mb-5" on:click={logOut}>Sign out</button>

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
                    <button class="btn btn-subscribed text-decoration-none" on:click={signInWithGoogle}>Sign in with Google</button>
                {/if}
        </div>  
        
        
    </section>
    </div>
    
</main>
    
    

