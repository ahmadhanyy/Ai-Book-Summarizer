import React, { useState } from 'react';
import './UploadForm.scss';
import Spinner from '../../assets/Spinner.gif';

interface UploadFormProps {
  onSummaryGenerated: (summary: string) => void;
}

const UploadForm: React.FC<UploadFormProps> = ({ onSummaryGenerated }) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setSelectedFile(event.target.files[0]);
    }
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    if (selectedFile) {
      setIsLoading(true);
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await fetch('http://127.0.0.1:5000/upload', { // Adjust URL as per your Flask server
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const data = await response.json();
          onSummaryGenerated(data.summary); // Pass summary back to parent component
        } else {
          console.error('Failed to summarize:', response.statusText);
          const errorMessage = 'Failed to generate summary. Please try again.';
          onSummaryGenerated(errorMessage); // Pass error message back to parent component
        }
      } catch (error) {
        console.error('Error summarizing:', error);
        const errorMessage = 'An error occurred while summarizing. Please try again.';
        onSummaryGenerated(errorMessage); // Pass error message back to parent component
      } finally {
        setIsLoading(false);
      }
    }
  };

  return (
    <div className="upload-form-container">
      <div className='spinner'>
        {isLoading && <img src={Spinner} alt="Loading..." className="upload-form__spinner" />}
      </div>
      <form className="upload-form" onSubmit={handleSubmit}>
        <div className="upload-form__group">
          <label htmlFor="file-upload" className="upload-form__label">
            Choose your file
          </label>
          <input 
            type="file" 
            id="file-upload" 
            className="upload-form__input" 
            onChange={handleFileChange} 
          />
          <div className="upload-form__buttons">
            <button type="submit" className="upload-form__button upload-form__button--primary" disabled={isLoading}>
              Upload
            </button>
            <button type="reset" className="upload-form__button upload-form__button--secondary" onClick={() => setSelectedFile(null)} disabled={isLoading}>
              Cancel
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default UploadForm;
