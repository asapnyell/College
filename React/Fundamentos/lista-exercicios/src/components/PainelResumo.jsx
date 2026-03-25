import NumeroInfo from './NumeroInfo';
import StatusUsuario from './StatusUsuario';
import ClassificacaoNota from './ClassificacaoNota';
import Produto from './Produto';

export default function PainelResumo() {
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1 style={{ alignItems: 'center', display: 'flex', justifyContent: 'center', border: '1px solid #ccc', padding: '10px', backgroundColor: 'black', color: 'white' }}>Painel de Resumo</h1>
      
      <section>
        <h2><u>Status de Usuários</u></h2>
        <StatusUsuario nome="Danyel" ativo={true} />
        <StatusUsuario nome="Visitante" ativo={false} />
      </section>

      <section>
        <h2><u>Controle de Estoque</u></h2>
        <Produto nome="Teclado Mecânico" quantidade={15} />
        <Produto nome="Mouse Gamer" quantidade={0} />
      </section>

      <section>
        <h2><u>Análise de Números</u></h2>
        <NumeroInfo numero={2000656066} />
        <NumeroInfo numero={2000656067} />
      </section>
      
      <section>
        <h2><u>Análise de Notas</u></h2>
        <ClassificacaoNota nota={10.0} />
      </section>
    </div>
  );
};

