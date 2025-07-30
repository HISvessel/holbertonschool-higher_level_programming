#!/usr/bin/node

/* Level 2: declaration of functions
Here, we will learn how to 
1)create custom user functions
    We will also learn how to declare and initialize them through
    expressive form and declarative form*/

sayHi(); //can be declared before initializing it to a function
function sayHi () {
  console.log("Hello!"); // prints a greeting
}
console.log("This line printed the first greeting in declare form");
console.log("--------------------------");

WelcomeUser(); // can also be declared before giving it a value
function WelcomeUser() {
  console.log("Hello, chat"); // this function greets the chat
}
console.log("This line printed the second greeting in declare form");
console.log("-------------------------");

console.log("Functions as declaration created");
console.log("-------------------------");
console.log(" ");
try {
  console.log("Testing for hoisting and declaration begins.");
  sayHi(); //called a second time, this time printing the message
  WelcomeUser(); //this will print before the error is triggered
  falseGreet(); //calling the function before defining it; triggers errors
  WelcomeUser(); // does not print, command is bypassed since the line above triggered an error
} catch(error) {
  if (error instanceof ReferenceError) {
    console.error("This cannot print, you created a Reference error.");
    console.error("Try defining the function before calling it.")
  } else {
    console.error("Another error.");
  }
}
console.log("First testing complete");
console.log("------------------------");
console.log(" ")
console.log("Commencing second tests");
const name = 'Kevin';
function greet() {
    console.log("Hello again, I'm ", name); //giving Kevin a chance to reintroduce himself
}

try {
  console.log("Introduce yourself, Paul") //welcoming Paul into the fray
  console.log("...........")
  lategreet();  
} catch(error) {
    console.error("Caught an error:", error.message); //Paul never showed, error message printed
}

const lategreet = function () {
    console.log("Hi, I'm Paul. Is it too late to say hello?");
};

console.log("Let's print these greetings now.");
greet();//Kevin reintroduced
lategreet();//Paul.....its a little too late 


/*Topic #2: Function Parameter and return values */

function greetPerson(name) {
    const greeting = "Hello " + name
   return greeting; // stores a small greeting phrase for a small dialogue
}

function fullName(first, last) {
  return first + '' + last;
}

console.log("")
console.log("-".repeat(20))
console.log("We will now introduce two people for a convo.")
console.log("")
function dialogue() {
  console.log("Dialogue: Begin!");
  console.log("Unknown: Hello, I'm Chat");
  console.log("Unknown 2: Hello, I'm Kevin");
  console.log("Kevin:", greetPerson("Chat") + ", pleasure to meet you");
  console.log("Chat:", greetPerson("Kevin") + ", pleasure is all mine");
}

dialogue();

const add = (a, b) => {return a + b}; /* short adding function */
/* if our arrow function is to return something, then place between curly braces*/
console.log(add(3, 4));

const difference = (a, b) => a - b;

result = difference(5, 2) /* can perform function to store in another var or const*/
console.log(result)

