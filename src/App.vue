<template>
  <div class="main">
    <div class="container row p-0">
      <div id="1" class="col temp">1 {{orderlist[0]}}</div>
      <div id="2" class="col temp">2</div>
      <div id="3" class="col temp">3</div>
      <div id="4" class="col temp">4</div>
      <div id="5" class="col temp">5</div>
      <div id="6" class="col temp">6</div>
      <div id="7" class="col temp">7</div>
      <div class="col temp">8</div>
    </div>

    <button class="button">Click</button>
  </div>
</template>

<script>
import orderlist from '../assets/orderlist.json'

export default {
  name: 'App',
  components: {
  },
  data: function () { 
    return    {
    orderlist: orderlist,
    sector: "",
  }},
  methods: {
  }
}
</script>

<style>
.main {
  width: 1280px;
  height: 80px;
}

.temp {
  height: 80px;
  border: solid 1px;
}

.button {
  position: absolute;
  top: 400px;
  left: 700px;
}
</style>
