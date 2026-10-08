import re, base64, json
html_path = r'd:\Lung game\Spot the Lung Risk – World Lung Day.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all base64 images that are not in the S array.
# The S array is the scenes. The home background is probably in CSS or somewhere.
matches = re.finditer(r'url\([\'\"]?(data:image.*?|.*?)[\'\"]?\)', text)
for m in matches:
    print('CSS url(...) found:', m.group(0)[:100])

matches = re.finditer(r'<img.*?src=[\'\"](data:image.*?|.*?)[\'\"]', text)
for m in matches:
    print('img tag found:', m.group(0)[:100])

matches = re.finditer(r'const [A-Z]=[\'\"](data:image/.*?|.*?)[\'\"]', text)
for m in matches:
    print('const variable found:', m.group(0)[:50])
