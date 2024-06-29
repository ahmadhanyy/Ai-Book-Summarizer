import React from 'react';
import './AboutPage.scss';

const AboutPage: React.FC = () => {
  return (
    <div className="about-page">
      <section className="about-hero">
        <h1>About SummaryFlow</h1>
        <p>Your trusted AI-powered book summarizer.</p>
      </section>
      
      <section className="about-content">
        <div className="about-text">
          <h2>Our Mission!</h2>
          <p>
            At SummaryFlow, we are dedicated to making knowledge accessible and
            digestible for everyone. Our cutting-edge AI technology transforms lengthy
            books into concise, insightful summaries, saving you time and enhancing your
            learning experience.
          </p>
        </div>

        <div className="about-text">
          <h2>Who We Are?</h2>
          <p>
            SummaryFlow is a passionate team of AI experts, software engineers, and book
            enthusiasts. We believe in the power of technology to revolutionize how we
            consume information. Our goal is to provide an easy-to-use, free service that
            empowers readers and learners around the globe.
          </p>
        </div>

        <div className="about-text">
          <h2>What We Do?</h2>
          <p>
            Our platform uses advanced natural language processing algorithms to analyze
            and summarize entire books. Whether you’re a student, a professional, or an
            avid reader, SummaryFlow helps you grasp the essential points of a book quickly
            and accurately.
          </p>
        </div>

        <div className="about-text">
          <h2>Why Choose Us?</h2>
          <ul>
            <li>Free and accessible for everyone.</li>
            <li>Accurate and reliable summaries.</li>
            <li>Fast processing times.</li>
            <li>User-friendly interface.</li>
            <li>Committed to enhancing your reading experience.</li>
          </ul>
        </div>
      </section>
    </div>
  );
};

export default AboutPage;
