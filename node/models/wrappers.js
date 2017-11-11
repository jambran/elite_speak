const PythonShell = require('python-shell');

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
