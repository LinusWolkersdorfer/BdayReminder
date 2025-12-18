<!-- src/svelte/routes/new.svelte -->
<!--POST bdays-->
<script>
    let response = "";
    let bday = "";
    let first = "";
    let last = "";

    async function sendToBackend() {
        const res = await fetch("http://localhost:8000/bdays", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                birthday: bday,
                first_name: first,
                last_name: last
            })
        });

        response = await res.json();
    }
</script>

<h1>New BDay</h1>

<input bind:value={bday} placeholder="YYYY-MM-DD" />
<input bind:value={first} placeholder="Vorname" />
<input bind:value={last} placeholder="Nachname" />

<button on:click={sendToBackend}>Abschicken</button>

{#if response}
    <p>Antwort: {JSON.stringify(response)}</p>
{/if}
