<script>
    import { onMount } from "svelte";

    let profiles = $state([]);
    let currentPage = $state(1);
    let loading = $state(true);

    // Initial logic helper
    function getInitials(name) {
        return name
            ? name
                  .split(" ")
                  .filter(Boolean)
                  .map((n) => n[0])
                  .join("")
                  .toUpperCase()
            : "?";
    }

    onMount(async () => {
        const url = new URL(window.location.href);
        const queryParams = new URLSearchParams(url.search);

        // Get page from URL, default to 1
        currentPage = Number(queryParams.get("page") ?? 1);

        // Calculate the range of IDs (e.g., Page 1: 1-5, Page 2: 6-10)
        const startID = (currentPage - 1) * 5 + 1;
        const endID = startID + 4;

        try {
            const fetchPromises = [];

            // Create 5 fetch requests simultaneously
            for (let id = startID; id <= endID; id++) {
                fetchPromises.push(
                    fetch(`http://127.0.0.1:5000/api/person/${id}`)
                        .then((res) => (res.ok ? res.json() : null))
                        .catch(() => null), // Ignore failed IDs (e.g., if ID doesn't exist)
                );
            }

            // Wait for all 5 to finish
            const results = await Promise.all(fetchPromises);

            // Filter out any nulls (failed fetches) and update state
            profiles = results.filter((p) => p !== null);
            loading = false;
        } catch (error) {
            console.error("Directory fetch failed:", error);
            loading = false;
        }
    });

    function changePage(step) {
        const next = currentPage + step;
        window.location.href = `/?page=${next}`;
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
                    <li class="nav-item"><a class="nav-link" href="../">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="/">People</a></li>
                    <li class="nav-item"><a class="nav-link" href="../executives">Executives</a></li>
                    <li class="nav-item"><a class="nav-link" href="../politicians">Politicians</a></li>
                    <li class="nav-item"><a class="nav-link" href="../account">Account</a></li>
                </ul>
            </div>
        </div>
    </nav>
</header>

<main class="mt-5">
    {#if loading}
        <div class="text-center text-white mt-5">
            <h3>Loading Transparency Data...</h3>
        </div>
    {:else}
        <div class="profile-list">
            {#each profiles as person}
                {@const is_Green = person.transparency_score > 70}
                {@const is_Orange = person.transparency_score <= 70 && person.transparency_score > 40}
                {@const is_Red = person.transparency_score <= 40}

                <section class="card-container row mx-1 mx-md-4 mb-4">
                    <div class="col-2 col-sm-1 col-avatar">
                        <div class="avatar" class:is_Green class:is_Orange class:is_Red>
                            {getInitials(person.name)}
                        </div>
                    </div>

                    <div class="col-10 col-sm-8 col-info" id="top-card">
                        <div class="name-row">
                            <h2>{person.name}</h2>
                        </div>
                        <p class="subtitle">{person.role} · {person.party} · Transparency Score : {person.transparency_score}</p>

                        <div class="tags">
                            {#each person.flags as flag}
                                <span class="tag" class:tag-flagged={flag.severity == "high"}>
                                    Conflict: {flag.summary}
                                </span>
                            {/each}
                        </div>
                    </div>

                    <div class="col-12 col-sm-3 col-action">
                        <a href="/profile/?id={person.id}" class="btn btn-subscribed text-decoration-none"> View Profile </a>
                    </div>
                </section>
            {/each}
        </div>

        <div class="text-center mt-5 mb-5 d-flex justify-content-center gap-3">
            <button class="btn btn-dark" disabled={currentPage <= 1} onclick={() => changePage(-1)}> Previous </button>
            <span class="text-white align-self-center">Page {currentPage}</span>
            <button class="btn btn-dark" onclick={() => changePage(1)}> Next </button>
        </div>
    {/if}
</main>
