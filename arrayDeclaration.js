//      constructor
//array コンストラクターを使って初期化する方法
/*
    オブジェクト化するときに、引数に値を指定して、
    オブジェクト化する仕組み
*/

let ary1 = new Array(1,2,3,4,5,6,7,8,9,10);
let ary2 = new Array('yamada','suzuki','yamashita','nishiyama','yoshimura');
let ary3 = new Array();
let ary4 = new Array(10);
//let a  = new class(variable,...);
console.log('\n**************')
console.log('arg1:' + ary1);
console.log('arg2:' + ary2);
console.log('arg3:' + ary3);
console.log('arg4:' + ary4);

//リテラル(literal)を使って初期化する方法
let ary5 = [1,2,3,4,5,6,7,8,9,10];
let ary6 = ['yamada','suzuki','yamashita','nishiyama','yoshimura'];
let ary7 = [];
let ary8 = [10];//ary8[0] = 10
console.log('\n***************')
console.log('arg5:' + ary5);
console.log('arg6:' + ary6);
console.log('arg7:' + ary7);
console.log('arg8:' + ary8);

//配列へ値の代入
let a = [];
a[0] = 45;
a[1] = 'bank';

//配列からデータを取り出す
let out1 = a[0];
let out2 = a[1];
console.log('\n***************')
console.log('out1:'+out1+'\nout2:'+out2);

//sort() メソッド(文字列だけ使える)
let num_array = [10,5,9,7,2,1,8,4,3,6,11];
let a_z = new Array('k','m','a','c','b','x','z','y');
console.log('\n***************')
console.log('sort() of a_z : ' + a_z.sort());

//tostring() and join() method
console.log('\n***************')
console.log('ary.toString():' + ary6.toString());
console.log('ary.join(\'/\'):' + ary6.join('/'));

//concat() method
let a1 = ['.com','.ac.jp','.net','.biz','.co.jp'];
let b = ['.ne.jp','.jp','.inc','.org','.info'];
let c = a1.concat(b);
console.log('\n***************')
console.log('非破壊的連結:' + c);

//LIFO method {push,pop}
//FIFO method {push,shift}
console.log('\n***************')
num_array.push(56);
console.log('push 56 in num_array:' +num_array);
num_array.pop();
console.log('after pop method :' + num_array);