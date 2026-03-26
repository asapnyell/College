import { useState } from 'react';
import Perfil from './components/Perfil';
import Acao from './components/Acao';
import './App.css';

export default function App() {
  // Estado centralizado
  const [status, setStatus] = useState("Estudando React");

  const finalizarTarefa = () => {
    setStatus("Atividade Concluída - Parabéns!");
  };

  return (
    <div className="app-container">
      <h1>Painel Interativo do Aluno</h1>
      
      {/* Comunicação Direta via Props */}
      <Perfil 
        nome="Danyel Henrique" 
        curso="Sistemas de Informação" 
        status={status} 
      />

      {/* Comunicação Indireta: passando função via props */}
      <Acao aoClicar={finalizarTarefa} />
    </div>
  );
}

