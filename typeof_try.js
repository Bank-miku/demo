// const num = document.getElementById('btn');
// let a = "500,000,000,000";
// let d = 758946543212356;
// let c = 2000;
// // let e = a+d;
const btn = document.getElementById('btn');
let b_1 = btn.value;


// // let c = b.toLocaleString('jpn');
// // e = e.toLocaleString('jpn');
let f = "";
const price_arry = b_1.split(",");
for (let index = 0; index < price_arry.length; index++) {
    // const element = array[index];
    console.log("price_array["+(index+1)+"]"+price_arry[index]);
    f += price_arry[index];
}

// console.log(typeof f);
// console.log(f);
let b = parseFloat(f);

// console.log(c+b);

const t = document.getElementById('test');

// let num_1 = num.value;
t.addEventListener("change",my_count);
let q_1;
function my_count(){
    q_1 = parseInt(document.getElementById("q").value);
    total();
}
function total(){
    let total;
    total = b*q_1;
    document.getElementById('total').innerHTML=total.toLocaleString('jpn');
}

// // e = e.toLocaleString('jpn');
// console.log(num_1);

