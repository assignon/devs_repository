import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Skills from "../views/Skills.vue";
import Works from "../views/Works.vue";
import Description from "../views/Description.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/skills",
    name: "Skills",
    component: Skills,
  },
  {
    path: "/works",
    name: "Works",
    component: Works,
  },
  {
    path: "/work/:name",
    name: "Description",
    component: Description,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
