// Function for the starting speak
function speak() {

  setTimeout(5000);

  utterance = new SpeechSynthesisUtterance("Benvenuto, chiedimi pure!");

  voices = speechSynthesis.getVoices();
  utterance.voice = voices[0]; 

  // Speak the text
  speechSynthesis.speak(utterance);
}

//Function to start the personalized speak
function speak_return(text) {

  setTimeout(5000);

  // Create a SpeechSynthesisUtterance
  utterance = new SpeechSynthesisUtterance(text);

  voices = speechSynthesis.getVoices();
  utterance.voice = voices[0]; 

  // Speak the text
  speechSynthesis.speak(utterance);
}

