<script>
  // aktueller Monat
  let month = new Date().getMonth(); // 0–11
  let bdaysReady = false;

  const monthNames = [
    "Januar", "Februar", "März", "April", "Mai", "Juni",
    "Juli", "August", "September", "Oktober", "November", "Dezember"
  ];

  const daysPerMonth = [
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
  ];

  let allBdays = [];

  let bdaysByMonth = Array.from({ length: 12 }, () => ({}));

  async function loadBdays() {
        const res = await fetch(`http://localhost:8000/bdays`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });

        return await res.json();
  }

  function prepareBdays(bdays) {
    // Reset
    let tmp = Array.from({ length: 12 }, () => ({}));

    for (const bday of bdays) {
      const [, m, d] = bday.birthday.split("-");
      const monthIndex = Number(m) - 1;
      const day = Number(d);

      if (!tmp[monthIndex][day]) {
        tmp[monthIndex][day] = [];
      }

      tmp[monthIndex][day].push(bday);
    }

    bdaysByMonth = tmp;   // jetzt ist alles gesetzt
    bdaysReady = true;     // Signal: fertig
  }

  function prevMonth() {
    month = (month + 11) % 12;
  }

  function nextMonth() {
    month = (month + 1) % 12;
  }

  // Initial laden
  loadBdays().then(bdays => {
    allBdays = bdays;
    prepareBdays(allBdays);
  });
</script>

<div class="nav">
  <button on:click={prevMonth}>←</button>
  <h2>{monthNames[month]}</h2>
  <button on:click={nextMonth}>→</button>
</div>

{#if !bdaysReady}
  <p>Lade Geburtstage…</p>
{:else}
  <div class="calendar">
    {#each Array(daysPerMonth[month]) as _, i}
      <div class="day">
        <div class="day-number">{i + 1}</div>

        {#each bdaysByMonth[month][String(i + 1)] ?? [] as bday}
          <a href={`#/get/${bday.id}`} class="bday"
            style="color: inherit; text-decoration: none; cursor: pointer;"  
            onmouseover="this.style.textDecoration='underline'" 
            onmouseout="this.style.textDecoration='none'">
            {bday.first_name} {bday.last_name} <br>
          </a>
        {/each}
      </div>
    {/each}
  </div>
{/if}



<style>
  .nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }

  .calendar {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 8px;
  }

  .day {
    border: 1px solid #ccc;
    min-height: 80px;
    padding: 6px;
  }

  .day-number {
    font-weight: bold;
  }
</style>
