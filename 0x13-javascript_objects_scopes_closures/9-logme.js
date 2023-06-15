#!/usr/bin/node
let noArg = 0;

exports.logMe = function (item) {
	if (item !== undefined) {
		console.log(`${noArg}: ${item}`);
		noArg++;
}
