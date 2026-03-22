<script>
    import { onMount } from "svelte";
    import { subscribe, unsubscribe, getSubscriptions } from "$lib/subscriptions";
    import { user } from "$lib/stores/auth";

    let personID = 0;
    let name = $state("");
    let company = $state("");
    let party = $state("");
    let role = $state("");
    let transactions = $state([]);
    let transparency_score = $state(0);
    let flags = $state([]);
    let subscribed = $state(false);

    let initials = $derived(
        name
            ? name
                  .split(" ")
                  .filter(Boolean)
                  .map((n) => n[0])
                  .join("")
                  .toUpperCase()
            : "?",
    );

    onMount(async () => {
        const url = new URL(window.location.href);
        personID = Number(new URLSearchParams(url.search).get("id") ?? 0);

        if (!personID) {
            console.error("No id provided in URL");
            return;
        }

        try {
            const response = await fetch(`http://127.0.0.1:5000/api/person/${personID}`);
            const data = await response.json();
            ({ name, party, company, role, transactions, transparency_score, flags } = data);

            // check subscription status after we have the person data
            if ($user) {
                const subs = await getSubscriptions();
                subscribed = subs.includes(personID);
            }
        } catch (error) {
            console.error("Fetch failed:", error);
        }
    });

    async function toggleSubscribe() {
        if (!$user) {
            console.log("No user logged in");
            window.location.href = "/account";
            return;
        }

        if (subscribed) {
            await unsubscribe(personID);
        } else {
            await subscribe(personID);
        }
        subscribed = !subscribed;
    }

    let is_Green = $derived(transparency_score > 70);
    let is_Orange = $derived(transparency_score <= 70 && transparency_score > 40);
    let is_Red = $derived(transparency_score <= 40);

    let totalReceived = $derived(
        transactions.reduce((sum, tx) => {
            const amt = Number(tx.amount || 0);
            return amt > 0 ? sum + amt : sum;
        }, 0) / 100,
    );

    let flagCount = $derived(flags.length);
</script>

<header id="top">
    <nav class="sticky-top navbar navbar-expand-lg navbar-light mt-0" style="border-bottom: 2px solid; margin-top: 5px; width: 100%;" aria-label="Main navigation for Glass Ledger">
        <div class="container-fluid mx-1 mx-md-4">
            <a class="navbar-brand d-flex justify-content-center align-items-center" href="../" aria-label="Go to Glass Ledger home page">
                <h2 class="mb-0"><span>Glass</span> <span class="text-primary-red">Ledger</span></h2>
            </a>

            <button class="navbar-toggler collapsed d-flex d-lg-none flex-column justify-content-around" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="toggler-icon top-bar"></span>
                <span class="toggler-icon middle-bar"></span>
                <span class="toggler-icon bottom-bar"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarContent">
                <ul class="navbar-nav ms-auto fs-4 justify-content-center align-items-center">
                    <li class="nav-item"><a class="nav-link" href="../">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="../people?field=none">People</a></li>
                    <li class="nav-item"><a class="nav-link" href="../people?field=executive">Executives</a></li>
                    <li class="nav-item"><a class="nav-link" href="../people?field=politician">Politicians</a></li>
                    <li class="nav-item"><a class="nav-link" href="../peopleaccount">Account</a></li>
                </ul>
            </div>
        </div>
    </nav>
</header>

<main class="mt-5">
    <section class="card-container row mx-1 mx-md-4">
        <div class="col-12 col-sm-1 col-avatar">
            <div class="avatar" class:is_Green class:is_Orange class:is_Red>{initials}</div>
        </div>

        <div class="col-10 col-sm-8 col-info" id="top-card">
            <div class="name-row">
                <h2>{name}</h2>
            </div>
            <p class="subtitle">{role} · {party ? party != 'none' : company} · Transparency Score : {transparency_score}</p>

            <div class="tags">
                {#each flags as flag}
                    <span class="tag" class:tag-flagged={flag.severity == "high"}>Conflict: {flag.summary}</span>
                {/each}
            </div>
        </div>
        <div class="col-12 col-sm-3 col-action">
            <button class="btn btn-subscribed" onclick={toggleSubscribe}>
                {subscribed ? "Unsubscribe" : "Subscribe"}
            </button>
        </div>
    </section>

    <section class="row row-stats mx-1 mx-md-4">
        <div class="col-6 col-md-4 stat">
            <span class="stat_value">
                £{totalReceived.toLocaleString("en-GB")}
            </span>
            <span class="stat_label">Total received From Recent</span>
        </div>
        <div class="col-6 col-md-4 stat">
            <span class="stat_value">{transparency_score}</span>
            <span class="stat_label">Transparency score</span>
        </div>
        <div class="col-6 offset-3 offset-md-0 col-md-4 stat">
            <span class="stat_value">{flagCount}</span>
            <span class="stat_label">Conflicts flagged</span>
        </div>
    </section>

    <section class="recent-transactions mx-1 mx-md-4">
        <h3>Recent Transactions</h3>
        {#each transactions as item}
            <script>
                item.amount = item.amount / 100;
            </script>
            <div class="card-container transaction-card row mx-1 mx-md-4">
                <div class="dot" class:is_Green={item.amount > 0} class:is_Red={item.amount < 0}></div>

                <div class="col-info">
                    <h4 class="transaction-title">{item.description}</h4>
                    <p class="subtitle transaction-subtitle">{item.source}</p>
                </div>
                <div class="transaction-details">
                    <span class="amount" class:is_Green={item.amount > 0} class:is_Red={item.amount < 0}>
                        £{(item.amount / 100).toLocaleString("en-GB")}
                    </span>
                    <span class="tag">{item.date}</span>
                </div>
            </div>
        {/each}
    </section>

    <div class="text-center mt-4">
        <button type="button" class="btn btn-dark btn-lg mb-3" onclick={() => window.scrollTo({ top: 0, behavior: "smooth" })}> Back To Top </button>
    </div>
</main>

<footer></footer>
