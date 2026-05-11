import { useCarrinho } from '../contexts/CarrinhoContext';

const listaDeProdutos = [
  { id: 1, nome: 'Mouse Gamer', preco: 150 },
  { id: 2, nome: 'Teclado Mecânico', preco: 350 },
  { id: 3, nome: 'Monitor 144hz', preco: 1200 },
  { id: 4, nome: 'Gabinete Gamer Kalkan Skye', preco: 300 },
  { id: 5, nome: 'Placa de Vídeo RTX 3060', preco: 2500 },
  { id: 6, nome: 'Processador Ryzen 5 5600X', preco: 1200 },
  { id: 7, nome: 'Memória RAM 16GB', preco: 400 },
  { id: 8, nome: 'SSD 1TB', preco: 500 },
  { id: 9, nome: 'Fonte 650W', preco: 350 },
  { id: 10, nome: 'Cooler para Processador', preco: 150 },
  { id: 11, nome: 'Placa-Mãe B550', preco: 800 },
  { id: 12, nome: 'Headset Gamer', preco: 200 },
  { id: 13, nome: 'Webcam Full HD', preco: 250 },
  { id: 14, nome: 'Mousepad Gamer', preco: 50 },
  { id: 15, nome: 'Cadeira Gamer', preco: 900 },
];

export default function ListaProdutos() {
  const { adicionarAoCarrinho } = useCarrinho();

  return (
    <div className="grade-produtos">
      {listaDeProdutos.map(produto => (
        <div key={produto.id} className="cartao-produto">
          <h3>{produto.nome}</h3>
          <p>R$ {produto.preco.toFixed(2)}</p>
          <button onClick={() => adicionarAoCarrinho(produto)}>
            Adicionar ao Carrinho
          </button>
        </div>
      ))}
    </div>
  );
}