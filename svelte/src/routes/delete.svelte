<!-- src/svelte/routes/delete.svelte -->
<!--DELETE by id-->
<script>
    let value = "";
    let response = "";

    async function sendToBackend() {
        const res = await fetch(`http://localhost:8000/bdays/${encodeURIComponent(value)}`, {
            method: "DELETE",
            headers: { "Content-Type": "application/json" }
        });

        response = await res.json();
    }
</script>

<h1>Delete BDay</h1>

<input bind:value placeholder="ID eingeben…" />

<button on:click={sendToBackend}>Abschicken</button>

{#if response}
    <p>Antwort: {JSON.stringify(response)}</p>
{/if}
