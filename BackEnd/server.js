const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const cors = require("cors");

const app = express();
const PORT = 3000;

// CORS para permitir requests do HTML direto
app.use(cors());

// Permitir JSON no POST
app.use(express.json());

// Conectar ao SQLite
const db = new sqlite3.Database("./banco_de_dados.db", sqlite3.OPEN_READWRITE, (err) => {
  if (err) console.error("Erro ao conectar ao banco:", err.message);
  else console.log("Conectado ao SQLite!");
});

// Rota principal
app.get("/", (req, res) => {
  res.send("Servidor rodando em http://localhost:3000 🚀");
});

// Listar todos os logins
app.get("/logins", (req, res) => {
  db.all("SELECT * FROM login_site", [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});

// Adicionar um login de teste
app.post("/logins", (req, res) => {
  const { nome, email, senha } = req.body; // agora bate com a tabela
  db.run(
    "INSERT INTO login_site (nome, email, senha) VALUES (?, ?, ?)",
    [nome, email, senha],
    function (err) {
      if (err) return res.status(500).json({ error: err.message });
      res.json({ id: this.lastID, nome, email, senha });
    }
  );
});

// Rota de login
app.post("/login", (req, res) => {
  const { email, senha } = req.body;

  const query = "SELECT * FROM login_site WHERE email = ? AND senha = ?";
  db.get(query, [email, senha], (err, row) => {
    if (err) res.status(500).json({ success: false, error: err.message });
    else if (row) res.json({ success: true, user: row.nome });
    else res.json({ success: false });
  });
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});