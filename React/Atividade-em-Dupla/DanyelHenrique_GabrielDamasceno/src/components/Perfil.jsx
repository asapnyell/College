import './Perfil.css';

export default function Perfil({ nome, curso, status }) {
  return (
    <div className="perfil-card">
      <h2>Perfil do Aluno</h2>
      <p><strong>Nome:</strong> {nome}</p>
      <p><strong>Curso:</strong> {curso}</p>
      <p className="status-badge"><strong>Status:</strong> {status}</p>
    </div>
  );
};

