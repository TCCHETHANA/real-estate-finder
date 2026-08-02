export default function PropertyCard({ property }) {
  return (
    <article className="card property-card">
      <div className="property-top">
        <h4>{property.location || "Featured Property"}</h4>
        <span className="price-pill">₹{Number(property.price || 0).toLocaleString()}</span>
      </div>
      <p><strong>Area:</strong> {property.area_sqft || "N/A"} sqft</p>
      {property.property_type && <p><strong>Type:</strong> {property.property_type}</p>}
      {property.amenities && <p><strong>Amenities:</strong> {property.amenities}</p>}
      {property.description && <p>{property.description}</p>}
    </article>
  );
}