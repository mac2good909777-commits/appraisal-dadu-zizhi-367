# -*- coding: utf-8 -*-
"""屋主簡要版 — 大字、少字、手機優先。"""
from _assets import LOGO

CSS = """
:root{--g:#4B872F;--f:#2B5937;--gold:#C0A434;--cream:#F5F3EE;--tx:#2B2B2B;--lt:#6B6B6B;--bd:#DDD9D2;}
*{box-sizing:border-box;-webkit-text-size-adjust:100%}
body{margin:0;background:#F2F0EB;color:var(--tx);
 font-family:"Noto Sans TC","Microsoft JhengHei",sans-serif;
 font-size:19px;line-height:1.95;letter-spacing:.3px}
.wrap{max-width:680px;margin:0 auto;background:#fff}
header{background:var(--f);padding:26px 22px;text-align:center;border-bottom:4px solid var(--gold)}
header img{width:108px;background:#fff;border-radius:6px;padding:9px;display:block;margin:0 auto 14px}
header h1{color:#fff;font-size:26px;font-weight:700;margin:0 0 8px;letter-spacing:1px}
header p{color:#C9D6C9;font-size:16px;margin:0;line-height:1.7}
main{padding:22px 20px 40px}
.sec{margin:0 0 26px}
.sec-t{font-size:21px;font-weight:700;color:var(--f);margin:0 0 12px;
 padding-left:13px;border-left:6px solid var(--g);line-height:1.5}
.box{border:2px solid var(--bd);border-radius:8px;padding:18px 18px 14px;background:#fff}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:12px;
 padding:11px 0;border-bottom:1px solid #EEE}
.row:last-child{border-bottom:0}
.row .k{color:var(--lt);font-size:17px;flex-shrink:0}
.row .v{font-weight:700;font-size:19px;text-align:right}
.price{background:var(--cream);border:2px solid var(--gold);border-radius:8px;
 padding:20px 18px;text-align:center;margin:0 0 14px}
.price .lb{font-size:17px;color:var(--lt);margin-bottom:6px}
.price .big{font-size:42px;font-weight:700;color:var(--f);line-height:1.25;letter-spacing:-.5px}
.price .unit{font-size:20px;font-weight:500}
.price .sub{font-size:16px;color:var(--lt);margin-top:6px}
.price.main{background:var(--f);border-color:var(--f)}
.price.main .lb{color:#B9CDB9}
.price.main .big{color:#fff}
.price.main .sub{color:#C9D6C9}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.note-box{background:#FBF4E6;border-left:6px solid var(--gold);border-radius:0 6px 6px 0;
 padding:16px 18px;margin:14px 0;font-size:18px;line-height:1.85}
.note-box b{color:var(--f)}
.warn-box{background:#FCEFEC;border-left:6px solid #C0533A}
.ok-box{background:#EDF3E8;border-left:6px solid var(--g)}
.num{display:inline-flex;align-items:center;justify-content:center;
 width:30px;height:30px;border-radius:50%;background:var(--g);color:#fff;
 font-size:17px;font-weight:700;margin-right:9px;flex-shrink:0}
.step{display:flex;align-items:flex-start;gap:4px;padding:13px 0;border-bottom:1px solid #EEE}
.step:last-child{border-bottom:0}
.step-c{flex:1}
.step-t{font-weight:700;color:var(--f);font-size:19px;margin-bottom:3px}
.step-d{font-size:17px;color:var(--lt);line-height:1.75}
footer{background:var(--f);color:#fff;padding:24px 20px;text-align:center;font-size:17px;line-height:2}
footer .nm{font-size:21px;font-weight:700;margin-bottom:4px}
footer .cm{color:#B9CDB9;font-size:15px;margin-top:10px;line-height:1.7}
.more{display:block;text-align:center;background:var(--cream);border:2px dashed var(--bd);
 border-radius:8px;padding:16px;margin:26px 0 0;color:var(--f);
 text-decoration:none;font-size:17px;font-weight:700}
@media(max-width:420px){
 body{font-size:18px}
 main{padding:18px 15px 32px}
 .price .big{font-size:36px}
 .two{grid-template-columns:1fr;gap:10px}
 .row{flex-direction:column;align-items:flex-start;gap:2px}
 .row .v{text-align:left}
 header h1{font-size:23px}
}
@media print{body{background:#fff}header,footer{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""

HTML = """<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<!-- Google tag (gtag.js) — GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H5VLHW8761"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-H5VLHW8761');
</script>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>土地價值評估摘要</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>
<div class="wrap">

<header>
<img src="data:image/png;base64,__LOGO__" alt="瑞禾開發">
<h1>您的土地價值評估</h1>
<p>臺中市大肚區 自治段<br>367・368・369 地號</p>
</header>

<main>

<div class="sec">
<div class="sec-t">一、土地基本資料</div>
<div class="box">
<div class="row"><span class="k">位置</span><span class="v">大肚區 福利路 117 巷</span></div>
<div class="row"><span class="k">面積</span><span class="v">123.5 坪（三筆合計）</span></div>
<div class="row"><span class="k">用途</span><span class="v">住宅區・可建築</span></div>
<div class="row"><span class="k">現況</span><span class="v">空地，無建物</span></div>
<div class="row"><span class="k">可蓋</span><span class="v">約 4 戶透天</span></div>
</div>
</div>

<div class="sec">
<div class="sec-t">二、建議價格</div>

<div class="price main">
<div class="lb">建議開價</div>
<div class="big">3,950<span class="unit"> 萬</span></div>
<div class="sub">每坪 32 萬</div>
</div>

<div class="price">
<div class="lb">合理成交範圍</div>
<div class="big" style="font-size:34px">3,100 – 3,580<span class="unit"> 萬</span></div>
<div class="sub">每坪 25 – 29 萬</div>
</div>

<div class="box">
<div class="row"><span class="k">最低底線</span><span class="v">2,720 萬（每坪 22 萬）</span></div>
</div>

<div class="note-box ok-box">
<b>為什麼是這個價格？</b><br>
隔壁 48 公尺的土地，兩年前成交每坪 30.9 萬；<br>
走路 2 分鐘的土地，成交每坪 28 萬。<br>
您這塊因為門前巷子較窄，價格會略低一些。
</div>
</div>

<div class="sec">
<div class="sec-t">三、稅金與實拿金額</div>
<div class="box">
<div class="row"><span class="k">土地增值稅</span><span class="v">約 153 萬</span></div>
<div class="row"><span class="k">若賣 3,300 萬</span><span class="v">實拿約 3,150 萬</span></div>
<div class="row"><span class="k">若賣 3,580 萬</span><span class="v">實拿約 3,430 萬</span></div>
</div>
<div class="note-box">
稅金已用<b>財政部官方網站試算確認</b>，金額正確。<br>
土地持有 47 年，可減稅 40%，所以稅金不算重。<br>
<span style="font-size:16px;color:#6B6B6B">※ 上表尚未扣除仲介服務費與代書費。</span>
</div>
</div>

<div class="sec">
<div class="sec-t">四、兩件要注意的事</div>

<div class="note-box warn-box">
<b>第一件：土地是兩個人的名字</b><br>
367、368 是一位的，369 是另一位的。<br>
<b>要賣，兩位都要同意、都要簽名。</b>
</div>

<div class="note-box warn-box">
<b>第二件：門前巷子是別人的地</b><br>
那條巷子登記在別人名下，您沒有持分。<br>
不過巷子已經用了四十多年，兩邊房子都合法蓋好了，
<b>通行應該沒問題</b>，但建議先去市政府確認。
</div>
</div>

<div class="sec">
<div class="sec-t">五、建議的三個步驟</div>
<div class="box">

<div class="step"><span class="num">1</span><div class="step-c">
<div class="step-t">先去市政府問建築線</div>
<div class="step-d">確認這塊地可以蓋房子、需不需要退縮。<br>規費只要 500 元，這步最重要。</div>
</div></div>

<div class="step"><span class="num">2</span><div class="step-c">
<div class="step-t">把地整理乾淨</div>
<div class="step-d">現在雜草和樹比較多。<br>花 3 到 5 萬整理，買方看了會願意出更好的價格。</div>
</div></div>

<div class="step"><span class="num">3</span><div class="step-c">
<div class="step-t">開價 3,950 萬開始談</div>
<div class="step-d">預留議價空間，<br>心裡守住 3,100 萬即可成交。</div>
</div></div>

</div>
</div>

<a class="more" href="./explain.html">想知道價格是怎麼算出來的？<br>點這裡看完整說明 →</a>
<a class="more" href="./index.html" style="margin-top:12px">想看所有資料來源與分析？<br>點這裡看完整報告 →</a>

</main>

<footer>
<div class="nm">張現傑</div>
<div>瑞禾開發｜建築、房產整合團隊</div>
<div class="cm">
本摘要為行情研判與委託前參考，<br>
非不動產估價師之正式估價報告書。<br>
製表日期：2026.09.23
</div>
</footer>

</div>
</body></html>"""

html = HTML.replace("__CSS__", CSS).replace("__LOGO__", LOGO)
with open('owner.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('done', len(html))
