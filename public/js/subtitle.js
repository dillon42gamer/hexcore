function getRandomGreeting() {
  var greetings = [
    "Downloading your passwords...",
    "WARNING: You may lose braincells if you proceed!",
    "Fortnite is cringe",
    "im faster than levi",
    "My iPad passcode is 345566 btw",
    "Sponsered by RAID SHADOW LEGENDS!",
    "youtube.com/watch?v=dQw4w9WgXcQ",
    "I spent too much time making these",
  ];
  var randomIndex = Math.floor(Math.random() * greetings.length);
  return greetings[randomIndex];
}

document.getElementById("subtitle").innerText = getRandomGreeting();