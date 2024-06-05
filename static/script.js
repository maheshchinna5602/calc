document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('calculator-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const num1 = document.getElementById('num1').value;
        const num2 = document.getElementById('num2').value;
        const operation = document.getElementById('operation').value;

        fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ num1, num2, operation })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.textContent = `Error: ${data.error}`;
            } else {
                resultDiv.textContent = `Result: ${data.result}`;
            }
        })
        .catch(error => {
            resultDiv.textContent = `Error: ${error}`;
        });
    });
});
