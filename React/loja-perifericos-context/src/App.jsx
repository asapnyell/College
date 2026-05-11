import { CarrinhoProvider } from './contexts/CarrinhoContext';
import { TemaProvider, useTema } from './contexts/TemaContext';
import Navbar from './components/Navbar';
import ListaProdutos from './components/ListaProdutos';
import './styles/global.css';

// Criamos um componente interno para aplicar a classe de tema
function AppContent() {
  const { tema } = useTema();

  return (
    <div className={`app-container ${tema}`}>
      <Navbar />
      <main>
        <h1>Loja Tech</h1>
        <ListaProdutos />
      </main>
    </div>
  );
}

function App() {
  return (
    <TemaProvider>
      <CarrinhoProvider>
        <AppContent />
      </CarrinhoProvider>
    </TemaProvider>
  );
}

export default App;