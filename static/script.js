document
  .getElementById("prediction-form")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    const temperature = parseFloat(
      document.getElementById("temperature").value,
    );
    const rainfall = parseFloat(document.getElementById("rainfall").value);
    const day_of_week = parseInt(document.getElementById("day_of_week").value);
    const month = parseInt(document.getElementById("month").value);

    const data = {
      temperature: temperature,
      rainfall: rainfall,
      day_of_week: day_of_week,
      month: month,
    };

    fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        document.getElementById("result").innerText =
          `Predicted Sales: ${result.predicted_sales} ice creams`;
      })
      .catch((error) => {
        console.error("Error:", error);
        document.getElementById("result").innerText =
          "An error occurred. Please try again.";
      });
  });
