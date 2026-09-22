# -*- coding: utf-8 -*-
from _assets import LOGO, IMG
from _sv import SV1, SV2, SV3

rows_land = [
 ("113.08","福利段 316","34.3","961","28.05","**同生活圈巷內素地**，坪數相近，常規交易","key"),
 ("113.07","自治段 376","238.1","7,359","30.92","同段大面積整批；含公設保留地，可建部分單價更高","key"),
 ("113.09","自治段 376-2","3.0","112","37.75","同街廓畸零補足","sub"),
 ("115.04","福利段 741","33.5","1,300","38.75","親友交易，僅供上緣參考","sub"),
 ("114.03","福山段 1249","55.8","1,605","28.77","市區臨路素地","key"),
 ("113.03","自治段 128-4","14.7","334","22.79","政府標讓售","sub"),
 ("113.03","自治段 189-2","29.5","673","22.79","政府標讓售","sub"),
 ("114.03","自治段 127","2.5","56","22.78","政府標讓售","sub"),
 ("114.03","福利段 118-6","1.0","23","22.98","政府標讓售","sub"),
 ("113.03","大東段 754","29.7","1,130","38.10","市區精華、含未登記建物","sub"),
 ("113.03","福德段 837","51.2","2,000","39.04","市區精華、含未登記建物","sub"),
 ("114.07","文昌段 2333-15","17.8","450","25.23","小坪數、含增建","sub"),
]

# (成交, 門牌, 建成年, 地坪, 建坪, 總價, 含建物地坪單價, 建物殘值單價, 反推地價)
rows_house = [
 ("113.03","福利路 150 巷 8 號","103","36.8","65.6","1,810","49.23","7.0","36.7","key"),
 ("114.06","福利路 152 巷 9 號","103","30.7","55.8","1,420","46.26","7.0","33.5","key"),
 ("114.01","福利路 152 巷 1 號","103","66.9","110.4","3,000","44.82","7.0","33.3","key"),
 ("113.06","福利路 118 巷 10 號","080","28.3","65.9","1,500","52.99","3.5","44.8","sub"),
 ("113.11","福利路 127 號","069","26.2","36.8","1,500","57.21","2.5","53.7","sub"),
 ("115.02","自治路 36 巷 19 號","104","38.3","67.2","1,880","49.15","7.0","36.8","sub"),
]


def tr_land(r):
    d, seg, p, total, unit, note, kind = r
    cls = ' class="hl"' if kind == "key" else ''
    note = note.replace('**', '')
    return ('<tr%s><td>%s</td><td>%s</td><td class="n">%s</td><td class="n">%s</td>'
            '<td class="n b">%s</td><td class="note">%s</td></tr>' % (cls, d, seg, p, total, unit, note))


def tr_house(r):
    d, addr, yr, lp, bp, total, gross, res, net, kind = r
    cls = ' class="hl"' if kind == "key" else ''
    return ('<tr%s><td>%s</td><td>%s</td><td class="n">%s</td><td class="n">%s</td>'
            '<td class="n">%s</td><td class="n">%s</td><td class="n">%s</td>'
            '<td class="n">%s</td><td class="n b">%s</td></tr>'
            % (cls, d, addr, yr, lp, bp, total, gross, res, net))


LAND = ''.join(tr_land(r) for r in rows_land)
HOUSE = ''.join(tr_house(r) for r in rows_house)

CSS = """
:root{--g:#4B872F;--f:#2B5937;--gold:#C0A434;--cream:#F5F3EE;--tx:#333;--lt:#888;--bd:#E8E6E1;--dn:#C0533A;}
*{box-sizing:border-box}
body{margin:0;background:#fff;color:var(--tx);font-family:"Noto Sans TC","Microsoft JhengHei",sans-serif;font-size:15px;line-height:1.8}
.wrap{max-width:960px;margin:0 auto}
header{background:var(--f);border-bottom:3px solid var(--gold);padding:28px 40px}
header .inner{max-width:960px;margin:0 auto;display:flex;align-items:center;gap:24px}
header img{width:120px;background:#fff;border-radius:4px;padding:8px}
header h1{color:#fff;font-size:28px;font-weight:700;letter-spacing:1px;margin:0 0 6px}
header p{color:#C9D6C9;font-size:14px;margin:0}
main{padding:40px}
h2{font-size:22px;font-weight:600;color:var(--f);margin:40px 0 16px;padding-left:12px;border-left:4px solid var(--g)}
h2:first-child{margin-top:0}
h3{font-size:17px;font-weight:600;color:var(--g);margin:24px 0 10px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:20px 0}
.kpi{background:#F8F8F5;border:1px solid var(--bd);padding:16px}
.kpi .lb{font-size:13px;color:#666;margin-bottom:4px}
.kpi .v{font-size:30px;font-weight:700;color:var(--gold);font-family:Inter,sans-serif;line-height:1.2}
.kpi .u{font-size:14px;color:#666;font-weight:500}
.card{border:1px solid var(--bd);border-radius:4px;padding:24px;margin:16px 0}
.concl{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--bd);margin:18px 0}
.concl > div{padding:20px;text-align:center;border-right:1px solid var(--bd)}
.concl > div:last-child{border-right:0}
.concl .t{font-size:14px;color:#666;margin-bottom:8px}
.concl .p{font-size:26px;font-weight:700;font-family:Inter,sans-serif;color:var(--f)}
.concl .s{font-size:13px;color:var(--lt);margin-top:6px}
.concl .mid{background:var(--cream)}
.concl .mid .p{color:var(--gold);font-size:30px}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:14px}
th{background:var(--f);color:#fff;padding:11px 12px;text-align:left;font-weight:500;white-space:nowrap}
td{padding:10px 12px;border-bottom:1px solid var(--bd);vertical-align:top}
tbody tr:nth-child(odd){background:#F8F8F5}
tr.hl{background:#EEF4EA !important}
tr.hl td{border-bottom:1px solid #D6E3CE}
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
ul{margin:8px 0 8px 20px;padding:0}
li{margin-bottom:6px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
footer{background:var(--f);color:#fff;font-size:13px;padding:22px 40px;margin-top:48px}
footer .inner{max-width:960px;margin:0 auto;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px}
footer span{color:#AFC3AF}
@media(max-width:760px){.kpis{grid-template-columns:repeat(2,1fr)}.concl{grid-template-columns:1fr}.two,.sv{grid-template-columns:1fr}main{padding:24px}header{padding:20px 24px}header .inner{flex-direction:column;align-items:flex-start;gap:14px}}
@media print{header,footer{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
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
<text x="280" y="218" text-anchor="middle" font-size="13" fill="#555">福利路 117 巷（現況寬約 5 – 6 m）</text>
<line x1="70" y1="26" x2="490" y2="26" stroke="#2B5937" stroke-width="1"/>
<text x="280" y="20" text-anchor="middle" font-size="13" fill="#2B5937" font-weight="600">臨路面寬 約 34.1 m</text>
<line x1="512" y1="40" x2="512" y2="190" stroke="#2B5937" stroke-width="1"/>
<text x="524" y="118" font-size="13" fill="#2B5937" font-weight="600">深度</text>
<text x="524" y="136" font-size="13" fill="#2B5937" font-weight="600">約 11.9 m</text>
<text x="70" y="252" font-size="12.5" fill="#888">全段面寬臨巷 → 可切 4 戶街屋型透天，每戶面寬約 8.5 m，無需留設內部通道</text>
</svg>
"""

BODY = """<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>大肚自治段土地估價</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>

<header><div class="inner">
<img src="data:image/png;base64,__LOGO__" alt="瑞禾開發">
<div><h1>土地價格評估報告</h1>
<p>臺中市大肚區 自治段 367・368・369 地號（福利路 117 巷）｜合計 123.5 坪｜評估基準日 2026.09.22（民國 115 年 9 月）</p></div>
</div></header>

<div class="wrap"><main>

<h2>一、標的概要</h2>
<div class="kpis">
<div class="kpi"><div class="lb">土地總面積</div><div class="v">123.5<span class="u"> 坪</span></div></div>
<div class="kpi"><div class="lb">使用分區</div><div class="v" style="font-size:22px">第三種<span class="u"> 住宅區</span></div></div>
<div class="kpi"><div class="lb">建蔽率 / 容積率</div><div class="v" style="font-size:22px">60<span class="u">%</span> / 200<span class="u">%</span></div></div>
<div class="kpi"><div class="lb">公告現值</div><div class="v">6.81<span class="u"> 萬/坪</span></div></div>
</div>

<div class="two">
<div>
<h3>基地條件</h3>
<ul>
<li>三筆相連成一完整矩形，<b>面寬約 34.1 m 全段臨巷</b>、深度約 11.9 m</li>
<li>367 地號 40.1 坪（132.57 ㎡），368、369 合計約 83.4 坪</li>
<li>素地，<b>無地上物</b>（地籍系統顯示無地上物資料）</li>
<li>臨 <b>福利路 117 巷</b>，現況柏油路寬約 5 – 6 m，雙向可通、非死巷</li>
<li>位於<b>沙田路一段街廓內</b>，鄰彰銀、台中商銀大肚分行與大肚國小，生活機能核心</li>
<li>法定可建：建築面積約 <b>74 坪</b>、總樓地板約 <b>247 坪</b></li>
<li>公告現值總額約 <b>841 萬</b>；公告地價 3,200 元/㎡（總額 42.4 萬）</li>
</ul>
</div>
<div class="mapbox"><img src="data:image/png;base64,__IMG__" alt="地籍圖"><div class="cap">標的地籍位置圖（釘選 367・368・369，共 123.5 坪）</div></div>
</div>

<h2>二、現場勘查：臨路與街廓</h2>
<div class="sv">
<figure><img src="data:image/webp;base64,__SV1__" alt="福利路117巷街景"><figcaption><b>福利路 117 巷（2026.01 街景）</b>　巷道柏油完整、路面劃設「請勿停車」，兩側為 3–4 層透天，右側住宅多設自有車庫捲門。</figcaption></figure>
<figure><img src="data:image/webp;base64,__SV2__" alt="福利路117巷內段"><figcaption><b>巷內段</b>　寬度約 5 – 6 m，單向會車、路邊可停一列車，末端可通往下一街廓，<b>非死巷</b>。</figcaption></figure>
</div>
<figure style="margin:0;border:1px solid #E8E6E1;padding:8px"><img src="data:image/webp;base64,__SV3__" alt="福利路與117巷口" style="width:100%;display:block"><figcaption class="cap"><b>福利路 ╳ 117 巷 巷口（2024.10 街景）</b>　巷口直接銜接福利路，轉角為月租停車場（1,000 元／月），後方可見坡上新建高級透天。巷口視野開闊、進出無阻礙，是本案的加分項。</figcaption></figure>

<div class="callout ok"><b>✓ 現勘四項結論：</b>
① 臨路為 <b>5 – 6 m 已開闢巷道</b>，柏油完整、兩側建物已全面開發，建築線與基地出入無疑慮（實際仍須向都發局申請指定建築線確認）。
② 巷口直接通福利路，<b>非死巷、進出順暢</b>，距大肚火車站、大肚夜市步行可及。
③ 街廓為成熟純住宅生活圈，屋齡多為民國 69 – 80 年老透天，夾雜 103 – 104 年新建案，<b>新屋在本巷內確有溢價空間</b>。
④ 標的本身（門牌約當福利路 117 巷 14 號位置）現況為<b>綠色鐵皮圍籬圈圍之空地</b>，界址明確、已與巷道分隔。</div>

<h3>標的現況（117 巷 14 號位置，2026.01 街景）</h3>
<p>圍籬內為未整理素地，長有<b>雜草、灌木與數株喬木</b>，地表可見零星磚瓦與舊磁磚殘跡，研判曾有低矮建物拆除後未整地。基地後方<b>緊鄰兩層樓老舊住宅與加蓋鐵皮屋背面</b>，無退縮空間 —— 此點正好印證地籍圖之判讀：<b>本案深度僅約 11.9 m，後界即為鄰房</b>。遠處可見電梯大樓，顯示本街廓周邊仍有較高強度開發。</p>
<div class="callout warn"><b>對價格的影響：</b>需計入<b>整地、雜草清除、喬木移除與廢棄物清運費用，概估 30 – 50 萬元</b>（約當 0.3 – 0.4 萬/坪）。金額不大，不改變價格區間，但<b>買方議價時必定提出</b>，建議屋主：<br>
（a）若求快，維持現況出售、開價時即預留此一讓價空間；<br>
（b）若想拉高成交價，<b>先自行整地清運後再上架</b> —— 乾淨方整的素地在現場觀感與買方想像力上的加分，通常遠高於 50 萬的成本。此外，圍籬內若有他人堆置物或使用痕跡，務必先行排除，避免後續點交爭議。</p></div>

<p style="font-size:13px;color:#888">※ 標的現況照片（Google 街景 2026.01）待檔案提供後補入本報告版面。</p>

<h2>三、重要修正：基地朝向與規劃效率</h2>
<div class="callout warn"><b>相較初版報告，此處為關鍵修正。</b>
初版誤讀為「面寬 11.9 m、深度 34.1 m」的窄長地；經街景與地籍圖比對，實際是
<b>面寬 34.1 m 全段臨巷、深度 11.9 m</b> 的「街屋型」基地。<b>這對價格是正面的</b> ——
全段臨路代表可直接切分 4 戶透天，每戶皆有獨立面寬與出入口，<b>無須留設內部通道，土地零浪費</b>；
規劃效率明顯高於同面積的窄長型基地，本次估價因此上修。</div>
__DIAGRAM__
<p style="font-size:14px;color:#555;margin-top:4px">
<b>唯一需注意的限制：</b>深度 11.9 m 對透天而言略淺（中部常見 12 – 15 m）。扣除前院退縮與後院法定空地後，
單層可建深度約 8 – 9 m，戶型需以樓層數（4 層）換取面積，一樓車庫＋客廳的配置會較緊湊。此點在議價時買方會提出。</p>

<h2>四、估價結論</h2>
<div class="concl">
<div><div class="t">屋主底線（快速變現）</div><div class="p">22 萬/坪</div><div class="s">總價約 2,720 萬</div></div>
<div class="mid"><div class="t">合理成交帶</div><div class="p">25 – 29 萬/坪</div><div class="s">總價約 3,090 – 3,580 萬</div></div>
<div><div class="t">建議開價</div><div class="p">32 萬/坪</div><div class="s">總價約 3,950 萬</div></div>
</div>

<div class="callout"><b>一句話結論：</b>以 <b>3,950 萬（32 萬/坪）開價</b>，守住 <b>3,100 萬（25 萬/坪）</b>，
成交落點合理推估在 <b>3,100 – 3,500 萬</b>。
較初版（開價 3,700 萬、合理帶 23 – 27 萬）<b>上修約 8%</b>，理由是現勘確認了三件事：
臨路為已開闢可通行巷道而非未開闢小徑、基地為全段臨路的街屋型地形、
以及新增福利路生活圈兩組更貼近的比較資料。</div>

<h2>五、比較法：同區土地成交</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">資料來源：內政部實價登錄，大肚區「土地」類交易。單價＝總價 ÷ 土地坪數（自算，不採公告單價）。綠底為主要比較案。</p>
<table><thead><tr><th>成交</th><th>地段地號</th><th class="n">土地坪</th><th class="n">總價(萬)</th><th class="n">單價(萬/坪)</th><th>備註</th></tr></thead>
<tbody>__LAND__</tbody></table>

<div class="callout"><b>比較案判讀：</b>
<ul style="margin-top:6px">
<li><b>福利段 316（113.08，34.3 坪、28.05 萬/坪）</b>是本次新增、也是<b>最貼近的比較案</b>——同一生活圈的巷內素地、常規交易（備註僅為總價微調）。本案單筆規模（40 坪）與之相當。<b>其比較效力已獲官方地籍資料客觀驗證，見下方說明。</b></li>
<li><b>自治段 376（113.07，238 坪、30.92 萬/坪）</b>為同段大面積整批成交，且含公設保留地，純可建部分實際高於 30.92 萬，構成本段價格的有力支撐。</li>
<li>本案 123.5 坪介於兩者之間：總價門檻（約 3,200 萬）高於 34 坪單筆案，須計入<b>大面積折讓約 10%</b>；但全段臨路可切 4 戶，買方層涵蓋自建自用與小型建商，折讓幅度有限。</li>
<li>自治段與福利段的政府標讓售案集中在 <b>22.78 – 22.98 萬/坪</b>，屬小坪數畸零補足，可視為<b>本區價格地板</b>。</li>
<li>福利段 741（38.75 萬）為親友交易、大東段 754 與福德段 837（38 – 39 萬）為含地上物之臨街精華地，三者皆屬<b>天花板參考</b>，本案素地不宜逕行比附。</li>
</ul></div>

<h3>比較案效力驗證：公告現值交叉比對</h3>
<p>「同生活圈」不應只憑段名相鄰推論。經內政部地籍圖資網路便民服務系統（115 年度公告現值）逐筆查證，
本案與主要比較案的<b>政府評定地價幾乎完全一致</b>：</p>
<table><thead><tr><th>地號</th><th class="n">登記面積(㎡)</th><th class="n">登記面積(坪)</th><th class="n">公告現值(元/㎡)</th><th class="n">換算(萬/坪)</th><th>地政事務所</th></tr></thead><tbody>
<tr class="hl"><td><b>自治段 367（本案）</b></td><td class="n">132.57</td><td class="n">40.1</td><td class="n">20,600</td><td class="n b">6.81</td><td>龍井</td></tr>
<tr class="hl"><td><b>福利段 316（比較案）</b></td><td class="n">101.94</td><td class="n">30.8</td><td class="n">20,700</td><td class="n b">6.84</td><td>龍井</td></tr>
</tbody></table>
<div class="callout ok"><b>✓ 兩者公告現值差距僅 0.5%</b>，代表政府對這兩塊地的區位條件評定為<b>同一價格帶</b>。
這是比「段名相鄰」更客觀的佐證 —— <b>福利段 316 作為主要比較案的效力成立</b>，其 28.05 萬/坪的成交價可直接對標，無須再做區位調整。
（附帶驗證：本案登記面積 132.57 ㎡ 與屋主提供之地籍資料完全相符。）</div>
<p style="font-size:14px;color:#555"><b>兩案位置：</b>本案自治段 367 位於<b>沙田路一段街廓內</b>，鄰近彰化銀行大肚分行、台中商業銀行大肚分行與大肚國小，
屬大肚市區的金融與生活機能核心；福利段 316 位於育樂街一帶，同為大肚市區成熟住宅區。</p>

<h2>六、交叉驗證一：福利路巷內透天扣建物殘值反推地價</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">本次改採<b>同一生活圈、同為巷內</b>的透天成交反推，比初版採用的自治路店住段更貼近。建物殘值依屋齡估：10 年內 7 萬/坪、30 年 4 萬/坪、45 年以上 2.5 萬/坪。</p>
<table><thead><tr><th>成交</th><th>門牌</th><th class="n">建成年</th><th class="n">地坪</th><th class="n">建坪</th><th class="n">總價(萬)</th><th class="n">含建物<br>地坪單價</th><th class="n">建物殘值<br>(萬/坪)</th><th class="n">反推地價<br>(萬/坪)</th></tr></thead>
<tbody>__HOUSE__</tbody></table>
<div class="callout">三筆 <b>103 年新透天（綠底）反推地價高度收斂在 33.3 – 36.8 萬/坪</b>，一致性極高，可信度佳。
老屋案（69 – 80 年）反推值偏高（44.8 – 53.7 萬），係因建物殘值難以精確認列，且福利路 127 號臨主要道路，僅供參考。
以 33 – 37 萬為「<b>單戶 30 坪級距、已開發完成</b>」的地價水準，本案為<b>整批素地</b>，需扣除開發風險與時間成本，
折讓 20 – 25% 後約 <b>25 – 29 萬/坪</b>，與比較法結論吻合。</div>

<h2>七、交叉驗證二：開發效益反推（買方付得起多少）</h2>
<div class="card">
<h3>情境：沿巷切分 4 戶街屋型透天（每戶地約 30.9 坪、建約 62 坪）</h3>
<table><thead><tr><th>項目</th><th class="n">保守</th><th class="n">樂觀</th><th>依據</th></tr></thead><tbody>
<tr><td>單戶售價</td><td class="n">1,700 萬</td><td class="n">1,900 萬</td><td class="note">同巷 103 年透天實績：福利路 152 巷 9 號 1,420 萬（30.7 地/55.8 建）、150 巷 8 號 1,810 萬（36.8/65.6）；新成屋加計屋齡差</td></tr>
<tr><td>總銷</td><td class="n">6,800 萬</td><td class="n">7,600 萬</td><td class="note">4 戶</td></tr>
<tr><td>營建成本</td><td class="n">－3,224 萬</td><td class="n">－3,224 萬</td><td class="note">62 坪 × 13 萬/坪 × 4 戶（RC 四層含雜項、基礎）</td></tr>
<tr><td>整地・清運・雜項</td><td class="n">－50 萬</td><td class="n">－30 萬</td><td class="note">現況雜草、喬木與舊建物殘跡之清除（見第二節現況說明）</td></tr>
<tr><td>管銷・稅費・利潤</td><td class="n">－1,020 萬</td><td class="n">－1,140 萬</td><td class="note">約總銷 15%</td></tr>
<tr class="hl"><td><b>土地可負擔總額</b></td><td class="n b">2,506 萬</td><td class="n b">3,206 萬</td><td class="note">＝總銷 － 營建 － 整地 － 管銷利潤</td></tr>
<tr class="hl"><td><b>換算土地單價</b></td><td class="n b">20.3 萬/坪</td><td class="n b">26.0 萬/坪</td><td class="note">÷ 123.5 坪</td></tr>
</tbody></table>
<p style="font-size:14px;margin:10px 0 0">小型建商的出價天花板約在 <b>26 萬/坪</b>；<b>自建自用買方</b>（不計開發利潤與管銷）可再往上約 3 – 4 萬，
到 <b>29 – 30 萬/坪</b>仍屬合理。三法交會處即為 <b>25 – 29 萬/坪</b> 的合理成交帶。</p>
</div>

<h2>八、銷售策略建議</h2>
<div class="two">
<div class="card"><h3>方案 A：整批出售（建議）</h3>
<ul>
<li>開價 <b>3,950 萬</b>（32 萬/坪），議價空間預留 18 – 20%</li>
<li>目標買方：<b>在地小建商</b>（首選，因可切 4 戶、規模剛好）、自建自用家庭、鄰地整合者</li>
<li>賣點主打「<b>大肚市區稀有整排素地，面寬 34 米全段臨路，可規劃 4 戶</b>」</li>
<li>預估銷售期 <b>4 – 8 個月</b></li>
</ul></div>
<div class="card"><h3>方案 B：分割單筆出售</h3>
<ul>
<li>依現有三筆地號分別出售，每筆約 40 坪，單筆開價 <b>1,450 萬</b>（36 萬/坪）</li>
<li>總額可望達 <b>4,100 – 4,350 萬</b>（＋10 ~ 15%）</li>
<li>本案地形有利分割：<b>每筆皆獨立臨巷，無需留設通道</b>，是分割單賣的最佳條件</li>
<li>代價：銷售期拉長至 <b>12 個月以上</b>，中間筆位通常最後才去化、須讓價</li>
</ul></div>
</div>

<div class="callout"><b>給屋主的三句話：</b>
① 本案最大的價值不在坪數，而在<b>「34 米面寬全段臨路」的地形</b> —— 同樣 123 坪，窄長型只能蓋 2 戶還要留通道，本案可切 4 戶且零浪費，這是買方願意加價的理由。
② 同生活圈最近的兩筆素地成交是 <b>28.05 萬/坪（福利段 316）</b>與 <b>30.92 萬/坪（自治段 376）</b>，價格基礎紮實，不必賤賣。
③ 開價 3,950 萬、心裡守 3,100 萬；若買方是自住自建、願意快速付款，<b>3,300 萬以上即可成交</b>。
④ 上架前<b>花 30 – 50 萬把地整乾淨</b>，是本案投報率最高的一筆錢 —— 買方看到雜草空地會殺價，看到方整素地會想像自己的房子。</div>

<h2>九、資料來源與免責</h2>
<ul style="font-size:14px;color:#555">
<li>地籍資料：內政部地籍圖資網路便民服務系統（easymap.moi.gov.tw），以地段代碼 9115（自治段）、9114（福利段）＋地號查得面積與 115 年度公告現值。</li>
<li>成交資料：內政部不動產交易實價查詢服務網，臺中市大肚區 112 年 Q1 – 115 年 Q2 買賣案件。</li>
<li>土地單價一律以「總價 ÷ 土地坪數」自行計算，未採用實登揭露之建物單價欄位。</li>
<li>已剔除備註載明親友／特殊關係、急買急賣、地清未辦繼承等非常規交易；政府標讓售案僅作地板參考，親友交易案僅作上緣參考，表列時均已註明。</li>
<li>現況照片取自 Google 街景服務（拍攝日期 2024.10 及 2026.01），巷道寬度為影像目視估計，<b>正式數值應以都市計畫圖及建築線指定為準</b>。</li>
<li>公告現值、面積、分區資料引自地籍查詢系統（115 年公告現值及地價），實際以地政事務所謄本為準。</li>
<li>開發效益試算之營建單價、售價與利潤率為經驗值假設，實際因設計、時點與融資條件而異。</li>
<li>本報告為<b>行情研判與委託前參考</b>，非不動產估價師法所定之估價報告書，不作為課稅、融資或訴訟依據。</li>
<li>尚待確認事項：建築線指定、退縮規定、地上有無占用或地役權、三筆土地之所有權人是否一致。</li>
</ul>

</main></div>

<footer><div class="inner">
<span>瑞禾開發｜建築、房產整合團隊</span>
<span>張現傑</span>
<span>製表日期：2026.09.22（第 3 版・含地籍查證）</span>
</div></footer>
</body></html>"""

html = (BODY.replace("__CSS__", CSS)
            .replace("__DIAGRAM__", DIAGRAM)
            .replace("__LOGO__", LOGO)
            .replace("__IMG__", IMG)
            .replace("__SV1__", SV1)
            .replace("__SV2__", SV2)
            .replace("__SV3__", SV3)
            .replace("__LAND__", LAND)
            .replace("__HOUSE__", HOUSE))

with open('大肚自治段367-369土地估價報告.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('done', len(html))
