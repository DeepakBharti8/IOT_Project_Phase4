const waterLevelElement = document.getElementById("water-level");
const warningMessageElement = document.getElementById("warning-message");

// Simulate real-time data from IoT sensors (replace with actual sensor data).
function fetchWaterLevelData() {
    return Math.random() * 10; // Replace with actual sensor data retrieval.
}

// Check water levels and issue warnings.
function checkWaterLevel() {
    const waterLevel = fetchWaterLevelData();
    waterLevelElement.innerText = `Water Level: ${waterLevel} meters`;

    if (waterLevel > 5) {
        warningMessageElement.innerText = "Flood Warning: Water level is dangerously high!";
    } else {
        warningMessageElement.innerText = "No warnings";
    }
}

// Fetch and check data periodically (adjust the interval as needed).
setInterval(checkWaterLevel, 10000); // Check every 10 seconds.
