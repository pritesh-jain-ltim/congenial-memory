import logo from './logo.svg';
import octofitLogo from '../public/octofitapp-small.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <nav>
        <img src={octofitLogo} className="App-logo-left" alt="Octofit Logo" />
        <a href="#home">Home</a>
        <a href="#features">Features</a>
        <a href="#leaderboard">Leaderboard</a>
        <a href="#profile">Profile</a>
      </nav>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Welcome to Octofit Tracker</h1>
        <p>
          Your all-in-one fitness tracking and team competition app.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <div style={{marginTop: '32px'}}>
          <button>Get Started</button>
          <button className="btn">Join a Team</button>
        </div>
      </header>
      <main>
        <section style={{margin: '40px auto', maxWidth: '900px'}}>
          <h2>Leaderboard</h2>
          <table>
            <thead>
              <tr>
                <th>Rank</th>
                <th>Team</th>
                <th>Points</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>OctoWarriors</td>
                <td>1200</td>
              </tr>
              <tr>
                <td>2</td>
                <td>FitSquad</td>
                <td>1100</td>
              </tr>
              <tr>
                <td>3</td>
                <td>PowerPandas</td>
                <td>950</td>
              </tr>
            </tbody>
          </table>
        </section>
      </main>
    </div>
  );
}

export default App;
