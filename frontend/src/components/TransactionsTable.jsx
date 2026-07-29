export default function TransactionsTable({ transactions, loading }) {
  return (
    <div className="card" style={{
      background: 'var(--surface)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius)',
      overflow: 'hidden',
    }}>
      <div style={{ padding: '1.25rem 1.5rem', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h3>Transactions</h3>
        {transactions.length > 0 && (
          <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
            {transactions.length} total
          </span>
        )}
      </div>

      {loading ? (
        <div style={{ padding: '1.5rem' }}>
          {[1, 2, 3].map((i) => (
            <div key={i} className="skeleton" style={{ height: '20px', marginBottom: '1rem', width: `${90 - i * 10}%` }} />
          ))}
        </div>
      ) : transactions.length === 0 ? (
        <div style={{ padding: '2.5rem 1.5rem', textAlign: 'center' }}>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
            No transactions yet. Upload a CSV above to get started.
          </p>
        </div>
      ) : (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ color: 'var(--text-secondary)', fontSize: '0.75rem', textAlign: 'left', textTransform: 'uppercase', letterSpacing: '0.03em' }}>
              <th style={{ padding: '0.75rem 1.5rem', fontWeight: 600 }}>Date</th>
              <th style={{ padding: '0.75rem 1.5rem', fontWeight: 600 }}>Description</th>
              <th style={{ padding: '0.75rem 1.5rem', textAlign: 'right', fontWeight: 600 }}>Amount</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map((t) => (
              <tr
                key={t.id}
                style={{ borderTop: '1px solid var(--border)', transition: 'background-color 120ms ease' }}
                onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#F8FAFC'}
                onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
              >
                <td style={{ padding: '0.75rem 1.5rem', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
                  {t.date}
                </td>
                <td style={{ padding: '0.75rem 1.5rem', fontSize: '0.9rem' }}>
                  {t.description}
                </td>
                <td
                  className="mono"
                  style={{
                    padding: '0.75rem 1.5rem',
                    textAlign: 'right',
                    fontSize: '0.9rem',
                    fontWeight: 600,
                    color: t.amount >= 0 ? 'var(--positive)' : 'var(--text)',
                  }}
                >
                  {t.amount >= 0 ? '+' : ''}${t.amount.toFixed(2)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}