
export default function NumeroInfo({numero}) {
    const status = numero === 0 ? 'zero' : numero % 2 === 0 ? 'par' : 'impar';
    return (
        <div className = {`numero-container ${status}`}>
            <h2>O número recebido foi: <strong>{numero}</strong></h2>
            <p>Resultado: <span>{status.toUpperCase()}</span></p>
        </div>
    );  
}