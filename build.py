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

<h2>四、產權結構與稅負（謄本查證）</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">依 115.09.23 調閱之土地電傳資料整理。<b>本節不揭露所有權人姓名、統一編號與住址</b>，僅呈現影響交易之結構性事實。</p>
<table><thead><tr><th>地號</th><th class="n">登記面積(㎡)</th><th class="n">坪</th><th>所有權</th><th class="n">土增稅(一般)</th><th class="n">土增稅(自宅)</th></tr></thead><tbody>
<tr><td>自治段 367</td><td class="n">132.57</td><td class="n">40.10</td><td>單獨所有（甲）</td><td class="n">49.7 萬</td><td class="n">19.8 萬</td></tr>
<tr><td>自治段 368</td><td class="n">135.56</td><td class="n">41.01</td><td>單獨所有（甲）</td><td class="n">50.8 萬</td><td class="n">20.2 萬</td></tr>
<tr><td>自治段 369</td><td class="n">140.14</td><td class="n">42.39</td><td><b>單獨所有（乙，另一人）</b></td><td class="n">52.5 萬</td><td class="n">20.9 萬</td></tr>
<tr class="self"><td><b>合計</b></td><td class="n"><b>408.27</b></td><td class="n"><b>123.50</b></td><td><b>分屬二位所有權人</b></td><td class="n"><b>152.9 萬</b></td><td class="n"><b>60.9 萬</b></td></tr>
</tbody></table>

<div class="callout warn"><b>⚠ 發現一：三筆土地並非同一人所有。</b>
367、368（合計 81.11 坪）屬同一所有權人；<b>369（42.39 坪）屬另一位所有權人</b>。
兩筆皆為單獨所有、無共有人，產權單純，但<b>整批出售必須兩位所有權人同時簽署委託與買賣契約</b>。
實務影響：① 委託書需兩份、兩人皆須到場或出具授權；② 任一方中途反悔即整案破局；
③ 買方調閱謄本時必然發現，事前未說明會影響信任。<b>建議簽委託前先確認兩位意向一致。</b></div>

<div class="callout warn"><b>⚠ 發現二：東側通路（福利路 117 巷）是私有土地，不是公有道路。</b>
該通路為<b>自治段 375 地號</b>，面積 594.11 ㎡（179.71 坪），長約 114.6 公尺，換算平均寬度 <b>5.18 公尺</b>
—— 與現場街景目測的 5–6 公尺完全吻合，可確認<b>巷道路身即為這筆私有土地</b>，且<b>共有人多達 6 位</b>。<br>
更需注意：375 的都市計畫分區登記為<b>「第三種住宅區」而非「道路用地」</b>，代表它在計畫上是建地，只是現況供通行使用。<br>
<b>影響：</b>本案建築線須依現有巷道相關規定認定，不能逕以計畫道路視之。
所幸該巷已開闢數十年、兩側建物林立、具正式門牌，<b>實務上認定為現有巷道的機會高</b>，風險屬中低。
<b>但務必於簽約前向臺中市都發局申請「指定建築線」取得書面確認</b> —— 這是本案唯一可能實質影響價值的法定風險。<br>
<b>另建議查明：</b>本案兩位所有權人是否同時持有 375 地號持分。若持有，出售時可一併處理通行權，對買方是強力加分；若未持有，須先確認通行無虞。</div>

<h3>屋主實拿試算（扣土地增值稅）</h3>
<p style="font-size:14px;color:#666;margin:0 0 4px">三筆前次移轉現值均為民國 68 年 11 月，持有逾 46 年。
下表以<b>一般用地稅率</b>（較保守）試算；若符合自用住宅用地要件稅額可降至 60.9 萬，惟素地通常難以適用，故以一般稅率為準。</p>
<table><thead><tr><th class="n">成交單價</th><th class="n">成交總價</th><th class="n">土增稅(一般)</th><th class="n">屋主淨得(未計服務費)</th></tr></thead><tbody>
<tr><td class="n">22 萬/坪（底線）</td><td class="n">2,717 萬</td><td class="n">－153 萬</td><td class="n b">2,564 萬</td></tr>
<tr class="hl"><td class="n">25 萬/坪</td><td class="n">3,088 萬</td><td class="n">－153 萬</td><td class="n b">2,935 萬</td></tr>
<tr class="hl"><td class="n">27 萬/坪</td><td class="n">3,334 萬</td><td class="n">－153 萬</td><td class="n b">3,182 萬</td></tr>
<tr class="hl"><td class="n">29 萬/坪</td><td class="n">3,582 萬</td><td class="n">－153 萬</td><td class="n b">3,429 萬</td></tr>
<tr><td class="n">32 萬/坪（開價）</td><td class="n">3,952 萬</td><td class="n">－153 萬</td><td class="n b">3,799 萬</td></tr>
</tbody></table>
<div class="callout"><b>好消息：稅負相對輕。</b>雖然持有近 47 年，但公告現值自民國 68 年的 2,100 元/㎡ 僅漲至 115 年的 20,600 元/㎡（約 9.8 倍），
而土增稅係按公告現值計算、非按市價，<b>三筆合計約 153 萬，僅約成交總價的 4.5%</b>。
兩位所有權人按各自面積分擔：甲（367＋368）約 100.4 萬、乙（369）約 52.5 萬。
另需自行負擔仲介服務費與代書費，實際淨得應再扣除。</div>

<h2>五、估價結論</h2>
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

<h2>六、比較法：同區土地成交</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">資料來源：內政部實價登錄，大肚區「土地」類交易。單價＝總價 ÷ 土地坪數（自算，不採公告單價）。
<b>已剔除 25 坪以下之畸零小地號</b>（該類多為補足或畸零地交易，單價失真、不具比較性）；
各案地號經內政部地籍圖資系統逐筆定位，<b>依與本案之直線距離由近而遠排序</b>，綠底為主要比較案。</p>
<table><thead><tr><th>成交</th><th>地段地號</th><th class="n">土地坪</th><th class="n">總價(萬)</th><th class="n">單價(萬/坪)</th><th class="n">直線距離</th><th class="c">現況</th><th>備註</th></tr></thead>
<tbody>__LAND__</tbody></table>

<div class="callout"><b>比較案判讀（依距離）：</b>
<ul style="margin-top:6px">
<li><b>自治段 376 — 僅 48 公尺（30.92 萬/坪）</b>：就在本案隔壁街廓，是<b>決定性的比較案</b>。238 坪大面積整批仍達 30.92 萬，且備註載明含公設保留地（道路地拉低平均），<b>純可建部分實際更高</b>。本案面積不到其一半、總價門檻更低，單價沒有低於此數的理由。</li>
<li><b>福利段 316 — 181 公尺（28.05 萬/坪）</b>：步行 2 分鐘距離的巷內素地，常規交易，坪數（34.3 坪）與本案單筆地號相當，且<b>公告現值與本案僅差 0.5%</b>。這是最貼近本案條件的一筆。</li>
<li><b>自治段 189-2 — 364 公尺（22.79 萬/坪）</b>：政府標讓售之小坪數畸零地，性質特殊、單價偏低，作為<b>本區價格地板</b>參考。</li>
<li><b>大東段 754 — 909 公尺（38.10 萬/坪）</b>：含未登記建物之臨街精華地，性質與素地不同，屬<b>天花板</b>，不宜逕行比附。</li>
<li><b>福山段 1249 — 3.98 公里（28.77 萬/坪）</b>：<b>經定位後確認位於另一生活圈</b>（近王田、追分一帶），與本案區位條件不可直接類比。<b>本版已將其自主要比較案降為對照案</b>，不納入定價依據。</li>
<li><b>福利段 741、福德段 837</b>：兩者單價雖高（38.75 / 39.04 萬），但<b>現行地籍已查無此地號</b>，推測成交後即辦理分割或合併改建；加上前者為親友交易、後者含未登記建物，皆不列入定價依據。</li>
</ul>
<b>小結：</b>距離 1 公里內、且性質為素地的常規交易，只有 <b>48 公尺的 30.92 萬</b>與 <b>181 公尺的 28.05 萬</b>兩筆 —— 兩者構成 <b>28 – 31 萬/坪</b>的核心區間。
本案 123.5 坪需計入大面積折讓，但全段臨路可切 4 戶的規劃優勢可抵銷大半，故合理成交帶訂在 <b>25 – 29 萬/坪</b>、開價 32 萬，於此有據。</div>

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

<h2>七、各案現場環境對照（空照・街景）</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">基地價值有很大一部分來自「周遭環境」——臨路寬窄、鄰房新舊、有無嫌惡設施、街廓完整度。
以下依距離順序，逐筆列出經地籍定位後的<b>空照圖與實景街景</b>，可直接在頁面上縮放與拖曳環視，親自比較各比較案與本案的環境差異。</p>
<div class="callout"><b>怎麼看：</b>左側空照看<b>街廓紋理與基地方正度</b>（屋頂密度高＝開發完整、留白多＝仍有素地）；
右側街景<b>用滑鼠拖曳即可轉一圈</b>，看臨路寬度、鄰房屋齡與巷弄整潔度。下方「四向街景」按鈕另開視窗，直接跳到朝北／東／南／西的固定視角。</p></div>
__SITES__

<h2>八、交叉驗證一：福利路巷內透天扣建物殘值反推地價</h2>
<p style="font-size:14px;color:#666;margin:0 0 4px">本次改採<b>同一生活圈、同為巷內</b>的透天成交反推，比初版採用的自治路店住段更貼近。建物殘值依屋齡估：10 年內 7 萬/坪、30 年 4 萬/坪、45 年以上 2.5 萬/坪。</p>
<table><thead><tr><th>成交</th><th>門牌</th><th class="n">建成年</th><th class="n">地坪</th><th class="n">建坪</th><th class="n">總價(萬)</th><th class="n">含建物<br>地坪單價</th><th class="n">建物殘值<br>(萬/坪)</th><th class="n">反推地價<br>(萬/坪)</th></tr></thead>
<tbody>__HOUSE__</tbody></table>
<div class="callout">三筆 <b>103 年新透天（綠底）反推地價高度收斂在 33.3 – 36.8 萬/坪</b>，一致性極高，可信度佳。
老屋案（69 – 80 年）反推值偏高（44.8 – 53.7 萬），係因建物殘值難以精確認列，且福利路 127 號臨主要道路，僅供參考。
以 33 – 37 萬為「<b>單戶 30 坪級距、已開發完成</b>」的地價水準，本案為<b>整批素地</b>，需扣除開發風險與時間成本，
折讓 20 – 25% 後約 <b>25 – 29 萬/坪</b>，與比較法結論吻合。</div>

<h2>九、交叉驗證二：開發效益反推（買方付得起多少）</h2>
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

<h2>十、銷售策略建議</h2>
<div class="two">
<div class="card"><h3>方案 A：整批出售（建議）</h3>
<ul>
<li>開價 <b>3,950 萬</b>（32 萬/坪），議價空間預留 18 – 20%</li>
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
<li>本報告為<b>行情研判與委託前參考</b>，非不動產估價師法所定之估價報告書，不作為課稅、融資或訴訟依據。</li>
<li>尚待確認事項：建築線指定、退縮規定、地上有無占用或地役權、三筆土地之所有權人是否一致。</li>
</ul>

</main></div>

<footer><div class="inner">
<span>瑞禾開發｜建築、房產整合團隊</span>
<span>張現傑</span>
<span>製表日期：2026.09.22（第 6 版・含產權查證）</span>
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
