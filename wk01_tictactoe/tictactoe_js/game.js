"use strict";

/* ============================================================
 * CONFIG — edit these if something doesn't line up
 * ============================================================ */

// The one line to change if the assets folder path is wrong:
const SPRITE_DIR = "../assets/sprites/";

const SPRITE_FILES = {
  X: "X_spritesheet.png",
  O: "O_spritesheet.png",
};

// Spritesheet layout (sheet is 1536x512). Frame size is computed from the
// loaded image: frameWidth = imageWidth / SHEET_COLUMNS, etc.
// Default assumes square 512x512 frames -> 3 frames in one row.
const SHEET_COLUMNS = 3;
const SHEET_ROWS = 1;
const TOTAL_FRAMES = SHEET_COLUMNS * SHEET_ROWS; // lower this if the last cells are empty

const ANIMATION_FPS = 6;       // 3 frames at 6 fps = one cycle every 0.5s
const ANIMATION_LOOPS = true;  // true = loop forever, false = play once and hold the last frame

// Look & feel
const MAX_BOARD_SIZE = 560;     // CSS pixels
const GRID_COLOR = "#222222";
const GRID_LINE_WIDTH = 6;      // CSS pixels
const HOVER_COLOR = "rgba(0, 0, 0, 0.06)";
const WIN_LINE_COLOR = "#d9382b";
const WIN_LINE_WIDTH = 8;
const SPRITE_PADDING = 0.12;    // fraction of a cell left empty around each mark

/* ============================================================
 * State
 * ============================================================ */

const WIN_LINES = [
  [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
  [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
  [0, 4, 8], [2, 4, 6],            // diagonals
];

const canvas = document.getElementById("board");
const ctx = canvas.getContext("2d");
const statusEl = document.getElementById("status");
const restartBtn = document.getElementById("restart");

const sprites = { X: null, O: null };

let board;         // array of 9: null | { mark: "X"|"O", placedAt: ms }
let currentPlayer; // "X" | "O"
let winner;        // null | "X" | "O"
let winLine;       // null | [a, b, c]
let isDraw;
let hoverCell;     // -1 or 0..8
let boardSize = 0; // CSS pixels

/* ============================================================
 * Setup
 * ============================================================ */

function newGame() {
  board = new Array(9).fill(null);
  currentPlayer = "X"; // X always goes first
  winner = null;
  winLine = null;
  isDraw = false;
  hoverCell = -1;
  updateStatus();
}

function updateStatus() {
  if (winner) statusEl.textContent = `${winner} wins!`;
  else if (isDraw) statusEl.textContent = "It's a draw.";
  else statusEl.textContent = `${currentPlayer}'s turn`;
}

function loadImage(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => reject(new Error(`Could not load ${src}`));
    img.src = src;
  });
}

async function loadSprites() {
  const [x, o] = await Promise.all([
    loadImage(SPRITE_DIR + SPRITE_FILES.X),
    loadImage(SPRITE_DIR + SPRITE_FILES.O),
  ]);
  sprites.X = x;
  sprites.O = o;
}

function resizeCanvas() {
  const available = Math.min(window.innerWidth - 32, window.innerHeight - 160);
  boardSize = Math.max(200, Math.min(MAX_BOARD_SIZE, available));
  const dpr = window.devicePixelRatio || 1;
  canvas.style.width = boardSize + "px";
  canvas.style.height = boardSize + "px";
  canvas.width = Math.round(boardSize * dpr);
  canvas.height = Math.round(boardSize * dpr);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}

/* ============================================================
 * Game logic
 * ============================================================ */

function checkResult() {
  for (const line of WIN_LINES) {
    const [a, b, c] = line;
    if (board[a] && board[b] && board[c] &&
        board[a].mark === board[b].mark && board[a].mark === board[c].mark) {
      winner = board[a].mark;
      winLine = line;
      return;
    }
  }
  if (board.every(cell => cell !== null)) isDraw = true;
}

function gameOver() {
  return winner !== null || isDraw;
}

function playCell(index) {
  if (gameOver() || board[index]) return;
  board[index] = { mark: currentPlayer, placedAt: performance.now() };
  checkResult();
  if (!gameOver()) currentPlayer = currentPlayer === "X" ? "O" : "X";
  updateStatus();
}

/* ============================================================
 * Input
 * ============================================================ */

function cellFromEvent(e) {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  if (x < 0 || y < 0 || x >= rect.width || y >= rect.height) return -1;
  const cellSize = rect.width / 3;
  return Math.floor(y / cellSize) * 3 + Math.floor(x / cellSize);
}

canvas.addEventListener("pointerdown", e => {
  const i = cellFromEvent(e);
  if (i >= 0) playCell(i);
});

canvas.addEventListener("pointermove", e => {
  hoverCell = cellFromEvent(e);
});

canvas.addEventListener("pointerleave", () => {
  hoverCell = -1;
});

restartBtn.addEventListener("click", newGame);
window.addEventListener("resize", resizeCanvas);

/* ============================================================
 * Rendering
 * ============================================================ */

function drawGrid() {
  const cell = boardSize / 3;
  ctx.strokeStyle = GRID_COLOR;
  ctx.lineWidth = GRID_LINE_WIDTH;
  ctx.lineCap = "round";
  const inset = GRID_LINE_WIDTH / 2;
  ctx.beginPath();
  for (let i = 1; i < 3; i++) {
    ctx.moveTo(i * cell, inset);
    ctx.lineTo(i * cell, boardSize - inset);
    ctx.moveTo(inset, i * cell);
    ctx.lineTo(boardSize - inset, i * cell);
  }
  ctx.stroke();
}

function drawHover() {
  if (hoverCell < 0 || board[hoverCell] || gameOver()) return;
  const cell = boardSize / 3;
  const col = hoverCell % 3;
  const row = Math.floor(hoverCell / 3);
  ctx.fillStyle = HOVER_COLOR;
  ctx.fillRect(col * cell, row * cell, cell, cell);
}

function currentFrame(placedAt, now) {
  const elapsed = Math.max(0, now - placedAt);
  const raw = Math.floor((elapsed / 1000) * ANIMATION_FPS);
  return ANIMATION_LOOPS ? raw % TOTAL_FRAMES : Math.min(raw, TOTAL_FRAMES - 1);
}

function drawMark(index, entry, now) {
  const img = sprites[entry.mark];
  const frameW = img.naturalWidth / SHEET_COLUMNS;
  const frameH = img.naturalHeight / SHEET_ROWS;
  const frame = currentFrame(entry.placedAt, now);
  const sx = (frame % SHEET_COLUMNS) * frameW;
  const sy = Math.floor(frame / SHEET_COLUMNS) * frameH;

  const cell = boardSize / 3;
  const pad = cell * SPRITE_PADDING;
  const size = cell - pad * 2;
  const dx = (index % 3) * cell + pad;
  const dy = Math.floor(index / 3) * cell + pad;
  ctx.drawImage(img, sx, sy, frameW, frameH, dx, dy, size, size);
}

function drawWinLine() {
  if (!winLine) return;
  const cell = boardSize / 3;
  const center = i => ({
    x: (i % 3) * cell + cell / 2,
    y: Math.floor(i / 3) * cell + cell / 2,
  });
  const a = center(winLine[0]);
  const c = center(winLine[2]);
  // Extend slightly past the end cells' centers
  const dx = c.x - a.x, dy = c.y - a.y;
  const len = Math.hypot(dx, dy);
  const ext = cell * 0.3;
  const ux = dx / len, uy = dy / len;
  ctx.strokeStyle = WIN_LINE_COLOR;
  ctx.lineWidth = WIN_LINE_WIDTH;
  ctx.lineCap = "round";
  ctx.beginPath();
  ctx.moveTo(a.x - ux * ext, a.y - uy * ext);
  ctx.lineTo(c.x + ux * ext, c.y + uy * ext);
  ctx.stroke();
}

function render(now) {
  ctx.clearRect(0, 0, boardSize, boardSize);
  drawHover();
  drawGrid();
  board.forEach((entry, i) => { if (entry) drawMark(i, entry, now); });
  drawWinLine();
  requestAnimationFrame(render);
}

/* ============================================================
 * Start
 * ============================================================ */

async function init() {
  resizeCanvas();
  newGame();
  statusEl.textContent = "Loading…";
  try {
    await loadSprites();
  } catch (err) {
    statusEl.textContent =
      `Couldn't load sprites from "${SPRITE_DIR}". Check SPRITE_DIR at the top of game.js.`;
    console.error(err);
    return;
  }
  updateStatus();
  requestAnimationFrame(render);
}

init();
