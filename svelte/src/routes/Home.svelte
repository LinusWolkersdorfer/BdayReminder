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
    const month = String(today.getMonth() + 1).padStart(2, "0");

    let age = today.getFullYear() - birth.getFullYear();

    // januar
    if (dateStr.substring(5, 7) == "01") {
      if(month != "01") {
        age += 1;
      }
    }
  
    return age;
  }

  let bdays = [];

  async function loadBirthdays(days) {
    const res = await fetch(
      `http://localhost:8000/bdays/upcoming?days=${days}`
    );
    bdays = await res.json();
  }

  function newrounter() {
    window.location.href = `#/new`;
  }

  // beim Laden der Seite
  loadBirthdays(7);
</script>

<button on:click={newrounter} style="background-color: green" >+</button>

<h1>Kommende Geburtstage</h1>

<div style="margin-bottom: 1rem;">
  <select
    id="days"
    
    on:change={event => loadBirthdays(event.target.value)}
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
    <option value="7" selected>7 Tage</option>
    <option value="14">14 Tage</option>
    <option value="31">31 Tage</option>
  </select>
</div>

<br>

<ul style="padding-left: 0; margin-left: 0;">
  {#each bdays as b}
  <li>
    <a href={`#/get/${b.id}`} 
    style="color: inherit; text-decoration: none; cursor: pointer;"  
    onmouseover="this.style.textDecoration='underline'" 
    onmouseout="this.style.textDecoration='none'">
  {b.first_name} {b.last_name}
  wird am {formatDayMonth(b.birthday)}
  {getTurningAge(b.birthday)} Jahre alt
    </a>
  </li>

  {/each}
</ul>
