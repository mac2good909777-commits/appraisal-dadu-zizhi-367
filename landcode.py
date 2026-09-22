# -*- coding: utf-8 -*-
"""
地號定位輔助工具 — 地段代碼查詢（NLSC 免費公開 API，免金鑰）

用法：
    python landcode.py 臺中市 大肚區            # 列出該區全部地段代碼
    python landcode.py 臺中市 大肚區 福利段      # 只查指定段，並輸出定位用連結
    python landcode.py 臺中市 大肚區 福利段 316  # 帶地號，輸出各圖台查詢指引

輸出的 sectcode 即 foundi、地籍圖資便民系統、謄本上使用的官方 4 碼地段代碼。
"""
import sys, io, subprocess, xml.etree.ElementTree as ET

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

API = "https://api.nlsc.gov.tw/other"


def get(url):
    """以 curl 取回 XML。

    NLSC 憑證缺 Subject Key Identifier，Python 3.13+ 的 ssl 會以
    CERTIFICATE_VERIFY_FAILED 拒絕連線，curl 則可正常驗證，故走 curl。
    """
    r = subprocess.run(
        ["curl", "-sS", "--max-time", "30", "-A", "Mozilla/5.0", url],
        capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("curl 失敗：%s" % r.stderr.decode('utf-8', 'replace').strip())
    return ET.fromstring(r.stdout)


def counties():
    root = get(f"{API}/ListCounty")
    return {i.findtext('countyname'): i.findtext('countycode') for i in root}


def towns(ccode):
    root = get(f"{API}/ListTown/{ccode}")
    return {i.findtext('townname'): i.findtext('towncode') for i in root}


def sections(ccode, tcode):
    root = get(f"{API}/ListLandSection/{ccode}/{tcode}")
    out = []
    for i in root:
        out.append((i.findtext('sectstr'), i.findtext('sectcode'), i.findtext('officestr')))
    return out


def fmt_landno(no):
    """316 → 0316-0000（官方 8 碼地號格式：母號 4 碼 + 子號 4 碼）"""
    no = str(no).strip()
    if '-' in no:
        m, s = no.split('-', 1)
    else:
        m, s = no, '0'
    return "%04d-%04d" % (int(m), int(s))


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return

    cname = a[0]
    cs = counties()
    if cname not in cs:
        print("找不到縣市：%s\n可用：%s" % (cname, '、'.join(cs)))
        return
    ccode = cs[cname]

    if len(a) == 1:
        for n, c in towns(ccode).items():
            print("%s\t%s" % (c, n))
        return

    tname = a[1]
    ts = towns(ccode)
    if tname not in ts:
        print("找不到鄉鎮市區：%s\n可用：%s" % (tname, '、'.join(ts)))
        return
    tcode = ts[tname]

    secs = sections(ccode, tcode)
    keyword = a[2] if len(a) > 2 else None
    hits = [s for s in secs if (keyword is None or keyword in s[0])]

    print("%s%s　縣市代碼 %s　鄉鎮代碼 %s" % (cname, tname, ccode, tcode))
    print("-" * 52)
    print("%-14s %-8s %s" % ("段名", "段代碼", "地政事務所"))
    for name, code, office in hits:
        print("%-14s %-8s %s" % (name, code, office))
    print("-" * 52)
    print("共 %d 段（全區 %d 段）" % (len(hits), len(secs)))

    if len(a) > 3 and len(hits) == 1:
        name, code, office = hits[0]
        no = fmt_landno(a[3])
        print()
        print("【定位標的】%s%s %s %s 地號" % (cname, tname, name, no))
        print()
        print("① 地籍圖資網路便民服務（免費・需人工輸入驗證碼）")
        print("   https://easymap.land.moi.gov.tw/R02/Index")
        print("   縣市=%s　鄉鎮=%s　段=%s（代碼 %s）　地號=%s" % (cname, tname, name, code, no))
        print()
        print("② foundi 房地快搜（已登入・土地查詢免費）")
        print("   搜尋字串：%s%s%s%s" % (cname, tname, name, no.replace('-0000', '')))
        print()
        print("③ 取得經緯度後開圖台／街景")
        print("   國土測繪圖資雲：https://maps.nlsc.gov.tw/go/{lon}/{lat}/19/EMAP-B/DMAPS")
        print("   Google 街景：https://www.google.com/maps?q&layer=c&cbll={lat},{lon}")


if __name__ == '__main__':
    main()
