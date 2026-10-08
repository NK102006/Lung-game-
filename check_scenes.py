import json, re

html_path = r'd:\Lung game\Spot the Lung Risk – World Lung Day.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'const S=(\[.*?\]);', html)
if m:
    data = json.loads(m.group(1))
    print('Scenes:')
    for i, s in enumerate(data):
        print(f"{i}: {s.get('name')}")
else:
    print('Could not find S array')

m_match = re.search(r'const M=[\"\'](data:image.*?|.*?)[\"\']', html)
if m_match:
    print('Found M (home image) of length: ' + str(len(m_match.group(1))))
else:
    print('Could not find M')
