const canvas = document.getElementById('fundo-estrelas');
const ctx = canvas.getContext('2d');
let width = window.innerWidth;
let height = window.innerHeight;
canvas.width = width;
canvas.height = height;

const estrelas = [];
const numEstrelas = 100;

for (let i = 0; i < numEstrelas; i++) {
  estrelas.push({
    x: Math.random() * width,
    y: Math.random() * height,
    raio: Math.random() * 1.5 + 0.5,
    dx: (Math.random() - 0.5) * 0.5,
    dy: (Math.random() - 0.5) * 0.5
  });
}

let mouse = { x: width / 2, y: height / 2 };

window.addEventListener('mousemove', function(e) {
  mouse.x = e.clientX;
  mouse.y = e.clientY;
});

function desenharEstrelas() {
  ctx.clearRect(0, 0, width, height);
  for (let estrela of estrelas) {
    ctx.beginPath();
    ctx.arc(estrela.x, estrela.y, estrela.raio, 0, Math.PI * 2);
    ctx.fillStyle = "#fff";
    ctx.shadowColor = "#fff";
    ctx.shadowBlur = 8;
    ctx.fill();
    ctx.closePath();

    // Movimento suave em direção ao mouse
    estrela.x += estrela.dx + (mouse.x - estrela.x) * 0.0005;
    estrela.y += estrela.dy + (mouse.y - estrela.y) * 0.0005;

    // Reposiciona se sair da tela
    if (estrela.x < 0 || estrela.x > width) estrela.x = Math.random() * width;
    if (estrela.y < 0 || estrela.y > height) estrela.y = Math.random() * height;
  }
  requestAnimationFrame(desenharEstrelas);
}

window.addEventListener('resize', () => {
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.width = width;
  canvas.height = height;
});

desenharEstrelas();