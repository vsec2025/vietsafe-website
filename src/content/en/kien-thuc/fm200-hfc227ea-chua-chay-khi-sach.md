---
layout: "layouts/article.njk"
title: "HFC-227ea (FM-200) Clean Agent Fire Suppression — System Design and TCVN 7161-9:2024"
description: "Complete technical guide to HFC-227ea (FM-200) clean agent fire suppression: applications, agent quantity calculation per TCVN 7161-9:2024, design requirements, hold time, room integrity, and safety criteria."
lang: "en"
permalink: "/en/kien-thuc/fm200-hfc227ea-chua-chay-khi-sach.html"
date: 2026-05-20
category: "ky-thuat"
---


<div class="abox"><p><strong>HFC-227ea (FM-200)</strong> — chemical name Heptafluoropropane — is a clean agent fire suppressant: colourless, odourless, non-conductive, and leaves no residue after discharge. Unlike water or dry powder suppression, which can cause catastrophic damage to electronic equipment, FM-200 extinguishes fires through rapid heat absorption without affecting machinery or assets — making it the system of choice for thousands of organisations protecting server rooms, switchrooms, archives and irreplaceable assets.</p></div>
<div class="trow"><span class="tag">HFC-227ea</span><span class="tag">FM-200</span><span class="tag">TCVN 7161-9:2024</span><span class="tag">Clean Agent</span><span class="tag">Server Room</span><span class="tag">Transformer Room</span></div>

<h2>1. What is HFC-227ea (FM-200) and why is it needed?</h2>
<p>In many modern facilities — particularly data centres, control rooms, dry-type transformer rooms, document archives and museums — the discharge of water to suppress a fire can cause damage far greater than the fire itself. A flooded server room can mean total data loss; a medium-voltage switchroom exposed to water can trigger a more serious incident than the original fire.</p>
<p>HFC-227ea (FM-200) solves this problem. The system operates on the <strong>total flooding</strong> principle: when sensors detect a fire, agent is discharged rapidly, distributing uniformly throughout the protected space, reaching design concentration within 10 seconds, and extinguishing the fire before it can spread.</p>

<h2>2. Typical applications of HFC-227ea (FM-200)</h2>
<table class="ctb"><thead><tr><th>Facility type</th><th>Reason HFC-227ea (FM-200) is preferred</th></tr></thead><tbody>
<tr><td>Server rooms, Data Centres</td><td>No wetting of equipment; no data interruption; extinguishes before hardware damage occurs</td></tr>
<tr><td>Transformer rooms, medium-voltage switchrooms</td><td>Non-conductive; no secondary short-circuit on discharge into live equipment</td></tr>
<tr><td>Control rooms, PLC/SCADA cabinets</td><td>Protects plant control systems and continuous production lines</td></tr>
<tr><td>Telecommunications rooms, central exchanges</td><td>Maintains telecom infrastructure without service interruption</td></tr>
<tr><td>Document archives, museums</td><td>Protects legal records, artworks and irreplaceable artefacts</td></tr>
<tr><td>Generator rooms, UPS and battery rooms</td><td>Controls electrical fires rapidly; prevents cascading failure in power systems</td></tr>
</tbody></table>

<h2>3. Agent quantity calculation — TCVN 7161-9:2024</h2>
<p>Under TCVN 7161-9:2024 (equivalent to ISO 14520-9:2019), the required HFC-227ea charge for each protected space is calculated individually, based on room volume, fire hazard class and ambient temperature. The core formula is:</p>
<div class="calc-box">
<div class="formula">Q = ( c / (100 − c) ) × ( V / v )</div>
<ul>
<li><strong>Q</strong> — required HFC-227ea charge (kg)</li>
<li><strong>c</strong> — design concentration (% v/v); typically 8.5% for server rooms</li>
<li><strong>V</strong> — net protected volume (m³), excluding fixed non-permeable objects</li>
<li><strong>v</strong> — specific volume of HFC-227ea vapour (m³/kg) = 0.1269 + 0.000513 × T (where T = room temperature °C)</li>
</ul>
</div>

<h3>Design concentration by fire hazard class</h3>
<table class="ctb"><thead><tr><th>Hazard class</th><th>Minimum design concentration</th><th>Notes</th></tr></thead><tbody>
<tr><td>Class B — Heptane (flammable liquids)</td><td>9.0%</td><td>Safety factor 1.3 × extinguishing concentration</td></tr>
<tr><td>Class A surface — Plastics, wood, paper</td><td>7.9%</td><td>Safety factor 1.3 × extinguishing concentration</td></tr>
<tr><td>Class A high-hazard — Cables, electronic equipment</td><td>8.5%</td><td>Server rooms, switchrooms, PLCs</td></tr>
</tbody></table>
<p style="font-size:0.8rem;color:#666">Source: Table 4, TCVN 7161-9:2024 (ISO 14520-9:2019)</p>

<div class="ibox"><strong>📐 Worked calculation example</strong>
<p style="font-size:0.87rem;margin:0.5rem 0 0;color:#444">Problem: Server room 6 × 5 × 3 m, temperature 20°C, containing 5 equipment racks (total volume 2.5 m³), design concentration 8.5%.</p>
<p style="font-size:0.87rem;margin:0.5rem 0 0;color:#444">Step 1 — Net volume: V = 6 × 5 × 3 = 90.0 m³</p>
<p style="font-size:0.87rem;margin:0.5rem 0 0;color:#444">Step 2 — Specific vapour volume at 20°C: v = 0.1269 + 0.000513 × 20 = 0.1372 m³/kg</p>
<p style="font-size:0.87rem;margin:0.5rem 0 0;color:#444">Step 3 — Required charge: Q = (8.5 / 91.5) × (90.0 / 0.1372) ≈ <strong>61.0 kg</strong></p>
<p style="font-size:0.87rem;margin:0.5rem 0 0;color:#888">Result: One cylinder of 82.5 litres / 42 bar, filled at ~740 kg/m³ (≤ 1,150 kg/m³ per TCVN 7161-9:2024)</p>
</div>

<h2>4. Key technical requirements</h2>
<ul>
<li><strong>Discharge time:</strong> The system must reach 95% of design concentration within 10 seconds (TCVN 7161-1:2022, Art. 7.9.1.1)</li>
<li><strong>Hold time:</strong> Design concentration must be maintained for a minimum of 10 minutes after discharge to ensure complete extinguishment</li>
<li><strong>Room integrity:</strong> All penetrations, floor/wall openings and HVAC openings must be sealed to prevent agent loss before the hold time has elapsed</li>
<li><strong>Automatic HVAC shutdown:</strong> All AHU and exhaust fans must shut down automatically on system activation (TCVN 7161-1:2022, Art. 7.4.3)</li>
<li><strong>Pre-discharge warning:</strong> Flashing lights and alarm sounders must operate throughout the delay period to allow occupant evacuation</li>
<li><strong>Occupant safety:</strong> NOAEL = 9.0% — the standard design concentration is within the safe limit for human exposure (TCVN 7161-9:2024, Table 7)</li>
</ul>

<div class="fqs" itemscope itemtype="https://schema.org/FAQPage">
<h2>Frequently Asked Questions</h2>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">Is HFC-227ea (FM-200) safe for people when the system discharges?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">At the standard design concentration (≤ 9.0% v/v), HFC-227ea causes no observable adverse effects — this is the NOAEL (No Observable Adverse Effect Level) recognised by TCVN 7161-9:2024. However, the system must include audible and visual alarms and a time delay (typically 30–60 seconds) before discharge, to allow occupants to evacuate before agent is released.</p></div>
</div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">Why must the room be airtight when using HFC-227ea (FM-200)?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">HFC-227ea must maintain its design concentration throughout the entire hold period (≥ 10 minutes) to fully extinguish the fire. If the room has significant leakage — under doors, through cable penetrations, or through unsealed HVAC openings — agent will escape and concentration will fall below the extinguishing level before the fire is fully controlled. A door fan test (enclosure integrity test) after installation is mandatory.</p></div>
</div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">How is HFC-227ea (FM-200) different from CO₂ suppression?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">CO₂ suppresses fires by reducing the oxygen concentration to a level that cannot sustain combustion — at design concentration (35–40%), CO₂ is immediately life-threatening. HFC-227ea suppresses by heat absorption; at design concentration (≤ 9%) it is safe for brief human exposure. HFC-227ea is therefore used in occupied spaces or spaces with regular human access; CO₂ systems require strict interlocks against accidental discharge and appropriate safety measures if used where people may be present.</p></div>
</div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">What periodic maintenance does an HFC-227ea system require?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">Under TCVN 7161-1:2022, HFC-227ea systems must be inspected every 6 months: cylinder weight verification (against the charged weight), pressure check, alarm and interlock functional test. If the agent mass has decreased by more than 5% from the design charge, the cylinder must be recharged.</p></div>
</div>
</div>
<div class="ctabox"><h3>Need HFC-227ea (FM-200) system design and consulting?</h3><p>VIETSAFE E&amp;C engineers provide FM-200 system design, agent quantity calculations, and complete fire safety dossier preparation for submission to the fire authority.</p><a href="/en/#contact" class="btnw">Contact us →</a></div>
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

