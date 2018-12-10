import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Update from '@/components/Update'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main
    },
    {
      path : '/:id',
      name : 'update',
      component : Update
    }


  ]
})
