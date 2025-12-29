<!-- src/svelte/routes/get_id.svelte -->
<!--GET by id provided in the url-->
<script>
    import { onMount } from "svelte";

    let entry = null;
    let id = window.location.hash.split("/")[2];
    let showModal = false; // Steuert, ob das Modal angezeigt wird

    // Funktion zum Löschen des Eintrags
    async function deleteEntry() {
        const res = await fetch(`http://localhost:8000/bdays/${id}`, {
        method: "DELETE", // DELETE-Methode verwenden
        headers: {
            "Content-Type": "application/json",
        },
        });

        if (res.ok) {
            window.location.href = `#/`;
        } else {
            console.error("Fehler beim Löschen");
        }
    }

    function transformBday(dateStr) {
        const months = [
            "Januar", "Februar", "März", "April", "Mai", "Juni",
            "Juli", "August", "September", "Oktober", "November", "Dezember"
        ];

        const date = new Date(dateStr); // String zu Date-Objekt umwandeln
        const day = date.getDate(); // Holen des Tages
        const month = months[date.getMonth()]; // Holen des Monats (aus dem Array)
        const year = date.getFullYear(); // Holen des Jahres


        return `${day}. ${month} ${year}`;
    }

    async function sendToBackend() {
        
        const res = await fetch(`http://localhost:8000/bdays/${id}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });

        entry = await res.json();
    }

    // Rufe die Funktion beim Laden der Komponente auf
    onMount(() => {
        sendToBackend();
    });

    // Modal schließen
    function closeModal() {
        showModal = false;
    }

    // Modal öffnen
    function openModal() {
        showModal = true;
    }
</script>

{#if entry}
  <h1>{entry.first_name} {entry.last_name}</h1>
  <h1>{transformBday(entry.birthday)}</h1>

  <a href="#/edit/{id}" style="text-decoration: none;">
    <button>Bearbeiten</button>
  </a>
  <div style="text-decoration: none;">
    <button style="background-color: red" on:click={openModal}>Löschen</button>
  </div>
{:else}
  <p>Lade Eintrag...</p>
{/if}

{#if showModal}
  <div class="modal">
    <div class="modal-content">
      <h2 style="color:black" >Willst du diesen Eintrag wirklich löschen?</h2>
      <button on:click={deleteEntry}>Ja, löschen</button>
      <button style="background-color: gray" on:click={closeModal}>Abbrechen</button>
    </div>
  </div>
{/if}

<style>
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Hintergrund dunkel */
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
  }

  button {
    padding: 8px 16px;
    margin: 10px;
    font-size: 1rem;
    cursor: pointer;
    border-radius: 5px;
  }

  .modal button {
    background-color: #f44336;
    color: white;
  }

  .modal button:hover {
    background-color: #d32f2f;
  }
</style>