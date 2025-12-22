<!-- src/svelte/routes/Home.svelte -->
<script>
  function formatDayMonth(dateStr) {
  const d = new Date(dateStr);
  const day = String(d.getDate()).padStart(2, "0");
  const month = String(d.getMonth() + 1).padStart(2, "0");
  return `${day}.${month}`;
}


  function getTurningAge(dateStr) {
    const birth = new Date(dateStr);
    const today = new Date();

    let age = today.getFullYear() - birth.getFullYear();

    // januar
    if (dateStr.substring(5, 7) == "01") {
      age += 1;
    }
  
    return age;
  }

  let days = 31;
  let bdays = [];

  async function loadBirthdays() {
    const res = await fetch(
      `http://localhost:8000/bdays/upcoming?days=${days}`
    );
    bdays = await res.json();
  }

  // beim Laden der Seite
  loadBirthdays();
</script>

<h1>Kommende Geburtstage</h1>

<div style="margin-bottom: 1rem;">
  <select
    id="days"
    bind:value={days}
    on:change={loadBirthdays}
    style="
      padding: 8px 12px;
      font-size: 0.95rem;
      border-radius: 8px;
      border: 1px solid #ccc;
      background-color: gray;
      cursor: pointer;
      min-width: 120px;
    "
  >
    <option value="7">7 Tage</option>
    <option value="14">14 Tage</option>
    <option value="31">31 Tage</option>
  </select>
</div>



<ul>
  {#each bdays as b}
    <p>
  {b.first_name} {b.last_name}
  wird am {formatDayMonth(b.birthday)}
  {getTurningAge(b.birthday)} Jahre alt
</p>

  {/each}
</ul>
