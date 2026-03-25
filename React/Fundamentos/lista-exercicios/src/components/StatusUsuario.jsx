

export default function StatusUsuario ({ nome, ativo }) {
  return (
    <div className="status-container">
      {ativo ? (
        <p className="usuario-ativo">Usuário ativo: <strong>{nome}</strong></p>
      ) : (
        <p className="usuario-inativo">Usuário inativo</p>
      )}
    </div>
  );
};

