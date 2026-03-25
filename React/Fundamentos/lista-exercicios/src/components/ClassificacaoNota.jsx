export default function ClassificacaoNota({ nota }) {
    const classificacao = (nota >= 9) ? "Excelente" : (nota >= 7) ? "Bom" : (nota >= 5) ? "Regular" : "Insuficiente";


    return (
        <div className={`nota-container ${classificacao.toLowerCase()}`}>
            <p>Nota: {nota}</p>
            <p>Classificação: <strong>{classificacao}</strong></p>
        </div>
    );
};
