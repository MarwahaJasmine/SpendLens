import { useState } from 'react';
import { analyzeSpending } from '../api';

export default function InsightsPanel() {
  const [insight, setInsight] = useState(null);
  const [cached, setCached] = useState(false);
  const [loading, setLoading] = useState(false);

  async function handleAnalyze() {
    setLoading(true);
    try {
      const result = await analyzeSpending();
      setInsight(result.insight);
      setCached(result.cached);
    } catch (err) {
      setInsight("Couldn't generate insights. Make sure transactions are uploaded and the server is running.");
    }
    setLoading(false);
  }

  return (
    <div style={{
      background: 'var(--surface)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius)',
      padding: '1.5rem',
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h3>Spending insights</h3>
        <span style={{
          fontSize: '0.7rem',
          color: 'var(--primary)',
          background: '#EEF2FF',
          padding: '0.2rem 0.5rem',
          borderRadius: '6px',
          fontWeight: 600,
        }}>
          AI-generated
        </span>
      </div>

      <button
        onClick={handleAnalyze}
        disabled={loading}
        style={{
          background: loading ? 'var(--text-secondary)' : 'var(--primary)',
          color: 'white',
          border: 'none',
          borderRadius: '8px',
          padding: '0.6rem 1.2rem',
          fontWeight: 500,
          width: '100%',
          marginBottom: '1rem',
        }}
      >
        {loading ? 'Analyzing...' : 'Generate insights'}
      </button>

      {insight && (
        <div>
          <p style={{ whiteSpace: 'pre-line', fontSize: '0.9rem', lineHeight: 1.6 }}>
            {insight}
          </p>
          <p style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', marginTop: '0.75rem' }}>
            {cached ? '⚡ Served from cache' : '✨ Freshly generated'}
          </p>
        </div>
      )}
    </div>
  );
}
