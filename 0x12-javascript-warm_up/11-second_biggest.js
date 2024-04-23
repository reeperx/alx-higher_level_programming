#!/usr/bin/node

const arguementList = process.argv.slice(2);
const numbers = arguementList.map(arg => parseInt(arg));

if (numbers.length < 2) {
	console.log(0);
} else {
	const sortedNumbers = numbers.sort((a, b) => b - a);
console.log(sortedNumbers[1]);
}
