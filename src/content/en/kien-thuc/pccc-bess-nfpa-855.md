---
layout: "layouts/article.njk"
title: "Fire Safety for Battery Energy Storage Systems (BESS) — Applying NFPA 855 in Vietnam"
description: "Technical guide to fire protection design for BESS under NFPA 855: EQ classification, thermal runaway detection, suppression systems, and Vietnamese regulatory compliance under Fire Safety Law 55/2024."
lang: "en"
permalink: "/en/kien-thuc/pccc-bess-nfpa-855.html"
date: 2026-06-11
category: "ky-thuat"
---


<div class="abox"><p><strong>Fire protection for Battery Energy Storage Systems (BESS)</strong> requires dedicated design under NFPA 855 combined with applicable Vietnamese regulations (QCVN 01:2021/BCA). BESS is a high-hazard installation because the lithium-ion thermal runaway failure mode differs fundamentally from conventional fires — it demands early thermal detection, specialist suppression, and dedicated emergency response procedures.</p></div>
<div class="trow"><span class="tag">NFPA 855</span><span class="tag">BESS Fire Safety</span><span class="tag">Thermal Runaway</span><span class="tag">QCVN 01</span><span class="tag">Lithium-ion</span><span class="tag">ESS</span></div>

<h2>1. Why BESS requires a dedicated fire protection approach</h2>
<p>Battery Energy Storage Systems are expanding rapidly across Vietnam on the back of the renewable energy boom. However, most current Vietnamese technical regulations (QCVN) contain <strong>no specific provisions</strong> for the fire hazards of lithium-ion battery chemistry. The critical hazard is <strong>thermal runaway</strong>: an overheated cell triggers adjacent cells in a self-sustaining chain reaction that is extremely difficult to extinguish, releasing toxic gases including hydrogen fluoride (HF) and carbon monoxide (CO) — even in the absence of a visible flame.</p>
<div class="ibox"><strong>📌 Incident record</strong><p style="font-size:0.85rem;margin:0;color:#555">Major BESS fires — including the APS McMicken facility (Arizona, 2019) and the Liverpool Energy Community (UK, 2021) — demonstrated that standard sprinkler response is insufficient to control thermal runaway propagation. Prolonged cooling after initial suppression is essential to prevent reignition.</p></div>

<h2>2. Applicable standards for BESS fire protection in Vietnam</h2>
<table class="ctb"><thead><tr><th>Standard</th><th>Scope</th><th>BESS type</th></tr></thead><tbody>
<tr><td><strong>NFPA 855 (2023)</strong></td><td>Installation requirements for stationary energy storage systems: compartmentation, ventilation, suppression, emergency response</td><td>All types</td></tr>
<tr><td><strong>NFPA 13</strong></td><td>Automatic sprinkler systems — discharge density for BESS rooms</td><td>Container / indoor</td></tr>
<tr><td><strong>NFPA 72</strong></td><td>Fire alarm and early-warning detection systems</td><td>All types</td></tr>
<tr><td><strong>UL 9540A</strong></td><td>Test method for thermal runaway fire propagation in battery systems</td><td>Lithium-ion</td></tr>
<tr><td><strong>QCVN 01:2021/BCA</strong></td><td>Basic fire safety requirements under Vietnamese law</td><td>All types</td></tr>
</tbody></table>

<h2>3. Design requirements under NFPA 855</h2>
<h3>3.1 Energy Quantity (EQ) classification and thresholds</h3>
<ul>
<li><strong>EQ ≤ 20 kWh per room:</strong> Exempt — applies to residential applications</li>
<li><strong>EQ 20–600 kWh:</strong> Compartmentation, ventilation, detection and suppression required per Chapter 12</li>
<li><strong>EQ &gt; 600 kWh:</strong> Technical justification report and quantitative risk analysis required</li>
</ul>

<h3>3.2 Early fire detection — three layers</h3>
<ul>
<li>Cell-level thermal monitoring integrated in the Battery Management System (BMS)</li>
<li>Gas detection: CO, H₂, HF — identifies thermal runaway at the earliest possible stage, before open flame</li>
<li>Conventional smoke/heat detection (NFPA 72) — the final detection layer</li>
</ul>

<h3>3.3 Suppression systems</h3>
<ul>
<li><strong>Water mist:</strong> Most effective cooling medium — the most widely used approach for indoor BESS</li>
<li><strong>Clean agents (CO₂, FK-5-1-12):</strong> For small enclosed rooms with limited EQ</li>
<li><strong>ESFR / CMSA sprinkler:</strong> For large-format BESS warehouse installations per NFPA 13 + NFPA 855</li>
</ul>
<p>The design objective is <strong>thermal propagation prevention</strong> — stopping the chain reaction from cell to cell. Flame suppression alone is insufficient.</p>

<h2>4. Vietnamese regulatory framework — Fire Safety Law 55/2024</h2>
<p>Under Fire Safety Law 55/2024 and Decree 105/2025, Vietnam has transitioned from a pre-approval to a post-inspection model. For BESS projects, project owners are advised to: (1) prepare a fire safety dossier referencing NFPA 855 alongside applicable QCVN; (2) develop a technical equivalency report comparing NFPA 855 provisions against Vietnamese regulations; (3) maintain the dossier in a form ready to present to the competent fire authority on demand; and (4) establish a dedicated inspection and emergency response plan specifically addressing lithium-ion thermal runaway. NFPA 855 can be applied in Vietnam under Art. 7 of Circular 06/2023/TT-BCA, subject to submission of the technical justification dossier to the fire authority for review.</p>

<div class="fqs" itemscope itemtype="https://schema.org/FAQPage">
<h2>Frequently Asked Questions</h2>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">How does NFPA 855 apply to rooftop BESS installations?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">Under NFPA 855 Chapter 15, outdoor and rooftop BESS installations must comply with minimum separation distances from egress routes and structural elements. In Vietnam, a technical justification dossier must be prepared under Fire Safety Law 55/2024 and presented to the competent authority for review if required.</p></div>
</div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">How is thermal runaway different from a conventional fire?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">Thermal runaway is a self-sustaining thermochemical reaction within the battery cell that generates heat, releases toxic gases (HF, CO) and flames — even without oxygen from outside the cell. Effective response requires continuous cooling for several hours to prevent chain propagation to adjacent cells. Firefighters require specialised SCBA and extended water supply.</p></div>
</div>
</div>

<div class="srcbox"><p style="font-weight:600;margin-bottom:0.5rem">References:</p><ul style="margin:0;padding-left:1.2rem"><li>NFPA 855 (2023 Edition) — Standard for the Installation of Stationary Energy Storage Systems</li><li>NFPA 13 (2022) — Standard for the Installation of Sprinkler Systems</li><li>UL 9540A — Test Method for Evaluating Thermal Runaway Fire Propagation in Battery Energy Storage Systems</li><li>QCVN 01:2021/BCA — National Technical Regulation on Fire Protection for Facilities</li></ul><p style="margin-top:0.5rem;font-style:italic;color:#666">This article is for technical reference only and does not substitute for legal or regulatory advice. Please consult current legislation and guidance from the competent authority for your specific project.</p></div>
<div class="ctabox"><h3>Need specialist BESS fire protection consulting?</h3><p>VIETSAFE E&amp;C engineers provide end-to-end support: technical justification reports, fire and smoke simulation (FDS), and complete fire safety dossier preparation.</p><a href="/en/#contact" class="btnw">Contact us →</a></div>
<footer class="sfooter">
  <p><strong style="color:#fff">VIETSAFE E&amp;C</strong> — Fire Safety Engineering &amp; Consulting</p>
  <p style="margin-top:0.4rem">
    <a href="/en/">Home</a> ·
    <a href="/en/pbd.html">PBD Services</a> ·
    <a href="/en/kien-thuc/">Knowledge</a> ·
    <a href="/en/#contact">Contact</a>
  </p>
  <p style="margin-top:0.3rem;font-size:0.72rem;color:rgba(255,255,255,0.25)">© 2025 VIETSAFE E&amp;C · FIRE SAFETY ENGINEERING &amp; CONSTRUCTION</p>
</footer>

