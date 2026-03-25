import NumeroInfo from './components/NumeroInfo'
import StatusUsuario from './components/StatusUsuario'
import ClassificacaoNota from './components/ClassificacaoNota'
import Produto from './components/Produto'

import './components/ClassificacaoNota.css'
import './components/StatusUsuario.css'
import './components/NumeroInfo.css'
import './components/Produto.css'
import './index.css' 

import PainelResumo from './components/PainelResumo'

export default function App() {

  return (
    <>
    <div className="App">
      <h1 className='exercicio-title'>Exercício 1 – Par, Ímpar ou Zero</h1>
      <NumeroInfo numero={0} />
      <NumeroInfo numero={5} />
      <NumeroInfo numero={10} />

      <h1 className='exercicio-title'>Exercício 2 – Status de Usuário</h1>
      <StatusUsuario nome="João" ativo={true} />
      <StatusUsuario nome="João" ativo={false} />

      <h1 className='exercicio-title'>Exercício 3 - Classificação de Nota</h1>
      <ClassificacaoNota nota={9.5} />
      <ClassificacaoNota nota={8} />
      <ClassificacaoNota nota={6} />
      <ClassificacaoNota nota={4} />

      <h1 className='exercicio-title'>Exercício 4 – Produto em Estoque</h1>
      <Produto nome="Camiseta" quantidade={10} />
      <Produto nome="Calça" quantidade={0} />

      <PainelResumo/>

    </div>
    </>
  )
}


