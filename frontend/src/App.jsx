import { useState, useEffect, useCallback } from 'react';
import UploadCard from './components/UploadCard';
import TransactionsTable from './components/TransactionsTable';
import InsightsPanel from './components/InsightsPanel';
import { getTransactions } from './api';

function App() {
  const [transactions, setTransactions] = useState([]);
  const [loadingTransactions, setLoadingTransactions] = useState(true);

  const loadTransactions = useCallback(async () => {
    setLoadingTransactions(true);
    try {
      const data = await getTransactions();
      setTransactions(data);
    } catch (err) {
      console.error('Failed to load transactions', err);
    }
    setLoadingTransactions(false);
  }, []);

  useEffect(() => {
    loadTransactions();
  }, [loadTransactions]);

  return (
    <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '2.5rem 1.5rem' }}>
      <header style={{
        marginBottom: '2.5rem',
        paddingBottom: '1.5rem',
        borderBottom: '1px solid var(--border)',
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '0.4rem' }}>
          <div style={{
            width: '10px',
            height: '10px',
            borderRadius: '3px',
            background: 'var(--primary)',
          }} />
          <h1 style={{ fontSize: '1.6rem' }}>SpendLens</h1>
        </div>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
          Upload a statement, see where your money goes.
        </p>
      </header>

      <div style={{ marginBottom: '1.5rem' }}>
        <UploadCard onUploadComplete={loadTransactions} />
      </div>

      <div
        className="dashboard-grid"
        style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem', alignItems: 'start' }}
      >
        <TransactionsTable transactions={transactions} loading={loadingTransactions} />
        <InsightsPanel hasTransactions={transactions.length > 0} />
      </div>
    </div>
  );
}

export default App;