CREATE TABLE IF NOT EXISTS healthcheck (
  id SERIAL PRIMARY KEY,
  note TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
INSERT INTO healthcheck (note) VALUES ('db ok');
