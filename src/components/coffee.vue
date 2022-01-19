<template>
  <div class="svg">
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 600 293" style="enable-background:new 0 0 600 293;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#EFEFEF;}
	.st1{fill:#E3E4E5;}
	.st2{fill:#2A333A;}
	.st3{opacity:0.5;fill:#9E9E9E;}
	.st4{fill:#5C5E60;}
	.st5{fill:#404244;}
	.st6{fill:#EBECED;}
	.st7{fill:#FFFFFF;}
	.st8{fill:#3C2415;}
	.st9{fill:#432818;}
	.st10{fill:#563726;}
	.st11{fill:#FCFCFC;}
	.st12{opacity:0.5;fill:#FCFCFC;}
	.st13{fill:none;stroke:#EBECED;stroke-width:5;stroke-miterlimit:10;}
	.st14{fill:#FEFEFE;}
	.st15{fill:#EF7665;}
	.st16{fill:#A4D9E4;}
	.st17{fill:#B8C7CD;}
	.st18{fill:#474A4E;}
	.st19{fill:#65B6C1;}
	.st20{fill:#F46C69;}
	.st21{fill:#7C7F83;}
	.st22{fill:#FFFFFE;}
	.st23{fill:#F96759;}
</style>

<g id="coffee">
	<g id="coffee_1_">
		<g>
			<path class="st6" d="M534.1,218.8l5.1-5.1c-2.6-3.5-5.7-6.5-9.3-8.9l-4.8,4.8L534.1,218.8z"/>
			<circle class="st7" cx="508.5" cy="236.5" r="33.6"/>
			<circle class="st6" cx="508.5" cy="236.5" r="31.2"/>
			<circle class="st8" cx="508.5" cy="236.5" r="28.1"/>
			<circle class="st9" cx="508.5" cy="236.5" r="24.9"/>
			<circle class="st10" cx="508.5" cy="236.5" r="21"/>
			<circle class="st9" cx="508.5" cy="236.5" r="19.9"/>
			<path class="st11" d="M539.2,213.7l6.6-6.6l-9.1-9.1l-6.8,6.8C533.5,207.2,536.6,210.2,539.2,213.7z"/>
		</g>
		<circle class="st10" cx="508.5" cy="236.5" r="5"/>
		<circle class="st8" cx="508.5" cy="236.5" r="4.5"/>
		<path class="st12" d="M508.5,260.4L508.5,260.4c-13,0-23.6-10.5-23.9-23.4c0-0.3-0.2-0.5-0.5-0.5h-0.1c-0.1,0-0.2,0.1-0.3,0.1
			s-0.1,0.2-0.1,0.3c0.3,13.5,11.3,24.4,24.9,24.4l0,0V260.4z"/>
	</g>
</g>
<g id="smoke_1_">
	<g id="smoke">
		<path class="st13" d="M496.3,167.7c0,0,5.6,5.1,0,12.1c-5.6,7-0.5,11.3,0,12.4"/>
		<path class="st13" d="M508.9,160.9c0,0,8,7.3,0,17.2s-0.7,16.2,0,17.6"/>
		<path class="st13" d="M520.9,167.7c0,0,5.6,5.1,0,12.1c-5.6,7-0.5,11.3,0,12.4"/>
	</g>
</g>


</svg>
  </div>
</template>

<script>
export default {
    name:'Coffee'
}
</script>

<style scoped>
.svg {
  position: absolute;
  bottom: -10px;
  width: 700px;
  left: 0;
  right: 0;
  margin: auto;
}

#coffee {
  animation: coffee 1s linear;
  transform-origin: 83% 80%;
}

#smoke {
  animation: smoke 3s infinite;
}

@keyframes coffee {
  0%{transform: scale(0); opacity: 0}
  50%{transform: scale(1.5); opacity: 1}
  100% {transform: scale(1); opacity:1}
}

@keyframes smoke {
  0%{transform: translateY(0px); opacity: 1;}
  50%{ opacity: .5;}
  100%{transform: translateY(-15px); opacity: 0;}
}
</style>
