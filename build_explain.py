# -*- coding: utf-8 -*-
"""地主說明版 — 文章口吻，明確給結論，過程點到為止。"""
from _assets import LOGO

GA = """<!-- Google tag (gtag.js) — GA4 -->
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
</script>"""

CSS = """
:root{--g:#4B872F;--f:#2B5937;--gold:#C0A434;--cream:#F5F3EE;--tx:#2E2E2E;--lt:#6E6E6E;--bd:#E2DED7;}
*{box-sizing:border-box;-webkit-text-size-adjust:100%}
body{margin:0;background:#EFEDE8;color:var(--tx);
 font-family:"Noto Serif TC","Noto Sans TC","Microsoft JhengHei",serif;
 font-size:18px;line-height:2.0;letter-spacing:.4px}
.wrap{max-width:720px;margin:0 auto;background:#fff}
header{background:var(--f);padding:34px 30px 28px;border-bottom:4px solid var(--gold)}
header img{width:96px;background:#fff;border-radius:5px;padding:8px;display:block;margin-bottom:18px}
header h1{color:#fff;font-size:25px;font-weight:700;margin:0 0 10px;line-height:1.6;letter-spacing:1px}
header .sub{color:#C2D2C2;font-size:15.5px;line-height:1.8;font-family:"Noto Sans TC",sans-serif}
main{padding:32px 30px 44px}
p{margin:0 0 20px;text-align:justify}
h2{font-size:20px;font-weight:700;color:var(--f);margin:38px 0 16px;line-height:1.6;
 padding-bottom:9px;border-bottom:2px solid var(--bd)}
h2:first-child{margin-top:0}
b{color:var(--f);font-weight:700}
.lead{font-size:19px;background:var(--cream);border-left:5px solid var(--gold);
 padding:20px 22px;margin:0 0 26px;line-height:1.95}
.lead p:last-child{margin-bottom:0}
.fig{border:2px solid var(--f);border-radius:6px;margin:24px 0;overflow:hidden}
.fig-h{background:var(--f);color:#fff;font-size:15px;padding:9px 18px;
 font-family:"Noto Sans TC",sans-serif;letter-spacing:.5px}
.fig-b{padding:20px 22px;text-align:center}
.fig-b .n{font-size:38px;font-weight:700;color:var(--f);line-height:1.3;
 font-family:"Noto Sans TC",sans-serif;letter-spacing:-.5px}
.fig-b .u{font-size:19px}
.fig-b .d{font-size:15.5px;color:var(--lt);margin-top:5px;font-family:"Noto Sans TC",sans-serif}
.grid{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--bd)}
.grid > div{padding:16px 18px;text-align:center;border-right:1px solid var(--bd)}
.grid > div:last-child{border-right:0}
.grid .n{font-size:24px;font-weight:700;color:var(--f);font-family:"Noto Sans TC",sans-serif}
.grid .d{font-size:14.5px;color:var(--lt);font-family:"Noto Sans TC",sans-serif;margin-top:3px}

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
.data{font-family:"Noto Sans TC",sans-serif;font-size:16px;background:#FAFAF8;
 border:1px solid var(--bd);border-radius:5px;padding:4px 18px;margin:22px 0}
.data .r{display:flex;justify-content:space-between;gap:14px;padding:12px 0;
 border-bottom:1px solid #EDEAE4;line-height:1.7}
.data .r:last-child{border-bottom:0}
.data .k{color:var(--lt);flex-shrink:0}
.data .v{font-weight:700;text-align:right;color:var(--tx)}
.mark{background:#FBF4E6;border-left:5px solid var(--gold);padding:18px 20px;margin:22px 0;
 font-size:17px;line-height:1.95}
.mark.w{background:#FCEFEC;border-left-color:#C0533A}
.mark p:last-child{margin-bottom:0}
.sign{margin-top:44px;padding-top:24px;border-top:2px solid var(--bd);
 font-family:"Noto Sans TC",sans-serif}
.sign .nm{font-size:21px;font-weight:700;color:var(--f);margin-bottom:2px}
.sign .ti{font-size:15px;color:var(--lt);line-height:1.8}
.links{display:grid;grid-template-columns:1fr;gap:12px;margin:30px 0 0}
.links a{display:block;text-align:center;background:var(--cream);border:1px solid var(--bd);
 border-radius:6px;padding:15px 12px;color:var(--f);text-decoration:none;
 font-size:15.5px;font-weight:700;line-height:1.6;font-family:"Noto Sans TC",sans-serif}
.links a span{display:block;font-size:13.5px;color:var(--lt);font-weight:400;margin-top:3px}
footer{background:var(--f);color:#B9CDB9;padding:22px 30px;font-size:14px;line-height:1.9;
 font-family:"Noto Sans TC",sans-serif}
@media(max-width:600px){
 body{font-size:17px;line-height:1.95}
 main{padding:24px 18px 34px}
 header{padding:26px 18px 22px}
 header h1{font-size:21px}
 h2{font-size:18.5px;margin:32px 0 14px}
 .lead{font-size:17.5px;padding:17px 18px}
 .fig-b .n{font-size:32px}
 .grid{grid-template-columns:1fr}
 .grid > div{border-right:0;border-bottom:1px solid var(--bd)}
 .grid > div:last-child{border-bottom:0}
 .data .r{flex-direction:column;gap:1px}
 .data .v{text-align:left}
 .links{grid-template-columns:1fr}
}
@media print{body{background:#fff}header,footer{-webkit-print-color-adjust:exact;print-color-adjust:exact}.links{display:none}}
"""

HTML = """<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="UTF-8">
__GA__
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>土地價格評估說明</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>
<div class="wrap">

<header>
<img src="data:image/png;base64,__LOGO__" alt="瑞禾開發">
<h1>關於您三筆土地的<br>價格評估說明</h1>
<div class="sub">臺中市大肚區自治段 367・368・369 地號｜合計 123.5 坪<br>
瑞禾開發　張現傑　2026 年 9 月 23 日</div>
</header>

<main>

<div class="lead">
<p>我們針對您這三筆土地做完了完整的行情查證，<b>結論是：合理的成交價格落在每坪 25 萬到 29 萬之間，總價約 3,100 萬到 3,580 萬。</b>建議以 3,950 萬開價，保留議價空間。</p>
<p>過程中有一件會影響交易的事，寫在後面，請您先過目。</p>
</div>

<div class="fig">
<div class="fig-h">建議開價</div>
<div class="fig-b">
<div class="n">3,950<span class="u"> 萬</span></div>
<div class="d">每坪 32 萬・預留議價空間</div>
</div>
<div class="grid">
<div><div class="n">3,100 – 3,580 萬</div><div class="d">合理成交範圍（每坪 25–29 萬）</div></div>
<div><div class="n">2,720 萬</div><div class="d">建議底線（每坪 22 萬）</div></div>
</div>
</div>

<h2>單價與總價對照</h2>
<p>以土地 123.5 坪計算，每坪單價對應的總價與扣除土地增值稅後的實拿金額如下。綠色為建議的合理成交範圍。</p>
<div class="ptab"><table><thead><tr><th>每坪</th><th>總價</th><th>扣稅後實拿</th></tr></thead><tbody><tr><td><b>22 萬</b><small>底線</small></td><td>2,717 萬</td><td><b>2,564 萬</b></td></tr><tr class="in"><td><b>25 萬</b></td><td>3,088 萬</td><td><b>2,935 萬</b></td></tr><tr class="in"><td><b>26 萬</b></td><td>3,211 萬</td><td><b>3,058 萬</b></td></tr><tr class="in"><td><b>27 萬</b></td><td>3,335 萬</td><td><b>3,182 萬</b></td></tr><tr class="in"><td><b>28 萬</b></td><td>3,458 萬</td><td><b>3,305 萬</b></td></tr><tr class="in"><td><b>29 萬</b></td><td>3,582 萬</td><td><b>3,429 萬</b></td></tr><tr><td><b>30 萬</b></td><td>3,705 萬</td><td><b>3,552 萬</b></td></tr><tr class="ask"><td><b>32 萬</b><small>開價</small></td><td>3,952 萬</td><td><b>3,799 萬</b></td></tr></tbody></table></div><p class="ptab-n"><span class="t">請留意「實拿」這一欄的計算範圍</span>綠色為建議的合理成交範圍。「實拿」<b>已扣除土地增值稅 152.9 萬</b>，但<b>尚未扣除仲介服務費與代書費用</b>，這兩項需自實拿金額再行扣除。</p>

<h2>這個價格是怎麼得出來的</h2>

<p>最有參考價值的，是離您這塊地<b>只有 48 公尺</b>的自治段 376 地號。那筆 238 坪，民國 113 年 7 月成交，換算每坪 30.92 萬。另一筆在 181 公尺外的福利段 316 地號，34 坪，同年 8 月成交，每坪 28.05 萬。</p>

<p>我們也用另外兩種方式交叉驗算過。一種是拿福利路巷內幾棟民國 103 年蓋的透天成交價，扣掉房屋本身的價值後回推地價，三筆算出來分別是 33.3、33.5、36.8 萬，那是「已經蓋好房子、單戶三十坪」的水準；整批素地要打折，換算下來約 25 到 29 萬。另一種是站在建商的角度算：這塊地蓋四戶透天能賣多少、扣掉營造成本和利潤後還剩多少買地，答案是每坪 26 萬左右。</p>

<p><b>三種算法都指向同一個區間，所以 25 到 29 萬這個數字是踏實的。</b></p>

<h2>為什麼不能直接用隔壁 376 的價格</h2>

<p>我知道 376 那筆就在旁邊、又是同一段，數字看起來最有說服力。但兩塊地有三個地方不一樣，直接套用會讓案子賣不掉。</p>

<p><b>第一是路。</b>376 臨的是有路權的計畫道路，您這塊臨的是福利路 117 巷 —— 那條巷子寬度只有 5.18 公尺，而且登記在別人名下。買方一定會拿這點議價。</p>

<p><b>第二是時間。</b>376 成交在 113 年 7 月，距離現在兩年兩個月。這兩年土地融資和建商的購地貸款明顯收緊，出價比當時保守。</p>

<p><b>第三是規模。</b>376 總價 7,359 萬，您這塊約 3,300 萬。這點其實對您有利 —— 門檻低了一半以上，買方從建商擴大到想自己蓋房子的家庭，客層寬得多。</p>

<p>綜合起來，您這塊地<b>撐得住 25 到 29 萬，但撐不到 30.92 萬</b>。開價 3,950 萬會讓您在心理上「只比 376 低一點」，實際成交落在合理區間。</p>

<h2>關於門前那條巷子</h2>

<div class="mark w">
<p><b>那條巷子是別人的土地，您沒有持分。</b></p>
<p>福利路 117 巷的路身是自治段 375 地號，有六位共有人，經過比對，<b>三筆土地的所有權人都不在其中</b>。</p>
</div>

<h2>稅金與您實際拿到的錢</h2>

<p>三筆土地民國 68 年取得，持有將近 47 年，依法可以減徵 40%。土地增值稅合計約 <b>153 萬</b>，大約是成交總價的 4.5%。這個數字我們用財政部官方網站的試算工具核對過，與謄本估算完全相同。</p>

<div class="data">
<div class="r"><span class="k">土地增值稅合計</span><span class="v">約 153 萬</span></div>
<div class="r"><span class="k">兩位分攤</span><span class="v">367＋368 約 100 萬<br>369 約 53 萬</span></div>
<div class="r"><span class="k">各價位實拿金額</span><span class="v">請見前方「單價與總價對照」</span></div>
</div>

<p style="font-size:16px;color:#6E6E6E">上表尚未扣除仲介服務費與代書費用。另外提醒一點：這三筆是素地、地上沒有房屋，<b>不符合自用住宅優惠稅率的條件</b>，所以是按一般稅率計算。另外，您名下「一生一次」的自用住宅優惠資格<b>不會因為這次交易被用掉</b>，將來出售自住房屋時仍然保留。</p>

<h2>我們建議的做法</h2>

<p><b>建議以 3,950 萬開價。</b>這塊地最值錢的地方，是<b>面寬 34 公尺整排臨路、深度 11.9 公尺</b>，可以直接切成四戶透天，每戶都有自己的出入口，不用留內部通道，土地一坪都不浪費。同樣 123 坪的地，如果是窄長型，只能蓋兩戶還得挪出走道。這是我們對外主推的重點。</p>

<p>預估四到八個月可以成交。如果買方是自住自建、付款條件乾脆，<b>3,300 萬以上我們就建議您考慮</b>。</p>

<div class="sign">
<div class="nm">張現傑</div>
<div class="ti">瑞禾開發｜建築、房產整合團隊<br>
如對本評估內容有任何疑問，歡迎隨時與我聯絡。</div>
</div>

<div class="links">
<a href="./index.html">完整分析報告<span>含所有資料來源</span></a>
</div>

</main>

<footer>
本說明為行情研判與委託前參考，非不動產估價師法所定之估價報告書。
成交資料取自內政部實價登錄，地籍與公告現值取自內政部地籍圖資系統，
土地增值稅經財政部稅務入口網試算核對。實際稅額以稽徵機關核定為準。
</footer>

</div>
</body></html>"""

html = (HTML.replace("__CSS__", CSS).replace("__LOGO__", LOGO).replace("__GA__", GA))
with open('explain.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('done', len(html))
