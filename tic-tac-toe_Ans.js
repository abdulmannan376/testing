const prompt = require('prompt-sync')({sigint: true});
 
// Random number from 1 - 100
//let numberInMind = Math.floor(Math.random() * 100) + 1;
let numberInMind= 55

// This variable is used to determine if the app should continue prompting the user for input
let foundCorrectNumber = false;
const name = prompt("> What's your name? ");
console.log("Hello "+name+", let's try to guess a number in my mind.")
 
while (!foundCorrectNumber) {
  // Step 1: Get user input (don't forget that the input is a string)
  
  const num = prompt("I have a number in my mind. It is between 0-100, guess it: ");

  // Step 2: Compare the guess to the secret answer and
  // let the user know the feedback (too large, too small, correct).
  if (num>numberInMind)
  {
    console.log("> It's too large. Next guess?")
  }
  else if (num<numberInMind)
  {
    console.log("> It's too small. Next guess?")
  }

  else
  {
    console.log("-------------------------")
    console.log("Congratulations "+name+", you won!")
    console.log("-------------------------")

    // We need to write bonus part over here
    foundCorrectNumber = true;
    let tryAgain = prompt('Try again?');

    if(tryAgain.toLowerCase() != 'no'){
      // Math.floor(Math.randon() * 100) + 1 
      // it is generatign random number greater than 0 and les than 101 or 100
      numberInMind = Math.floor(Math.random() * 100) + 1;
      console.log(numberInMind);
      foundCorrectNumber = false;
    }else{
      console.log("Happy to see you. Better luck next time.");

    }



  }
  
}


// Bonus Point: prompt user and provide option for user to start a new game after winning
// const playagain = prompt("Do you want to play again? (Y/N)");