<!-- src/svelte/routes/edit_id.svelte -->
<!--UPDATE by id provided in the url-->
<script>
    let entry = null;
    let id = window.location.hash.split("/")[2];

    let fname = "";
    let lname = "";
    let bd = "";

    async function get_entry() {
        
        const res = await fetch(`http://localhost:8000/bdays/${id}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });

        entry = await res.json();
        fname = entry.first_name;
        lname = entry.last_name;
        bd = entry.birthday;
    }

    async function update_entry() {
        
        const res = await fetch(`http://localhost:8000/bdays/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                first_name: fname,
                last_name: lname,
                birthday: bd
            })
        });

        if (res.ok) {
            // Nach dem Speichern auf die Get-Seite zurückleiten
            window.location.href = `#/get/${id}`;
        } else {
            console.error("Fehler beim Speichern");
        }
    }

    get_entry();
</script>

{#if entry}
  <h1>Bearbeiten</h1>
    <input bind:value={bd} placeholder="YYYY-MM-DD" style="width: 200px;"/>
    <br/>
    <br/>
    <input bind:value={fname} placeholder="Vorname" style="width: 200px;"/>
    <br/>
    <br/>
    <input bind:value={lname} placeholder="Nachname" style="width: 200px;"/>
    <br/>
    <br/>
    <button on:click={update_entry}>Speichern</button>
{:else}
  <p>Lade Eintrag...</p>
{/if}
