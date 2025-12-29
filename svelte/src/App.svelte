<!-- src/App.svelte -->
<script>
  import Router from 'svelte-spa-router';
  import Layout from './Layout.svelte';
  import Home from './routes/Home.svelte';
  import Page1 from './routes/new.svelte';
  //import Page2 from './routes/get.svelte';
  //import Page3 from './routes/get_all.svelte';
  //import Page4 from './routes/delete.svelte';
  //import Page5 from './routes/edit.svelte';
  import Page6 from './routes/get_id.svelte';
  import Page7 from './routes/edit_id.svelte';
  import Page8 from './routes/calendar.svelte';

  const routes = {
    '/': Home,
    '/new': Page1,
    //'/get': Page2,
    //'/get_all': Page3,
    //'/delete': Page4,
    //'/edit': Page5
    '/get/:id': Page6,
    '/edit/:id': Page7,
    '/calendar/': Page8
  }
</script>

<Layout>
  <Router {routes} />
</Layout>
