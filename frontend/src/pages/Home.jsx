import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import FeaturedProperties from "../components/FeaturedProperties";

export default function Home() {
  return (
    <div style={{ background: "#EDF1EF", minHeight: "100vh" }}>
      <Navbar />
      <Hero />
      <FeaturedProperties />
    </div>
  );
}