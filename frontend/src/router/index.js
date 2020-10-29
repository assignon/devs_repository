import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Skills from "../views/Skills.vue";
import Works from "../views/Works.vue";
import Description from "../views/Description.vue";
import Review from "../views/Review.vue";

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
  //review modes routes
  {
    path: "/review/:mode", //mode: [reviewer, input, view]
    name: "ReviewMode",
    component: Review,
  },
  // {
  //   path: "/review/:reviewer",
  //   name: "Home",
  //   component: Home,
  // },
  // {
  //   path: "/review/:reviewer",
  //   name: "Home",
  //   component: Home,
  // },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
