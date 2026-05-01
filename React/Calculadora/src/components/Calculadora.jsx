import { useState } from 'react'
import './Calculadora.css'

const Calculadora = () => {
  const [form, setForm] = useState({ valor1: 0, valor2: 0 })
  const [resultado, setResultado] = useState(0)

  // O switch centraliza todas as operações em um lugar só
  const calcular = (operacao) => {
    const value1 = Number(form.valor1)
    const value2 = Number(form.valor2)

    switch (operacao) {
      case '+':
        setResultado(value1 + value2)
        break
      case '-':
        setResultado(value1 - value2)
        break
      case '*':
        setResultado(value1 * value2)
        break
      case '/':
        setResultado(value2 !== 0 ? value1 / value2 : 'Erro: div por 0')
        break
      case '%':
        setResultado(value1 % value2)
        break
      default:
        setResultado(0)
    }
  }

  return (
    <div className="calculadora">
      <div className='inputs'>
      <input
        type="number"
        value={form.valor1}
        onChange={(e) => setForm({ ...form, valor1: e.target.value })}
      />
      <input
        type="number"
        value={form.valor2}
        onChange={(e) => setForm({ ...form, valor2: e.target.value })}
      />
      </div>
      <div>
        <p style={{ marginTop: '12px', color: '#555' }}>
          Digite os valores e clique em uma operação para calcular o resultado:
        </p>
      </div>
      
      <div className='botoes'>
        <button style={{ margin: '5px' }} onClick={() => calcular('+')}>+</button>
        <button style={{ margin: '5px' }} onClick={() => calcular('-')}>-</button>
        <button style={{ margin: '5px' }} onClick={() => calcular('*')}>*</button>
        <button style={{ margin: '5px' }} onClick={() => calcular('/')}>/</button>
        <button style={{ margin: '5px' }} onClick={() => calcular('%')}>%</button>
      </div>
      <div className="resultado">
        Resultado: <span>{resultado}</span>
      </div>
    </div>
  )
}

export default Calculadora