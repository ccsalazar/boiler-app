"use client";
import React, { useState } from 'react';

const CounterButton: React.FC = () => {
  const [counter, setCounter] = useState<number>(0);

  const incrementCounter = async () => {
    console.log("Going to call backend")
    try {
      // Make a POST request to the Flask API endpoint
      const response = await fetch('http://localhost:5000/increment_counter', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        mode: 'cors' // Ensure CORS mode
      });

      if (response.ok) {
        // If the request is successful, update the counter state
        const data = await response.json();
        console.log("DATA: ", data)
        setCounter(data.count);
      } else {
        // Handle error response
        console.error('Failed to increment counter');
      }
    } catch (error) {
      // Handle network error
      console.error('Network error:', error);
    }
  };

  return (
    <div>
      <h1>Counter: {counter}</h1>
      <button onClick={incrementCounter}>Increment Counter</button>
    </div>
  );
};

export default CounterButton;