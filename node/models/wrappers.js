const PythonShell = require('python-shell');
const { parseDefinitions, speakManyText } = require('./textToSpeech.js');

function runPython(scriptName, scriptPath, onFunction) {
  const pyshell = new PythonShell(scriptName, { 'scriptPath': __dirname + '/../../' + scriptPath});

  pyshell.on('message', (message) => {
    console.log(message);
  })

  pyshell.end( (err) => {
    if (err) throw err;
    console.log('finished');
  })
}
