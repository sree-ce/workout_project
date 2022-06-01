import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { HomePage } from './Pages/HomePage/HomePage';
import { SignupPage } from './Pages/SignupPage/SignupPage';
import { LoginPage } from './Pages/LoginPage/LoginPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<HomePage />} path='/' />
        <Route element={<SignupPage />} path='/signup' />
        <Route element={<LoginPage />} path='/login' />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
