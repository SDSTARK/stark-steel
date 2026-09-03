# -*- coding: utf-8 -*-
"""Steel-industry terminology corrections for the new table translations.

Machine translation mangles: Spangle, Chromated, Hairline, etc.
- EXACT: full hand-crafted override for the most critical keys.
- REPLACE: per-language substring fixes applied to ALL keys (safe: only
  matches the wrong MT forms).
"""
import json, os, re

ROOT = r"C:/Users/Administrator/WorkBuddy/2026-08-12-16-19-26"
OUT_DIR = os.path.join(ROOT, "translations")
LANGS = ['zh', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ar', 'ja', 'ko',
         'vi', 'th', 'tr', 'id', 'hi']

# ---- Full hand-crafted overrides for critical keys ----
EXACT = {
    'p05R1C1': {  # Item
        'zh': '项目', 'es': 'Elemento', 'fr': 'Article', 'de': 'Position',
        'it': 'Voce', 'pt': 'Item', 'ru': 'Позиция', 'ar': 'البند',
        'ja': '項目', 'ko': '항목', 'vi': 'Mục', 'th': 'รายการ',
        'tr': 'Kalem', 'id': 'Item', 'hi': 'वस्तु',
    },
    'p05R11C1': {  # HL hairline
        'zh': 'HL（发丝纹）', 'es': 'HL (acabado satinado)',
        'fr': 'HL (finition satinée)', 'de': 'HL (Haarlinien-Finish)',
        'it': 'HL (finitura satinata)', 'pt': 'HL (acabamento escovado)',
        'ru': 'HL (волосяное покрытие)', 'ar': 'HL (تشطيب خطوط الشعر)',
        'ja': 'HL（ヘアライン仕上げ）', 'ko': 'HL (헤어라인 가공)',
        'vi': 'HL (hoàn thiện chải mờ)', 'th': 'HL (ผิวขัดเส้นละเอียด)',
        'tr': 'HL (fırçalı satine kaplama)', 'id': 'HL (finishing satin)',
        'hi': 'HL (बाल-रेखा फिनिश)',
    },
    'p06R7C1': {  # Hairline finish
        'zh': '发丝纹', 'es': 'Líneas finas (acabado satinado)',
        'fr': 'Lignes fines (finition satinée)', 'de': 'Haarlinie',
        'it': 'Linea sottile (finitura satinata)', 'pt': 'Linhas finas (acabamento escovado)',
        'ru': 'Волосяная линия', 'ar': 'خطوط الشعر (تشطيب)',
        'ja': 'ヘアライン仕上げ', 'ko': '헤어라인 가공', 'vi': 'Đường chải mờ',
        'th': 'ผิวขัดเส้นละเอียด', 'tr': 'Saç teli (fırçalı)',
        'id': 'Garis halus (satin)', 'hi': 'बाल-रेखा फिनिश',
    },
    'p06R9C1': {  # Mirror (No.8)
        'zh': '镜面（No.8）', 'es': 'Espejo (No. 8)', 'fr': 'Miroir (n° 8)',
        'de': 'Spiegel (Nr. 8)', 'it': 'Specchio (n. 8)', 'pt': 'Espelho (nº 8)',
        'ru': 'Зеркало (№ 8)', 'ar': 'مرآة (رقم 8)', 'ja': '鏡面（No.8）',
        'ko': '거울 (No.8)', 'vi': 'Gương (số 8)', 'th': 'กระจกเงา (เบอร์ 8)',
        'tr': 'Ayna (No. 8)', 'id': 'Cermin (No. 8)', 'hi': 'दर्पण (नं. 8)',
    },
    # ---- NEW critical keys ----
    'p09t2R5C2': {  # Spangle / minimized / zero spangle, passivated or oiled
        'zh': '锌花 / 小锌花 / 零锌花，钝化或涂油',
        'es': 'Flor de zinc / flor de zinc minimizada / cero flor de zinc, pasivada o aceitada',
        'fr': 'Floraison de zinc / floraison réduite / zéro floraison, passivée ou huilée',
        'de': 'Zinkblüte / minimierte Zinkblüte / Null-Zinkblüte, passiviert oder geölt',
        'it': 'Fiore di zinco / fiore di zinco minimizzato / zero fiore di zinco, passivato o oliato',
        'pt': 'Flor de zinco / flor de zinco minimizada / zero flor de zinco, passivada ou oleada',
        'ru': 'Цветы цинка / минимизированные цветы цинка / нулевые цветы цинка, пассивированные или с маслом',
        'ar': 'زهرة الزنك / زهرة زنك مصغرة / صفر زهرة زنك، ممرر بالكرومات أو مدهون',
        'ja': '亜鉛花 / 微細亜鉛花 / ゼロ亜鉛花、クロメート処理または油着け',
        'ko': '아연꽃 / 미세 아연꽃 / 무아연꽃, 크로메이트 처리 또는 오일 처리',
        'vi': 'Hoa kẽm / hoa kẽm tối thiểu / không hoa kẽm, thụ động hóa hoặc bôi dầu',
        'th': 'ดอกสังกะสี / ดอกสังกะสีขนาดเล็ก / ไม่มีดอกสังกะสี พาสซิเวชันหรือเคลือบน้ำมัน',
        'tr': 'Çinko çiçeği / küçültülmüş çinko çiçeği / sıfır çinko çiçeği, kromatlanmış veya yağlanmış',
        'id': 'Spangle / spangle minimal / nol spangle, dipasivasi atau dilumasi',
        'hi': 'जस्त फूल / न्यूनतम जस्त फूल / शून्य जस्त फूल, पैसिवेटेड या तैलीकृत',
    },
    'p18t1R10C2': {  # Chromated, oiled, anti-fingerprint, PVC film protected
        'zh': '铬化处理，涂油，抗指纹，PVC 膜保护',
        'es': 'Cromatizado, aceitado, anti-huella, protegido con película PVC',
        'fr': 'Chromaté, huilé, anti-trace, protégé par film PVC',
        'de': 'Chromatiert, geölt, fingerabdruckfest, mit PVC-Folie geschützt',
        'it': 'Cromatato, oliato, anti-impronta, protetto con film PVC',
        'pt': 'Cromatizado, oleado, anti-impressão digital, protegido por filme PVC',
        'ru': 'Хроматированный, промасленный, антиотпечатковый, защищенный ПВХ пленкой',
        'ar': 'معالج بالكرومات، مدهون، مقاوم للبصمة، محمي بفيلم PVC',
        'ja': 'クロメート処理、油着け、耐指紋、PVCフィルム保護',
        'ko': '크로메이트 처리, 오일 처리, 지문 방지, PVC 필름 보호',
        'vi': 'Cromat hóa, bôi dầu, kháng vân tay, bảo vệ bằng màng PVC',
        'th': 'โครเมต, เคลือบน้ำมัน, กันลายนิ้วมือ, ป้องกันด้วยฟิล์ม PVC',
        'tr': 'Kromatlanmış, yağlanmış, parmak izine karşı dayanıklı, PVC film korumalı',
        'id': 'Kromat, dilumasi, anti-sidik jari, dilindungi film PVC',
        'hi': 'क्रोमेटेड, तैलीकृत, एंटी-फिंगरप्रिंट, PVC फिल्म संरक्षित',
    },
    'p06t2R5C2': {  # 2B, BA, No.1, No.4 brushed, HL hairline, 8K mirror
        'zh': '2B、BA、No.1、No.4 拉丝、HL 发丝纹、8K 镜面',
        'es': '2B, BA, No.1, No.4 satinado, HL satinado (líneas finas), espejo 8K',
        'fr': '2B, BA, No.1, No.4 satiné, HL satiné (lignes fines), miroir 8K',
        'de': '2B, BA, No.1, No.4 gebürstet, HL Haarlinie, 8K Spiegel',
        'it': '2B, BA, No.1, No.4 satinato, HL satinato (linea sottile), specchio 8K',
        'pt': '2B, BA, No.1, No.4 escovado, HL escovado (linhas finas), espelho 8K',
        'ru': '2B, BA, No.1, No.4 шлифованный, HL волосяная линия, 8K зеркало',
        'ar': '2B، BA، No.1، No.4 مشطوف، HL خطوط الشعر، 8K مرآة',
        'ja': '2B、BA、No.1、No.4 ヘアライン、HL ヘアライン、8K 鏡面',
        'ko': '2B, BA, No.1, No.4 브러시, HL 헤어라인, 8K 거울',
        'vi': '2B, BA, No.1, No.4 chải, HL chải mờ (đường tóc), gương 8K',
        'th': '2B, BA, No.1, No.4 ขัด, HL ผิวขัดเส้นละเอียด, 8K กระจกเงา',
        'tr': '2B, BA, No.1, No.4 fırçalı, HL fırçalı satine, 8K ayna',
        'id': '2B, BA, No.1, No.4 sikat, HL garis halus, cermin 8K',
        'hi': '2B, BA, No.1, No.4 ब्रश्ड, HL बाल-रेखा, 8K दर्पण',
    },
}

# ---- Targeted substring replacements on ALL keys ----
REPLACE = {
    'zh': [
        (r'亮片', '锌花'), (r'水花', '锌花'), (r'亮片花', '锌花'),
        (r'镀铬', '铬化'), (r'铬镀', '铬化'),
        (r'皮肤通过', '精整轧制'), (r'皮肤通行证', '精整轧制'),
    ],
    'es': [
        (r'(?i)Lentejuela', 'Flor de zinc'),
        (r'Cromado', 'Cromatizado'), (r'cromado', 'cromatizado'),
        (r'Pasado por la piel', 'Skin-passed'), (r'Paso de piel', 'Skin-passed'),
    ],
    'fr': [
        (r'(?i)paillette', 'fleur de zinc'),
        (r'Chromé', 'Chromaté'), (r'Chromée', 'Chromatée'),
        (r'Passé à la peau', 'Skin-pass'),
    ],
    'de': [
        (r'Pailletten', 'Zinkblumen'), (r'Flitter', 'Zinkblumen'),
        (r'hautverträglich', 'skin-passed'), (r'Hautverträglich', 'Skin-passed'),
    ],
    'it': [
        (r'lustrini', 'fiori di zinco'), (r'Lustrini', 'Fiori di zinco'),
        (r'Angolo', 'Fiore di zinco'),
        (r'Passato nella pelle', 'Skin-passed'),
    ],
    'pt': [
        (r'(?i)lantejola', 'flor de zinco'),
        (r'Cromado', 'Cromatizado'),
        (r'Passado na Pele', 'Skin-passed'), (r'Passar pela pele', 'Skin-passed'),
    ],
    'ru': [
        (r'блестками', 'цветами цинка'), (r'блестки', 'цветы цинка'),
        (r'блесток', 'цвет цинка'),
        (r'Хромированный', 'хроматированный'), (r'хромированный', 'хроматированный'),
        (r'пропитка кожей', 'скин-пас'), (r'через кожу', 'скин-пас'),
    ],
    'ar': [
        (r'لمعة', 'زهرة الزنك'), (r'لمع', 'زهرة الزنك'),
        (r'مطلي بالكروم', 'معالج بالكرومات'), (r'الكروم', 'الكرومات'),
        (r'تمرير الجلد', 'سكين-باس'), (r'عبر الجلد', 'سكين-باس'),
    ],
    'ja': [
        (r'スパンコール', '亜鉛花'), (r'輝き', '亜鉛花'),
    ],
    'vi': [
        (r'Hình chữ nhật', 'Hoa kẽm'), (r'hình chữ nhật', 'hoa kẽm'),
        (r'hình đốm', 'hoa kẽm'),
        (r'Mạ crôm', 'cromat hóa'), (r'mạ crôm', 'cromat hóa'),
        (r'Da qua', 'cán tinh chỉnh'), (r'qua da', 'cán tinh chỉnh'),
    ],
    'th': [
        (r'แพรวพราว', 'ดอกสังกะสี'), (r'ประกาย', 'ดอกสังกะสี'),
        (r'โครเมี่ยม', 'โครเมต'),
        (r'ทู่', 'พาสซิเวชัน'), (r'ผ่านผิวหนัง', 'สกิน-พาส'), (r'ผิวหนัง', 'สกิน-พาส'),
    ],
    'tr': [
        (r'(?i)\bpul\b', 'Çinko çiçeği'), (r'\bpullu\b', 'çinko çiçekli'),
        (r'Deriden Geçirilmiş', 'skin-pass'), (r'deri', 'skin-pass'),
    ],
    'id': [
        (r'Spangle', 'Spangle'),
        (r'Dikrom', 'kromat'), (r'Dikromat', 'kromat'),
        (r'Dikelilingi Kulit', 'skin-pass'), (r'kulit', 'skin-pass'),
    ],
    'ko': [
        (r'피부 통과', '스킨패스'), (r'피부', '스킨패스'),
    ],
    'hi': [],
}


def apply_replace(text, lang):
    for pat, rep in REPLACE.get(lang, []):
        text = re.sub(pat, rep, text)
    return text


def main():
    for lg in LANGS:
        f = os.path.join(OUT_DIR, 'table_%s.json' % lg)
        d = json.load(open(f, encoding='utf-8'))
        changed = []
        for k, trans in EXACT.items():
            if lg in trans and k in d:
                if d[k] != trans[lg]:
                    d[k] = trans[lg]
                    changed.append(k)
        for k in d:
            if k in EXACT:
                continue
            new = apply_replace(d[k], lg)
            if new != d[k]:
                d[k] = new
                changed.append(k)
        if changed:
            json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            print('%-3s fixed %d: %s' % (lg, len(changed), ', '.join(sorted(set(changed))[:12])))
        else:
            print('%-3s no changes' % lg)


if __name__ == '__main__':
    main()
