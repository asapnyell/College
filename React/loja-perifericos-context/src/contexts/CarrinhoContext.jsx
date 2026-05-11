import { createContext, useState, useContext } from 'react';

const CarrinhoContext = createContext();

export function CarrinhoProvider({ children }) {
  const [itens, setItens] = useState([]);

  function adicionarAoCarrinho(produto) {
    setItens([...itens, produto]);
  }

  function limparCarrinho() {
    setItens([]);
  }

  const valorTotal = itens.reduce((acumulador, item) => acumulador + item.preco, 0);

  return (
    <CarrinhoContext.Provider value={{ itens, adicionarAoCarrinho, limparCarrinho, valorTotal }}>
      {children}
    </CarrinhoContext.Provider>
  );
}

export const useCarrinho = () => useContext(CarrinhoContext);