import { useState, useEffect, useCallback } from 'react';
import UploadCard from './components/UploadCard';
import TransactionsTable from './components/TransactionsTable';
import InsightsPanel from './components/InsightsPanel';
import { getTransactions } from './api';

function App() {
  const [transactions, setTransactions] = useState([]);

  const loadTransactions = useCallback(async () => {
    try {
      const data = await getTransactions();
      setTransactions(data);
    } catch (err) {
      console.error('Failed to load transactions', err);
    }
  }, []);

  useEffect(() => {
    loadTransactions();
  }, [loadTransactions]);

  return (
    <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '2.5rem 1.5rem' }}>
      <header style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.75rem' }}>SpendLens</h1>
        <p style={{ color: 'var(--text-secondary)', marginTop: '0.25rem' }}>
          Upload a statement, see where your money goes.
        </p>
      </header>

      <div style={{ marginBottom: '1.5rem' }}>
        <UploadCard onUploadComplete={loadTransactions} />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem' }}>
        <TransactionsTable transactions={transactions} />
        <InsightsPanel />
      </div>
    </div>
  );
}

export default App;