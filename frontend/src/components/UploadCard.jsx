import { useState, useRef } from 'react';
import { uploadCSV } from '../api';

export default function UploadCard({ onUploadComplete }) {
  const [isDragging, setIsDragging] = useState(false);
  const [status, setStatus] = useState(null);
  const fileInputRef = useRef(null);

  async function handleFile(file) {
    if (!file || !file.name.endsWith('.csv')) {
      setStatus({ type: 'error', message: 'Please upload a .csv file' });
      return;
    }
    setStatus({ type: 'loading', message: 'Uploading...' });
    try {
      const result = await uploadCSV(file);
      setStatus({ type: 'success', message: result.message });
      onUploadComplete();
    } catch (err) {
      setStatus({ type: 'error', message: 'Upload failed. Check the server is running.' });
    }
  }

  return (
    <div
      onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
      onDragLeave={() => setIsDragging(false)}
      onDrop={(e) => {
        e.preventDefault();
        setIsDragging(false);
        handleFile(e.dataTransfer.files[0]);
      }}
      style={{
        background: 'var(--surface)',
        border: `2px dashed ${isDragging ? 'var(--primary)' : 'var(--border)'}`,
        borderRadius: 'var(--radius)',
        padding: '2rem',
        textAlign: 'center',
        transition: 'border-color 150ms ease',
      }}
    >
      <h3 style={{ marginBottom: '0.5rem' }}>Upload a bank statement</h3>
      <p style={{ color: 'var(--text-secondary)', marginBottom: '1rem', fontSize: '0.9rem' }}>
        Drop a CSV file here, or click to browse
      </p>
      <input
        ref={fileInputRef}
        type="file"
        accept=".csv"
        style={{ display: 'none' }}
        onChange={(e) => handleFile(e.target.files[0])}
      />
      <button
        onClick={() => fileInputRef.current.click()}
        style={{
          background: 'var(--primary)',
          color: 'white',
          border: 'none',
          borderRadius: '8px',
          padding: '0.6rem 1.2rem',
          fontWeight: 500,
        }}
      >
        Choose file
      </button>
      {status && (
        <p style={{
          marginTop: '1rem',
          fontSize: '0.85rem',
          color: status.type === 'error' ? '#DC2626' : 'var(--positive)',
        }}>
          {status.message}
        </p>
      )}
    </div>
  );
}
