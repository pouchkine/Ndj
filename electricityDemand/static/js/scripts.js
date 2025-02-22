document.getElementById('predictionForm').onsubmit = function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    fetch('/predict', {
        method: 'POST',
        body: formData
    }).then(response => response.json())
      .then(data => {
          document.getElementById('model1Result').textContent = data.model1_prediction;
          document.getElementById('model2Result').textContent = data.model2_prediction;
      });
};
