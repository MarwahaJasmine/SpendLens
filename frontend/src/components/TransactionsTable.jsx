export default function TransactionsTable({ transactions }) {
  return (
    <div style={{
      background: 'var(--surface)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius)',
      overflow: 'hidden',
    }}>
      <div style={{ padding: '1.25rem 1.5rem', borderBottom: '1px solid var(--border)' }}>
        <h3>Transactions</h3>
      </div>
      {transactions.length === 0 ? (
        <p style={{ padding: '1.5rem', color: 'var(--text-secondary)' }}>
          No transactions yet. Upload a CSV to get started.
        </p>
      ) : (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ color: 'var(--text-secondary)', fontSize: '0.8rem', textAlign: 'left' }}>
              <th style={{ padding: '0.75rem 1.5rem' }}>Date</th>
              <th style={{ padding: '0.75rem 1.5rem' }}>Description</th>
              <th style={{ padding: '0.75rem 1.5rem', textAlign: 'right' }}>Amount</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map((t) => (
              <tr key={t.id} style={{ borderTop: '1px solid var(--border)' }}>
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