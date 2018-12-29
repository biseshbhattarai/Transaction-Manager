<template>

  <body>

    <!-- Navigation -->


    <!-- Page Content -->
    
    <div class="container">
      <button v-on:click="getProfit">Load data</button>

      <div class="row">

        <!-- Blog Entries Column -->
        <div class="col-md-8">

          <h1 class="my-4">Transaction Mananger
          </h1>

          <!-- Blog Post -->
          <div class="card mb-4">
            <div class="card-body">
              <h2 class="card-title">Items</h2>
                      <ul class="list-unstyled mb-0"  v-for="item in items" :key="item.id" >
                          <li><router-link v-bind:to="{name: 'update', params:{id:item.id}}" >{{item.product_name}}</router-link></li>

                        

                    
                   
                  </ul>
                        <ul class="list-unstyled mb-0" v-for="item in credit_products" :key="item.id"  >
                    
                      <li><router-link v-bind:to="{name: 'update', params:{id:item.id}}" >{{item.product_name}} <small>Payment on credit</small></router-link></li>

                    
                   
                  </ul>
                  <ul class="list-unstyled mb-0" v-for="item in out_of_stock_products" :key="item.id" >
                    
                     
                      <li><router-link v-bind:to="{name: 'update', params:{id:item.id}}" >{{item.product_name}} <small>Out of stock</small></router-link></li>

                    
                   
                  </ul><br>
                  <ul class="list-unstyled mb-0" v-for="item in credit_and_out_of_stock" :key="item.id" >
                    
                    
                      <li><router-link v-bind:to="{name: 'update', params:{id:item.id}}"   >{{item.product_name}} <small>Credit and out of stock</small></router-link></li>

                    
                   
                  </ul>
            </div>
            <div class="card-footer text-muted">
             
            </div>
          </div>


            <div v-if = "show" class="card mb-4">
            <div class="card-body">
              <h2 class="card-title">{{searchResults.product_name}}</h2>
              <ul class="list-unstyled mb-0"  >
                <li>Quantity : {{searchResults.quantity}}</li>
                <li>No of sales : {{searchResults.no_of_sales}}</li>
                <li>Category : {{searchResults.category}}</li>
                <li>Sales amount : {{searchResults.sales_amt}}</li>
                <li>Cost amount : {{searchResults.cost_amt}}</li>
                <li>Creditor detail : {{searchResults.creditor_name}}</li>
                <li>Remaining stock : {{searchResults.remaining_stock}}</li>

                <!-- <li>Sales amount : {{searchResults.sales_amt}}</li> -->


              </ul>

            </div>
          

            </div>
            
            <div v-if="old_view" class="card-footer">
               
                <!-- <li>Sales amount : {{searchResults.sales_amt}}</li> -->


              </ul>

            </div>
          
          


      
          <!-- Pagination -->
 
        </div>

        <!-- Sidebar Widgets Column -->
        <div class="col-md-4">

          <!-- Search Widget -->
          <div class="card my-4">
            <h5 class="card-header">Search</h5>
            <div class="card-body">
              <div class="input-group">
               <select v-model="searchitem" class="form-control" id="exampleFormControlSelect1">
                            <option v-for="category in all_items" :key="category.id">{{category.product_name}}</option>
               </select>                
                            <span class="input-group-btn">
                  <button v-on:click.prevent="searchProduct"  class="btn btn-secondary" type="button">Go!</button>
                </span>
              </div>
            </div>
          </div>

          <!-- Categories Widget -->
          <div class="card my-4">
            <h5 class="card-header">Add an Item</h5>
            <div class="card-body">
              <div class="row">
                <div class="col-lg-6">
                  <form  v-if="no_view">
                        <div class="form-group">
                          <label for="exampleInputEmail1">Username</label>
                          <input type="text" class="form-control" id="exampleInputEmail1" v-model="user">
                        </div>
                        <div class="form-group">
                          <label for="exampleFormControlSelect1">Category</label>
                          <select v-model="category" class="form-control" id="exampleFormControlSelect1">
                            <option v-for="category in categories" :key="category.id">{{category.id}}</option>
                           
                          </select>
                        </div>
                        <div class="form-group">
                          <label for="exampleInputPassword1">Product</label>
                          <input type="text" class="form-control" v-model="product_name" id="exampleInputPassword1" placeholder="Product name....">

                          </div>
                        <div class="form-group">
                          <label for="exampleInputPassword1">Cost amount</label>
                          <input type="integer" class="form-control" v-model="cost_amt" id="exampleInputPassword1" placeholder="Cost amt...">
                        </div>
                        <div class="form-group">
                          <label for="exampleInputPassword1">Sales amount</label>
                          <input type="integer" class="form-control" v-model="sales_amt" id="exampleInputPassword1" placeholder="Sales amt....">
                        </div>
                        <div class="form-group">
                          <label for="exampleInputPassword1">No of sales</label>
                          <input type="integer" class="form-control" id="exampleInputPassword1" v-model="no_of_sales" placeholder="No of sales...">
                        </div>
                        <div class="form-group">
                          <label for="exampleInputPassword1">Quantity</label>
                          <input type="integer" class="form-control" v-model="quantity" id="exampleInputPassword1" placeholder="Quantity....">
                        </div>
                       
                        <button type="submit" v-on:click.prevent="postProduct" class="btn btn-primary">Submit</button>
                  </form>
                </div>
               
              </div>
            </div>
            <br>
            <button type="submit" v-on:click.prevent="closeTransaction" class="btn btn-primary">Close transaction</button>

          </div>

      
          <!-- Side Widget -->
          <div  class="card my-4">
            <h5 class="card-header">Transaction</h5>
            <div class="card-body">
              <p>Total sales : {{fetch_total_sales}}</p>
              <br>
              <h4>Older Transactions</h4>
              <ul v-for="old in old_data" v-bind:key="old.date" class="list-unstyled mb-0"  >
                <li><strong>{{old.date}}</strong> : {{old.total_sales}}</li>
              </ul>
           
            </div>
          </div>
        </div>

      </div>
      <!-- /.row -->

    
    </div>
    

  </body>

</template>


<script>
import axios from 'axios';
export default {
  name: 'main',
  data () {
    return {
        capital : null,
        categories : [],
        user : null,
        items : [],
        out_of_stock : false,
        credit : '',
        credit_products : [],
        out_of_stock_products : [],
        credit_and_out_of_stock : [],
        searchitem : null,
        no_of_sales : 0,
        cost_amt : null,
        sales_amt : null,
        product_name : null,
        quantity : null,
        category : 1,
        searchResults : {no_of_sales:null, remaining_stock : null ,category: null, creditor_name : null ,cost_amt:null, sales_amt:null, product_name : null, quantity:null, out_of_stock:null, credit : false, created : null, modified : null},
        show : false,
        all_items : [],
        sales1 : [],
        sales2 : [], 
        sales3 : [], 
        sales4 : [],
        total_sales : [],
        view : true,
        int : 0,
        no_view : true,
        fetch_total_sales : null,
        product : {product_name:null, no_of_sales:null },
        old : [],
        old_view : false,
        old_data : [],
        today_sales : null,
        sales : null
 

    }
  },

  methods : {
    getCapital : function(){
      axios.get('http://127.0.0.1:8000/products/')
      .then(response => {
        // console.log(response.data)

        response.data.forEach(i => {
          this.all_items.push(i)
          this.total_sales.push( i.no_of_sales * i.sales_amt)
          if (i.no_of_sales >= i.quantity && i.credit == true) {
              this.credit_and_out_of_stock.push(i)
              this.sales1.push(i.sales_amt * i.no_of_sales)
          }else if (i.no_of_sales < i.quantity && i.credit == true){
            this.credit_products.push(i)
            this.sales2.push(i.no_of_sales * i.sales)
          }else if (i.no_of_sales >= i.quantity && i.credit == false){
            this.out_of_stock_products.push(i)
            this.sales3.push(i.no_of_sales * i.sales_amt)
          }else{
            this.items.push(i)
            this.sales4.push( i.no_of_sales * i.sales_amt)
            // this.sales4.product_name.push(i.product_name)

            // console.log(this.sales4)
          }
       
         
        })
})
      .catch(err => {if (err) {console.log(err) , alert('Cannot retrieve data ::: Please make sure the server is running')}})
      },
    postProduct : function() {
      axios.post('http://127.0.0.1:8000/products/', {
        user : this.user,
        no_of_sales : this.no_of_sales,
        cost_amt : this.cost_amt,
        sales_amt : this.sales_amt,
        product_name : this.product_name,
        quantity : this.quantity,
        category : this.category
        })
        .then(response => console.log(response.data))
        .catch(err => {if (err){if (err.response.status == 400){alert('Please fill in the form completely')}else{alert(err)}}})
        // this.getCapital()
        this.no_of_sales = null,
        this.cost_amt = null,
        this.sales_amt = null,
        this.product_name = null, 
        this.quantity = null 
        this.$router.push('/')
        
    },
    showupdate : function(){
   
      this.view = true
    
    },
    getProfit: function(){
      let data = 0;
      console.log(this.total_sales)
        this.total_sales.forEach(i => {
          if ( i != undefined){
            data += i
          }
          
        })
        console.log(data)
      localStorage.setItem('total_sales', data)
    },
    fetchUser : function() {
      axios.get('http://127.0.0.1:8000/users/')
      .then(response => {
        response.data.forEach(d => this.user = d.id)
      })
      .catch(err => console.log(err))

    },
    fetchCategory : function(){
      axios.get('http://127.0.0.1:8000/category/')
      .then(response =>{this.categories = response.data} )

    },
    UpdateIt : function(){
      axios.put('http://127.0.0.1:8000/product/'+this.updateItem, {
        no_of_sales : this.product.no_of_sales,
        product_name : this.product.product_name
      })
      .then(response => console.log(response.data))
      .catch(err => {if(err){throw err}})
      this.product.no_of_sales = null;

    },
    // Search item based on keywords
    searchProduct : function() {
      axios.get('http://127.0.0.1:8000/products/?search=' + this.searchitem)
      .then(response => {response.data.forEach(data => {
        this.searchResults.product_name = data.product_name,
        this.searchResults.no_of_sales = data.no_of_sales,
        this.searchResults.cost_amt = data.cost_amt,
        this.searchResults.sales_amt  = data.sales_amt,
        this.searchResults.quantity = data.quantity,
        this.searchResults.out_of_stock = data.out_of_stock,
        this.searchResults.created = data.created,
        this.searchResults.modified = data.modified,
        this.searchResults.category = data.category,
        this.searchResults.creditor_name = data.creditor_name
        if (data.quantity > data.no_of_sales){
          this.searchResults.remaining_stock = data.quantity - data.no_of_sales
        }else{
          this.searchResults.remaining_stock = 'Out of stock'
        }

      })})
      .catch(err => console.log(err))
      this.show = true

},


updateItem : function(){
  if (this.updateItem != null){
      axios.get('http://127.0.0.1:8000/product/'+ this.updateItem)
      .then(response => {this.product.no_of_sales = response.data.no_of_sales, this.product.product_name = response.data.product_name})
      .catch(err => console.log(err))
  }

},

// Fetches older days' transaction 
fetchSingleData : function(){
  console.log('Sending.....')
  axios.get('http://127.0.0.1:8000/single/')
  .then(response => {
    this.today_sales = response.data[response.data.length - 1].total_sales
    response.data.forEach(i => {
      this.old_data.push(i)
    })
  })
  .catch(err => console.log(err))

},

// Calculate present day transaction by subtracting yesterday's transaction from today's one


// Close transaction and save the days' transactions in the database
closeTransaction: function(){
  if (this.fetch_total_sales > this.today_sales){
    this.sales = this.fetch_total_sales - this.today_sales
  }else if (this.today_sales > this.fetch_total_sales){
    this.sales = this.today_sales - this.fetch_total_sales
  
  }
  console.log(this.fetch_total_sales)
  console.log(this.today_sales)
  console.log(this.fetch_total_sales - this.today_sales)
console.log(this.sales)
  axios.post('http://127.0.0.1:8000/single/', {
      total_sales : this.sales
  })
  .then(response => {
     alert('Transaction closed & saved')
     this.fetch_total_sales = this.old_data[this.old_data.length - 1].total_sales - this.fetch_total_sales
     if (fetch_total_sales < 1){
       this.fetch_total_sales = this.fetch_total_sales * -1
     }
     localStorage.setItem('total_sales', this.fetch_total_sales)


    })
  .catch(err => {throw err})
  


}
  },
  created () {
    this.getCapital(),
    this.fetchUser(),
    this.fetchCategory(),
    // Fetches total sales of the day 
    this.fetch_total_sales = localStorage.getItem('total_sales'),
    this.fetchSingleData()
  }
  
}
</script>

