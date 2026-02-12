export const metadata = {
  title: "HelloWorld Demo",
  description: "Simple static Next.js app for Selenium + Allure demo",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body style={{ margin: 0 }}>{children}</body>
    </html>
  );
}
