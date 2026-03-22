<script>
    import { onMount } from "svelte";
    import { subscribe, unsubscribe, getSubscriptions } from "$lib/subscriptions";
    import { user } from "$lib/stores/auth";

    let politicians = $state([]);
    let userSubscriptions = $state([]);
    let loading = $state(true);

    // Helper to calculate initials for each person in a list
    function getInitials(name) {
        return name
            ? name.split(" ").filter(Boolean).map((n) => n[0]).join("").toUpperCase()
            : "?";
    }

    onMount(async () => {
        try {
            // Fetch the list of politicians
            const response = await fetch(`http://127.0.0.1:5000/api/people/field/politician`);
            politicians = await response.json();

            // Fetch current user subscriptions if logged in
            if ($user) {
                userSubscriptions = await getSubscriptions();
            }
        } catch (error) {
            console.error("Fetch failed:", error);
        } finally {
            loading = false;
        }
    });

    async function toggleSubscribe(id) {
        if (!$user) {
            window.location.href = "/account";
            return;
        }

        const isSubscribed = userSubscriptions.includes(id);
        if (isSubscribed) {
            await unsubscribe(id);
            userSubscriptions = userSubscriptions.filter(subId => subId !== id);
        } else {
            await subscribe(id);
            userSubscriptions = [...userSubscriptions, id];
        }
    }

    // Calculations for the Summary Stats (Total of all politicians on page)
    let globalTotalReceived = $derived(
        politicians.reduce((acc, p) => {
            const personTotal = (p.transactions || []).reduce((sum, tx) => {
                const amt = Number(tx.amount || 0);
                return amt > 0 ? sum + amt : sum;
            }, 0);
            return acc + personTotal;
        }, 0) / 100
    );

    let globalFlagCount = $derived(
        politicians.reduce((acc, p) => acc + (p.flags?.length || 0), 0)
    );
</script>

<header id="top">
    <nav class="sticky-top navbar navbar-expand-lg navbar-light mt-0" style="border-bottom: 2px solid; margin-top: 5px; width: 100%;">
        <div class="container-fluid mx-1 mx-md-4">
            <a class="navbar-brand d-flex justify-content-center align-items-center" href="../">
                <h2 class="mb-0"><span>Glass</span> <span class="text-primary-red">Ledger</span></h2>
            </a>
            <div class="collapse navbar-collapse" id="navbarContent">
                <ul class="navbar-nav ms-auto fs-4">
                    <li class="nav-item"><a class="nav-link" href="../">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="../people">People</a></li>
                    <li class="nav-item"><a class="nav-link" href="../executives">Executives</a></li>
                    <li class="nav-item"><a class="nav-link" href="/">Politicians</a></li>
                    <li class="nav-item"><a class="nav-link" href="../account">Account</a></li>
                </ul>
            </div>
        </div>
    </nav>
</header>

<main class="mt-5">
    {#if loading}
        <div class="text-center text-white"><h3>Loading Politicians...</h3></div>
    {:else}
        <section class="row row-stats mx-1 mx-md-4">
            <div class="col-6 col-md-4 stat">
                <span class="stat_value">£{globalTotalReceived.toLocaleString("en-GB")}</span>
                <span class="stat_label">Global Total Received</span>
            </div>
            <div class="col-6 col-md-4 stat">
                <span class="stat_value">{politicians.length}</span>
                <span class="stat_label">Politicians Listed</span>
            </div>
            <div class="col-6 col-md-4 stat">
                <span class="stat_value">{globalFlagCount}</span>
                <span class="stat_label">Total Conflicts Flagged</span>
            </div>
        </section>

        {#each politicians as person}
            {@const is_Green = person.transparency_score > 70}
            {@const is_Orange = person.transparency_score <= 70 && person.transparency_score > 40}
            {@const is_Red = person.transparency_score <= 40}
            {@const isSubscribed = userSubscriptions.includes(person.id)}

            <div class="politician-entry mb-5 border-bottom pb-5">
                <section class="card-container row mx-1 mx-md-4">
                    <div class="col-12 col-sm-1 col-avatar">
                        <div class="avatar" class:is_Green class:is_Orange class:is_Red>
                            {getInitials(person.name)}
                        </div>
                    </div>

                    <div class="col-10 col-sm-8 col-info">
                        <div class="name-row"><h2>{person.name}</h2></div>
                        <p class="subtitle">
                            {person.role} · {person.party || person.company} · Score: {person.transparency_score}
                        </p>

                        <div class="tags">
                            {#each person.flags || [] as flag}
                                <span class="tag" class:tag-flagged={flag.severity == "high"}>
                                    Conflict: {flag.summary}
                                </span>
                            {/each}
                        </div>
                    </div>

                    <div class="col-12 col-sm-3 col-action">
                        <button class="btn btn-subscribed" onclick={() => toggleSubscribe(person.id)}>
                            {isSubscribed ? "Unsubscribe" : "Subscribe"}
                        </button>
                    </div>
                </section>

                {#if person.transactions?.length > 0}
                    <section class="recent-transactions mx-1 mx-md-4 mt-3">
                        <h4 class="text-white">Recent Transactions for {person.name}</h4>
                        {#each person.transactions as item}
                            <div class="card-container transaction-card row mx-1 mx-md-4 mb-2">
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
                {/if}
            </div>
        {/each}
    {/if}

    <div class="text-center mt-4">
        <button type="button" class="btn btn-dark btn-lg mb-3" onclick={() => window.scrollTo({ top: 0, behavior: "smooth" })}> Back To Top </button>
    </div>
</main>

<footer></footer>
