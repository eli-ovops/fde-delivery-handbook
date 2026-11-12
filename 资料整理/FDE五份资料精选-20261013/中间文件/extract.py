from pathlib import Path
from pypdf import PdfReader
import hashlib,json,unicodedata

root=Path('/Volumes/EXTERNAL/FDE/资料整理/FDE五份资料精选-20261013')
names=['84页FDE从入门到精通(1).pdf','2026中国FDE人才招聘与职业能力报告.pdf','AI时代OPC发展实践报告-阿里云.pdf','FDE起步手册（书籍版）.pdf','135页前线部署工程师（FDE）从零入门指南.pdf']
manifest=[]
for i,name in enumerate(names,1):
    path=Path('/Users/USER/Downloads')/name
    reader=PdfReader(path)
    pages=[{'page':p+1,'text':unicodedata.normalize('NFKC',page.extract_text() or '')} for p,page in enumerate(reader.pages)]
    out=root/'提取原文'/f'D{i}.json'
    out.write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
    (out.with_suffix('.txt')).write_text('\n\n'.join(f'===== D{i} PDF页 {p["page"]} =====\n{p["text"]}' for p in pages),encoding='utf-8')
    item={'id':f'D{i}','source':str(path),'pages':len(pages),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'characters':sum(len(p['text']) for p in pages),'low_text_pages':[p['page'] for p in pages if len(p['text'].strip())<80],'extraction':'pypdf','pages_file':str(out)}
    manifest.append(item)
    print(json.dumps(item,ensure_ascii=False),flush=True)
(root/'读取覆盖.json').write_text(json.dumps({'documents':manifest,'intermediates':{'directory':str(root/'中间文件'),'created_for':'本次PDF文本提取与OCR核查','retention':'收尾核对，保留仍需复用的提取脚本与必要图表证据'}},ensure_ascii=False,indent=2),encoding='utf-8')
