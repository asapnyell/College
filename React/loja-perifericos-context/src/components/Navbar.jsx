import { useCarrinho } from '../contexts/CarrinhoContext';
import { useTema } from '../contexts/TemaContext';

export default function Navbar() {
  const { itens, valorTotal, limparCarrinho } = useCarrinho();
  const { tema, alternarTema } = useTema();

  return (
    <nav className="navbar">
      <h2>🛒 Minha Loja</h2>
      <div className="controles">
        <button onClick={alternarTema} className="btn-tema">
          {tema === 'claro' ? '🌙 Modo Escuro' : '☀️ Modo Claro'}
        </button>
        <span>Itens: {itens.length}</span>
        <span> | Total: R$ {valorTotal.toFixed(2)}</span>
         <button onClick={limparCarrinho} className="btn-limpar">Limpar</button>
      </div>
    </nav>
  );
}


 
