import './Acao.css'; 

export default function Acao({ aoClicar }) {
  return (
    <div className="acao-container">
      <button className="btn-acao" onClick={aoClicar}>
        Concluir Atividade
      </button>
    </div>
  );
};
