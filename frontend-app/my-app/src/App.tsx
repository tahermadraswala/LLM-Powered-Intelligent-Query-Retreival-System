import React from 'react';
import QueryForm from './components/QueryForm';
import './styles/App.css';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Insurance Query Processor</h1>
        <p>Please enter your insurance query below:</p>
      </header>
      <main>
        <QueryForm />
      </main>
    </div>
  );
};

export default App;