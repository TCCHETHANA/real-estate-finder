const BASE_URL = "http://localhost:5000/api";

export async function searchProperties(params) {
  const query = new URLSearchParams(params).toString();
  const res = await fetch(`${BASE_URL}/search/?${query}`);
  if (!res.ok) throw new Error("Search request failed");
  return res.json();
}

export async function predictPrice(data) {
  const res = await fetch(`${BASE_URL}/predict/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Prediction request failed");
  return res.json();
}