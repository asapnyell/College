function Card(props) {
  const estilo = {
    border: `3px solid ${props.cor}`,
    borderRadius: '8px',
    padding: '20px',
    margin: '20px',
  }

  const cabecalho = {
    backgroundColor: props.cor,
    color: '#575757',
    padding: '10px',
    fontSize: '24px',
    textAlign: 'center',
    borderRadius: '6px 6px 0 0',
    marginBottom: '20px',
  }

  return (
    <div style={estilo}>
      <div style={cabecalho}>{props.titulo}</div>
      {props.aberto && props.children}
    </div>
  )
}

export default Card