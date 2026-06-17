/**
 * diagnosis.js — 診断ロジック・結果タイプ判定
 */

/**
 * 回答配列からresultTypeを判定する
 * @param {Array<{questionId: number, value: string}>} answers
 * @returns {string} resultType key
 */
export function calcResultType(answers) {
  const values = answers.map(a => a.value);

  // Q5（転職の本気度）が最優先
  const q5 = values[4];
  if (q5 === 'urgent' || q5 === 'stuck') {
    return 'action_needed';
  }

  // Q1（現状）でフリーター・既卒は支援が必要
  const q1 = values[0];
  if (q1 === 'freeter' || q1 === 'graduate') {
    // Q5が情報収集なら info_gathering
    if (q5 === 'info') return 'info_gathering';
    return 'support_needed';
  }

  // Q5が情報収集段階
  if (q5 === 'info') return 'info_gathering';

  // Q3（壁）が「一人でやるのが不安」または Q4がエージェント未使用・怖い
  const q3 = values[2];
  const q4 = values[3];
  if (q3 === 'alone' || q4 === 'unknown' || q4 === 'scary') {
    return 'support_needed';
  }

  // Q4でエージェントを使ったことがあるが行き詰まり
  if (q4 === 'used' && q5 === 'medium') {
    return 'restart';
  }

  return 'support_needed';
}
