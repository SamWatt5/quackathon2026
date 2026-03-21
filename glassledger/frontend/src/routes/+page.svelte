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
                        <a class="nav-link" href="#politicians">Politicians</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#executives">Executives</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#institutions">Institutions</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#watchlist">Watchlist</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <script>
        import { onMount } from "svelte";
        import { apiData, drinkNames } from './store.js';

        let id = '';

        onMount(() => {
            const url = new URL(window.location.href);
            const queryParams = new URLSearchParams(url.search);
            id = queryParams.get('id') || 'No id provided';
        });


        onMount(async () => {
        fetch(`http://127.0.0.1:5000/api/person/${id}`)
        .then(response => response.json())
        .then(data => {
                console.log(data);
            apiData.set(data);
        }).catch(error => {
            console.log(error);
            return [];
        });
        });



        
    </script>
</header>

<main class="mt-5">
    <section class="card-container row mx-1 mx-md-4">
        <div class="col-2 col-sm-1 col-avatar">
            <div class="avatar">JH</div>
        </div>
        
        <p>Name: {name}</p>
        <p>Age: {age}</p>

        <div class="col-10 col-sm-8 col-info" id="top-card">
            <div class="name-row">
                <h2>James Harlow</h2>
            </div>
            <p class="subtitle">Secretary of State for Energy · Conservative MP · Elected 2010</p>
            <div class="tags">
                <span class="tag tag-flagged">Flagged: conflict of interest</span>
                <span class="tag">Energy sector</span>
                <span class="tag">North Sea Ventures donor</span>
                <span class="tag">4 declared interests</span>
            </div>
        </div>

        <div class="col-12 col-sm-3 col-action">
            <button type="button" class="btn btn-subscribed">Subscribed</button>
        </div>
    </section>
    
    <section class="row row-stats mx-1 mx-md-4">
        <div class="col-6 col-md-3 stat">
            <span class="stat_value">£84.5k</span>
            <span class="stat_label">Energy donations</span>
        </div>
        <div class="col-6 col-md-3 stat">
            <span class="stat_value">£210k</span>
            <span class="stat_label">Total received</span>
        </div>
        <div class="col-6 col-md-3 stat">
            <span class="stat_value">34</span>
            <span class="stat_label">Transparency score</span>
        </div>
        <div class="col-6 col-md-3 stat">
            <span class="stat_value">12</span>
            <span class="stat_label">Conflicts flagged</span>
        </div>
    </section>
    
    <section class="recent-transactions mx-1 mx-md-4">
        <h3>Recent Transactions</h3>
        <div class="card-container transaction-card row mx-1 mx-md-4">
            <div class="dot"></div>
            
            <div class="col-info">
                <h4 class="transaction-title">Donation - North Sea Ventures Ltd</h4>
                <p class="subtitle transaction-subtitle">Secretary of State for Energy · Conservative MP · Elected 2010</p>
            </div>
            <div class="transaction-details">
                <span class="amount">+22,000</span>
                <span class="tag">Energy sector</span>
            </div>
        </div>
        <div class="card-container transaction-card row mx-1 mx-md-4">
            <div class="dot"></div>
            
            <div class="col-info">
                <h4 class="transaction-title">Donation - North Sea Ventures Ltd</h4>
                <p class="subtitle transaction-subtitle">Secretary of State for Energy · Conservative MP · Elected 2010</p>
            </div>
            <div class="transaction-details">
                <span class="amount">+22,000</span>
                <span class="tag">Energy sector</span>
            </div>
        </div>
        <div class="card-container transaction-card row mx-1 mx-md-4">
            
            
            <div class="col-info">
                <div class="dot"></div>
                <h4 class="transaction-title">Donation - North Sea Ventures Ltd</h4>
                <p class="subtitle transaction-subtitle">Secretary of State for Energy · Conservative MP · Elected 2010</p>
            </div>
            <div class="transaction-details">
                <span class="amount">+22,000</span>
                <span class="tag">Energy sector</span>
            </div>
        </div>
        <div class="card-container transaction-card row mx-1 mx-md-4">
            <div class="dot"></div>
            
            <div class="col-info">
                <h4 class="transaction-title">Donation - North Sea Ventures Ltd</h4>
                <p class="subtitle transaction-subtitle">Secretary of State for Energy · Conservative MP · Elected 2010</p>
            </div>
            <div class="transaction-details">
                <span class="amount">+22,000</span>
                <span class="tag">Energy sector</span>
            </div>
        </div>


    </section>

    
    <div class="text-center mt-4">
        <button 
            type="button" 
            class="btn btn-dark btn-lg mb-3" 
            onclick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>
            Back To Top
        </button>
    </div>
</main>

<footer>
    </footer>
    
        
    
   