import re
html_path = r'd:\Lung game\Spot the Lung Risk – World Lung Day.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'data:image/.*?[,\"\']', text)
for m in matches:
    print('Found data:image at', m.start(), 'length:', len(m.group(0)))
