const say = require('say');

function parseDefinitions(definitions) {
  const jsonDefinitions = JSON.parse(definitions);
  const stringDefs = [];
  for (var key in jsonDefinitions) {
    stringDefs.push(key + ": " + jsonDefinitions[key]['pos'].toLowerCase() + ": " + jsonDefinitions[key]['def'].toLowerCase());
  }
  return stringDefs;
}

function speakManyText(strings) {
  for (var str in strings) {
    speakText(strings[str]);
  }
}

function speakText(string) {
  say.speak(string);
}

module.exports = {
  parseDefinitions,
  speakManyText,
  speakText
}
