import SearchBar from "../components/SearchBar";
import PriceEstimator from "../components/PriceEstimator";

export default function Home() {
  return (
    <section className="hero-section">
      <div className="hero-copy">
        <p className="eyebrow">Smart property search</p>
        <h1>Find homes that fit your budget and lifestyle.</h1>
        <p>
          Compare listings, filter by location and amenities, and get a price estimate powered by your ML model.
        </p>
      </div>

      <div className="stack">
        <SearchBar />
        <PriceEstimator />
      </div>
    </section>
  );
}