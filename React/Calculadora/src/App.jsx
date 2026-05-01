import Card from './components/Card'
import Calculadora from './components/Calculadora'

function App() {
  return (
    <div>
      <Card titulo="Exercício - Calculadora" cor="#dbe1e3" aberto={true}>
        <Calculadora />
      </Card>
    </div>
  )
} 

export default App
