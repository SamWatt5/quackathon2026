<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import '../global.css';
	let { children } = $props();

	const currentYear = new Date().getFullYear();

</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<!-- Import Bootstrap-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">    

    <!-- Import Animation Library -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
	 <!-- Import Bootstrap-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

</svelte:head>

{@render children()}

<footer>
    <div class="container-fluid">
        <div class="row text-center justify-content-center align-items-center mt-5" style="border-top: 2px solid var(--Black);">
            <p>© {currentYear} Glass Ledger - All Rights Reserved</p>
        </div>
    </div>
</footer>
