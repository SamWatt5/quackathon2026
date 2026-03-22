<script>
    import { onMount } from "svelte";
    import { page } from '$app/stores'; // 1. Import the page store

    let field = $state('none');
    let profiles = $state([]);
    let currentPage = $state(1);
    let loading = $state(true);

    function getInitials(name) {
        return name ? name.split(" ").filter(Boolean).map((n) => n[0]).join("").toUpperCase() : "?";
    }

    // 2. Use $effect to watch for URL changes
    $effect(() => {
        // This line makes the entire effect "subscribe" to URL changes
        const url = $page.url; 
        const queryParams = url.searchParams;

        currentPage = Number(queryParams.get("page") ?? 1);
        field = queryParams.get("field") ?? 'none';
        
        loadProfiles();
    });

    async function loadProfiles() {
        loading = true;
        const startID = (currentPage - 1) * 5 + 1;
        const endID = startID + 4; // Use +4 to fetch exactly 5 items (e.g. 1, 2, 3, 4, 5)

        try {
            if (field === 'none') {
                const fetchPromises = [];
                for (let id = startID; id <= endID; id++) {
                    fetchPromises.push(
                        fetch(`http://127.0.0.1:5000/api/person/${id}`)
                            .then((res) => (res.ok ? res.json() : null))
                            .catch(() => null)
                    );
                }
                const results = await Promise.all(fetchPromises);
                profiles = results.filter((p) => p !== null);
            } else {
                const response = await fetch(`http://127.0.0.1:5000/api/people/field/${field}`);
                const allProfiles = await response.json();
                
                // Note: startID-1 because array indices start at 0
                const displayedPeople = allProfiles.slice(startID - 1, startID + 4);
                
                const fetchPromises = displayedPeople.map(person =>
                    fetch(`http://127.0.0.1:5000/api/person/${person.id}`)
                        .then((res) => (res.ok ? res.json() : null))
                        .catch(() => null)
                );
                
                const results = await Promise.all(fetchPromises);
                profiles = results.filter((p) => p !== null);
            }
        } catch (error) {
            console.error("Fetch failed:", error);
        } finally {
            loading = false;
        }
    }

    function changePage(step) {
        const next = currentPage + step;
        // Navigation will now trigger the $effect above
        window.location.href = `/?page=${next}&field=${field}`;
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
                    <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="/?field=none">People</a></li>
                    <li class="nav-item"><a class="nav-link" href="/?field=executive">Executives</a></li>
                    <li class="nav-item"><a class="nav-link" href="/?field=politician">Politicians</a></li>
                    <li class="nav-item"><a class="nav-link" href="/account">Account</a></li>
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
        <div class="profile-list col-12">
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
                        <p class="subtitle">{person.role} {person.party ? person.party != 'none' : person.company} · Transparency Score : {person.transparency_score}</p>

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
