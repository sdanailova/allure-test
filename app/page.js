export default function HomePage() {
  return (
    <main style={{
      minHeight: "100vh",
      display: "grid",
      placeItems: "center",
      fontFamily: "Arial, sans-serif",
      background: "#f8fafc"
    }}>
      <section style={{ textAlign: "center", padding: 24 }}>
        <h1 data-testid="hero-title" style={{ marginBottom: 8 }}>HelloWorld</h1>
        <p data-testid="hero-subtitle" style={{ marginTop: 0 }}>
          This is a tiny Next.js static site for Allure report demo.
        </p>
      </section>
    </main>
  );
}
