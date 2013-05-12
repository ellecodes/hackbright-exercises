// What number's bigger?

// Write a function named greaterNum that:
	// takes 2 arguments, both numbers.
	// returns whichever number is the greater (higher) number.
// Call that function 2 times with different number pairs, and log the output to make sure it works (e.g. "The greater number of 5 and 10 is 10.").

function greaterNum(num1, num2) {
	if (num1 > num2) {
		return num1;
	} 
	else {
		return num2;
	}
}

console.log(greaterNum(10, 20));

// The World Translator

// Write a function named helloWorld that:
	// takes 1 argument, a language code (e.g. "es", "de", "en")
	// returns "Hello, World" for the given language, for atleast 3 languages. It should default to returning English.
// Call that function for each of the supported languages and log the result to make sure it works.
function helloWorld(lang) {
	if (lang == 'es') {
		return 'Hola Mundo'; 
	} else if (lang == 'de') {
		return 'Hallo Welt';
	} else if (lang == 'en') {
		return 'Hello, World';
	} else {
		return 'Hello, World';
	} 
}

console.log(helloWorld('es'));
console.log(helloWorld('de'));
console.log(helloWorld('en'));
console.log(helloWorld('fr'));



// The Grade Assigner

// Write a function named assignGrade that:
	// takes 1 argument, a number score.
	// returns a grade for the score, either "A", "B", "C", "D", or "F".
// Call that function for a few different scores and log the result to make sure it works.

function assignGrade(score) {
	if (score >= 90) {
		return 'Your Score is: ' + score + '. Your Grade is: A.'; 
	} else if (score < 90 && score >= 80) {
		return 'Your Score is: ' + score + '. Your Grade is: B.'; 
	} else if (score < 80 && score >= 70) {
		return 'Your Score is: ' + score + '. Your Grade is: C.'; 
	} else if (score < 70 && score >= 60) {
		return 'Your Score is: ' + score + '. Your Grade is: D.'; 
	} else if (score < 60) {
		return 'Your Score is: ' + score + '. Your Grade is: F.'; 
	} 
}

console.log(assignGrade('100'));
console.log(assignGrade('95'));
console.log(assignGrade('90'));
console.log(assignGrade('85'));
console.log(assignGrade('80'));
console.log(assignGrade('75'));
console.log(assignGrade('70'));
console.log(assignGrade('65'));
console.log(assignGrade('60'));
console.log(assignGrade('55'));
console.log(assignGrade('50'));
console.log(assignGrade('45'));
console.log(assignGrade('40'));
console.log(assignGrade('0'));

// Better solution:
function assignGrade(score) {
    if (score > 90) {
        return 'A';
    } else if (score > 80) {
        return 'B';
    } else if (score > 70) {
        return 'C';
    } else if (score > 65) {
        return 'D';
    } else {
        return 'F';
    }
}

console.log('You got a ' + assignGrade(95));
console.log('You got a ' + assignGrade(65));


// The Pluralizer

// Write a function named pluralize that:
	// takes 2 arguments, a noun and a number.
	// returns the number and pluralized form, like "5 cats" or "1 dog".
// Call that function for a few different scores and log the result to make sure it works.
// Bonus: Make it handle a few collective nouns like "sheep" and "geese".

function pluralize(noun, num) {
	if (num > 1) {
		return num + ' ' + noun + 's';
	} else {
		return num + ' ' + noun;
	}	
}

console.log(pluralize('cat', 5));
console.log(pluralize('fish', 10));
console.log(pluralize('dog', 1));

// Better solution:
function pluralize(noun, number) {
    if (number != 1 && noun != 'sheep' && noun != 'geese') {
        return number + ' ' + noun + 's';
    } else {
        return number + ' ' + noun;
    }
}
console.log('I have ' + pluralize('cat', 0));
console.log('I have ' + pluralize('cat', 1));
console.log('I have ' + pluralize('cat', 2));

