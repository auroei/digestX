import { NextPage } from 'next';
import Layout from '../components/Layout';

const Home: NextPage = () => {
  return (
    <Layout>
      <div className="container">
        <h1>Welcome to DigestX</h1>
        <p>Your AI-powered content digest platform</p>
      </div>
    </Layout>
  );
};

export default Home; 