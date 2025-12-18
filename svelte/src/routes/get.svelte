<!-- src/svelte/routes/get.svelte -->
<!--GET by id-->
<script>
    let value = "";
    let response = "";

    async function sendToBackend() {
        const res = await fetch(`http://localhost:8000/bdays/${encodeURIComponent(value)}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });

        response = await res.json();
    }
</script>

<h1>Get BDay by ID</h1>

<input bind:value placeholder="ID eingeben…" />

<button on:click={sendToBackend}>Abschicken</button>

{#if response}
    <p>Antwort: {JSON.stringify(response)}</p>
{/if}
