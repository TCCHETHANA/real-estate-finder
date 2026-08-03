import "./Hero.css";

export default function Hero() {
  return (
    <section className="hero">
      <svg className="hero__blueprint" viewBox="0 0 1200 600" preserveAspectRatio="none">
        <rect x="120" y="80" width="380" height="260" fill="none" stroke="#2C4870" strokeWidth="1" opacity="0.25" />
        <line x1="310" y1="80" x2="310" y2="340" stroke="#2C4870" strokeWidth="1" opacity="0.25" />
        <rect x="700" y="220" width="320" height="220" fill="none" stroke="#2C4870" strokeWidth="1" opacity="0.25" />
        <circle cx="860" cy="330" r="4" fill="#2C4870" opacity="0.3" />
      </svg>

      <div className="hero__content">
        <span className="hero__eyebrow">FIND · COMPARE · MOVE IN</span>
        <h1>Every home starts as a floor plan.<br />Yours starts here.</h1>
        <p>Search verified listings by location, budget, and layout — matched to how you actually want to live.</p>

        <div className="hero__search">
          <div className="hero__search-field">
            <label>LOCATION</label>
            <input type="text" placeholder="City, neighborhood, ZIP" />
          </div>
          <div className="hero__search-divider" />
          <div className="hero__search-field">
            <label>TYPE</label>
            <select defaultValue="">
              <option value="" disabled>Any</option>
              <option>Apartment</option>
              <option>House</option>
              <option>Villa</option>
            </select>
          </div>
          <div className="hero__search-divider" />
          <div className="hero__search-field">
            <label>BUDGET</label>
            <select defaultValue="">
              <option value="" disabled>Any</option>
              <option>Under $200k</option>
              <option>$200k–$500k</option>
              <option>$500k+</option>
            </select>
          </div>
          <button className="hero__search-btn">Search</button>
        </div>
      </div>
    </section>
  );
}