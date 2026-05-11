import { createContext, useState, useContext } from 'react';

const TemaContext = createContext();

export function TemaProvider({ children }) {
  // Inicializa o tema buscando no localStorage ou padrão 'claro'
  const [tema, setTema] = useState(localStorage.getItem('tema_salvo') || 'claro');

  // Alterna entre claro e escuro
  function alternarTema() {
    const novoTema = tema === 'claro' ? 'escuro' : 'claro';
    setTema(novoTema);
    localStorage.setItem('tema_salvo', novoTema);
  }

  return (
    <TemaContext.Provider value={{ tema, alternarTema }}>
      {children}
    </TemaContext.Provider>
  );
}

export const useTema = () => useContext(TemaContext);