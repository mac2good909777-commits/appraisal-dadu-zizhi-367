# -*- coding: utf-8 -*-
"""買方版物件說明 — 不含屋主背景、不含價格與稅務試算、不含議價策略。

資料來源同 build.py（第 16 版報告），僅保留買方需要的標的條件、特色與應揭露事項。
"""
from _assets import LOGO, IMG
from _sv import SV1, SV2, SV3

CSS = """
:root{--g:#4B872F;--f:#2B5937;--gold:#C0A434;--cream:#F5F3EE;--tx:#333;--lt:#888;--bd:#E8E6E1;--dn:#C0533A;}
*{box-sizing:border-box}
body{margin:0;background:#fff;color:var(--tx);font-family:"Noto Sans TC","Microsoft JhengHei",sans-serif;font-size:15px;line-height:1.8}
.wrap{max-width:960px;margin:0 auto}
header{background:var(--f);border-bottom:3px solid var(--gold);padding:28px 40px}
header .inner{max-width:960px;margin:0 auto;display:flex;align-items:center;gap:24px}
header img{width:100px;background:#fff;border-radius:4px;padding:8px}
header .tag{display:inline-block;color:var(--gold);font-size:13px;letter-spacing:.18em;font-weight:700;margin:0 0 7px}
header h1{color:#fff;font-size:28px;font-weight:700;letter-spacing:1px;margin:0 0 7px}
header p{color:#C9D6C9;font-size:14px;margin:0;line-height:1.7}
main{padding:40px}
h2{font-size:22px;font-weight:600;color:var(--f);margin:42px 0 16px;padding-left:12px;border-left:4px solid var(--g)}
h2:first-child{margin-top:0}
h3{font-size:17px;font-weight:600;color:var(--g);margin:24px 0 10px}
.lead{font-size:15.5px;color:#555;margin:0 0 22px;line-height:1.9}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:20px 0}
.kpi{background:#F8F8F5;border:1px solid var(--bd);padding:16px}
.kpi .lb{font-size:13px;color:#666;margin-bottom:4px}
.kpi .v{font-size:30px;font-weight:700;color:var(--gold);font-family:Inter,sans-serif;line-height:1.2}
.kpi .u{font-size:14px;color:#666;font-weight:500}
.card{border:1px solid var(--bd);border-radius:4px;padding:22px 24px;margin:16px 0}
.card h4{margin:0 0 8px;font-size:16.5px;color:var(--f);font-weight:700}
.card p{margin:0;font-size:14.5px;color:#666;line-height:1.8}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:14px}
th{background:var(--f);color:#fff;padding:11px 12px;text-align:left;font-weight:500;white-space:nowrap}
td{padding:10px 12px;border-bottom:1px solid var(--bd);vertical-align:top}
tbody tr:nth-child(odd){background:#F8F8F5}
.n{text-align:right;font-family:Inter,sans-serif;white-space:nowrap}
.b{font-weight:700;color:var(--f)}
.note{font-size:12.5px;color:#777;line-height:1.6}
.callout{background:var(--cream);border-left:4px solid var(--gold);padding:16px 20px;margin:18px 0;font-size:14.5px}
.callout b{color:var(--f)}
.warn{background:#FBF1EE;border-left:4px solid var(--dn)}
.ok{background:#EEF4EA;border-left:4px solid var(--g)}
.mapbox{border:1px solid var(--bd);padding:10px;margin:16px 0}
.mapbox img{width:100%;display:block}
.cap{font-size:12.5px;color:var(--lt);margin-top:8px;line-height:1.55}
.sv{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0}
.sv figure{margin:0;border:1px solid var(--bd);padding:8px}
.sv img{width:100%;display:block}
.sv figcaption{font-size:12.5px;color:#666;margin-top:7px;line-height:1.55}
.diagram{border:1px solid var(--bd);background:#F8F8F5;padding:20px;margin:16px 0;text-align:center}
.feat{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:18px 0}
.feat>div{display:flex;gap:12px;border:1px solid var(--bd);border-radius:4px;padding:16px 18px}
.feat .no{font-family:Inter,sans-serif;font-size:20px;font-weight:700;color:var(--gold);line-height:1.4;flex-shrink:0}
.feat .ft{font-size:15.5px;font-weight:700;color:var(--f);margin-bottom:4px}
.feat .fd{font-size:14px;color:#666;line-height:1.75}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:18px 0}
.three .card{margin:0}
.ask{background:var(--cream);border:1px solid var(--gold);border-radius:4px;padding:26px 28px;margin:20px 0;text-align:center}
.ask .t{font-size:13px;color:#8A7A3A;letter-spacing:.18em;font-weight:700;margin-bottom:8px}
.ask .v{font-size:30px;font-weight:700;color:var(--f);letter-spacing:2px}
.ask .s{font-size:14.5px;color:#666;margin-top:10px;line-height:1.85}
ul{margin:8px 0 8px 20px;padding:0}
li{margin-bottom:7px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
footer{background:var(--f);color:#fff;font-size:13.5px;padding:28px 40px;margin-top:50px}
footer .inner{max-width:960px;margin:0 auto}
footer .nm{font-size:20px;font-weight:700;margin-bottom:3px}
footer .ti{color:#C9D6C9;margin-bottom:12px}
footer .tel{font-family:Inter,sans-serif;font-size:22px;font-weight:700;color:var(--gold);letter-spacing:1px}
footer .cm{color:#AFC3AF;font-size:12.5px;margin-top:14px;line-height:1.8}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:14px 0;position:relative}
.tw table{margin:0;min-width:520px}
@media(max-width:760px){.kpis{grid-template-columns:repeat(2,1fr)}.two,.sv,.feat,.three{grid-template-columns:1fr}main{padding:22px 16px}header{padding:22px 16px}header .inner{flex-direction:column;align-items:flex-start;gap:14px}header h1{font-size:23px}body{font-size:16px}h2{font-size:20px}h3{font-size:16.5px}table{font-size:13.5px}th,td{padding:8px 9px}.callout{padding:14px 15px;font-size:14px}ul{margin-left:18px}.kpi .v{font-size:26px}footer{padding:24px 16px}.ask{padding:22px 18px}.ask .v{font-size:25px}}
@media(max-width:760px){.tw::before{content:"← 表格可左右滚動 →";display:block;font-size:12px;color:#A09A90;text-align:right;margin-bottom:3px;letter-spacing:.5px}}
@media(max-width:420px){.kpis{grid-template-columns:1fr}}
@media print{body{background:#fff}header,footer{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""

DIAGRAM = """
<svg viewBox="0 0 640 260" width="100%" style="max-width:600px" xmlns="http://www.w3.org/2000/svg">
<rect x="70" y="40" width="420" height="150" fill="#FBE9DC" stroke="#C0533A" stroke-width="2"/>
<line x1="210" y1="40" x2="210" y2="190" stroke="#C0533A" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="350" y1="40" x2="350" y2="190" stroke="#C0533A" stroke-width="1" stroke-dasharray="4 3"/>
<text x="140" y="120" text-anchor="middle" font-size="15" fill="#8A4028">369</text>
<text x="280" y="120" text-anchor="middle" font-size="15" fill="#8A4028">368</text>
<text x="420" y="120" text-anchor="middle" font-size="15" fill="#8A4028">367</text>
<rect x="70" y="196" width="420" height="34" fill="#E3E6E8" stroke="#AAB0B5" stroke-width="1"/>
<text x="280" y="218" text-anchor="middle" font-size="13" fill="#555">&#31119;&#21033;&#36335; 117 &#24055;&#65288;&#29694;&#27841;&#23485;&#32004; 5 &#8211; 6 m&#65289;</text>
<line x1="70" y1="26" x2="490" y2="26" stroke="#2B5937" stroke-width="1"/>
<text x="280" y="20" text-anchor="middle" font-size="13" fill="#2B5937" font-weight="600">&#33251;&#36335;&#38754;&#23485; &#32004; 34.1 m</text>
<line x1="512" y1="40" x2="512" y2="190" stroke="#2B5937" stroke-width="1"/>
<text x="524" y="118" font-size="13" fill="#2B5937" font-weight="600">&#28145;&#24230;</text>
<text x="524" y="136" font-size="13" fill="#2B5937" font-weight="600">&#32004; 11.9 m</text>
<text x="70" y="252" font-size="12.5" fill="#888">&#20840;&#27573;&#38754;&#23485;&#33251;&#24055; &#8594; &#21487;&#20999; 4 &#25142;&#34903;&#23627;&#22411;&#36879;&#22825;&#65292;&#27599;&#25142;&#38754;&#23485;&#32004; 8.5 m&#65292;&#28961;&#38656;&#30041;&#35373;&#20839;&#37096;&#36890;&#36947;</text>
</svg>
"""

BODY = """<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<!-- Google tag (gtag.js) - GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H5VLHW8761"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  // 自家裝置標記：任一頁加 ?ga=off 造訪一次，之後該瀏覽器的流量都標成 internal。
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
<title>大肚市區 整排素地 123.5 坪｜自治段 367・368・369</title>
<meta name="description" content="臺中市大肚區自治段 367・368・369，福利路 117 巷，純建地 123.5 坪。第三種住宅區，建蔽 60%／容積 200%，面寬約 34.1 公尺全段臨巷，可規劃 4 戶街屋型透天。價格備索。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>

<header><div class="inner">
<img src="data:image/png;base64,__LOGO__" alt="瑞禾開發">
<div>
<div class="tag">TAICHUNG DADU&nbsp;&nbsp;/&nbsp;&nbsp;RESIDENTIAL LAND</div>
<h1>大肚市區 整排素地 123.5 坪</h1>
<p>臺中市大肚區 自治段 367・368・369｜福利路 117 巷<br>第三種住宅區・純建地・面寬約 34.1 公尺全段臨巷</p>
</div>
</div></header>

<div class="wrap"><main>

<h2>一、標的概要</h2>
<p class="lead">位於大肚市區沙田路一段街廓內的三筆相連素地，合計 123.5 坪，整批釋出。
基地為全段臨巷的街屋型地形，法定可建建築面積約 74 坪、總樓地板約 247 坪。</p>

<div class="kpis">
<div class="kpi"><div class="lb">土地總面積<span class="note"> ・純建地</span></div><div class="v">123.5<span class="u"> 坪</span></div></div>
<div class="kpi"><div class="lb">使用分區</div><div class="v" style="font-size:22px">第三種<span class="u"> 住宅區</span></div></div>
<div class="kpi"><div class="lb">建蔽率 / 容積率</div><div class="v" style="font-size:22px">60<span class="u">%</span> / 200<span class="u">%</span></div></div>
<div class="kpi"><div class="lb">臨路面寬<span class="note"> ・全段臨巷</span></div><div class="v">34.1<span class="u"> m</span></div></div>
</div>

<div class="two">
<div>
<div class="tw"><table><tbody>
<tr><td style="width:34%">座落</td><td class="b">臺中市大肚區 福利路 117 巷</td></tr>
<tr><td>地號</td><td>自治段 367・368・369（三筆相連）</td></tr>
<tr><td>登記面積</td><td>408.27 ㎡ ／ <b>123.50 坪</b><br><span class="note">367：40.10 坪｜368：41.01 坪｜369：42.39 坪</span></td></tr>
<tr><td>都市計畫分區</td><td>第三種住宅區（建蔽 60%／容積 200%）</td></tr>
<tr><td>基地尺寸</td><td>面寬約 34.1 m × 深度約 11.9 m，完整矩形</td></tr>
<tr><td>臨路</td><td>福利路 117 巷，現況柏油路寬約 5 – 6 m，雙向可通、非死巷</td></tr>
<tr><td>現況</td><td>素地，無地上物（鐵皮圍籬圈圍，界址明確）</td></tr>
<tr><td>法定可建</td><td>建築面積約 74 坪／總樓地板約 247 坪</td></tr>
<tr><td>公告現值</td><td>20,600 元/㎡（約 6.81 萬/坪），總額約 841 萬</td></tr>
<tr><td>交易方式</td><td>三筆整批出售</td></tr>
</tbody></table></div>
</div>
<div class="mapbox"><img src="data:image/png;base64,__IMG__" alt="地籍圖"><div class="cap">標的地籍位置圖（釘選 367・368・369，共 123.5 坪）</div></div>
</div>

<h2>二、基地特色</h2>

<div class="feat">
<div><div class="no">01</div><div>
<div class="ft">全段臨巷，可規劃 4 戶</div>
<div class="fd">面寬約 34.1 m 全段臨巷，可直接切分 4 戶街屋型透天，每戶約 8.5 m 面寬、各有獨立出入口，<b>無須留設內部通道</b>。</div>
</div></div>
<div><div class="no">02</div><div>
<div class="ft">純建地，產權單純</div>
<div class="fd">三筆皆為單獨所有、無共有人，<b>無公設保留地、無地上物</b>，交易標的即 123.50 坪建地。</div>
</div></div>
<div><div class="no">03</div><div>
<div class="ft">市區生活機能核心</div>
<div class="fd">位於沙田路一段街廓內，鄰<b>彰化銀行、台中商業銀行大肚分行與大肚國小</b>；巷口直通福利路，距大肚火車站、大肚夜市步行可及。</div>
</div></div>
<div><div class="no">04</div><div>
<div class="ft">成熟純住宅街廓</div>
<div class="fd">兩側為 3 – 4 層透天，街廓開發已近完整；巷內夾雜民國 103 – 104 年新建透天，<b>新屋在本巷內有實際成交紀錄</b>。</div>
</div></div>
</div>

<div class="diagram">__DIAGRAM__
<div class="cap" style="text-align:left">基地朝向示意：面寬 34.1 m 全段臨巷、深度 11.9 m 的街屋型基地。
相較同面積的窄長型土地，全段臨路不需犧牲土地留設通道，<b>規劃效率明顯較高</b>。</div>
</div>

<h2>三、現場環境</h2>
<div class="sv">
<figure><img src="data:image/webp;base64,__SV1__" alt="福利路117巷街景"><figcaption><b>福利路 117 巷（2026.01 街景）</b>　巷道柏油完整、路面劃設「請勿停車」，兩側為 3 – 4 層透天，右側住宅多設自有車庫捲門。</figcaption></figure>
<figure><img src="data:image/webp;base64,__SV2__" alt="福利路117巷內段"><figcaption><b>巷內段</b>　寬度約 5 – 6 m，單向會車、路邊可停一列車，末端可通往下一街廓，<b>非死巷</b>。</figcaption></figure>
</div>
<figure style="margin:0;border:1px solid #E8E6E1;padding:8px"><img src="data:image/webp;base64,__SV3__" alt="福利路與117巷口" style="width:100%;display:block"><figcaption class="cap"><b>福利路 ╳ 117 巷 巷口（2024.10 街景）</b>　巷口直接銜接福利路，轉角為月租停車場，後方可見坡上新建透天。巷口視野開闊、進出無阻礙。</figcaption></figure>

<div class="callout ok"><b>✓ 現勘重點：</b>
① 臨路為 <b>5 – 6 m 已開闢巷道</b>，柏油完整、排水溝與門牌齊備，兩側建物已全面開發。
② 巷口直接通福利路，<b>非死巷、進出順暢</b>。
③ 街廓為成熟純住宅生活圈，屋齡多為民國 69 – 80 年老透天，夾雜 103 – 104 年新建案。
④ 標的現況為綠色鐵皮圍籬圈圍之空地，界址明確、已與巷道分隔。</div>

<h2>四、現況與應注意事項</h2>
<p class="lead">以下四項為賣方主動揭露，相關圖資與法規條文均可提供查閱。
買方亦可自行調閱謄本、向臺中市都發局查詢，所述內容與公開資料一致。</p>

<div class="tw"><table><thead><tr><th style="width:24%">項目</th><th>說明</th></tr></thead><tbody>
<tr><td class="b">① 門前巷道<br>為私有土地</td><td>福利路 117 巷之路身為<b>自治段 375 地號</b>（面積 594.11 ㎡，6 人共有），
都市計畫分區登記為第三種住宅區而非道路用地。<b>本標的不含該巷道任何持分</b>，通行依據為該巷之現有巷道／既成道路地位。<br>
<span class="note">該巷自民國 68 年分割留設後供通行逾 40 年，已鋪設柏油、劃設標線、設置排水溝並編訂門牌；兩側房屋屋齡自民國 69 年至 103 年，全部領有門牌、屬合法建築。</span></td></tr>
<tr><td class="b">② 建築線指定<br>與退讓</td><td>依<b>臺中市建築管理自治條例第 19 條</b>，現有巷道之認定共六款，其中第 1 款（既成道路）、第 2 款（已納入維護管理之公眾通行道路）、第 4 款（曾指定建築線且已核准建築完成）均<b>無須土地所有權人出具同意書</b>；本案巷道兩側房屋皆已合法建築完成。<br>
惟依<b>同條例第 20 條</b>，本巷長約 114.6 m、現況平均寬約 5.18 m 未達 6 m，
<b>可能須兩旁均等退讓約 0.41 m（本案約 4.2 坪）始得指定建築線</b>。<br>
<span class="note">退讓為依條文推算之預估值，實際應以臺中市都發局指定建築線結果為準；買方可自行申請確認（規費新臺幣 500 元，每增一條道路加收 100 元）。</span></td></tr>
<tr><td class="b">③ 基地深度<br>約 11.9 m</td><td>深度較中部常見的 12 – 15 m 略淺。扣除前院退縮與後院法定空地後，<b>單層可建深度約 8 – 9 m</b>，戶型需以樓層數（4 層）換取面積，一樓車庫＋客廳之配置會較緊湊。</td></tr>
<tr><td class="b">④ 現況需整地</td><td>圍籬內為未整理素地，長有雜草、灌木與數株喬木，地表可見零星磚瓦與舊磁磚殘跡。
<b>整地、雜草清除、喬木移除與廢棄物清運概估 30 – 50 萬元</b>。<br>
<span class="note">另：三筆土地分屬二位所有權人，皆為單獨所有、無共有人；整批交易須兩位同時簽署買賣契約。</span></td></tr>
</tbody></table></div>

<h2>五、適合的規劃方向</h2>
<div class="three">
<div class="card"><h4>小型建商</h4><p>沿巷切分 4 戶街屋型透天，每戶地約 30.9 坪、建約 62 坪。地形零浪費，開發規模與去化期適中。</p></div>
<div class="card"><h4>自建自用</h4><p>取單側 1 – 2 戶寬度自建，其餘保留或分售。市區生活圈、步行可達學校與金融機構。</p></div>
<div class="card"><h4>鄰地整合</h4><p>三筆相連成完整矩形，與鄰地合併可進一步擴大街廓深度與基地規模。</p></div>
</div>

<h2>六、價格與洽詢</h2>
<div class="ask">
<div class="t">PRICE ON REQUEST</div>
<div class="v">價格備索</div>
<div class="s">本案採預約制提供完整資料與現場帶看。<br>
需要地籍圖、都市計畫分區圖或建築線相關資料，請來電洽詢。</div>
</div>

<div class="callout"><b>可提供查閱之資料：</b>
<ul style="margin-top:6px">
<li>三筆土地之<b>地籍圖、登記面積與 115 年度公告現值</b>（內政部地籍圖資系統查得）</li>
<li>門前巷道（自治段 375）之<b>面積、寬度換算與共有情形</b></li>
<li><b>臺中市建築管理自治條例第 19、20 條</b>條文，與現有巷道認定六款之逐項檢視</li>
<li>基地切分 4 戶之<b>配置示意與法定可建量試算</b></li>
</ul></div>

<h2>七、資料來源與免責</h2>
<ul style="font-size:14px;color:#555">
<li>地籍資料與定位：內政部地籍圖資網路便民服務系統（easymap.moi.gov.tw，圖資版本 2026.08.21），以地段代碼＋地號逐筆查得面積、115 年度公告現值與宗地位置。</li>
<li>現況照片取自 Google 街景服務（拍攝日期 2024.10 及 2026.01），巷道寬度為影像目視估計與地籍面積換算值，<b>正式數值應以都市計畫圖及建築線指定為準</b>。</li>
<li>公告現值、面積、分區資料引自地籍查詢系統（115 年公告現值及地價），實際以地政事務所謄本為準。</li>
<li>法定可建量為依建蔽率、容積率推算之概估值，實際須由建築師依基地條件與退縮規定規劃後確認。</li>
<li>建築線相關規定引自臺中市建築管理自治條例第 19、20 條；既成道路公用地役關係要件引自司法院釋字第 400 號解釋；<b>退讓面積為依條文推算之預估值，實際應以都發局指定建築線結果為準</b>。</li>
<li>尚待確認事項：建築線指定與退縮規定、地上有無占用或地役權。建議買方於簽約前自行向臺中市都發局申請指定建築線確認。</li>
<li>本說明為<b>物件資訊提供</b>，非不動產估價師法所定之估價報告書，亦不構成要約；交易條件以買賣雙方另行簽訂之契約為準。</li>
</ul>

</main></div>

<footer><div class="inner">
<div class="nm">張現傑</div>
<div class="ti">瑞禾開發｜工業地產部業務總監</div>
<div class="tel">0953-909-777</div>
<div class="cm">
瑞禾不動產經紀股份有限公司｜不動產經紀人（108）中市經紀字第 01847 號<br>
本案採預約制提供資料與帶看　｜　製表日期：2026.10.08
</div>
</div></footer>
</body></html>"""

html = (BODY.replace("__CSS__", CSS)
            .replace("__DIAGRAM__", DIAGRAM)
            .replace("__LOGO__", LOGO)
            .replace("__IMG__", IMG)
            .replace("__SV1__", SV1)
            .replace("__SV2__", SV2)
            .replace("__SV3__", SV3))

with open('buyer.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('buyer.html', len(html))
