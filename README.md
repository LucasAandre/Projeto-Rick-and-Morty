<h1>🛸 API Rick and Morty — FastAPI, OOP e Consumo de API Externa</h1>

<p>
Este projeto é uma API construída com <strong>FastAPI</strong>, consumindo dados da 
<strong>API pública Rick and Morty</strong> e aplicando conceitos de 
<strong>Python Orientado a Objetos</strong>, <strong>parse e tratamento de JSON</strong> 
e <strong>arquitetura em camadas (Service Layer)</strong> para organização da lógica de negócio.
</p>

<ul>
  <li>✔️ Buscar personagens da API Rick and Morty</li>
  <li>✔️ Tratar e retornar apenas os dados relevantes ao usuário</li>
  <li>🔄 Estrutura modular com possibilidade de evoluções futuras</li>
</ul>

<hr/>

<h2>🚀 Tecnologias Utilizadas</h2>
<ul>
  <li>Python 3.10+</li>
  <li>FastAPI</li>
  <li>Uvicorn</li>
  <li>Requests</li>
  <li>Programação Orientada a Objetos (OOP)</li>
</ul>

<hr/>

<h2>📁 Estrutura do Projeto</h2>

<pre>
rickmorty_api/
│
├── main.py
└── services/
      └── rick_morty_api.py
</pre>

<hr/>

<h2>🔄 Endpoints da API</h2>

<h3>1️⃣ Buscar personagens</h3>
<p><strong>Método:</strong> GET</p>
<pre>/api/personagens/</pre>
<p><strong>Dados retornados (exemplo):</strong></p>
<ul>
  <li>nome</li>
  <li>status</li>
  <li>espécie</li>
  <li>imagem</li>
</ul>

<p><em>Novas rotas serão adicionadas conforme a evolução do projeto.</em></p>

<hr/>

<h2>🧠 Conceitos Aplicados</h2>
<ul>
  <li>Consumo de API externa com <code>requests</code></li>
  <li>Parse e transformação de dados JSON</li>
  <li>Lógica de negócio desacoplada usando Service Layer</li>
  <li>Boas práticas de organização de API REST</li>
  <li>Retornos estruturados em JSON</li>
</ul>

<hr/>

<h2>▶️ Como Executar o Projeto</h2>

<h3>1. Criar o ambiente virtual</h3>
<pre><code>python3 -m venv venv</code></pre>

<h3>2. Ativar o ambiente</h3>
<p><strong>Linux / Mac:</strong></p>
<pre><code>source venv/bin/activate</code></pre>
<p><strong>Windows:</strong></p>
<pre><code>venv\Scripts\activate</code></pre>

<h3>3. Instalar dependências</h3>
<pre><code>pip install fastapi uvicorn requests</code></pre>

<h3>4. Executar o servidor</h3>
<pre><code>uvicorn main:app --reload</code></pre>

<h3>5. Documentação automática</h3>
<ul>
  <li>Swagger UI: <code>http://127.0.0.1:8000/docs</code></li>
</ul>

<hr/>

<h2>📌 Próximas Funcionalidades</h2>
<ul>
  <li>Busca de personagem por ID</li>
  <li>Avaliação de episódios</li>
  <li>Integração com banco de dados</li>
  <li>Validação de localizações em comum entre personagens</li>
  <li>Autenticação de usuário</li>
</ul>

<hr/>

<h2>👨‍💻 Autor</h2>
<p>
<strong>Lucas André</strong> — Desenvolvedor Backend em formação<br/>
Apaixonado por Python, APIs, dados e construção de produtos.
</p>

