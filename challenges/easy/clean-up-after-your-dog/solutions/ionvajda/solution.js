const garden1 = [
  ["_", "_", "_", "_", "_", "_"],
  ["_", "_", "_", "_", "@", "_"],
  ["@", "_", "_", "_", "_", "_"],
];

const garden2 = [
  ["_", "_", "_", "_"],
  ["_", "_", "_", "_"],
  ["@", "_", "_", "D"],
];

function cleanUp(garden, bags, cap) {
  const gardenToString = garden.toString();
  const totalCrap = gardenToString.split("@").length - 1;
  if (gardenToString.includes("D")) {
    return "Dog!!";
  }
  return bags * cap >= totalCrap ? "Clean" : "Cr@p";
}

cleanUp(garden1, 2, 2) == "Clean";
cleanUp(garden1, 1, 1) == "Cr@p";
cleanUp(garden2, 2, 2) == "Dog!!";
