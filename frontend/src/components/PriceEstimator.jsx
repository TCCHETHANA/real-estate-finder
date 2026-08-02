import { useState } from "react";
import { predictPrice } from "../api";

export default function PriceEstimator() {
  const [form, setForm] = useState({
    area_sqft: "",
    location: "",
    property_type: "",
  });
  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handlePredict = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await predictPrice(form);
      if (data.error) setError(data.error);
      else setPrice(data.predicted_price);
    } catch (err) {
      setError("Failed to fetch prediction. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h3>Estimate a fair price</h3>
      <div className="field-grid">
        <input name="area_sqft" type="number" placeholder="Area (sqft)" value={form.area_sqft} onChange={handleChange} />
        <input name="location" placeholder="Location" value={form.location} onChange={handleChange} />
        <input name="property_type" placeholder="Property Type" value={form.property_type} onChange={handleChange} />
      </div>
      <button onClick={handlePredict} disabled={loading}>
        {loading ? "Estimating..." : "Estimate Price"}
      </button>

      {error && <p className="status error">{error}</p>}
      {price !== null && <p className="status">Estimated Price: ₹{Number(price).toLocaleString()}</p>}
    </div>
  );
}