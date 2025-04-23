import React from 'react';

const Dashboard = ({ onLogout }) => {
  return (
    <div style={{ padding: '2rem' }}>
      <h2>Welcome to Dispatch Dashboard</h2>
      <p>This is a placeholder dashboard.</p>
      <button onClick={onLogout}>Logout</button>
    </div>
  );
};

export default Dashboard;
