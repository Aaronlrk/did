<template>
  <div class="main">
    <!-- 전체 가로 -->
    <div class="container row p-0">
<!-- 각각의 id는 sector를 의미한다 -->
      <div id=1 class="col temp d-flex">
        <div id="ordernums" class="ordnums col-3 "></div>
        <div class="mt-1 text-center col">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"> </div>
        </div>
      </div>

      <div id=2 class="col temp d-flex">
        <div id="ordernums" class="ordnums col-3 "></div>
        <div class="mt-1 text-center col">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>

      <div id="3" class="col temp d-flex">
        <div id="ordernums" class="ordnums col-3 "></div>
        <div class="mt-1 text-center col">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>

      <div id="4" class="col temp d-flex">
       <div id="ordernums" class="ordnums col-3 "></div>
        <div class="mt-1 text-center col">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>

      <div id="5" class="col temp d-flex">
        <div id="ordernums" class="ordnums col-3 "></div>
        <div class="mt-1 text-center col">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>

      <div id="6" class="col temp d-flex">
        <div id="ordernums" class="ordnums col-3 "></div>
        <div class="mt-1 text-center col">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>

      <div id="7" class="col temp d-flex">
        <div id="ordernums" class="ordnums col-3 "></div>
        <div class="mt-1 text-center col">
          <div id="name" class="name"></div>
          <div id="coffee" class="coffee"></div>
        </div>
      </div>

      <div class="col back temp text-center">
        <div style="color:black">STARBUCKS</div>
        <div>다음 칸 : {{sector+1}}</div>
        <div>주문번호 : {{now}}</div>
      </div>
  </div>

  <div class="mt-5 d-flex justify-content-around">
    <div>
      <button class="btn btn-primary" @click="update1">update 1</button>
      <button class="btn btn-danger" @click="delete1">delete 1</button>
    </div>

    <div>
      <button class="btn btn-primary" @click="update2">update 2</button>
      <button class="btn btn-danger" @click="delete2">delete 2</button>
    </div>

    <div>
      <button class="btn btn-primary" @click="update3">update 3</button>
      <button class="btn btn-danger" @click="delete3">delete 3</button>
    </div>

    <div>
      <button class="btn btn-primary" @click="update4">update 4</button>
      <button class="btn btn-danger" @click="delete4">delete 4</button>
    </div>

    <div>
      <button class="btn btn-primary" @click="update5">update 5</button>
      <button class="btn btn-danger" @click="delete5">delete 5</button>
    </div>

    <div>
      <button class="btn btn-primary" @click="update6">update 6</button>
      <button class="btn btn-danger" @click="delete6">delete 6</button>
    </div>

    <div>
      <button class="btn btn-primary" @click="update7">update 7</button>
      <button class="btn btn-danger" @click="delete7">delete 7</button>
    </div>
  </div>

  <div class="button d-flex ">
    <input type="text" class="btn btn-success text-center" readonly autofocus @keyup.enter="updateorder" value="Press Enter">
    <button class="btn btn-danger" @click="deleteorder">deleteAll</button>
  </div>
    <!-- <button class="button btn-success" @keyup.enter="updateorder">Click</button> -->
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
        el.childNodes[1].childNodes[0].classList.add("slidein")
        el2.childNodes[1].childNodes[0].classList.remove("slidein")

        el.childNodes[0].classList.add('fadeinnum')
        el2.childNodes[0].classList.remove('fadeinnum')

        el.childNodes[1].childNodes[1].classList.add("fade-in")
        el2.childNodes[1].childNodes[1].classList.remove("fade-in")
      } else {
      this.sector+=1
      const el = document.getElementById(`${this.sector}`)
      const el2 = document.getElementById(`${this.sector-1}`)
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;

      el.childNodes[1].childNodes[0].classList.add("slidein")
      el2.childNodes[1].childNodes[0].classList.remove("slidein")

      el.childNodes[0].classList.add("fadeinnum")
      el2.childNodes[0].classList.remove("fadeinnum")

      el.childNodes[1].childNodes[1].classList.add("fade-in")
      el2.childNodes[1].childNodes[1].classList.remove("fade-in")

      if (this.sector > 6) {
        this.sector = 0
      }
      console.log(this.sector)
      this.now +=1
      }
    },


    deleteorder: function () {
      var i
      for ( i=1; i<8; i++) {
         const el = document.getElementById(i)
         el.childNodes[0].innerText = "";
      el.childNodes[1].childNodes[0].innerText = "";
      el.childNodes[1].childNodes[1].innerText = "";
      el.childNodes[1].childNodes[0].classList.remove("slidein")
      el.childNodes[0].classList.remove('fadeinnum')
      el.childNodes[1].childNodes[1].classList.remove("fade-in")
      }
    },

    update1: function () {
      const el = document.getElementById(1)
      
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;
      this.sector = 1
      this.now +=1
      el.childNodes[1].childNodes[0].classList.add("slidein")
      el.childNodes[0].classList.add('fadeinnum')
      el.childNodes[1].childNodes[1].classList.add("fade-in")
    },
    delete1: function() {
      const el = document.getElementById(1)
      el.childNodes[0].innerText = "";
      el.childNodes[1].childNodes[0].innerText = "";
      el.childNodes[1].childNodes[1].innerText = "";
      el.childNodes[1].childNodes[0].classList.remove("slidein")
      el.childNodes[0].classList.remove('fadeinnum')
      el.childNodes[1].childNodes[1].classList.remove("fade-in")
    },

    update2: function () {
      const el = document.getElementById(2)
      
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;
      this.sector = 2
      this.now +=1
      el.childNodes[1].childNodes[0].classList.add("slidein")
      el.childNodes[0].classList.add('fadeinnum')
      el.childNodes[1].childNodes[1].classList.add("fade-in")
    },
    delete2: function() {
      const el = document.getElementById(2)
      el.childNodes[0].innerText = "";
      el.childNodes[1].childNodes[0].innerText = "";
      el.childNodes[1].childNodes[1].innerText = "";
      el.childNodes[1].childNodes[0].classList.remove("slidein")
      el.childNodes[0].classList.remove('fadeinnum')
      el.childNodes[1].childNodes[1].classList.remove("fade-in")
    },

    update3: function () {
      const el = document.getElementById(3)
      
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;
      this.sector = 3
      this.now +=1
      el.childNodes[1].childNodes[0].classList.add("slidein")
      el.childNodes[0].classList.add('fadeinnum')
      el.childNodes[1].childNodes[1].classList.add("fade-in")
    },
    delete3: function() {
      const el = document.getElementById(3)
      el.childNodes[0].innerText = "";
      el.childNodes[1].childNodes[0].innerText = "";
      el.childNodes[1].childNodes[1].innerText = "";
      el.childNodes[1].childNodes[0].classList.remove("slidein")
      el.childNodes[0].classList.remove('fadeinnum')
      el.childNodes[1].childNodes[1].classList.remove("fade-in")
    },

    update4: function () {
      const el = document.getElementById(4)
      
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;
      this.sector = 4
      this.now +=1
      el.childNodes[1].childNodes[0].classList.add("slidein")
      el.childNodes[0].classList.add('fadeinnum')
      el.childNodes[1].childNodes[1].classList.add("fade-in")
    },
    delete4: function() {
      const el = document.getElementById(4)
      el.childNodes[0].innerText = "";
      el.childNodes[1].childNodes[0].innerText = "";
      el.childNodes[1].childNodes[1].innerText = "";
      el.childNodes[1].childNodes[0].classList.remove("slidein")
      el.childNodes[0].classList.remove('fadeinnum')
      el.childNodes[1].childNodes[1].classList.remove("fade-in")
    },

    update5: function () {
      const el = document.getElementById(5)
      
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;
      this.sector = 5
      this.now +=1
      el.childNodes[1].childNodes[0].classList.add("slidein")
      el.childNodes[0].classList.add('fadeinnum')
      el.childNodes[1].childNodes[1].classList.add("fade-in")
    },
    delete5: function() {
      const el = document.getElementById(5)
      el.childNodes[0].innerText = "";
      el.childNodes[1].childNodes[0].innerText = "";
      el.childNodes[1].childNodes[1].innerText = "";
      el.childNodes[1].childNodes[0].classList.remove("slidein")
      el.childNodes[0].classList.remove('fadeinnum')
      el.childNodes[1].childNodes[1].classList.remove("fade-in")
    },

    update6: function () {
      const el = document.getElementById(6)
      
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;
      this.sector = 6
      this.now +=1
      el.childNodes[1].childNodes[0].classList.add("slidein")
      el.childNodes[0].classList.add('fadeinnum')
      el.childNodes[1].childNodes[1].classList.add("fade-in")
    },
    delete6: function() {
      const el = document.getElementById(6)
      el.childNodes[0].innerText = "";
      el.childNodes[1].childNodes[0].innerText = "";
      el.childNodes[1].childNodes[1].innerText = "";
      el.childNodes[1].childNodes[0].classList.remove("slidein")
      el.childNodes[0].classList.remove('fadeinnum')
      el.childNodes[1].childNodes[1].classList.remove("fade-in")
    },

    update7: function () {
      const el = document.getElementById(7)
      
      el.childNodes[0].innerText = orderlist[this.now].num;
      el.childNodes[1].childNodes[0].innerText = orderlist[this.now].name;
      el.childNodes[1].childNodes[1].innerText = orderlist[this.now].coffee;
      this.sector = 7
      this.now +=1
      el.childNodes[1].childNodes[0].classList.add("slidein")
      el.childNodes[0].classList.add('fadeinnum')
      el.childNodes[1].childNodes[1].classList.add("fade-in")
    },
    delete7: function() {
      const el = document.getElementById(7)
      el.childNodes[0].innerText = "";
      el.childNodes[1].childNodes[0].innerText = "";
      el.childNodes[1].childNodes[1].innerText = "";
      el.childNodes[1].childNodes[0].classList.remove("slidein")
      el.childNodes[0].classList.remove('fadeinnum')
      el.childNodes[1].childNodes[1].classList.remove("fade-in")
    },

  }
}
</script>

<style>


@font-face {
  font-family: 'Santana-Black';
  src: url('../assets/fonts/Santana-Black.ttf') format('truetype');
}

.main {
  width: 1280px;
  height: 80px;
  /* background-image:  url('../assets/background.gif'); */
  background-color: #036635;
  background-position: 60% 40% ;
}

.back {
  font-family: 'Santana-Black';
  font-weight: bold;
}

.temp {
  height: 80px;
  color: white;
  width: 160px;
}

.ordnums{
  font-family: 'Santana-Black';
 font-weight: bold;
 font-size: 100%;
 text-align: center;
 letter-spacing: 4px;
 writing-mode: vertical-lr;
 text-orientation: upright;
}

.name{
  font-family: 'Santana-Black';
  color: black;
  font-weight: bold;

  font-size: 1vw;

}

.slidein {
  animation-duration: 1s;
  animation-name: slidein;
}


@keyframes slidein {
  from {
    opacity: 0;
    margin-left: 200%;
  }

  to {
    opacity: 1;
    margin-left: 0%;
}}

.fadeinnum {
  animation-duration: 1s;
  animation-name: walkin;
}

@keyframes walkin {
  from {
    margin-top: 80%;
  }

  to {
    margin-top: 0%;
}

}

.coffee{
  color: white;
  font-weight: bold;
  display: inline-block;
  font-size: 1vw;
  font-family: 'Santana-Black', cursive;
}

.button {
  position: absolute;
  width: 10%;
  height: 10%;
  top: 400px;
  left: 500px;
}

.fade-in {
  display: inline-block;
  animation: fadein 3s;
  -moz-animation: fadein 3s; /* Firefox */
  -webkit-animation: fadein 3s; /* Safari and Chrome */
  -o-animation: fadein 3s; /* Opera */
}
@keyframes fadein {
    from {
        opacity:0;
    }
    to {
        opacity:1;
    }
}
@-moz-keyframes fadein { /* Firefox */
    from {
        opacity:0;
    }
    to {
        opacity:1;
    }
}
@-webkit-keyframes fadein { /* Safari and Chrome */
    from {
        opacity:0;
    }
    to {
        opacity:1;
    }
}
@-o-keyframes fadein { /* Opera */
    from {
        opacity:0;
    }
    to {
        opacity: 1;
    }
}
</style>
