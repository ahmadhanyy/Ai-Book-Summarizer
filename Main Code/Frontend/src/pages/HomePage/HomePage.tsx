import React, { useState } from 'react';
import UploadForm from '../../components/UploadForm/UploadForm';
import SummaryDisplay from '../../components/SummaryDisplay/SummaryDisplay';
import './HomePage.scss';

const HomePage: React.FC = () => {
  const [summary, setSummary] = useState<string | null>(null);

  const handleSummaryGenerated = (generatedSummary: string) => {
    setSummary(generatedSummary);
  };

  return (
    <div className="home-page">
      <section className="hero">
        <h1>Summarize Entire Books with AI - For Free</h1>
        <p>Instantly get concise and accurate summaries of your favorite books with our advanced AI technology.</p>
        <a href="#upload" className="cta-button">Upload Your Book Now</a>
      </section>

      <section className="features">
        <h2>Why Use Our AI Book Summarizer?</h2>
        <div className="features-list">
          <div className="feature-item">
            <h3>Fast and Efficient</h3>
            <p>Get detailed summaries within seconds, saving you hours of reading time.</p>
          </div>
          <div className="feature-item">
            <h3>Accurate and Reliable</h3>
            <p>Our AI ensures the key points and insights are captured accurately from every book.</p>
          </div>
          <div className="feature-item">
            <h3>Completely Free</h3>
            <p>Enjoy unlimited book summaries without any cost or hidden fees.</p>
          </div>
          <div className="feature-item">
            <h3>User-Friendly</h3>
            <p>Simple and intuitive interface for easy book uploads and summary downloads.</p>
          </div>
        </div>
      </section>
      <section className="how-it-works">
        <h2>How It Works?</h2>
        <div className="steps">
          <div className="step">
            <h3>1. Upload Your Book</h3>
            <p>Choose your PDF book file and upload it to our platform.</p>
          </div>
          <div className="step">
            <h3>2. Let Our AI Process It</h3>
            <p>Our advanced AI technology will analyze and summarize the book within seconds.</p>
          </div>
          <div className="step">
            <h3>3. Get Your Summary</h3>
            <p>Receive a comprehensive summary that captures all the key points and insights.</p>
          </div>
        </div>
      </section>

      {summary && <SummaryDisplay summary={summary} />}

      <div id="upload">
        <UploadForm onSummaryGenerated={handleSummaryGenerated} />
      </div>
    </div>
  );
};

export default HomePage;