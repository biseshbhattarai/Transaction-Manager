<template>
<div>
  <div class="container">
    <router-link to="/"><button type="submit"  class="btn btn-primary">Go Back</button></router-link>
  </div>
   <div class="card my-4">
            <br>
            <h5 class="card-header">Update</h5>
            <div class="card-body">
              <div class="row">
                <div class="col-lg-6">
                  <form>
                    <div class="form-group">
                          <label for="exampleInputPassword1">No of sales</label>
                          <input type="number" class="form-control" step="1" v-model="product.no_of_sales" placeholder="No of sales...">
                        </div>
                        <div class="form-group">
                          <label for="exampleInputPassword1">Product Name</label>
                          <input type="text" class="form-control" v-model="product.product_name" placeholder="No of sales...">
                        </div>
                        <div class="checkbox">
                          <label><input v-model="product.credit" type="checkbox" value="">Credit</label>

                        </div>
                        <br>
                        <small>Optional field (Only required when credit is ticked.)</small>
                        <div  class="form-group">
                          <label>Creditor name</label>
                          <input class="form-control" type="text" v-model="product.creditor_name" placeholder="creditor name"/>
                        </div>
                     
                        <button type="submit" v-on:click.prevent="updateItem" class="btn btn-primary">Submit</button>
                  </form>
                </div>
               
              </div>
            </div>
          </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
  name : 'update',
  data () {
    return {
      product : {id: null, no_of_sales:null, creditor_name : null ,category: null, cost_amt:null, sales_amt:null, product_name : null, quantity:null, out_of_stock:null, credit : false, created : null, modified : null, user:null},
      on_credit : false,
      creditor : [{creditor_name : null, amt : null}],    
    }
  },
  methods : {
    getItem : function(){
      axios.get('http://127.0.0.1:8000/product/' + this.$route.params.id)
      .then(response => {
        this.product.id = response.data.id,
        this.product.product_name = response.data.product_name,
        this.product.no_of_sales = response.data.no_of_sales,
        this.product.credit = response.data.credit,
        this.product.user  = response.data.user,
        this.product.category = response.data.category,
        this.product.created = response.data.created,
        this.product.out_of_stock = response.data.out_of_stock,
        this.product.modified  = response.data.modified,
        this.product.sales_amt = response.data.sales_amt,
        this.product.cost_amt = response.data.cost_amt,
        this.product.quantity = response.data.quantity,
        this.product.creditor_name = response.data.creditor_name

      })
      .catch(err => console.log(err))
    },
    updateItem : function(){
      // console.log(this.product.credits)
      // if (this.product.credit == true){
      //   this.on_credit = true
      //   localStorage.setItem('creditor', this.creditor.creditor_name, this.credit.amt)
      // }
      // console.log(this.product)
   
      axios.put('http://127.0.0.1:8000/product/' + this.$route.params.id + '/', {
          // id: this.product.id,
          user: this.product.user,
          no_of_sales: this.product.no_of_sales,
          category: this.product.category,
          cost_amt: this.product.cost_amt,
          sales_amt: this.product.sales_amt,
          product_name: this.product.product_name,
          quantity: this.product.quantity,
          out_of_stock: this.product.out_of_stock,
          credit: this.product.credit,
          creditor_name : this.product.creditor_name
          // created : this.product.created
       
        })
        .then(response => console.log(response.data))
        .catch(err => console.log(err))
        this.$router.push('/')

    }
  },
  created(){
    this.getItem();
  }

}
</script>

<style>

</style>
