# AdSense-readiness fixes: privacy disclosure, disclaimer heading, Excel pricing text.
import sys

EDITS = {
 'privacy.html': [
  ('<p class="policy-updated"><strong>Last updated:</strong> October 2026</p>',
   '<p class="policy-updated"><strong>Last updated:</strong> November 2026</p>', 1),
  ('<li>The pages themselves do not run advertising or analytics scripts. Whoever hosts the website may keep standard server logs, which we do not control.</li>',
   '<li>We do not run our own analytics scripts. Whoever hosts the website may keep standard server logs, which we do not control. Advertising on this site is described below.</li>', 1),
  ('<h2>Please be careful what you share</h2>',
   '<h2>Advertising</h2>\n<p>This website may show ads served by Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your earlier visits to this website or other websites.</p>\n<p>Google\u2019s use of advertising cookies lets it and its partners show ads based on your visits to this site and other sites on the internet. You can turn off personalised advertising in <a href="https://adssettings.google.com/" rel="noopener">Google Ads Settings</a>, and opt out of some third-party vendors\u2019 cookies for personalised advertising at <a href="https://www.aboutads.info/choices/" rel="noopener">www.aboutads.info/choices</a>.</p>\n<h2>Please be careful what you share</h2>', 1),
 ],
 'disclaimer.html': [
  ('>Dis<span class="text-gradient">claimer</span></h1>',
   '><span class="text-gradient">Disclaimer</span></h1>', 1),
 ],
}
ROW_PAGES = ['data-cleaning.html','data-formatting.html','excel-data-entry.html','excel-formulas.html','mis-report.html']
for p in ROW_PAGES:
    EDITS[p] = [
     ('<span class="service-range">5,000+ rows</span>',
      '<span class="service-range">5,001+ rows</span>', 1),
     ('<p>The Pro and Enterprise ranges both include 5,000 rows as listed. At that boundary, ask which package applies. Confirm the scope and price before placing an order.</p>',
      '<p>Pro covers files up to 5,000 rows; larger files are custom-priced under Enterprise. Confirm the scope and price before placing an order.</p>', 1),
     ('Enterprise is custom-priced for 5,000+ rows. At exactly 5,000 rows, confirm the applicable package because the listed ranges overlap.',
      'Enterprise is custom-priced for files above 5,000 rows. Confirm the scope and price before placing an order.', 1),
    ]
EDITS['pdf-to-excel.html'] = [
     ('<span class="service-range">25+ pages</span>',
      '<span class="service-range">26+ pages</span>', 1),
     ('<p>The Pro and Enterprise ranges both include 25 pages as listed. At exactly 25 pages, ask which package applies. Confirm scope, price and any delivery estimate before work starts.</p>',
      '<p>Pro covers files up to 25 pages; larger files are custom-priced under Enterprise. Confirm scope, price and any delivery estimate before work starts.</p>', 1),
     ('Enterprise is custom-priced for 25+ pages. At exactly 25 pages, confirm the applicable package because the listed ranges overlap.',
      'Enterprise is custom-priced for files above 25 pages. Confirm scope and price before work starts.', 1),
    ]

fail = False
for fn, subs in EDITS.items():
    try:
        s = open(fn, encoding='utf-8').read()
    except FileNotFoundError:
        print('MISSING FILE:', fn); fail = True; continue
    for old, new, n in subs:
        c = s.count(old)
        if c != n:
            print(f'COUNT MISMATCH {fn}: expected {n}, found {c} for {old[:60]!r}')
            fail = True
            continue
        s = s.replace(old, new)
    if not fail:
        open(fn, 'w', encoding='utf-8').write(s)
        print('OK', fn)
sys.exit(1 if fail else 0)
