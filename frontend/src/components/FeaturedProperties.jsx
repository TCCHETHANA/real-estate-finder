import PropertyCard from "./PropertyCard";
import "./FeaturedProperties.css";

const listings = [
  {
    id: 1,
    image: "/images/hero.jpg",
    title: "Maple Ridge Residence",
    address: "412 Maple Ridge Rd, Austin, TX",
    price: "$385,000",
    beds: 3,
    baths: 2,
    sqft: 1840,
    verified: true,
  },
  {
    id: 2,
    image: "/images/hero.jpg",
    title: "Harborview Loft",
    address: "88 Harborview Ave, Seattle, WA",
    price: "$612,000",
    beds: 2,
    baths: 2,
    sqft: 1290,
    verified: true,
  },
  {
    id: 3,
    image: "/images/hero.jpg",
    title: "Cedar Hollow Cottage",
    address: "27 Cedar Hollow Ln, Asheville, NC",
    price: "$249,000",
    beds: 2,
    baths: 1,
    sqft: 980,
    verified: false,
  },
];

export default function FeaturedProperties() {
  return (
    <section className="featured">
      <div className="featured__header">
        <span className="featured__eyebrow">SELECTED · 03 OF {listings.length}</span>
        <h2>Featured listings</h2>
        <p>A short list, chosen for fit — not for filling space.</p>
      </div>

      <div className="featured__grid">
        {listings.map((listing) => (
          <PropertyCard key={listing.id} property={listing} />
        ))}
      </div>
    </section>
  );
}