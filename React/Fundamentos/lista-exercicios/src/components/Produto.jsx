

export default function Produto({ nome, quantidade }) {
  return (
    <div className="produto-card">
      <h3>{nome}</h3>
      {quantidade > 0 && <p className="em-estoque">Em estoque ({quantidade} unidades)</p>}
      {quantidade === 0 && <p className="esgotado">Produto esgotado</p>}
    </div>
  );
};

