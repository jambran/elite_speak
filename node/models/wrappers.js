const PythonShell = require('python-shell');
const path = require('path');
const fs = require('fs');

function runPython(scriptName, scriptPath) {
  const pyshell = new PythonShell(scriptName, { 'scriptPath': __dirname + '/../../' + scriptPath});

  pyshell.on('message', (message) => {
    console.log(message);
  })

  pyshell.end( (err) => {
    if (err) throw err;
    console.log('finished');
  })
}
