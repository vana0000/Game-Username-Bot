import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [usernames, setUsernames] = useState('');
  const [availabilityResults, setAvailabilityResults] = useState({});

  // Function to check username availability
  const checkAvailability = async () => {
    try {
      // Make POST request to backend API with the usernames string
      const response = await axios.post('http://localhost:8080/api/check-availability', {
        usernames: usernames
      });

      // Update the availability results state
      setAvailabilityResults(response.data);
    } catch (error) {
      // Handle error
      console.error('There was an error checking the usernames availability:', error);
      setAvailabilityResults({ error: 'Error checking username availability.' });
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Username Availability Checker</h1>
      <input
        type="text"
        value={usernames}
        onChange={(e) => setUsernames(e.target.value)}
        placeholder="Enter usernames separated by commas"
      />
      <button onClick={checkAvailability}>Check Availability</button>

      {Object.keys(availabilityResults).length > 0 && (
        <div style={{ marginTop: '20px' }}>
          <strong>Results:</strong>
          <ul>
            {Object.entries(availabilityResults).map(([username, message]) => (
              <li key={username}>
                <strong>{username}:</strong> {message}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
