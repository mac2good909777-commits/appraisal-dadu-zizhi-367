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

.ptab{margin:22px 0;border:2px solid var(--bd);border-radius:7px;overflow:hidden}
.ptab table{width:100%;border-collapse:collapse;font-family:"Noto Sans TC",sans-serif}
.ptab th{background:var(--f);color:#fff;font-size:15px;font-weight:500;padding:11px 10px;text-align:center}
.ptab td{padding:12px 10px;text-align:center;border-bottom:1px solid #EEE;font-size:17px;line-height:1.5}
.ptab tr:last-child td{border-bottom:0}
.ptab tr.in{background:#EDF3E8}
.ptab tr.in td{font-weight:500}
.ptab tr.ask{background:var(--f)}
.ptab tr.ask td,.ptab tr.ask b{color:#fff}
.ptab small{display:block;font-size:12.5px;color:var(--lt);font-weight:400;margin-top:1px}
.ptab tr.ask small{color:#B9CDB9}
.ptab b{color:var(--f);font-weight:700}
.ptab-n{font-size:16.5px;background:#FBF4E6;border:2px solid var(--gold);border-radius:7px;padding:15px 17px;margin:16px 0 24px;color:var(--tx);line-height:1.85;font-family:"Noto Sans TC",sans-serif}
.ptab-n b{color:#9A6B00}
.ptab-n .t{display:block;font-weight:700;color:var(--f);margin-bottom:4px;font-size:16px}
@media(max-width:420px){.ptab td{font-size:15.5px;padding:10px 5px}.ptab th{font-size:13.5px;padding:9px 5px}}
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
  // 自家裝置標記：任一頁加 ?ga=off 造訪一次，之後該瀏覽器的流量都標成 internal，
  // 由 GA 的「內部流量」資料篩選器排除；?ga=on 解除。
  (function(){
    var K='ga_internal', q=location.search, internal=false;
    try{
      if(q.indexOf('ga=off')>-1){ localStorage.setItem(K,'1'); }
      if(q.indexOf('ga=on')>-1){ localStorage.removeItem(K); }
      internal = localStorage.getItem(K)==='1';
    }catch(e){}
    gtag('config','G-H5VLHW8761', internal ? {traffic_type:'internal'} : {});
  })();
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

<div class="ptab-title" style="font-size:17px;color:#6B6B6B;margin:18px 0 8px">每坪單價 → 總價 → 實拿</div>
<div class="ptab"><table><thead><tr><th>每坪</th><th>總價</th><th>實拿</th></tr></thead><tbody><tr><td><b>22 萬</b></td><td>2,717 萬</td><td><b>2,564 萬</b></td></tr><tr class="in"><td><b>25 萬</b></td><td>3,088 萬</td><td><b>2,935 萬</b></td></tr><tr class="in"><td><b>26 萬</b></td><td>3,211 萬</td><td><b>3,058 萬</b></td></tr><tr class="in"><td><b>27 萬</b></td><td>3,335 萬</td><td><b>3,182 萬</b></td></tr><tr class="in"><td><b>28 萬</b></td><td>3,458 萬</td><td><b>3,305 萬</b></td></tr><tr class="in"><td><b>29 萬</b></td><td>3,582 萬</td><td><b>3,429 萬</b></td></tr><tr><td><b>30 萬</b></td><td>3,705 萬</td><td><b>3,552 萬</b></td></tr><tr class="ask"><td><b>32 萬</b></td><td>3,952 萬</td><td><b>3,799 萬</b></td></tr></tbody></table></div><p class="ptab-n"><span class="t">「實拿」是扣稅後、扣服務費前的金額</span>綠色為合理範圍。<br>實拿<b>已扣土地增值稅 153 萬</b>，<br>但<b>尚未扣仲介服務費與代書費</b>。</p>

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
土地持有 47 年，依法減徵 40%。<br>
<span style="font-size:16px;color:#6B6B6B">※ 上表尚未扣除仲介服務費與代書費。</span>
</div>
</div>

<div class="sec">
<div class="sec-t">四、要注意的一件事</div>

<div class="note-box warn-box">
<b>門前巷子是別人的地</b><br>
那條巷子登記在別人名下，您沒有持分。<br>
巷子已開闢四十多年，兩側房屋都是合法建築。<br>
<b>建議先向市政府申請指定建築線確認。</b>
</div>
</div>

<div class="sec">
<div class="sec-t">五、建議做法</div>
<div class="box">

<div class="step"><span class="num">✓</span><div class="step-c">
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
