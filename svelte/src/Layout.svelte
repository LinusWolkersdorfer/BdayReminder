<!-- src/Layout.svelte -->
<nav>
  <a href="#/">Home</a>
  <a href="#/calendar">Kalender</a>
  <!--a href="#/new">New</a-->
  <!--a href="#/get">Get</a-->
  <!--a href="#/get_all">Get All</a-->
  <!--a href="#/delete">Delete</a-->
  <!--a href="#/edit">Edit</a-->
</nav>

<main>
  <slot></slot>
</main>

<style>
nav {
  background: #1a1a1a;
  padding: 10px;
}
nav a {
  color: var(--fg);
  margin-right: 20px;
  text-decoration: none;
}
main {
  padding: 20px;
}
</style>
