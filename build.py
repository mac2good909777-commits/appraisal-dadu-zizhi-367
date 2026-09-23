# -*- coding: utf-8 -*-
from _assets import LOGO, IMG
from _sv import SV1, SV2, SV3

# (成交, 地段地號, 土地坪, 總價萬, 單價, 直線距離m, 緯度, 經度, 備註, 權重)
# 已剔除 25 坪以下案件；依與本案之直線距離由近而遠排序
rows_land = [
 ("—","自治段 367・368・369（本案）","123.5","—","—",0,24.153926,120.545323,"評估標的","self"),
 ("113.07","自治段 376","238.1","7,359","30.92",48,24.153656,120.545696,"同街廓、大面積整批；含公設保留地，可建部分單價更高","key"),
 ("113.08","福利段 316","34.3","961","28.05",181,24.152972,120.543881,"同生活圈巷內素地，常規交易","key"),
 ("113.03","自治段 189-2","29.5","673","22.79",364,24.156280,120.547813,"政府標讓售，價格地板","sub"),
 ("113.03","大東段 754","29.7","1,130","38.10",909,24.145909,120.547052,"含未登記建物、臨街精華地，屬天花板","sub"),
 ("114.03","福山段 1249","55.8","1,605","28.77",3981,24.123249,120.565544,"距本案近 4 公里，另一生活圈，僅供對照","far"),
 ("115.04","福利段 741","33.5","1,300","38.75",None,None,None,"親友交易；現行地籍查無此號，推測成交後已分割合併","na"),
 ("113.03","福德段 837","51.2","2,000","39.04",None,None,None,"含未登記建物；現行地籍查無此號，推測成交後已分割合併","na"),
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
    d, seg, p, total, unit, dist, lat, lon, note, kind = r
    cls = {'key': ' class="hl"', 'self': ' class="self"', 'na': ' class="na"'}.get(kind, '')
    if kind == 'self':
        dtxt = '<b>標的</b>'
    elif dist is None:
        dtxt = '<span class="muted">無法定位</span>'
    elif dist >= 1000:
        dtxt = '<b>%.1f km</b>' % (dist / 1000.0)
    else:
        dtxt = '<b>%d m</b>' % dist
    if lat is None:
        sv = '<span class="muted">—</span>'
    else:
        sv = ('<a class="sv-link" target="_blank" rel="noopener" '
              'href="https://www.google.com/maps?q&amp;layer=c&amp;cbll=%.6f,%.6f">街景</a>'
              ' · <a class="sv-link" target="_blank" rel="noopener" '
              'href="https://www.google.com/maps/search/?api=1&amp;query=%.6f,%.6f">地圖</a>'
              % (lat, lon, lat, lon))
    return ('<tr%s><td>%s</td><td>%s</td><td class="n">%s</td><td class="n">%s</td>'
            '<td class="n b">%s</td><td class="n">%s</td><td class="c">%s</td>'
            '<td class="note">%s</td></tr>'
            % (cls, d, seg, p, total, unit, dtxt, sv, note))


def tr_house(r):
    d, addr, yr, lp, bp, total, gross, res, net, kind = r
    cls = ' class="hl"' if kind == "key" else ''
    return ('<tr%s><td>%s</td><td>%s</td><td class="n">%s</td><td class="n">%s</td>'
            '<td class="n">%s</td><td class="n">%s</td><td class="n">%s</td>'
            '<td class="n">%s</td><td class="n b">%s</td></tr>'
            % (cls, d, addr, yr, lp, bp, total, gross, res, net))



def site_blocks():
    """為每筆可定位的地號產生『空照 + 可環視街景』對照區塊。"""
    out = []
    for r in rows_land:
        d, seg, p_, total, unit, dist, lat, lon, note, kind = r
        if lat is None:
            continue
        if kind == 'self':
            badge = '<span class="badge self-b">評估標的</span>'
            meta = '%s 坪' % p_
        else:
            badge = '<span class="badge">%s</span>' % (
                ('%.1f km' % (dist / 1000.0)) if dist >= 1000 else ('%d m' % dist))
            meta = '%s 坪 ｜ 成交 %s ｜ <b>%s 萬/坪</b>' % (p_, d, unit)
        sat = ('https://maps.google.com/maps?q=%.6f,%.6f&amp;t=k&amp;z=19&amp;output=embed'
               % (lat, lon))
        sv = ('https://maps.google.com/maps?q=%.6f,%.6f&amp;layer=c&amp;cbll=%.6f,%.6f'
              '&amp;cbp=11,0,0,0,0&amp;output=svembed' % (lat, lon, lat, lon))
        dirs = ' '.join(
            '<a class="dir" target="_blank" rel="noopener" '
            'href="https://www.google.com/maps?q&amp;layer=c&amp;cbll=%.6f,%.6f&amp;cbp=11,%d,0,0,0">%s</a>'
            % (lat, lon, h, nm)
            for h, nm in [(0, '朝北'), (90, '朝東'), (180, '朝南'), (270, '朝西')])
        out.append(
            '<div class="site">'
            '<div class="site-h">%s<span class="site-t">%s</span>'
            '<span class="site-m">%s</span></div>'
            '<div class="site-b">'
            '<figure><iframe loading="lazy" src="%s"></iframe>'
            '<figcaption>空照圖（衛星，可縮放）</figcaption></figure>'
            '<figure><iframe loading="lazy" src="%s"></iframe>'
            '<figcaption>街景（<b>可直接拖曳環視四周</b>）</figcaption></figure>'
            '</div>'
            '<div class="site-f">四向街景另開：%s　<span class="note">%s</span></div>'
            '</div>' % (badge, seg, meta, sat, sv, dirs, note))
    return ''.join(out)


SITES = site_blocks()

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
.c{text-align:center;white-space:nowrap}
tr.self{background:#FFF8E1 !important}
tr.self td{border-bottom:2px solid var(--gold);font-weight:600}
tr.na td{color:#999}
.muted{color:#aaa}
.sv-link{color:var(--g);text-decoration:none;border-bottom:1px solid #C6DCB8;font-size:13px}
.sv-link:hover{color:var(--f);border-bottom-color:var(--f)}
.site{border:1px solid var(--bd);margin:16px 0;background:#fff}
.site-h{background:#F8F8F5;border-bottom:1px solid var(--bd);padding:11px 16px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.site-t{font-weight:700;color:var(--f);font-size:16px}
.site-m{font-size:13.5px;color:#666;margin-left:auto}
.badge{background:var(--g);color:#fff;font-size:12.5px;font-weight:600;padding:2px 9px;border-radius:2px;font-family:Inter,sans-serif}
.badge.self-b{background:var(--gold)}
.site-b{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:12px}
.site-b figure{margin:0}
.site-b iframe{width:100%;height:280px;border:1px solid var(--bd);display:block;background:#EEE}
.site-b figcaption{font-size:12.5px;color:#666;margin-top:6px}
.site-f{border-top:1px solid var(--bd);padding:9px 16px;font-size:13px;background:#FCFCFA}
.dir{display:inline-block;color:var(--g);text-decoration:none;border:1px solid #C6DCB8;border-radius:2px;padding:1px 9px;margin-right:4px;font-size:12.5px}
.dir:hover{background:var(--g);color:#fff;border-color:var(--g)}
@media(max-width:760px){.site-b{grid-template-columns:1fr}}
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
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:14px 0;position:relative}
.tw table{margin:0;min-width:560px}
@media(max-width:760px){.kpis{grid-template-columns:repeat(2,1fr)}.concl{grid-template-columns:1fr}.two,.sv{grid-template-columns:1fr}main{padding:20px 16px}header{padding:20px 16px}header .inner{flex-direction:column;align-items:flex-start;gap:14px}header h1{font-size:23px}body{font-size:16px}h2{font-size:20px}h3{font-size:16.5px}table{font-size:13.5px}th,td{padding:8px 9px}.site-b iframe{height:230px}.site-m{margin-left:0;width:100%}.concl .p{font-size:24px}.kpi .v{font-size:26px}.callout{padding:14px 15px;font-size:14px}ul{margin-left:18px}}
@media(max-width:760px){.tw::before{content:"← 表格可左右滑動 →";display:block;font-size:12px;color:#A09A90;text-align:right;margin-bottom:3px;letter-spacing:.5px}}
@media(max-width:420px){.kpis{grid-template-columns:1fr}.dir{margin-bottom:4px}}
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
<!-- Google tag (gtag.js) — GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H5VLHW8761"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-H5VLHW8761');
</script>
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

<p style="margin:0 0 18px;display:flex;gap:10px;flex-wrap:wrap"><a href="./explain.html" style="display:inline-block;background:#F5F3EE;border:1px solid #C0A434;border-radius:4px;padding:9px 16px;color:#2B5937;text-decoration:none;font-size:14.5px;font-weight:600">✉ 給地主的說明版 →</a><a href="./owner.html" style="display:inline-block;background:#F5F3EE;border:1px solid #C0A434;border-radius:4px;padding:9px 16px;color:#2B5937;text-decoration:none;font-size:14.5px;font-weight:600">📄 重點摘要版（大字）→</a></p>
<h2>一、標的概要</h2>
<div class="kpis">
<div class="kpi"><div class="lb">土地總面積<span class="note"> ・純建地</span></div><div class="v">123.5<span class="u"> 坪</span></div></div>
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

<h2>四、產權結構與稅負（謄本查證）</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">依 115.09.23 調閱之土地電傳資料整理。
基於個人資料保護，<b>僅列所有權人姓氏與戶籍所在縣市</b>，不揭露完整姓名、統一編號與詳細住址。</p>
<div class="tw"><table><thead><tr><th>地號</th><th class="n">登記面積(㎡)</th><th class="n">坪</th><th>所有權人</th><th>取得原因</th><th class="n">土增稅(一般)<br><span class="note" style="color:#dfe">適用</span></th><th class="n">土增稅(自宅)<br><span class="note" style="color:#dfe">本案不適用</span></th></tr></thead><tbody>
<tr><td>自治段 367</td><td class="n">132.57</td><td class="n">40.10</td><td>陳姓（臺中市）· 單獨所有</td><td class="note">68 年買賣</td><td class="n">49.7 萬</td><td class="n">19.8 萬</td></tr>
<tr><td>自治段 368</td><td class="n">135.56</td><td class="n">41.01</td><td>陳姓（臺中市）· 單獨所有<br><span class="note">與 367 為同一人</span></td><td class="note">68 年買賣</td><td class="n">50.8 萬</td><td class="n">20.2 萬</td></tr>
<tr><td>自治段 369</td><td class="n">140.14</td><td class="n">42.39</td><td><b>陳姓（臺中市）· 單獨所有</b><br><span class="note">與 367、368 <b>非同一人</b></span></td><td class="note">97 年配偶贈與</td><td class="n">52.5 萬</td><td class="n">20.9 萬</td></tr>
<tr class="self"><td><b>合計</b></td><td class="n"><b>408.27</b></td><td class="n"><b>123.50</b></td><td><b>分屬二位所有權人</b></td><td></td><td class="n"><b>152.9 萬</b></td><td class="n"><b>60.9 萬</b></td></tr>
</tbody></table></div>

<div class="callout warn"><b>⚠ 發現一：三筆土地並非同一人所有。</b>
367、368（合計 81.11 坪）屬同一所有權人；<b>369（42.39 坪）屬另一位所有權人</b>。
兩筆皆為單獨所有、無共有人，產權單純，但<b>整批出售必須兩位所有權人同時簽署委託與買賣契約</b>。
實務影響：① 委託書需兩份、兩人皆須到場或出具授權；② 任一方中途反悔即整案破局；
③ 買方調閱謄本時必然發現，事前未說明會影響信任。<b>建議簽委託前先確認兩位意向一致。</b></div>

<div class="callout warn"><b>⚠ 發現二：東側通路（福利路 117 巷）是私有土地，不是公有道路。</b>
該通路為<b>自治段 375 地號</b>，面積 594.11 ㎡（179.71 坪），長約 114.6 公尺，換算平均寬度 <b>5.18 公尺</b>
—— 與現場街景目測的 5–6 公尺完全吻合，可確認<b>巷道路身即為這筆私有土地</b>，<b>共有人 6 位</b>
（已調閱 2 位：陳姓〔臺中市〕持分 1/2、陳姓〔臺北市〕持分 1/4，其餘 1/4 由 4 人持有）。<br>
更需注意：375 的都市計畫分區登記為<b>「第三種住宅區」而非「道路用地」</b>，代表它在計畫上是建地，只是現況供通行使用。</div>

<h3>建築線認定：法規依據與退讓試算</h3>
<p>依<b>臺中市建築管理自治條例第 19 條</b>，現有巷道包含「經道路主管機關認定屬既成道路者」、
「經政府部門認定為已興闢、已納入維護管理之公眾通行道路者」，以及私設通路經土地所有權人出具
<b>經公證之供公眾通行同意書</b>或無償捐贈土地作為道路者等情形。
本巷已開闢數十年、兩側建物林立、具正式門牌並納入市政清運維護，<b>依第 1、2 款認定為現有巷道的機會高</b>。</p>
<div class="callout warn"><b>⚠ 但第 20 條的退讓規定對本案有實質影響。</b>
該條規定：面臨寬 2 公尺以上現有巷道之基地，若巷道<b>單向出口逾 40 公尺、或雙向出口逾 80 公尺</b>，
應「兩旁均等退讓，以合計達到<b>六公尺</b>寬度之邊界線作為建築線」。<br>
本巷長約 <b>114.6 公尺</b>，無論認定為單向或雙向出口<b>均已超過門檻</b>；而現況寬度僅 5.18 公尺，<b>未達 6 公尺</b>
—— 因此<b>本案很可能需要退讓後始得指定建築線</b>。
<div class="tw"><table style="margin-top:10px"><thead><tr><th>退讓情形</th><th class="n">退讓寬度</th><th class="n">損失面積</th><th>說明</th></tr></thead><tbody>
<tr class="hl"><td>兩旁均等退讓（條文原則）</td><td class="n">0.41 m</td><td class="n b">約 4.2 坪</td><td class="note">本案與對側各退一半，為最可能情形</td></tr>
<tr><td>單側退足（保守假設）</td><td class="n">0.82 m</td><td class="n b">約 8.5 坪</td><td class="note">若對側建物已無退讓空間，可能要求本案退足</td></tr>
</tbody></table></div>
<b>價值影響：</b>以 27 萬/坪計，退讓 4.2 坪約影響 <b>113 萬</b>、退讓 8.5 坪約影響 <b>230 萬</b>（約總價的 3% – 7%）。
退讓部分通常不得計入法定空地與容積基地面積，屬實質損失。<br>
<b>這是本案目前最需要花錢釐清的一件事。</b>指定建築線規費僅新臺幣 500 元（每增一條道路加收 100 元），
<b>建議立刻申請，用 500 元換一個確定答案</b> —— 結果會直接影響開價與買方信心。</div>

<h3>⚠ 自用住宅優惠稅率：本案確定不適用</h3>
<div class="callout warn"><b>結論先講：本案三筆均為素地、地上無建物，<u>無法適用</u>自用住宅優惠稅率，應以一般用地稅率計算，合計約 153 萬。</b>
先前表格所列之「自宅稅率 60.9 萬」僅為謄本系統的制式估算欄位，<b>本案不具適用資格，不得列入屋主淨得計算</b>。</div>
<p><b>法規依據：</b></p>
<ul style="font-size:14px">
<li><b>土地稅法第 9 條</b>：自用住宅用地，指土地所有權人或其配偶、直系親屬於該地<b>辦竣戶籍登記</b>，且無出租或供營業用之<b>住宅用地</b>。</li>
<li><b>土地稅法施行細則</b>進一步明定：自用住宅用地，<b>以其土地上之建築改良物屬土地所有權人或其配偶、直系親屬所有者為限</b>。</li>
<li>兩者合併解讀：<b>「有房屋」是前提，「設籍」是要件</b>。素地沒有建築改良物，自始不屬於「住宅用地」，
更無從辦理戶籍登記 —— <b>本案三筆謄本均載明無地上物，故不符合要件</b>。</li>
</ul>

<h3>釐清：「數筆土地合併申報」能不能讓素地一起適用？</h3>
<div class="callout"><b>不能。這是常見的誤解，說明如下：</b>
<ul style="margin-top:6px">
<li><b>確實有「合併視為一次」的規定</b>：同一土地所有權人出售<b>數筆自用住宅用地</b>，
若訂約日期相同、且於同一天申報移轉現值，可<b>視為一次出售</b>，
合計面積未超過都市土地 3 公畝（約 90.75 坪）部分，適用 10% 優惠稅率。</li>
<li><b>但這條規定解決的是「次數」問題，不是「資格」問題。</b>
其目的在於：避免所有權人一次賣掉房屋坐落的數筆土地時，被認定用掉好幾次「一生一次」的額度。
<b>前提是「這數筆土地各自都要是自用住宅用地」</b>。</li>
<li><b>因此，並非「其中一筆有設籍，其餘素地就能搭便車」。</b>
每一筆土地都必須各自符合「地上有自用住宅建物 ＋ 辦竣戶籍登記」的要件，
無建物的素地不會因為與有建物的土地同時申報而取得資格。</li>
<li><b>唯一可能的例外情形</b>是：房屋<b>跨坐落於數筆地號</b>，或相鄰地號確屬該房屋之法定空地／基地範圍，
此時該數筆可整體認定為房屋基地。<b>但本案三筆皆無任何地上物，不存在此種情形。</b></li>
</ul></div>
<p style="font-size:14px;color:#555"><b>對屋主的實務提醒：</b>若屋主名下另有自用住宅，
其「一生一次」或「一生一屋」的資格<b>並不會因本案出售而被使用掉</b>（因本案本來就按一般稅率課徵），
該額度仍可保留給日後出售真正的自用住宅時使用 —— 這點可主動告知，屬於正面訊息。</p>

<h3>屋主實拿試算（扣土地增值稅）</h3>
<p style="font-size:14px;color:#666;margin:0 0 4px">三筆前次移轉現值均為民國 68 年 11 月，持有逾 46 年。
下表<b>以一般用地稅率計算</b>（依上述，本案不適用自用住宅優惠稅率）。</p>
<div class="tw"><table><thead><tr><th class="n">每坪單價</th><th class="n">成交總價</th><th class="n">土地增值稅</th><th class="n">屋主實拿</th><th>備註</th></tr></thead><tbody><tr><td class="n b">22 萬</td><td class="n">2,717 萬</td><td class="n">－152.9 萬</td><td class="n b">2,564 萬</td><td class="note">快速變現之最低建議</td></tr><tr class="hl"><td class="n b">25 萬</td><td class="n">3,088 萬</td><td class="n">－152.9 萬</td><td class="n b">2,935 萬</td><td class="note"><b>合理成交帶</b></td></tr><tr class="hl"><td class="n b">26 萬</td><td class="n">3,211 萬</td><td class="n">－152.9 萬</td><td class="n b">3,058 萬</td><td class="note"><b>合理成交帶</b></td></tr><tr class="hl"><td class="n b">27 萬</td><td class="n">3,335 萬</td><td class="n">－152.9 萬</td><td class="n b">3,182 萬</td><td class="note"><b>合理成交帶</b></td></tr><tr class="hl"><td class="n b">28 萬</td><td class="n">3,458 萬</td><td class="n">－152.9 萬</td><td class="n b">3,305 萬</td><td class="note"><b>合理成交帶</b></td></tr><tr class="hl"><td class="n b">29 萬</td><td class="n">3,582 萬</td><td class="n">－152.9 萬</td><td class="n b">3,429 萬</td><td class="note"><b>合理成交帶</b></td></tr><tr><td class="n b">30 萬</td><td class="n">3,705 萬</td><td class="n">－152.9 萬</td><td class="n b">3,552 萬</td><td class="note">需條件極佳或買方特別需求</td></tr><tr class="self"><td class="n b">32 萬</td><td class="n">3,952 萬</td><td class="n">－152.9 萬</td><td class="n b">3,799 萬</td><td class="note">建議開價，預留議價空間</td></tr></tbody></table></div>
<div class="callout"><b>好消息：稅負相對輕。</b>雖然持有近 47 年，但公告現值自民國 68 年的 2,100 元/㎡ 僅漲至 115 年的 20,600 元/㎡（約 9.8 倍），
而土增稅係按公告現值計算、非按市價，<b>三筆合計約 153 萬，僅約成交總價的 4.5%</b>。
兩位所有權人按各自面積分擔：367＋368 約 100.4 萬、369 約 52.5 萬。
另需自行負擔仲介服務費與代書費，實際淨得應再扣除。</div>

<h3>稅額驗證：三方獨立核對</h3>
<p>土地增值稅為本次評估中<b>唯一涉及法定稅額的數字</b>，已用三種獨立來源交叉核對，結果完全一致：</p>
<div class="tw"><table><thead><tr><th>驗證來源</th><th class="n">367 一般稅率<br><span class="note" style="color:#dfe">本案適用</span></th><th class="n">367 自宅稅率<br><span class="note" style="color:#dfe">僅供對照</span></th><th>說明</th></tr></thead><tbody>
<tr><td>① 謄本電傳系統估算</td><td class="n">496,534</td><td class="n">197,621</td><td class="note">115.09.23 調閱之原始估算值</td></tr>
<tr><td>② 本報告獨立試算</td><td class="n">496,534</td><td class="n">197,621</td><td class="note">依土地稅法第 33 條公式自行計算</td></tr>
<tr class="hl"><td><b>③ 財政部稅務入口網官方試算</b></td><td class="n b">496,534</td><td class="n b">197,621</td><td class="note">etax.nat.gov.tw 線上試算工具實際輸入驗證</td></tr>
</tbody></table></div>
<div class="callout ok"><b>✓ 三方數值完全相同，無任何差異。</b>採用之計算參數如下：
<ul style="margin-top:6px">
<li><b>臺灣地區消費者物價總指數 271.10%</b>（民國 68 年 11 月為基期至 115 年）
—— 此數值係以三筆土地各自獨立反推，三者結果<b>完全一致</b>，並經官方試算工具驗證無誤。</li>
<li><b>漲價倍數 2.618 倍</b>（＞2 倍）→ 適用<b>第三級稅率</b>。</li>
<li><b>持有年限 47 年</b>（＞40 年）→ 減徵率 40%，累進差額係數 B＝0.18。</li>
<li>適用公式：<b>應徵稅額 ＝ a × 32% － b × 18%</b>
（a＝土地漲價總數額；b＝物價指數調整後之原地價總額）。</li>
<li>換算<b>單位稅負：一般稅率約 1.24 萬/坪、自用住宅稅率約 0.49 萬/坪</b>，可用於快速估算任何持分。</li>
</ul>
<span class="note">註：官方試算之「前次移轉年月」欄位經測試，68 年 11 月與 69 年 9 月結果相同，因兩者同屬「持有 40 年以上」級距，減徵率一致。
本試算僅供概算，<b>實際應納稅額仍以申報時稽徵機關核定之發單資料為準</b>。</span></div>

<h3>自治段 375（巷道）持分：務必一併計算</h3>
<div class="callout warn"><b>⚠ 若本案所有權人同時持有 375 地號持分，該持分應一併納入交易與稅負計算。</b>
理由有三：① 買方取得通行權才完整，<b>有持分等於解決通行疑慮</b>，是強力賣點；
② 若屋主保留持分不賣，日後仍是共有人，徒增困擾；
③ 該持分同樣需課徵土地增值稅，<b>不計入會低估屋主稅負、誤導淨得</b>。<br>
<b>目前資料缺口：</b>375 共 6 位所有權人，已調閱 2 位（持分 1/2、1/4），
<b>其餘 1/4 由 4 人持有，本案屋主之持分比例尚未查明</b>。建議調閱完整謄本或請屋主提供權狀確認。</div>
<h3>⚠ 關鍵查證結果：本案所有權人並未持有巷道（375）任何持分</h3>
<div class="callout warn"><b>經逐一比對所有權人資料，確認如下：</b>
<div class="tw"><table style="margin-top:10px"><thead><tr><th>對象</th><th>姓氏</th><th>戶籍縣市</th><th class="n">375 持分</th></tr></thead><tbody>
<tr><td>375 登記次序 0001</td><td>陳姓</td><td>臺中市（大肚區）</td><td class="n">1/2</td></tr>
<tr><td>375 登記次序 0009</td><td>陳姓</td><td>臺北市</td><td class="n">1/4</td></tr>
<tr><td>375 其餘 4 位共有人</td><td><b>非陳姓</b></td><td class="note">—</td><td class="n">合計 1/4</td></tr>
<tr class="self"><td><b>本案 367・368 所有權人</b></td><td>陳姓</td><td>臺中市（北區）</td><td class="n b">無持分</td></tr>
<tr class="self"><td><b>本案 369 所有權人</b></td><td>陳姓</td><td>臺中市（西屯區）</td><td class="n b">無持分</td></tr>
</tbody></table></div>
已調閱之 2 位雖同為陳姓，但<b>統一編號與戶籍地均與本案所有權人不同，確非同一人</b>；
其餘 4 位共有人經查非陳姓。<b>結論：本案三筆土地的所有權人，對門前巷道不具任何持分。</b></div>

<div class="callout"><b>這件事帶來一好一壞兩個結果：</b>
<ul style="margin-top:6px">
<li><b>好的一面 —— 計價單純化。</b>本案交易標的就是<b>純建地 123.50 坪</b>，
不存在巷道持分的分段計價問題，總坪數即建地坪數，
也<b>不會產生巷道持分的土地增值稅</b>。先前的分段計價試算於本案<b>不適用</b>（保留於下方僅供日後類案參考）。</li>
<li><b>壞的一面 —— 通行權沒有產權保障。</b>買方取得土地後，
通行必須依賴該巷「現有巷道」的公用地役關係，<b>而非自身持分</b>。
這是買方必定會提出的疑慮，也是議價的施力點。</li>
</ul></div>

<h3>關鍵釐清：什麼情況需要所有權人同意書？</h3>
<div class="callout"><b>「私設巷道指定建築線要所有權人同意」這個認知<u>只對了一半</u>。</b>
依<b>臺中市建築管理自治條例第 19 條</b>，現有巷道之認定共有六款，
<b>其中只有第 6 款需要土地所有權人出具同意書，第 1 至 5 款均不需要</b>：</p>
<div class="tw"><table style="margin-top:10px"><thead><tr><th class="c">款次</th><th>認定事由</th><th class="c">需同意書</th><th>本案適用性</th></tr></thead><tbody>
<tr class="hl"><td class="c"><b>1</b></td><td>經道路主管機關認定屬<b>既成道路</b>者</td><td class="c b">否</td><td class="note"><b>有機會</b> — 開闢逾 40 年、已達公用地役關係要件</td></tr>
<tr class="hl"><td class="c"><b>2</b></td><td>經政府部門認定為已興闢、<b>已納入維護或管理</b>之公眾通行市區道路者</td><td class="c b">否</td><td class="note"><b>有機會</b> — 已鋪柏油、劃標線、設排水溝、編訂門牌</td></tr>
<tr><td class="c">3</td><td>私人自行闢設之通路，申請人無法舉證時，<b>製作路網圖公告 30 日無人異議</b>者</td><td class="c b">否</td><td class="note">備援路徑 — 但須賭共有人不提異議</td></tr>
<tr class="hl"><td class="c"><b>4</b></td><td><b>曾指定建築線且已核准建築完成</b>之巷道、備案道路者</td><td class="c b">否</td><td class="note"><b>最可能 — 見下方說明</b></td></tr>
<tr><td class="c">5</td><td>農地重劃道路現況為道路且供公眾通行者</td><td class="c b">否</td><td class="note">不適用</td></tr>
<tr class="na"><td class="c">6</td><td>土地重劃、區段徵收闢建之道路，<b>或土地所有權人出具經公證之供公眾通行同意書</b>、捐贈土地者</td><td class="c b" style="color:#C0533A">是</td><td class="note"><b>這才是您擔心的情形</b> — 本案應無須走此款</td></tr>
</tbody></table></div></div>

<div class="callout ok"><b>✓ 本案最強的論點在第 4 款：兩側房屋已合法建築完成。</b>
福利路 117 巷、118 巷兩側建物林立，實價登錄可查得多筆房地交易，
<b>屋齡自民國 69 年至 103 年不等，全部領有正式門牌、屬合法建築</b>。<br>
<b>關鍵推論：這些房屋當年要取得建造執照，必須先指定建築線；
而它們能指定到建築線，唯一的可能就是這條巷道已被認定為現有巷道。</b>
換言之，<b>此巷「曾指定建築線且已核准建築完成」幾乎是可確認的事實</b>，正好落在第 4 款。<br>
而第 4 款<b>不需要任何所有權人同意</b>。</div>

<div class="callout ok"><b>✓ 第二道防線：既成道路之公用地役關係（司法院釋字第 400 號）。</b>
依該號解釋，既成道路成立公用地役關係需具備三要件，本案逐項檢視：
<div class="tw"><table style="margin-top:10px"><thead><tr><th>要件</th><th>本案情形</th><th class="c">符合</th></tr></thead><tbody>
<tr><td>為<b>不特定公眾通行所必要</b>，非僅圖便利或省時</td><td class="note">該巷為 117 巷各戶對外之<b>唯一通路</b>，無替代路徑</td><td class="c b">✓</td></tr>
<tr><td>公眾通行之初，<b>土地所有權人未加阻止</b></td><td class="note">自民國 68 年分割留設後即供通行，<b>逾 40 年未見阻止</b></td><td class="c b">✓</td></tr>
<tr><td><b>年代久遠未曾中斷</b>，一般人已無從記憶其起始</td><td class="note">開闢逾 40 年，兩側房屋最早為民國 69 年即已存在</td><td class="c b">✓</td></tr>
</tbody></table></div>
<b>三要件均具備。</b>一旦成立公用地役關係，土地所有權人<b>已無從自由使用收益、亦不得阻止通行</b>，
此時循第 1 款「既成道路」認定，同樣不需同意書。</div>

<h3>風險情境與價值影響</h3>
<div class="tw"><table><thead><tr><th>情境</th><th>認定結果</th><th class="c">研判機率</th><th class="n">對價值影響</th></tr></thead><tbody>
<tr class="hl"><td><b>A（最可能）</b></td><td>循第 4 款或第 1、2 款認定為現有巷道，<b>免同意書</b>；現況寬度獲准維持</td><td class="c b">高</td><td class="n b">無影響<br>維持 25–29 萬/坪</td></tr>
<tr class="hl"><td><b>B（次可能）</b></td><td>認定為現有巷道但<b>依第 20 條須退讓至 6 m</b></td><td class="c b">中</td><td class="n b">－4.2 ~ 8.5 坪<br>約 113–230 萬</td></tr>
<tr class="na"><td><b>C（最壞）</b></td><td>僅能循第 6 款，<b>須 6 位共有人出具經公證之同意書</b>而無法取得 → 不能指定建築線</td><td class="c b">低</td><td class="n b" style="color:#C0533A">重大減損<br>詳見下方</td></tr>
</tbody></table></div>
<div class="callout warn"><b>關於情境 C 的誠實說明：</b>
若真的落入此情境，土地將<b>無法申請建造執照</b>，價值不再以建地計算，
僅能以空地、停車場或農業使用評價，<b>市場價值可能僅剩建地價的三至五成</b>。
這是本案唯一的重大下行風險。<br>
<b>但研判機率低</b>，理由已如前述：兩側房屋皆已合法建築完成，此巷不可能從未被指定過建築線。
若當年能指定，現在沒有理由不能 —— 除非該巷曾發生廢道或改道，而現況顯然並未如此。</div>

<div class="callout ok"><b>✓ 查證順序建議（由低成本到高成本，不必一開始就簽委託）：</b>
<ol style="margin:8px 0 0 20px">
<li><b>先查鄰房建照紀錄（成本最低、最關鍵）。</b>向都發局申請查閱 117 巷既有房屋之<b>建造執照存根</b>，
確認當年<b>是否曾以此巷指定建築線</b>。只要查到一件，第 4 款即告成立，整個疑慮立即解除。</li>
<li><b>向都發局承辦窗口口頭諮詢。</b>攜地籍圖說明位置，詢問該巷是否已列入<b>既成道路圖資</b>或曾有指定紀錄。
此步驟免費，且通常當場就能得到方向性答覆。</li>
<li><b>正式申請指定建築線</b>（規費新臺幣 500 元，每增一條道路加收 100 元）。取得書面結果，
同時確定<b>是否需退讓、退讓幾公尺</b>。</li>
</ol>
<b>前兩步幾乎零成本，卻能解決本案最大的不確定性。建議在與屋主洽談委託的同時並行進行。</b></div>

<div class="callout warn"><b>⚠ 對開價時機的建議：在取得建築線指定結果前，不宜正式對外開價。</b>
理由不是保守，而是這張書面有機會讓本案從「有疑慮的土地」變成「有官方背書的土地」——
兩者在買方心中的價差，遠超過 500 元規費與數週等待。
若貿然開價後才發現須退讓，屆時再調降價格，將嚴重損害案件信譽與屋主信任。</div>

<h3>附：巷道持分計價原則（本案不適用，供日後類案參考）</h3>
<div class="callout"><b>若標的含私設道路持分，計價原則如下：</b>
<ul style="margin-top:6px">
<li><b>總面積包含私設道路持分</b>，銷售文件的總坪數應含巷道持分，這才是完整的交易標的。</li>
<li><b>但單價必須分段計算</b>：道路持分供公眾通行、不可建築，市場計價僅為建地單價的 <b>20% – 30%</b>。</li>
<li><b>對外呈現總坪數、議價時分段討論</b>；巷道持分可作為最後讓步籌碼，保住建地單價不破底。</li>
</ul></div>

<h2>五、估價結論</h2>
<div class="concl">
<div><div class="t">屋主底線（快速變現）</div><div class="p">22 萬/坪</div><div class="s">總價約 2,720 萬</div></div>
<div class="mid"><div class="t">合理成交帶</div><div class="p">25 – 29 萬/坪</div><div class="s">總價約 3,090 – 3,580 萬</div></div>
<div><div class="t">建議開價</div><div class="p">32 萬/坪</div><div class="s">總價約 3,950 萬</div></div>
</div>

<div class="callout"><b>※ 計價基礎：本案交易標的為<u>純建地 123.50 坪</u>。</b>
經查證，所有權人未持有門前巷道（自治段 375）任何持分，
故<b>無巷道持分之計價與稅負問題，總坪數即建地坪數</b>。
惟通行權須依賴現有巷道認定，相關風險與應對見第四章。</div>

<div class="callout"><b>一句話結論：</b>以 <b>3,950 萬（32 萬/坪）開價</b>，守住 <b>3,100 萬（25 萬/坪）</b>，
成交落點合理推估在 <b>3,100 – 3,500 萬</b>。
較初版（開價 3,700 萬、合理帶 23 – 27 萬）<b>上修約 8%</b>，理由是現勘確認了三件事：
臨路為已開闢可通行巷道而非未開闢小徑、基地為全段臨路的街屋型地形、
以及新增福利路生活圈兩組更貼近的比較資料。</div>

<h2>六、比較法：同區土地成交</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">資料來源：內政部實價登錄，大肚區「土地」類交易。單價＝總價 ÷ 土地坪數（自算，不採公告單價）。
<b>已剔除 25 坪以下之畸零小地號</b>（該類多為補足或畸零地交易，單價失真、不具比較性）；
各案地號經內政部地籍圖資系統逐筆定位，<b>依與本案之直線距離由近而遠排序</b>，綠底為主要比較案。</p>
<div class="tw"><table><thead><tr><th>成交</th><th>地段地號</th><th class="n">土地坪</th><th class="n">總價(萬)</th><th class="n">單價(萬/坪)</th><th class="n">直線距離</th><th class="c">現況</th><th>備註</th></tr></thead>
<tbody>__LAND__</tbody></table></div>

<div class="callout"><b>比較案判讀（依距離）：</b>
<ul style="margin-top:6px">
<li><b>自治段 376 — 僅 48 公尺（30.92 萬/坪）</b>：距離最近、同段、面積 238 坪整批成交。
但<b>距離近不等於條件相同</b> —— 本案與其在臨路、時點與基地條件上均有明顯落差，
<b>不宜直接套用其單價</b>，詳見下方「與自治段 376 的差異分析」專節。</li>
<li><b>福利段 316 — 181 公尺（28.05 萬/坪）</b>：步行 2 分鐘距離的巷內素地，常規交易，坪數（34.3 坪）與本案單筆地號相當，且<b>公告現值與本案僅差 0.5%</b>。這是最貼近本案條件的一筆。</li>
<li><b>自治段 189-2 — 364 公尺（22.79 萬/坪）</b>：政府標讓售之小坪數畸零地，性質特殊、單價偏低，作為<b>本區價格地板</b>參考。</li>
<li><b>大東段 754 — 909 公尺（38.10 萬/坪）</b>：含未登記建物之臨街精華地，性質與素地不同，屬<b>天花板</b>，不宜逕行比附。</li>
<li><b>福山段 1249 — 3.98 公里（28.77 萬/坪）</b>：<b>經定位後確認位於另一生活圈</b>（近王田、追分一帶），與本案區位條件不可直接類比。<b>本版已將其自主要比較案降為對照案</b>，不納入定價依據。</li>
<li><b>福利段 741、福德段 837</b>：兩者單價雖高（38.75 / 39.04 萬），但<b>現行地籍已查無此地號</b>，推測成交後即辦理分割或合併改建；加上前者為親友交易、後者含未登記建物，皆不列入定價依據。</li>
</ul>
<b>小結：</b>距離 1 公里內、性質為素地的常規交易只有兩筆 —— 48 公尺的 30.92 萬與 181 公尺的 28.05 萬。
其中 376 因條件較優須向下調整（見下節），<b>真正可直接對標的是 181 公尺、28.05 萬的福利段 316</b>；
本案再計入大面積折讓與建築線退讓風險，合理成交帶訂在 <b>25 – 29 萬/坪</b>、開價 32 萬。</div>

<h3>與自治段 376 的差異分析（談判關鍵）</h3>
<div class="callout warn"><b>⚠ 此節請務必於與屋主溝通前詳讀。</b>
自治段 376 距本案僅 48 公尺、同屬自治段，<b>且據了解該案亦為同一方出售</b>。
屋主極可能以「我旁邊那塊賣 30.92 萬，這塊也要這個價」為定錨。
但兩案在三個面向上存在實質落差，<b>直接套用會導致開價過高、案件滯銷</b>：</div>
<div class="tw"><table><thead><tr><th>比較項目</th><th>自治段 376</th><th>本案 367・368・369</th><th>對單價的影響</th></tr></thead><tbody>
<tr class="hl"><td><b>臨路條件</b></td><td>依地籍圖判讀<b>臨南側較寬計畫道路</b>，路權明確</td><td>臨 <b>5.18 m 私設巷道</b>（自治段 375，6 人共有），<b>且可能需退讓至 6 m</b></td><td class="b">▼ 顯著不利</td></tr>
<tr class="hl"><td><b>成交時點</b></td><td>113 年 7 月</td><td>評估基準 115 年 9 月（<b>相隔 2 年 2 個月</b>）</td><td class="b">▼ 不利</td></tr>
<tr><td><b>基地規模</b></td><td>238.1 坪，總價 7,359 萬</td><td>123.5 坪，總價約 3,300 萬</td><td>△ 總價門檻低，<b>對本案有利</b></td></tr>
<tr><td><b>基地形狀</b></td><td>大面積完整街廓</td><td>面寬 34 m × 深 11.9 m，<b>深度偏淺</b></td><td>◯ 可切 4 戶，規劃效率佳但戶型受限</td></tr>
<tr><td><b>交易性質</b></td><td>含公共設施保留地用地</td><td>純建地、無公設保留地</td><td>△ 本案<b>單純度較高</b></td></tr>
</tbody></table></div>
<div class="callout"><b>建議對屋主的說法（三句話）：</b><br>
① <b>「376 那塊的路，跟這塊的路不一樣。」</b>376 臨的是有路權的計畫道路，本案臨的是 6 位共有人的私設巷道，
而且依臺中市建管自治條例，巷長 114 公尺、寬度不足 6 公尺，很可能還要退讓 —— <b>這是買方一定會拿來砍價的點</b>。<br>
② <b>「時間差了兩年多。」</b>113 年 7 月是土地交易相對熱絡的時點；114 年以降土地融資與建商購地貸款明顯趨緊，
小型建商出價轉趨保守，這點在本報告第九節的開發效益反推中已反映（建商出價天花板約 26 萬/坪）。<br>
③ <b>「但這塊有 376 沒有的優點。」</b>總價只要 3,300 萬左右、門檻低一半以上，買方層從建商擴大到自建自用家庭；
而且是純建地、沒有公設保留地，產權單純。<b>這些優點能撐住 25–29 萬，但撐不到 30.92 萬。</b><br><br>
<b>實務建議：</b>開價 32 萬/坪保留議價空間，讓屋主心理上「比 376 只低一點」；
但內部要有共識，<b>成交落在 25–29 萬即屬合理</b>。若堅持 30.92 萬以上，依目前條件預估將面臨長期滯銷。</div>

<h3>比較案效力驗證：公告現值交叉比對</h3>
<p>「同生活圈」不應只憑段名相鄰推論。經內政部地籍圖資網路便民服務系統（115 年度公告現值）逐筆查證，
本案與主要比較案的<b>政府評定地價幾乎完全一致</b>：</p>
<div class="tw"><table><thead><tr><th>地號</th><th class="n">登記面積(㎡)</th><th class="n">登記面積(坪)</th><th class="n">公告現值(元/㎡)</th><th class="n">換算(萬/坪)</th><th>地政事務所</th></tr></thead><tbody>
<tr class="hl"><td><b>自治段 367（本案）</b></td><td class="n">132.57</td><td class="n">40.1</td><td class="n">20,600</td><td class="n b">6.81</td><td>龍井</td></tr>
<tr class="hl"><td><b>福利段 316（比較案）</b></td><td class="n">101.94</td><td class="n">30.8</td><td class="n">20,700</td><td class="n b">6.84</td><td>龍井</td></tr>
</tbody></table></div>
<div class="callout ok"><b>✓ 兩者公告現值差距僅 0.5%</b>，代表政府對這兩塊地的區位條件評定為<b>同一價格帶</b>。
這是比「段名相鄰」更客觀的佐證 —— <b>福利段 316 作為主要比較案的效力成立</b>，其 28.05 萬/坪的成交價可直接對標，無須再做區位調整。
（附帶驗證：本案登記面積 132.57 ㎡ 與屋主提供之地籍資料完全相符。）</div>
<p style="font-size:14px;color:#555"><b>兩案位置：</b>本案自治段 367 位於<b>沙田路一段街廓內</b>，鄰近彰化銀行大肚分行、台中商業銀行大肚分行與大肚國小，
屬大肚市區的金融與生活機能核心；福利段 316 位於育樂街一帶，同為大肚市區成熟住宅區。</p>

<h2>七、各案現場環境對照（空照・街景）</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">基地價值有很大一部分來自「周遭環境」——臨路寬窄、鄰房新舊、有無嫌惡設施、街廓完整度。
以下依距離順序，逐筆列出經地籍定位後的<b>空照圖與實景街景</b>，可直接在頁面上縮放與拖曳環視，親自比較各比較案與本案的環境差異。</p>
<div class="callout"><b>怎麼看：</b>左側空照看<b>街廓紋理與基地方正度</b>（屋頂密度高＝開發完整、留白多＝仍有素地）；
右側街景<b>用滑鼠拖曳即可轉一圈</b>，看臨路寬度、鄰房屋齡與巷弄整潔度。下方「四向街景」按鈕另開視窗，直接跳到朝北／東／南／西的固定視角。</p></div>
__SITES__

<h2>八、交叉驗證一：福利路巷內透天扣建物殘值反推地價</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">本次改採<b>同一生活圈、同為巷內</b>的透天成交反推，比初版採用的自治路店住段更貼近。建物殘值依屋齡估：10 年內 7 萬/坪、30 年 4 萬/坪、45 年以上 2.5 萬/坪。</p>
<div class="tw"><table><thead><tr><th>成交</th><th>門牌</th><th class="n">建成年</th><th class="n">地坪</th><th class="n">建坪</th><th class="n">總價(萬)</th><th class="n">含建物<br>地坪單價</th><th class="n">建物殘值<br>(萬/坪)</th><th class="n">反推地價<br>(萬/坪)</th></tr></thead>
<tbody>__HOUSE__</tbody></table></div>
<div class="callout">三筆 <b>103 年新透天（綠底）反推地價高度收斂在 33.3 – 36.8 萬/坪</b>，一致性極高，可信度佳。
老屋案（69 – 80 年）反推值偏高（44.8 – 53.7 萬），係因建物殘值難以精確認列，且福利路 127 號臨主要道路，僅供參考。
以 33 – 37 萬為「<b>單戶 30 坪級距、已開發完成</b>」的地價水準，本案為<b>整批素地</b>，需扣除開發風險與時間成本，
折讓 20 – 25% 後約 <b>25 – 29 萬/坪</b>，與比較法結論吻合。</div>

<h2>九、交叉驗證二：開發效益反推（買方付得起多少）</h2>
<div class="card">
<h3>情境：沿巷切分 4 戶街屋型透天（每戶地約 30.9 坪、建約 62 坪）</h3>
<div class="tw"><table><thead><tr><th>項目</th><th class="n">保守</th><th class="n">樂觀</th><th>依據</th></tr></thead><tbody>
<tr><td>單戶售價</td><td class="n">1,700 萬</td><td class="n">1,900 萬</td><td class="note">同巷 103 年透天實績：福利路 152 巷 9 號 1,420 萬（30.7 地/55.8 建）、150 巷 8 號 1,810 萬（36.8/65.6）；新成屋加計屋齡差</td></tr>
<tr><td>總銷</td><td class="n">6,800 萬</td><td class="n">7,600 萬</td><td class="note">4 戶</td></tr>
<tr><td>營建成本</td><td class="n">－3,224 萬</td><td class="n">－3,224 萬</td><td class="note">62 坪 × 13 萬/坪 × 4 戶（RC 四層含雜項、基礎）</td></tr>
<tr><td>整地・清運・雜項</td><td class="n">－50 萬</td><td class="n">－30 萬</td><td class="note">現況雜草、喬木與舊建物殘跡之清除（見第二節現況說明）</td></tr>
<tr><td>管銷・稅費・利潤</td><td class="n">－1,020 萬</td><td class="n">－1,140 萬</td><td class="note">約總銷 15%</td></tr>
<tr class="hl"><td><b>土地可負擔總額</b></td><td class="n b">2,506 萬</td><td class="n b">3,206 萬</td><td class="note">＝總銷 － 營建 － 整地 － 管銷利潤</td></tr>
<tr class="hl"><td><b>換算土地單價</b></td><td class="n b">20.3 萬/坪</td><td class="n b">26.0 萬/坪</td><td class="note">÷ 123.5 坪</td></tr>
</tbody></table></div>
<p style="font-size:14px;margin:10px 0 0">小型建商的出價天花板約在 <b>26 萬/坪</b>；<b>自建自用買方</b>（不計開發利潤與管銷）可再往上約 3 – 4 萬，
到 <b>29 – 30 萬/坪</b>仍屬合理。三法交會處即為 <b>25 – 29 萬/坪</b> 的合理成交帶。</p>
</div>

<h2>十、銷售策略建議</h2>
<div class="two">
<div class="card"><h3>方案 A：整批出售（建議）</h3>
<ul>
<li>開價 <b>3,950 萬</b>（123.50 坪 × 32 萬），議價空間預留 18 – 20%</li>
<li><b>通行權的說明方式（重要）：</b>買方必然詢問門前巷道權屬。
建議<b>主動、誠實說明</b>：巷道為他人共有之私有地，屋主無持分，
但該巷屬已開闢逾四十年之現有巷道、兩側房屋皆合法建築完成，通行無虞；
<b>並出示建築線指定結果作為佐證</b>。隱瞞或含糊帶過，一旦買方自行查出將全面失去信任。</li>
<li>目標買方：<b>在地小建商</b>（首選，因可切 4 戶、規模剛好）、自建自用家庭、鄰地整合者</li>
<li>賣點主打「<b>大肚市區稀有整排素地，面寬 34 米全段臨路，可規劃 4 戶</b>」</li>
<li>預估銷售期 <b>4 – 8 個月</b></li>
<li><b>前置作業（務必先做）：</b>① 取得兩位所有權人一致同意並簽妥委託；② 向都發局申請指定建築線，確認現有巷道認定無虞</li>
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
④ 上架前<b>花 30 – 50 萬把地整乾淨</b>，是本案投報率最高的一筆錢 —— 買方看到雜草空地會殺價，看到方整素地會想像自己的房子。<br>⑤ <b>兩件事要先處理好再開賣</b>：土地分屬兩位所有權人，兩人得意向一致；東側巷道是私有地，建築線要先向都發局問清楚。這兩點買方一查就知道，<b>主動說明是加分，被動被發現是扣分</b>。</div>

<h2>十一、資料來源與免責</h2>
<ul style="font-size:14px;color:#555">
<li>地籍資料與定位：內政部地籍圖資網路便民服務系統（easymap.moi.gov.tw，圖資版本 2026.08.21），以地段代碼＋地號逐筆查得面積、115 年度公告現值與宗地位置；座標由 EPSG:3857 轉 WGS84，直線距離以 Haversine 公式計算至宗地幾何中心，誤差約 ±10 公尺。</li>
<li>成交資料：內政部不動產交易實價查詢服務網，臺中市大肚區 112 年 Q1 – 115 年 Q2 買賣案件。</li>
<li>土地單價一律以「總價 ÷ 土地坪數」自行計算，未採用實登揭露之建物單價欄位。</li>
<li>已剔除備註載明親友／特殊關係、急買急賣、地清未辦繼承等非常規交易；政府標讓售案僅作地板參考，親友交易案僅作上緣參考，表列時均已註明。</li>
<li>現況照片取自 Google 街景服務（拍攝日期 2024.10 及 2026.01），巷道寬度為影像目視估計，<b>正式數值應以都市計畫圖及建築線指定為準</b>。</li>
<li>公告現值、面積、分區資料引自地籍查詢系統（115 年公告現值及地價），實際以地政事務所謄本為準。</li>
<li>開發效益試算之營建單價、售價與利潤率為經驗值假設，實際因設計、時點與融資條件而異。</li>
<li>自用住宅優惠稅率之適用，依土地稅法第 9 條、第 34 條及同法施行細則規定判斷；本案三筆均無地上建物，不符自用住宅用地要件，故一律按一般用地稅率計算。</li>
<li>土地增值稅：依土地稅法第 33 條公式計算，並經財政部稅務入口網（etax.nat.gov.tw）線上試算工具與謄本系統估算值三方核對一致；僅供概算，實際以稽徵機關核定發單為準。</li>
<li>建築線相關規定引自臺中市建築管理自治條例第 19、20 條；既成道路公用地役關係要件引自司法院釋字第 400 號解釋；退讓面積為依條文推算之預估值，實際應以都發局指定建築線結果為準。</li>
<li>本報告為<b>行情研判與委託前參考</b>，非不動產估價師法所定之估價報告書，不作為課稅、融資或訴訟依據。</li>
<li>尚待確認事項：建築線指定、退縮規定、地上有無占用或地役權、三筆土地之所有權人是否一致。</li>
</ul>

</main></div>

<footer><div class="inner">
<span>瑞禾開發｜建築、房產整合團隊</span>
<span>張現傑</span>
<span>製表日期：2026.09.22（第 14 版）</span>
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
            .replace("__SITES__", SITES)
            .replace("__HOUSE__", HOUSE))

with open('大肚自治段367-369土地估價報告.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('done', len(html))
