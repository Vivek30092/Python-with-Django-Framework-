// Programming and Script have one difference is the Compilations.
//Write a program to reverse a 3-digit without any loop.

var n = 123;
d1 = parseInt(n/100);
d2 = parseInt((n%100)/10);
d3 = n%10;

rev = d3*100 + d2*10 + d1*1;

document.writeln(rev);


// WAP to print sum first and last digit num.

var num = 4568, a, b , sum;
a = parseInt(num / 1000);
b = num % 10;

sum = a+b;

document.writeln("Sum is"+ sum);


var  pri, rate, time, I;

pri = 1000;
rate = 2;
time = 4;

I = (pri*rate*time)/100;

document.writeln("intereset"+I)

//WAP to find the grades of std on the basis of its percentage.

var maths = 50, hindi = 77, eng = 88, science = 87, sst = 65, total, perTotal;
total = maths + hindi + eng + science + sst;

perTotal = total/5;

if(perTotal>90)
    document.writeln("grade is A " + "Marks = " + perTotal);

else if (80<perTotal<=90)
    document.writeln("grade is A "+ "Marks = " + perTotal);

else if (70<perTotal<=80)
    document.writeln("grade is B+ "+ "Marks = " + perTotal);

else if (60<perTotal<=70)
    document.writeln("grade is B " + "Marks = "+ perTotal);

else if (perTotal<33) 
    document.writeln("You are fail "+ "Marks = " + perTotal);


//Functions
// Syntx:
function sum(a,b){
    a+b
}

// Addition of two nums: no args and with return values
function add(){
    var a = 100, b =400;
    var sum = a + b;
    return sum;
}
document.writeln("sum is " +add());

