const hackathonList = document.getElementById('hackathon-list');

// Add a click event listener to the hackathon list
hackathonList.addEventListener('click', event => {
  if (event.target.classList.contains('enroll-button')) {
    // If the clicked element is an enroll button, display the enrollment form
    displayEnrollmentForm(event);
  } else if (event.target.classList.contains('submit-button')) {
    // If the clicked element is a submit button, display the entry submission form
    displaySubmitEntryForm(event);
  }
});

// Function to display the hackathon enrollment form
function displayEnrollmentForm(event) {
  // Get the hackathon ID from the data attribute on the button
  const hackathonId = event.target.dataset.id;

  // Replace the enroll button with the form
  const button = event.target;
  const form = document.createElement('form');
  form.innerHTML = `
    <label for="participant-name">Name:</label>
    <input type="text" id="participant-name" required>
    <br>
    <label for="participant-email">Email:</label>
    <input type="email" id="participant-email" required>
    <br>
    <button type="submit">Enroll</button>
  `;
  button.parentElement.replaceChild(form, button);

  // Add a submit event listener to the form
  form.addEventListener('submit', event => {
    event.preventDefault();
    const name = document.getElementById('participant-name').value;
    const email = document.getElementById('participant-email').value;

    // Send a POST request to the enrollment API
    fetch(`/api/hackathons/${hackathonId}/enrollments/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name,
        email
      })
    })
    .then(response => response.json())
    .then(data => {
      // Display a success message
      const message = document.createElement('p');
      message.textContent = 'You have successfully enrolled!';
      form.parentElement.replaceChild(message, form);
    })
    .catch(error => {
      // Display an error message
      const message = document.createElement('p');
      message.textContent = 'There was an error enrolling. Please try again.';
      form.parentElement.replaceChild(message, form);
    });
  });
}

// Function to display the hackathon entry submission form
function displaySubmitEntryForm(event) {
  // Get the hackathon ID from the data attribute on the button
  const hackathonId = event.target.dataset.id;

  // Replace the submit entry button with the form
  const button = event.target;
  const form = document.createElement('form');
  form.innerHTML = `
    <label for="entry-name">Name:</label>
    <input type="text" id="entry-name" required>
    <br>
    <label for="entry-summary">Summary:</label>
    <textarea id="entry-summary" required></textarea>
    <br>
    <label for="entry-submission">Submission URL:</label>
    <input type="url" id="entry-submission" required>
    <br>
    <button type="submit">Submit Entry</button>
  `;
  button.parentElement.replaceChild(form, button);

  // Add a submit event listener to the form
  form.addEventListener('submit', (event) => {
    event.preventDefault();

    // Get the form data
    const name = document.querySelector('#entry-name').value;
    const summary = document.querySelector('#entry-summary').value;
    const submissionUrl = document.querySelector('#entry-submission').value;

    // Make a POST request to create a new entry
    fetch(`/api/hackathons/${hackathonId}/entries/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({
        name,
        summary,
        submission_url: submissionUrl
      })
    })
    .then(response => {
      if (response.ok) {
        // Reload the page to show the new entry
        location.reload();
      } else {
        // Display an error message
        alert('Error creating entry');
      }
    });
  });
}
