'''

<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Lista de Receitas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .receita {
      margin-bottom: 30px;
    }
    .receita h2 {
      color: #2c3e50;
      cursor: pointer;
    }
    .receita img {
      max-width: 300px;
      display: block;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <h1>Receitas</h1>
  <div id="lista-receitas"></div>

  <script>
    async function carregarReceitas() {
      try {
        // Consome a rota GET da sua API
        const response = await fetch("https://beck-end-do-site-de-receitas-2.onrender.com/receita/receber");
        const receitas = await response.json();

        const container = document.getElementById("lista-receitas");

        receitas.forEach(receita => {
          const div = document.createElement("div");
          div.className = "receita";

          // Nome da receita (clicável)
          const titulo = document.createElement("h2");
          titulo.textContent = receita.nome_da_receita;
          titulo.onclick = () => {
            // Redireciona para receita.html passando o ID da receita
            window.location.href = `receita.html?id=${receita.id}`;
          };

          // Foto da receita
          const img = document.createElement("img");
          if (receita.foto) {
            img.src = receita.foto;
            img.alt = receita.nome_da_receita;
          } else {
            img.src = "https://via.placeholder.com/300x200?text=Sem+Foto";
            img.alt = "Sem foto";
          }

          div.appendChild(titulo);
          div.appendChild(img);
          container.appendChild(div);
        });
      } catch (error) {
        console.error("Erro ao carregar receitas:", error);
      }
    }

    carregarReceitas();
  </script>
</body>
</html>






<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<<<<<<< HEAD
  <title>Receitas Deliciosas</title>
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Quicksand', sans-serif;
      background: #fdf6f0;
      color: #333;
    }

    header {
      background: linear-gradient(135deg, #ff7043, #ffcc80);
      color: white;
      padding: 20px;
      text-align: center;
      box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    header h1 {
      margin: 0;
      font-size: 2rem;
    }

    .receitas-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      padding: 30px;
      max-width: 1200px;
      margin: auto;
    }

    .card {
      background: white;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      overflow: hidden;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      text-align: center;
    }

    .card:hover {
      transform: translateY(-5px);
      box-shadow: 0 6px 14px rgba(0,0,0,0.15);
    }

    .card-title {
      background: #ffe0b2;
      padding: 12px;
      font-weight: bold;
      font-size: 18px;
    }

    .card-title a {
      text-decoration: none;
      color: #d35400;
      transition: color 0.3s;
    }

    .card-title a:hover {
      color: #e64a19;
    }

    .card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-bottom: 1px solid #eee;
    }

    footer {
      text-align: center;
      padding: 15px;
      background: #ff7043;
      color: white;
      margin-top: 30px;

  <title>Receitas Do MasterChef</title>
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; }

    html, body {
      margin: 0;
      padding: 0;
      font-family: 'Quicksand', sans-serif;
      background-color: #fffaf4;
      color: #333;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .dark-mode {
      background-color: #2c2c2c;
      color: #f5f5f5;
    }

    header {
      background-color: #ff7043;
      color: white;
      padding: 15px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .menu-icon {
      font-size: 24px;
      cursor: pointer;
    }

    .menu-options {
      display: none;
      position: absolute;
      top: 60px;
      right: 20px;
      background-color: white;
      border: 1px solid #ccc;
      border-radius: 8px;
      padding: 10px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
      z-index: 10;
    }

    .menu-aberto {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .menu-options button {
      background-color: #ff7043;
      color: white;
      border: none;
      border-radius: 5px;
      padding: 8px 12px;
      font-size: 14px;
      cursor: pointer;
      transition: background 0.3s;
    }

    .menu-options button:hover {
      background-color: #e64a19;
    }

    .receitas-container {
      padding: 30px 20px;
      max-width: 800px;
      margin: auto;
    }

    h2 {
      text-align: center;
      font-size: 28px;
      margin-bottom: 20px;
      color: #ff7043;
    }

    h2::before { content: "🍽️ "; }

    .receita-card {
      background: #fff3e0;
      border-radius: 10px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      padding: 20px;
      margin-bottom: 25px;
      animation: fadeInUp 0.5s ease;
      transition: transform 0.2s ease;
    }

    .receita-card:hover {
      transform: translateY(-5px);
    }

    .titulo-receita {
      font-weight: bold;
      font-size: 20px;
      margin-bottom: 15px;
      color: #ff7043;
      text-align: center;
    }

    .titulo-receita a {
      text-decoration: none;
      color: inherit;
    }

    .titulo-receita a:hover {
      color: #e64a19;
    }

    .receita-foto {
      max-width: 70%;
      border-radius: 8px;
      display: block;
      margin: 0 auto;
    }

    @keyframes fadeInUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 600px) {
      h2 { font-size: 22px; }
      .titulo-receita { font-size: 18px; }

    }
  </style>
</head>
<body>

  <header>

    <h1>🍲 Receitas Deliciosas</h1>
  </header>

  <div class="receitas-container" id="lista-receitas"></div>

  <footer>
    <p>Feito por David</p>
  </footer>

  <script>
    const API_BASE = "https://beck-end-do-site-de-receitas-vslw.vercel.app";

    async function buscarReceitas() {
      const res = await fetch(`${API_BASE}/receita/receber`);
      if (!res.ok) throw new Error("Erro ao buscar receitas");
      return await res.json();
    }

    async function carregarReceitas() {
      const container = document.getElementById("lista-receitas");
      container.innerHTML = "";
      const receitas = await buscarReceitas();

      receitas.forEach(r => {
        const div = document.createElement("div");
        div.className = "card";
        div.innerHTML = `
          <div class="card-title">
            <a href="receita.html?id=${r.id}">
              ${r.nome_da_receita}
            </a>
          </div>
          ${r.foto ? `<img src="${r.foto}" alt="${r.nome_da_receita}" />` : `<img src="https://via.placeholder.com/300x200?text=Sem+Foto" alt="Sem foto" />`}
        `;
        container.appendChild(div);
      });
    }

    carregarReceitas();

    <h1>🍲 Receitas</h1>
    <div>
      <button onclick="toggleDarkMode()">🌙 Modo Escuro</button>
      <span class="menu-icon" onclick="toggleMenu()">☰</span>
    </div>
    <div class="menu-options" id="menu">
      <button onclick="window.location.href='cadastrar.html'">Cadastrar Receita</button>
      <button onclick="window.location.href='cad_usuario3.html'">Registrar-se</button>
      <button onclick="window.location.href='cad_usuario2.html'">Fazer Login</button>
    </div>
  </header>

  <div class="receitas-container">
    <h2>📚 Lista de Receitas</h2>

    <!-- Receita 1 -->
    <div class="receita-card">
      <div class="titulo-receita">
        <a href="receita.html?id=50">Bolo de Milho</a>
      </div>
      <img class="receita-foto" src="imagens2/bolo-de-flocao-de-milho.jpg" alt="Bolo de Milho">
    </div>

    <!-- Receita 2 -->
    <div class="receita-card">
      <div class="titulo-receita">
        <a href="receita.html?id=10">Bife a Cavalo</a>
      </div>
      <img class="receita-foto" src="imagens2/bife_cavalo.jpg" alt="Bife a Cavalo">
    </div>
  </div>

    <!-- Receita 3 -->
    <div class="receita-card">
      <div class="titulo-receita">
        <a href="receita.html?id=61">Bolo de Chocolate</a>
      </div>
      <img class="receita-foto" src="imagens2/bolo-de-chocolate-rapido-e-molhadinho-capa.png" alt="Bolo de chocolate">
    </div>
  </div>

  <script>
    function toggleMenu() {
      const menu = document.getElementById("menu");
      menu.classList.toggle("menu-aberto");
    }

    function toggleDarkMode() {
      document.body.classList.toggle("dark-mode");
    }
>>>>>>> f869874 (ediçao do index)
  </script>

</body>
</html>







<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Receitas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fffaf4;
      margin: 0;
      padding: 0;
    }

    .receitas-container {
      max-width: 800px;
      margin: auto;
      padding: 20px;
      text-align: center;
    }

    h2 {
      font-size: 28px;
      margin-bottom: 20px;
    }

    .titulo-receita {
      font-weight: bold;
      font-size: 20px;
      margin: 20px 0 10px;
      color: #ff7043;
    }

    .titulo-receita a {
      text-decoration: none;
      color: inherit;
    }

    .titulo-receita a:hover {
      text-decoration: underline;
    }

    .receita-foto {
      max-width: 60%;
      border-radius: 8px;
      margin-bottom: 30px;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
  </style>
</head>
<body>

  <div class="receitas-container">
    <h2>📚 Lista de Receitas</h2>
    <!-- Receita 1 -->
    <div class="titulo-receita">
      <a href="receita.html?id=50">Bolo de Milho</a>
    </div>
    <img class="receita-foto" src="imagens2/bolo-de-flocao-de-milho.jpg" alt="Bolo de Milho">

    <!-- Receita 2 -->
    <div class="titulo-receita">
      <a href="receita.html?id=10">Bife a Cavalo</a>
    </div>
    <img class="receita-foto" src="imagens2/bife_cavalo.jpg" alt="Bife a Cavalo">
  </div>

</body>
</html>





<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Receitas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fffaf4;
      margin: 0;
      padding: 0;
    }

    .receitas-container {
      max-width: 800px;
      margin: auto;
      padding: 20px;
      text-align: center;
    }

    h2 {
      font-size: 28px;
      margin-bottom: 20px;
    }

    .titulo-receita {
      font-weight: bold;
      font-size: 20px;
      margin: 20px 0 10px;
      cursor: pointer;
      color: #ff7043;
    }

    .titulo-receita:hover {
      text-decoration: underline;
    }

    .receita-foto {
      max-width: 60%;
      border-radius: 8px;
      margin-bottom: 30px;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
  </style>
</head>
<body>

  <div class="receitas-container">
    <h2>📚 Lista de Receitas</h2>

    <!-- Receita 1 -->
    <div class="titulo-receita" onclick="mostrarDetalhes(1)">
      Bolo de Milho
    </div>
    <img class="receita-foto" src="imagens2/bolo-de-flocao-de-milho.jpg" alt="Bolo de Milho">

    <!-- Receita 2 -->
    <div class="titulo-receita" onclick="mostrarDetalhes(2)">
      Bife a Cavalo
    </div>
    <img class="receita-foto" src="imagens2/bife_cavalo.jpg" alt="Bife a Cavalo">

    <!-- Receita 3 -->
    <div class="titulo-receita" onclick="mostrarDetalhes(3)">
      Lasanha
    </div>
    <img class="receita-foto" src="imagens2/lasanha.jpg" alt="Lasanha">

    <!-- Área para detalhes -->
    <div id="detalhes-receita"></div>
  </div>

  <script>
    const API_BASE = "https://beck-end-do-site-de-receitas-vslw.vercel.app";

    async function mostrarDetalhes(id) {
      try {
        const res = await fetch(`${API_BASE}/receita/especifico/${id}`);
        if (!res.ok) throw new Error("Erro ao buscar receita");
        const receita = await res.json();

        document.getElementById("detalhes-receita").innerHTML = `
          <h2>${receita.nome_da_receita}</h2>
          <h3>Ingredientes</h3>
          <ul>${receita.ingredientes.split("\n").map(i => `<li>${i}</li>`).join("")}</ul>
          <h3>Modo de Preparo</h3>
          <p>${receita.modo_de_preparo}</p>
        `;
      } catch (err) {
        console.error(err);
        alert("Erro ao carregar detalhes da receita");
      }
    }
  </script>

</body>
</html>








<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Receitas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fffaf4;
      margin: 0;
      padding: 0;
    }

    .receitas-container {
      max-width: 800px;
      margin: auto;
      padding: 20px;
      text-align: center;
    }

    h2 {
      font-size: 28px;
      margin-bottom: 20px;
    }

    .titulo-receita {
      font-weight: bold;
      font-size: 20px;
      margin: 20px 0 10px;
      color: #ff7043;
    }

    .titulo-receita a {
      text-decoration: none;
      color: inherit;
      cursor: pointer;
    }

    .titulo-receita a:hover {
      text-decoration: underline;
    }

    .receita-foto {
      max-width: 60%;
      border-radius: 8px;
      margin-bottom: 30px;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
  </style>
</head>
<body>

  <div class="receitas-container">
    <h2>📚 Lista de Receitas</h2>
    <div id="lista-receitas"></div>
  </div>

  <script>
    const API_BASE = "https://beck-end-do-site-de-receitas-vslw.vercel.app";

    // Função para buscar todas as receitas
    async function buscarReceitas() {
      const res = await fetch(`${API_BASE}/receita/receber`);
      if (!res.ok) throw new Error("Erro ao buscar receitas");
      return await res.json();
    }

    // Função para carregar receitas na lista
    async function carregarReceitas() {
      const container = document.getElementById("lista-receitas");
      container.innerHTML = "";
      const receitas = await buscarReceitas();

      receitas.forEach(r => {
        const div = document.createElement("div");
        div.innerHTML = `
          <div class="titulo-receita">
            <a href="receita.html?id=${r.id}">
              ${r.nome_da_receita}
            </a>
          </div>
          ${r.imagem_url ? `<img class="receita-foto" src="${r.imagem_url}" alt="${r.nome_da_receita}" />` : ""}
        `;
        container.appendChild(div);
      });
    }

    // Chamada inicial para carregar lista
    carregarReceitas();
  </script>

</body>
</html>






'''