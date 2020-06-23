import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import Notfound from "../components/NotFound";
import versions from "../page/versions"

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/home",
      name: 'Home',
      component: HelloWorld
    },
    // {
    //   path: "/customer",
    //   name: 'customer',
    //   component: Customer
    // },
    {
      path: "/versions",
      name: 'versions',
      component: versions
    },
    {
      path: '*',
      name: '404',
      component: Notfound
    },

  ]
})
