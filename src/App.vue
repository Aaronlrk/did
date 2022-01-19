<template>
  <div class="main">
    <div class="container row p-0">
      <div id=1 class="col temp d-flex">
        <div id="ordernums" class="ordnums col-5 "></div>
        <div class="mt-1 text-center">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"> </div>
        </div>
      </div>

      <div id=2 class="col temp d-flex">
        <div id="ordernums" class="ordnums col-5 "></div>
        <div class="mt-1 text-center">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>
      <div id="3" class="col temp d-flex">
        <div id="ordernums" class="ordnums col-5 "></div>
        <div class="mt-1 text-center">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>
      <div id="4" class="col temp d-flex">
       <div id="ordernums" class="ordnums col-5 "></div>
        <div class="mt-1 text-center">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>
      <div id="5" class="col temp d-flex">
        <div id="ordernums" class="ordnums col-5 "></div>
        <div class="mt-1 text-center">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>
      <div id="6" class="col temp d-flex">
        <div id="ordernums" class="ordnums col-5 "></div>
        <div class="mt-1 text-center">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>
      <div id="7" class="col temp d-flex">
        <div id="ordernums" class="ordnums col-5 "></div>
        <div class="mt-1 text-center">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>
      <div class="col temp">
        <div>Next : {{sector+1}}</div>
        <div></div>
      </div>
    <button class="button btn-success" @keyup.enter="updateorder">Click</button>
  </div>
  </div>

</template>

<script>
import orderlist from '../assets/orderlist.json'
// import Coffee from '@/components/coffee.vue'
export default {
  name: 'App',
  components: {
    // Coffee
  },
  data: function () { 
    return    {
    orderlist: orderlist,
    sector: 0,
    name: "",
    ordernums: "",
    coffee: "",
    now: 0,
  }},
  methods: {
    updateorder: function () {
      if(this.sector == 0 ) {
        const el = document.getElementById(1)
        const el2 = document.getElementById(7)
        el.childNodes[0].innerText = orderlist[this.now].num;
        el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
        el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;
        this.sector +=1
        this.now +=1

        el.childNodes[1].childNodes[0].classList.add("fadein")
        el2.childNodes[1].childNodes[0].classList.remove("fadein")

        el.childNodes[0].classList.add('fadeinnum')
        el.childNodes[0].classList.remove('fadeinnum')

      } else {
      this.sector+=1
      const el = document.getElementById(`${this.sector}`)
      const el2 = document.getElementById(`${this.sector-1}`)
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;

      el.childNodes[1].childNodes[0].classList.add("fadein")
      el2.childNodes[1].childNodes[0].classList.remove("fadein")

      el.childNodes[0].classList.add('fadeinnum')

      if (this.sector > 6) {
        this.sector = 0
      }
      console.log(this.sector)
      this.now +=1
      }
    },

    deleteorder: function () {

    }
  }
}
</script>

<style>
.main {
  width: 1280px;
  height: 80px;
  background-image:  url('../assets/background.gif');
  background-position: 60% 40% ;
}

.temp {
  height: 80px;
  color: white;

}

.ordnums{
 font-size: 100%;
 text-align: center;
 letter-spacing: 4px;
 writing-mode: vertical-lr;
 text-orientation: upright;
}

.name{
  font-size: 80%;

}

.fadein {
  animation-duration: 2s;
  animation-name: slidein;
}

@keyframes slidein {
  from {
    margin-left: 80%;
    width: 300%
  }

  to {
    margin-left: 0%;
    width: 100%;
  }
}

.fadeinnum {
  animation-duration: 1s;
  animation-name: walkin;
}

@keyframes walkin {
  from {
    margin-top: 80%;
    width: 300%
  }

  to {
    margin-top: 0%;
    width: 100%;
}

}

.coffee{
  font-size: 60%;

}

.button {
  position: absolute;
  width: 10%;
  height: 10%;
  top: 400px;
  left: 500px;
}
</style>
