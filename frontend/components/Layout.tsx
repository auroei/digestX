import { ReactNode } from 'react';
import Head from 'next/head';

interface LayoutProps {
  children: ReactNode;
  title?: string;
}

const Layout = ({ children, title = 'DigestX' }: LayoutProps) => {
  return (
    <div>
      <Head>
        <title>{title}</title>
        <meta name="description" content="Your AI-powered content digest" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header>
        <nav>
          <h1>DigestX</h1>
        </nav>
      </header>

      <main>{children}</main>

      <footer>
        <p>&copy; {new Date().getFullYear()} DigestX. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Layout; 