#!/usr/bin/env python3
import re
import os
from pathlib import Path
from html.parser import HTMLParser
from html.unescape import unescape

BASE_OLD = '/tmp/vietsafe-website'
BASE_NEW = '/tmp/vietsafe-11ty/src/content'

# Article metadata
ARTICLES = {
    'kien-thuc/pccc-bess-nfpa-855.html': {
        'vi_title': 'PCCC cho Hệ thống Lưu trữ Pin BESS — NFPA 855',
        'en_title': 'Fire Safety for Battery Energy Storage Systems (BESS) — NFPA 855',
        'vi_desc': 'Hướng dẫn thiết kế PCCC cho BESS theo NFPA 855 tại Việt Nam.',
        'en_desc': 'Fire protection design for BESS under NFPA 855 in Vietnam.',
        'date': '2026-06-11',
        'category': 'ky-thuat'
    },
    'kien-thuc/nfpa-5000-nha-tren-150m.html': {
        'vi_title': 'NFPA 5000 cho Nhà Siêu Cao Tầng trên 150m',
        'en_title': 'NFPA 5000 for Super High-Rise Buildings Above 150 m',
        'vi_desc': 'Áp dụng NFPA 5000 cho nhà trên 150m tại Việt Nam.',
        'en_desc': 'Applying NFPA 5000 for buildings above 150m in Vietnam.',
        'date': '2026-06-09',
        'category': 'ky-thuat'
    },
    'kien-thuc/tu-nghiem-thu-pccc-2025.html': {
        'vi_title': 'Tự Nghiệm Thu PCCC từ 1/7/2025',
        'en_title': 'Fire Safety Self-Certification from 1 July 2025',
        'vi_desc': 'Hướng dẫn tự nghiệm thu PCCC theo Luật 55/2024.',
        'en_desc': 'Self-certification guide under Fire Safety Law 55/2024.',
        'date': '2026-06-07',
        'category': 'phap-ly'
    },
    'kien-thuc/chu-dau-tu-trach-nhiem-pccc-ket-hop-tu-van.html': {
        'vi_title': 'Chủ Đầu Tư Trách Nhiệm PCCC & Tư Vấn',
        'en_title': 'Project Owner Liability and Fire Safety Consulting',
        'vi_desc': 'Phân tích trách nhiệm chủ đầu tư trong bối cảnh hậu kiểm.',
        'en_desc': 'Analysis of owner liability in the post-inspection model.',
        'date': '2026-06-05',
        'category': 'phap-ly'
    },
    'kien-thuc/tinh-toan-pbd-theo-sfpe.html': {
        'vi_title': 'Tính Toán Thiết Kế theo Hiệu Năng (PBD) - SFPE',
        'en_title': 'Performance-Based Design (PBD) - SFPE Handbook',
        'vi_desc': 'Hướng dẫn PBD và tính toán theo SFPE Handbook.',
        'en_desc': 'PBD methodology and calculations per SFPE Handbook.',
        'date': '2026-05-28',
        'category': 'mo-phong'
    },
    'kien-thuc/fm200-hfc227ea-chua-chay-khi-sach.html': {
        'vi_title': 'Khí HFC-227ea (FM-200) - Chữa Cháy Sạch',
        'en_title': 'HFC-227ea (FM-200) Clean Agent Fire Suppression',
        'vi_desc': 'Hệ thống chữa cháy khí sạch FM-200 theo TCVN.',
        'en_desc': 'FM-200 clean agent suppression per TCVN 7161-9:2024.',
        'date': '2026-05-20',
        'category': 'ky-thuat'
    },
    'kien-thuc/xe-dien-khu-sac-doi-pin-qcvn04-2026.html': {
        'vi_title': 'PCCC Xe Điện - QCVN 04 Sửa Đổi 01:2026',
        'en_title': 'Fire Safety for EV Charging - QCVN 04 Amendment 01:2026',
        'vi_desc': 'Yêu cầu PCCC cho khu sạc xe điện theo QCVN 04.',
        'en_desc': 'Fire safety requirements for EV charging per QCVN 04.',
        'date': '2026-06-18',
        'category': 'ky-thuat'
    },
}

def extract_main_content(html):
    """Extract main content from <main> tag"""
    match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    return match.group(1) if match else ''

def create_article_md(slug, lang, title, desc, date, category, html_content):
    """Create markdown file for article"""
    content = extract_main_content(html_content)

    # Convert HTML to basic markdown (simplified)
    content = content.replace('<div class="abox">', '').replace('</div>', '')
    content = re.sub(r'<[^>]+>', '', content)  # Strip remaining HTML
    content = re.sub(r'\n{3,}', '\n\n', content)  # Normalize whitespace

    slug_path = slug.split('/')[-1]

    md = f"""---
layout: "layouts/base.njk"
title: "{title}"
description: "{desc}"
lang: "{lang}"
permalink: "/{lang if lang == 'en' else ''}{'/kien-thuc/' if 'kien-thuc' in slug else '/'}{slug_path}"
date: {date}
category: "{category}"
---

<section style="background:linear-gradient(135deg,#1a1a1a,#2d0a13);color:#fff;padding:3.5rem 2rem 3rem;text-align:center">
  <div class="wrap">
    <h1 style="font-size:clamp(1.4rem,3vw,2.2rem);font-weight:800;max-width:800px;margin:0 auto">{title}</h1>
  </div>
</section>

<main style="max-width:860px;margin:0 auto;padding:3rem 2rem">
{content[:500]}...

<p style="margin-top:1rem"><a href="/{lang if lang == 'en' else ''}{'/' if lang == 'en' else ''}" style="color:var(--red)">← Quay lại</a></p>
</main>
"""
    return md

# Create directories
Path(f'{BASE_NEW}/vi/kien-thuc').mkdir(parents=True, exist_ok=True)
Path(f'{BASE_NEW}/en/kien-thuc').mkdir(parents=True, exist_ok=True)

print("✓ 11ty migration script created")
print("Ready to convert HTML files to markdown")
