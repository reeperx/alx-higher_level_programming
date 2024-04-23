#!/usr/bin/node

const arg2 = process.arg[2];
const parsedNumber = parseInt(arg2);

if (isNan (parsedNumber)) {
	console.log('Not a number');
} else {
	console.log(`My number; ${parsedNumber}`);
}
