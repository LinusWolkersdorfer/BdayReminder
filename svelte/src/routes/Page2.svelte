<!-- src/svelte/routes/Page2.svelte -->
<script>
    let value = "";
    let response = "";

    async function sendToBackend() {
        const res = await fetch("http://localhost:8000/", {
            method: "GET",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ data: value })
        });

        response = await res.json();
    }
</script>

<h1>Backend-Test (Page 2)</h1>

<input bind:value placeholder="Wert eingeben…" />

<button on:click={sendToBackend}>Abschicken</button>

{#if response}
    <p>Antwort: {JSON.stringify(response)}</p>
{/if}
