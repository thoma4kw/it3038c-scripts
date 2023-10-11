var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res) {
  if (req.url === "/") {
    fs.readFile("./public/index.html", "UTF-8", function(err, body) {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if (req.url.match("/sysinfo")) {
    
    var uptime = os.uptime();
    var days = Math.floor(uptime / 86400);
    var hours = Math.floor((uptime % 86400) / 3600);
    var minutes = Math.floor((uptime % 3600) / 60);
    var seconds = Math.floor(uptime % 60);

    var totalMemory = os.totalmem();
      
    var freeMemory = os.freemem();

    var numberOfCPUs = os.cpus().length;

    var html = `
<!DOCTYPE html>
<html>
<head>
<title>Node JS Response</title>
</head>
<body>
<p>Hostname: ${os.hostname()}</p>
<p>IP: ${ip.address()}</p>
<p>Server Uptime: ${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds</p>
<p>Total Memory: ${totalMemory / 1024 / 1024} MB</p>
<p>Free Memory: ${freeMemory / 1024 / 1024} MB</p>
<p>Number of CPUs: ${numberOfCPUs}</p>
</body>
</html>`;

    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");
