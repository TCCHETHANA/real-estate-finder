import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { searchProperties } from "../api";
import PropertyCard from "../components/PropertyCard";

const fallbackProperties = [
  {
    location: "Bangalore, Karnataka",
    price: 7500000,
    area_sqft: 1200,
    property_type: "Apartment",
    amenities: "Gym, Parking, Pool",
    description: "Bright apartment in a well-connected neighborhood.",
  },
  {
    location: "Pune, Maharashtra",
    price: 9800000,
    area_sqft: 1550,
    property_type: "Villa",
    amenities: "Garden, Security",
    description: "Spacious villa with modern interiors.",
  },
];

export default function Results() {
  const [searchParams] = useSearchParams();
  const [properties, setProperties] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchResults = async () => {
      setLoading(true);
      try {
        const data = await searchProperties(Object.fromEntries(searchParams));
        setProperties(Array.isArray(data) ? data : []);
        setError(null);
      } catch (err) {
        setProperties(fallbackProperties);
        setError("Failed to load properties. Is the backend running?");
      } finally {
        setLoading(false);
      }
    };

    fetchResults();
  }, [searchParams]);

  if (loading) return <p className="status">Loading properties...</p>;

  return (
    <section className="results-page">
      <h2>Search Results</h2>
      {error && <p className="status error">{error}</p>}
      {properties.length === 0 ? (
        <p className="status">No properties match your criteria.</p>
      ) : (
        <div className="property-grid">
          {properties.map((property, idx) => (
            <PropertyCard key={idx} property={property} />
          ))}
        </div>
      )}
    </section>
  );
}