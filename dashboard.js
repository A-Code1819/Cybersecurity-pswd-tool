function entropyGraph(entropy){

let canvas = document.createElement("canvas")

document.body.appendChild(canvas)

let ctx = canvas.getContext("2d")

ctx.fillStyle="lime"

ctx.fillRect(10,100-entropy,40,entropy)

}