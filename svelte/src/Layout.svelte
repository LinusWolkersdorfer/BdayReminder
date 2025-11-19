<!-- src/Layout.svelte -->
<nav>
  <a href="#/">Home</a>
  <a href="#/page1">Page 1</a>
  <a href="#/page2">Page 2</a>
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
