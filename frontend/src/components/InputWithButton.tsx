// src/components/InputWithButton.tsx
import { useState } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Alert, AlertDescription, AlertTitle } from './ui/alert';
import { AlertCircle } from 'lucide-react';

const InputWithButton: React.FC = () => {
  const [inputValue, setInputValue] = useState('');
  const [responseErrorMessage, setResponseErrorMessage] = useState('');
  const [responseMessage, setResponseMessage] = useState('');

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setResponseErrorMessage(''); // Clear the alert when the user changes input
    const sanitizedInput = event.target.value.replace(/[^A-Za-z]/g, '');
    setInputValue(sanitizedInput); // Update the input value
  };

  const handleSubmit = async () => {
    if (inputValue.trim()) {
      try {
        const response = await fetch('http://localhost:5000/submit', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ input: inputValue }), // Send the input as JSON
        });

        const data = await response.json();

        if (response.ok) {
          // Handle success
          console.log(data.message);
          setResponseMessage(data.message);
        } else {
          // Handle error
          setResponseErrorMessage(data.error);
        }
      } catch (error) {
        // Handle network errors
        setResponseErrorMessage('Error submitting data');
        console.error(error);
      }
    }
  };

  const isButtonDisabled = inputValue.trim() === '';

  return (
    <div className="flex justify-center items-center py-10">
      <div className="flex flex-col items-center space-y-4 w-auto">
        <div className="flex items-center space-x-2 w-full rounded-lg border border-slate-300 p-2 shadow-sm">
          <Input
            value={inputValue}
            onChange={handleInputChange}
            placeholder="Please enter your prompt word"
            pattern="[A-Za-z]+"
            className="w-80 p-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-500"
          />
          <Button
              onClick={handleSubmit}
              disabled={isButtonDisabled}
              className={`${
                isButtonDisabled
                  ? 'bg-slate-300 text-slate-500 cursor-not-allowed'
                  : 'bg-slate-600 text-white hover:bg-slate-500 focus:ring-slate-500'
              } p-2 rounded-lg focus:outline-none focus:ring-2`}
          >
            Start
          </Button>
        </div>
        {responseErrorMessage && (
          <Alert variant="destructive" className="w-full">
            <AlertCircle className="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>
              {responseErrorMessage}
            </AlertDescription>
          </Alert> 
        )}
      </div>
    </div>
  );
};

export default InputWithButton;