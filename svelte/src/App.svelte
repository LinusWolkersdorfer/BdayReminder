<!-- src/App.svelte -->
<script>
  import Router from 'svelte-spa-router';
  import Layout from './Layout.svelte';
  import Home from './routes/Home.svelte';
  import Page1 from './routes/Page1.svelte';
  import Page2 from './routes/Page2.svelte';

  const routes = {
    '/': Home,
    '/page1': Page1,
    '/page2': Page2
  }
</script>

<Layout>
  <Router {routes} />
</Layout>
