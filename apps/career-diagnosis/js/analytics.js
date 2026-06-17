/**
 * analytics.js — GA4イベント計測・UTMパラメータ管理
 *
 * 計測イベント：
 *   page_view         → gtag('config') で自動送信
 *   start_diagnosis   → 診断開始ボタンクリック時
 *   complete_diagnosis → 結果画面表示時（result_type付き）
 *   cta_click         → CTAボタンクリック時（button_location付き）
 *
 * UTM保持：
 *   URLのutm_*パラメータをsessionStorageに保存し、
 *   全イベントに付与することでGA4での流入元分析を可能にする。
 *   例: ?utm_source=threads&utm_medium=profile&utm_campaign=career_diagnosis
 */

const UTM_KEYS = [
  'utm_source',
  'utm_medium',
  'utm_campaign',
  'utm_content',
  'utm_term',
];

function saveUtmParams() {
  const params = new URLSearchParams(window.location.search);
  UTM_KEYS.forEach(key => {
    const val = params.get(key);
    if (val) sessionStorage.setItem(key, val);
  });
}

function getUtmParams() {
  const result = {};
  UTM_KEYS.forEach(key => {
    const val = sessionStorage.getItem(key);
    if (val) result[key] = val;
  });
  return result;
}

export function trackEvent(eventName, extra = {}) {
  if (typeof window.gtag !== 'function') {
    console.warn('[GA4] gtag not ready, skipping:', eventName);
    return;
  }
  const isDebug = new URLSearchParams(window.location.search).get('debug_mode') === '1';
  const params = {
    ...getUtmParams(),
    ...(isDebug ? { debug_mode: true } : {}),
    ...extra,
  };
  if (isDebug) console.log('[GA4]', eventName, params);
  window.gtag('event', eventName, params);
}

export function initAnalytics() {
  saveUtmParams();
}
