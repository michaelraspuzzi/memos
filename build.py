#!/usr/bin/env python3
"""Build the HTML memos from the Markdown sources.

Each memo becomes a standalone, self-contained HTML page in plain document
style: Times New Roman, light mode, with a copy-for-agents button and a
Markdown download button at the top. Run: python3 build.py
"""

import base64
import html
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

MEMOS = [
    ("bachelors-degree", "The bachelor's degree"),
    ("harvard-hybrid-masters", "Harvard hybrid master's programs"),
    ("bouldering-grades", "Bouldering grades"),
    # Companies that closed
    ("cal-com", "Cal.com"),
    ("tldraw", "tldraw"),
    ("gemini-cli", "Google, Gemini CLI"),
    ("meta-llama", "Meta, Llama"),
    # Companies that stayed open
    ("clickhouse", "ClickHouse"),
    ("supabase", "Supabase"),
    ("n8n", "n8n"),
]

STYLE = """
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  html { background: #ffffff; }
  body {
    background: #ffffff;
    color: #111111;
    font-family: "Times New Roman", Times, serif;
    font-size: 18px;
    line-height: 1.55;
    margin: 0;
  }
  .page { max-width: 46em; margin: 0 auto; padding: 2rem 1.5rem 5rem; }

  .bar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    align-items: center;
    padding-bottom: 0.9rem;
    margin-bottom: 1.6rem;
    border-bottom: 1px solid #cccccc;
  }
  .bar .home {
    font-size: 0.85rem;
    margin-right: auto;
    color: #555555;
  }
  button.act {
    font-family: "Times New Roman", Times, serif;
    font-size: 0.85rem;
    background: #f4f4f2;
    color: #111111;
    border: 1px solid #999999;
    border-radius: 2px;
    padding: 0.32rem 0.8rem;
    cursor: pointer;
  }
  button.act:hover { background: #e8e8e4; }
  button.act:focus-visible { outline: 2px solid #7a1c14; outline-offset: 2px; }
  button.act.done { background: #e6efe6; border-color: #4a7a4a; }

  h1, h2, h3, h4 { font-weight: bold; margin: 0; }
  h1 { font-size: 2rem; line-height: 1.15; }
  h2 { font-size: 1.4rem; line-height: 1.2; margin-top: 2.4rem; padding-top: 0.9rem; border-top: 2px solid #111111; }
  h3 { font-size: 1.1rem; margin-top: 1.6rem; }
  p { margin: 0.75rem 0 0; }
  ul, ol { margin: 0.7rem 0 0; padding-left: 1.5rem; }
  li { margin-bottom: 0.4rem; }
  a { color: #111111; }
  a:hover { color: #7a1c14; }
  a:focus-visible { outline: 2px solid #7a1c14; outline-offset: 2px; }
  hr { border: 0; border-top: 1px solid #cccccc; margin: 2rem 0 0; }
  code {
    font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    font-size: 0.88em;
    background: #f4f4f2;
    padding: 0.05em 0.3em;
    border-radius: 2px;
  }
  pre {
    margin: 1rem 0 0;
    padding: 1rem;
    overflow-x: auto;
    background: #f4f4f2;
    border: 1px solid #cccccc;
    line-height: 1.45;
  }
  pre code { padding: 0; background: transparent; font-size: 0.78rem; }
  blockquote {
    margin: 1rem 0 0;
    padding: 0.1rem 0 0.1rem 1rem;
    border-left: 3px solid #999999;
  }
  blockquote p { margin-top: 0.4rem; }
  blockquote p:first-child { margin-top: 0; }
  blockquote em.attrib { font-style: normal; font-size: 0.85rem; color: #555555; }

  figure { margin: 1.35rem 0 0; }
  figure img { display: block; width: 100%; height: auto; border: 1px solid #cccccc; }
  figcaption { margin-top: 0.45rem; color: #555555; font-size: 0.82rem; line-height: 1.35; }

  .tablewrap { overflow-x: auto; margin-top: 1.1rem; border: 1px solid #cccccc; }
  table { border-collapse: collapse; width: 100%; min-width: 34em; font-size: 0.92rem; }
  th, td { text-align: left; padding: 0.5rem 0.7rem; border-bottom: 1px solid #cccccc; vertical-align: top; }
  thead th { background: #f4f4f2; border-bottom: 1px solid #111111; }
  tbody tr:last-child td { border-bottom: 0; }

  .foot { margin-top: 3rem; padding-top: 0.9rem; border-top: 3px double #111111; font-size: 0.85rem; color: #555555; }
"""

SCRIPT = r"""
  (function () {
    var src = document.getElementById('memo-src');
    var raw = '';
    try {
      var bin = atob((src.textContent || '').replace(/\s+/g, ''));
      var bytes = new Uint8Array(bin.length);
      for (var k = 0; k < bin.length; k++) { bytes[k] = bin.charCodeAt(k); }
      raw = new TextDecoder('utf-8').decode(bytes);
    } catch (e) { raw = ''; }
    var name = document.body.getAttribute('data-slug') + '.md';

    var copy = document.getElementById('btn-copy');
    copy.addEventListener('click', function () {
      var done = function () {
        copy.textContent = 'Copied';
        copy.classList.add('done');
        setTimeout(function () {
          copy.textContent = 'Copy for agents';
          copy.classList.remove('done');
        }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(raw).then(done, fallback);
      } else {
        fallback();
      }
      function fallback() {
        var ta = document.createElement('textarea');
        ta.value = raw;
        ta.setAttribute('readonly', '');
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); done(); } catch (e) { /* no-op */ }
        document.body.removeChild(ta);
      }
    });

    var dl = document.getElementById('btn-download');

    function flash(label) {
      var was = dl.textContent;
      dl.textContent = label;
      dl.classList.add('done');
      setTimeout(function () {
        dl.textContent = was;
        dl.classList.remove('done');
      }, 1600);
    }

    function blobSave() {
      var blob = new Blob([raw], { type: 'text/markdown;charset=utf-8' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = name;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
    }

    dl.addEventListener('click', function () {
      // On claude.ai the host mediates saves; on GitHub Pages a blob link works.
      if (window.claude && typeof window.claude.use === 'function') {
        window.claude.use('downloads').then(function (d) {
          if (!d) { blobSave(); return; }
          d.save({ filename: name, data: raw }).then(
            function () { flash('Saved'); },
            function (e) { if (!e || e.code !== 'declined') { blobSave(); } }
          );
        }, blobSave);
        return;
      }
      blobSave();
    });
  })();
"""


# ---------------------------------------------------------------- inline

def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    return text


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


# ---------------------------------------------------------------- convert

def convert(md):
    lines = md.split('\n')
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == '---':
            out.append('<hr>')
            i += 1
            continue

        # A source footer is rendered as the visual footer used by the memo pages.
        m = re.match(r'^<footer>(.*)</footer>$', stripped)
        if m:
            out.append('<div class="foot">%s</div>' % inline(m.group(1)))
            i += 1
            continue

        # fenced code block
        m = re.match(r'^```([A-Za-z0-9_-]*)$', stripped)
        if m:
            lang = m.group(1)
            i += 1
            code_lines = []
            while i < n and lines[i].strip() != '```':
                code_lines.append(lines[i])
                i += 1
            if i < n:
                i += 1
            cls = ' class="language-%s"' % html.escape(lang, quote=True) if lang else ''
            out.append('<pre><code%s>%s</code></pre>' %
                       (cls, html.escape('\n'.join(code_lines), quote=False)))
            continue

        m = re.match(r'^(#{1,4})\s+(.*)$', stripped)
        if m:
            level = len(m.group(1))
            out.append('<h%d>%s</h%d>' % (level, inline(m.group(2)), level))
            i += 1
            continue

        # image, optionally followed immediately by an italic caption
        m = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', stripped)
        if m:
            alt = html.escape(m.group(1), quote=True)
            src = html.escape(m.group(2), quote=True)
            caption = None
            if i + 1 < n:
                cm = re.match(r'^\*([^*].*)\*$', lines[i + 1].strip())
                if cm:
                    caption = inline(cm.group(1))
                    i += 1
            out.append('<figure><img src="%s" alt="%s">%s</figure>' %
                       (src, alt, '<figcaption>%s</figcaption>' % caption if caption else ''))
            i += 1
            continue

        # table
        if stripped.startswith('|') and i + 1 < n and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            head = cells(stripped)
            i += 2
            body = []
            while i < n and lines[i].strip().startswith('|'):
                body.append(cells(lines[i].strip()))
                i += 1
            out.append('<div class="tablewrap"><table><thead><tr>' +
                       ''.join('<th>%s</th>' % inline(c) for c in head) +
                       '</tr></thead><tbody>')
            for row in body:
                out.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in row) + '</tr>')
            out.append('</tbody></table></div>')
            continue

        # blockquote
        if stripped.startswith('>'):
            quoted = []
            while i < n and lines[i].strip().startswith('>'):
                quoted.append(re.sub(r'^\s*>\s?', '', lines[i]))
                i += 1
            out.append('<blockquote>')
            for q in quoted:
                q = q.strip()
                if not q:
                    continue
                if re.match(r'^\*[^*]+\*$', q):
                    out.append('<p><em class="attrib">%s</em></p>' % inline(q.strip('*')))
                else:
                    out.append('<p>%s</p>' % inline(q))
            out.append('</blockquote>')
            continue

        # ordered list
        if re.match(r'^\d+\.\s+', stripped):
            items = []
            while i < n and re.match(r'^\d+\.\s+', lines[i].strip()):
                items.append(re.sub(r'^\d+\.\s+', '', lines[i].strip()))
                i += 1
            out.append('<ol>' + ''.join('<li>%s</li>' % inline(t) for t in items) + '</ol>')
            continue

        # bullet list
        if re.match(r'^[-*]\s+', stripped):
            items = []
            while i < n and re.match(r'^[-*]\s+', lines[i].strip()):
                items.append(re.sub(r'^[-*]\s+', '', lines[i].strip()))
                i += 1
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(t) for t in items) + '</ul>')
            continue

        # paragraph
        para = [stripped]
        i += 1
        while i < n and lines[i].strip() and not re.match(r'^(#{1,4}\s|>|\||-\s|\*\s|\d+\.\s|```|---$)', lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        body = inline(' '.join(para))
        if body.startswith('<em>') and body.endswith('</em>') and 'Compiled' in body:
            out.append('<p class="foot">%s</p>' % body)
        else:
            out.append('<p>%s</p>' % body)

    return '\n'.join(out)


# ---------------------------------------------------------------- pages

def page(title, slug, body_html, raw_md, home_label, home_href):
    payload = base64.b64encode(raw_md.encode('utf-8')).decode('ascii')
    home = ('<span class="home"><a href="%s">%s</a></span>' % (home_href, home_label)
            if home_href else '<span class="home">%s</span>' % home_label)
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<style>%s</style>
</head>
<body data-slug="%s">
<div class="page">
  <div class="bar">
    %s
    <button class="act" id="btn-copy" type="button">Copy for agents</button>
    <button class="act" id="btn-download" type="button">Download .md</button>
  </div>
%s
</div>
<script type="text/plain" id="memo-src">%s</script>
<script>%s</script>
</body>
</html>
""" % (html.escape(title), STYLE, slug, home, body_html, payload, SCRIPT)


def main():
    for slug, name in MEMOS:
        md_path = os.path.join(ROOT, 'memos', slug + '.md')
        with open(md_path, encoding='utf-8') as f:
            raw = f.read()
        out = page('%s | Closing the Source' % name, slug, convert(raw), raw,
                   'Closing the Source', '../index.html')
        with open(os.path.join(ROOT, 'memos', slug + '.html'), 'w', encoding='utf-8') as f:
            f.write(out)
        print('built memos/%s.html' % slug)

    with open(os.path.join(ROOT, 'README.md'), encoding='utf-8') as f:
        raw = f.read()
    # The web index links straight to the HTML pages; the dual
    # "Markdown / Web" cell only makes sense on github.com.
    web = re.sub(
        r'\[Markdown\]\(memos/([a-z0-9.-]+)\.md\)\s*/\s*'
        r'\[Web\]\(https://[^)]+\)',
        r'[Open memo](memos/\1.html)', raw)
    web = re.sub(r'\(memos/([a-z0-9.-]+)\.md\)', r'(memos/\1.html)', web)
    out = page('Closing the Source', 'closing-the-source', convert(web), raw,
               'Seven memos on open source as a business decision', None)
    with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(out)
    print('built index.html')


if __name__ == '__main__':
    main()
