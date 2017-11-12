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

function textToSpeechWrapper() {
  const pyshell = new PythonShell('main_script.py', { 'scriptPath': __dirname + '/../../'});

  pyshell.on('message', (message) => {
    if (message.startsWith('DEF_FLAG')) {
      const definitions = parseDefinitions(message.substring(8));
      speakManyText(definitions);
    }
  })

  pyshell.end( (err) => {
    if (err) throw err;
    console.log('finished');
  })
}
