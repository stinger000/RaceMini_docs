import re
content = ""
with open("docs/index.md", "r", encoding='utf-8') as md_file:
    content = md_file.read()
with open("docs/index.md", "r", encoding='utf-8') as md_file:
    lines = md_file.readlines()
    print(lines)
    for line in lines:
        match = re.search(r'\(img\/(.*).jpg\)', line, re.M | re.I)
        if match:
            image_name = match.group(1)
            print(f"![_image](img/{image_name}.jpg)")
            content = content.replace(f"![_image](img/{image_name}.jpg)", f'<picture>\n \
    <source srcset="img/avif/{image_name}.avif" type="image/avif">\n \
    <img src="img/{image_name}.jpg" alt="_img" loading="lazy" />\n \
</picture>')

with open("docs/index.md", "w", encoding='utf-8') as new:
    new.write(content)
# for line in lines:
#     pattern = r'\!\[(.*)\]\(img\/(.*).jpg\)'
