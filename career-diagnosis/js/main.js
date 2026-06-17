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
}

// ===========================
// Question rendering
// ===========================
function renderQuestion() {
  const q = questions[currentIndex];

  $('question-number').textContent = `Q${currentIndex + 1} / ${questions.length}`;
  $('question-text').textContent   = q.text;

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

  updateProgress();
  $('next-btn').disabled = !answers.find(a => a.questionId === q.id);
}

// ===========================
// Option selection
// ===========================
function onOptionSelect(btn, questionId) {
  document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');

  // answers 更新
  const idx = answers.findIndex(a => a.questionId === questionId);
  const entry = { questionId, value: btn.dataset.value };
  if (idx >= 0) answers[idx] = entry;
  else answers.push(entry);

  $('next-btn').disabled = false;
}

// ===========================
// Navigation
// ===========================
function goNext() {
  if (currentIndex < questions.length - 1) {
    currentIndex++;
    renderQuestion();
  } else {
    showLoading();
  }
}

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
  $('cta-btn').textContent            = result.cta;

  const adviceList = $('advice-list');
  adviceList.innerHTML = '';
  result.advice.forEach(text => {
    const li = document.createElement('li');
    li.textContent = text;
    adviceList.appendChild(li);
  });

  setupShare(result);
  showScreen('screen-result');
  updateProgress();
  $('progress-fill').style.width = '100%';
}

// ===========================
// Share
// ===========================
function setupShare(result) {
  const shareText = `【転職タイプ診断】\n「${result.title}」でした！\n\nあなたも診断してみて👇`;
  const pageUrl   = location.href;

  $('share-threads').onclick = () => {
    const url = `https://www.threads.net/intent/post?text=${encodeURIComponent(shareText + '\n' + pageUrl)}`;
    window.open(url, '_blank', 'noopener');
  };

  $('share-x').onclick = () => {
    const url = `https://x.com/intent/tweet?text=${encodeURIComponent(shareText)}&url=${encodeURIComponent(pageUrl)}`;
    window.open(url, '_blank', 'noopener');
  };
}

// ===========================
// CTA click
// ===========================
function onCtaClick() {
  // プロフィールリンクへ遷移（LINE登録先）
  // TODO: 実際のLINE URLに差し替える
  window.open('https://lin.ee/XXXXXXX', '_blank', 'noopener');
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

  $('next-btn').addEventListener('click', goNext);
  $('prev-btn').addEventListener('click', goPrev);
  $('cta-btn').addEventListener('click', onCtaClick);
  $('retry-btn').addEventListener('click', retryDiagnosis);
}

document.addEventListener('DOMContentLoaded', init);
