document.getElementById('survey-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const inputs = document.querySelectorAll('input[name="answer"]');
    inputs.forEach(input => {
        const answer = input.value;
        const surveyId = input.getAttribute('data-survey-id');

        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ survey_id: surveyId, answer: answer }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Відповідь успішно надіслана!');
                input.value = ''; // Очистити поле після відправки
            }
        });
    });
});

