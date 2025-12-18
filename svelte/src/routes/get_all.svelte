<!-- src/svelte/routes/get_all.svelte -->
<!--GET all-->
<script>
    let response = "";

    async function sendToBackend() {
        const res = await fetch(`http://localhost:8000/bdays`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });

        response = await res.json();
    }
</script>

<h1>Get all BDays</h1>

<button on:click={sendToBackend}>Abschicken</button>

{#if response}
    <p>Antwort: {JSON.stringify(response)}</p>
{/if}
