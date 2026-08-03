import "./Navbar.css";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar__brand">
        <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
          <path d="M4 14 L14 5 L24 14 M7 12 V23 H21 V12" stroke="#16233B" strokeWidth="1.6" fill="none" />
        </svg>
        <span>Nestly</span>
      </div>
      <nav className="navbar__links">
        <a href="/buy">Buy</a>
        <a href="/rent">Rent</a>
        <a href="/sell">Sell</a>
        <a href="/agents">Agents</a>
      </nav>
      <div className="navbar__actions">
        <a href="/login" className="navbar__link">Sign in</a>
        <a href="/signup" className="navbar__cta">List a property</a>
      </div>
    </header>
  );
}