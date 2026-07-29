const API_BASE = "http://127.0.0.1:8000";

export async function uploadCSV(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE}/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) throw new Error("Upload failed");
  return response.json();
}

export async function getTransactions() {
  const response = await fetch(`${API_BASE}/transactions`);
  if (!response.ok) throw new Error("Failed to fetch transactions");
  return response.json();
}

export async function analyzeSpending() {
  const response = await fetch(`${API_BASE}/analyze`);
  if (!response.ok) throw new Error("Analysis failed");
  return response.json();
}