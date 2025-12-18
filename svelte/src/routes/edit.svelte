<!-- src/svelte/routes/edit.svelte -->
<!--PUT bdays-->
<script>
    let value = "";
    let response = "";
    let bday = "";
    let first = "";
    let last = "";

    async function sendToBackend() {
        const res = await fetch(`http://localhost:8000/bdays/${encodeURIComponent(value)}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                first_name: first,
                last_name: last,
                birthday: bday
            })
        });

        response = await res.json();
    }
</script>

<h1>Edit BDay</h1>

<input bind:value={value} placeholder="ID eingeben..." />

<input bind:value={bday} placeholder="YYYY-MM-DD" />
<input bind:value={first} placeholder="Vorname" />
<input bind:value={last} placeholder="Nachname" />

<button on:click={sendToBackend}>Abschicken</button>

{#if response}
    <p>Antwort: {JSON.stringify(response)}</p>
{/if}
