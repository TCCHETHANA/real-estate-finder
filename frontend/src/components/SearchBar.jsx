import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function SearchBar() {
  const [budgetMin, setBudgetMin] = useState("");
  const [budgetMax, setBudgetMax] = useState("");
  const [location, setLocation] = useState("");
  const [amenities, setAmenities] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    const filters = {};
    if (budgetMin) filters.budget_min = budgetMin;
    if (budgetMax) filters.budget_max = budgetMax;
    if (location) filters.location = location;
    if (amenities) filters.amenities = amenities;

    const params = new URLSearchParams(filters);
    navigate(`/results?${params.toString()}`);
  };

  return (
    <form onSubmit={handleSubmit} className="card search-form">
      <h3>Find a home</h3>
      <div className="field-grid">
        <input type="number" placeholder="Min Budget" value={budgetMin} onChange={(e) => setBudgetMin(e.target.value)} />
        <input type="number" placeholder="Max Budget" value={budgetMax} onChange={(e) => setBudgetMax(e.target.value)} />
        <input type="text" placeholder="Location" value={location} onChange={(e) => setLocation(e.target.value)} />
        <input type="text" placeholder="Amenities (gym, parking)" value={amenities} onChange={(e) => setAmenities(e.target.value)} />
      </div>
      <button type="submit">Search Properties</button>
    </form>
  );
}