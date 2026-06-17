/**
 * main.js — 画面遷移・フロー管理
 */

import { calcResultType } from './diagnosis.js';

// ===========================
// State
// ===========================
let questions = [];
let results = {};
let currentIndex = 0;
let answers = [];

// ===========================
// DOM helpers
// ===========================
const $ = id => document.getElementById(id);

function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  $(id).classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // sticky CTA は結果画面のみ
  const stickyCta = $('sticky-cta');
  if (id === 'screen-result') {
    stickyCta.classList.remove('hidden');
  } else {
    stickyCta.classList.add('hidden');
  }
}

// ===========================
// Data load
// ===========================
async function loadData() {
  const res = await fetch('./data/questions.json');
  const data = await res.json();
  questions = data.questions;
  results   = data.results;
}

// ===========================
// Progress
// ===========================
function updateProgress() {
  const total = questions.length;
  const done  = currentIndex;
  const pct   = Math.round((done / total) * 100);

  $('progress-fill').style.width = pct + '%';
  $('progress-current').textContent = done;
  $('progress-total').textContent   = total;

  // step dots
  const stepsEl = $('progress-steps');
  stepsEl.innerHTML = '';
  for (let i = 0; i < total; i++) {
    const dot = document.createElement('div');
    dot.className = 'progress-step-dot';
    if (i < done) dot.classList.add('done');
    else if (i === done) dot.classList.add('active');
    stepsEl.appendChild(dot);
  }
}

// ===========================
// Question rendering
// ===========================
function renderQuestion() {
  const q = questions[currentIndex];

  $('question-text').textContent = q.text;

  const list = $('options-list');
  list.innerHTML = '';

  q.options.forEach(opt => {
    const btn = document.createElement('button');
    btn.className   = 'option-btn';
    btn.textContent = opt.label;
    btn.dataset.value = opt.value;

    // 前回選択を復元
    const prev = answers.find(a => a.questionId === q.id);
    if (prev && prev.value === opt.value) {
      btn.classList.add('selected');
    }

    btn.addEventListener('click', () => onOptionSelect(btn, q.id));
    list.appendChild(btn);
  });

  const prevBtn = $('prev-btn');
  prevBtn.disabled = currentIndex === 0;

  updateProgress();
}

// ===========================
// Option selection → 自動遷移
// ===========================
function onOptionSelect(btn, questionId) {
  // 連打防止
  if (btn.classList.contains('selecting')) return;

  document.querySelectorAll('.option-btn').forEach(b => {
    b.classList.remove('selected');
    b.disabled = true;
  });
  btn.classList.add('selecting');

  // answers 更新
  const idx = answers.findIndex(a => a.questionId === questionId);
  const entry = { questionId, value: btn.dataset.value };
  if (idx >= 0) answers[idx] = entry;
  else answers.push(entry);

  // 300ms後に自動遷移
  setTimeout(() => {
    if (currentIndex < questions.length - 1) {
      currentIndex++;
      renderQuestion();
    } else {
      showLoading();
    }
  }, 300);
}

// ===========================
// Back navigation
// ===========================
function goPrev() {
  if (currentIndex > 0) {
    currentIndex--;
    renderQuestion();
  }
}

// ===========================
// Loading → Result
// ===========================
function showLoading() {
  showScreen('screen-loading');
  setTimeout(showResult, 1800);
}

function showResult() {
  const typeKey = calcResultType(answers);
  const result  = results[typeKey];

  $('result-emoji').textContent       = result.emoji;
  $('result-title').textContent       = result.title;
  $('result-description').textContent = result.description;

  const ctaBtnText = $('cta-btn-text');
  if (ctaBtnText) ctaBtnText.textContent = '無料サポートを受け取る';

  const adviceList = $('advice-list');
  adviceList.innerHTML = '';
  result.advice.forEach(text => {
    const li = document.createElement('li');
    li.textContent = text;
    adviceList.appendChild(li);
  });

  setupCtaButtons();
  showScreen('screen-result');

  // progress 100%
  $('progress-fill').style.width = '100%';
}

// ===========================
// CTA
// ===========================
function setupCtaButtons() {
  const lineUrl = 'https://lin.ee/WqfZFyd';

  $('cta-btn').onclick = () => window.open(lineUrl, '_blank', 'noopener');
  $('sticky-cta-btn').onclick = () => window.open(lineUrl, '_blank', 'noopener');
}

// ===========================
// Retry
// ===========================
function retryDiagnosis() {
  currentIndex = 0;
  answers      = [];
  showScreen('screen-question');
  renderQuestion();
}

// ===========================
// Init
// ===========================
async function init() {
  await loadData();

  $('start-btn').addEventListener('click', () => {
    showScreen('screen-question');
    renderQuestion();
  });

  $('prev-btn').addEventListener('click', goPrev);
  $('retry-btn').addEventListener('click', retryDiagnosis);
}

document.addEventListener('DOMContentLoaded', init);
