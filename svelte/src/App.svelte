<!-- src/App.svelte -->
<script>
  import Router from 'svelte-spa-router';
  import Layout from './Layout.svelte';
  import Home from './routes/Home.svelte';
  import Page1 from './routes/new.svelte';
  import Page2 from './routes/get.svelte';
  import Page3 from './routes/get_all.svelte';
  import Page4 from './routes/delete.svelte';
  import Page5 from './routes/edit.svelte';

  const routes = {
    '/': Home,
    '/new': Page1,
    '/get': Page2,
    '/get_all': Page3,
    '/delete': Page4,
    '/edit': Page5
  }
</script>

<Layout>
  <Router {routes} />
</Layout>
