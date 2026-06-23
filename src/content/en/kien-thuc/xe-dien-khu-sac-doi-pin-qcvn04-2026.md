---
layout: "layouts/article.njk"
title: "Fire Safety for EV Charging Zones and Battery-Swap Stations — Amendment 01:2026 to QCVN 04:2021/BXD"
description: "Detailed comparison of fire safety requirements for EV parking zones, EV charging zones, and battery-swap stations under Circular 31/2026/TT-BXD — Amendment 01:2026 to QCVN 04:2021/BXD."
lang: "en"
permalink: "/en/kien-thuc/xe-dien-khu-sac-doi-pin-qcvn04-2026.html"
date: 2026-06-18
category: "ky-thuat"
---


<div class="abox"><p>Circular 31/2026/TT-BXD, issued on 15 June 2026 (effective 15 December 2026), promulgated <strong>Amendment 01:2026 to QCVN 04:2021/BXD</strong> — the National Technical Regulation on Fire Safety for Residential Buildings. For the first time, Vietnamese regulation explicitly differentiates fire safety requirements across three distinct zone types that are frequently confused in design and authority review: <strong>EV parking zones</strong>, <strong>EV charging zones</strong>, and <strong>battery-swap stations</strong>.</p></div>
<div class="trow"><span class="tag">QCVN 04:2021/BXD</span><span class="tag">Amendment 01:2026</span><span class="tag">EV Fire Safety</span><span class="tag">Battery-Swap</span><span class="tag">Thermal Runaway</span><span class="tag">Circular 31/2026</span></div>

<h2>1. Why three separate zone types? — The thermal runaway hazard</h2>
<p>Lithium-ion batteries — whether in electric vehicles or in dedicated battery-swap cabinets — can enter <strong>thermal runaway</strong>: an uncontrolled self-heating reaction that releases toxic gases (H₂, CO, HF) and heat without requiring an external ignition source. Amendment 01:2026 differentiates requirements across zone types because the thermal runaway risk profile differs fundamentally:</p>
<ul>
<li><strong>EV parking zones</strong> (vehicles parked, not charging): vehicles carry full or partial battery charge but are not under active electrical load — risk profile is broadly similar to a conventional car park with elevated thermal consequences if a cell fails.</li>
<li><strong>EV charging zones</strong> (active charging): the charging process introduces additional heat load to the battery, increasing the probability of thermal runaway during or immediately after charging. Compartmentation and suppression are mandatory.</li>
<li><strong>Battery-swap stations</strong> (batteries stored and swapped): multiple batteries at various states of charge are stored simultaneously — a single thermal runaway event can propagate to adjacent batteries in storage, making this the highest-risk zone type.</li>
</ul>

<h2>2. Comparison of requirements across the three zone types</h2>
<table class="ctb"><thead><tr><th>Criterion</th><th>EV Parking Zone (§2.10.1)</th><th>EV Charging Zone (§2.10.2)</th><th>Battery-Swap Station (§2.11)</th></tr></thead><tbody>
<tr><td>Fire compartment</td><td>Per QCVN 06</td><td>≤ 3,000 m² on grade / ≤ 1,200 m² basement (cars) — separate compartment required</td><td>≤ 500 m² — separate compartment required; minimum 6 m separation or fire curtain / drencher</td></tr>
<tr><td>Maximum slots / zone</td><td>Not specified</td><td>Basement: ≤ 25 cars / ≤ 50 two-wheelers per zone. On grade: ≤ 30 / ≤ 80 per zone</td><td>Not applicable (limited by EQ)</td></tr>
<tr><td>Automatic suppression</td><td>Per occupancy type</td><td>Mandatory (sprinkler)</td><td>Mandatory (sprinkler or deluge)</td></tr>
<tr><td>Battery / charger capacity</td><td>No specific limit</td><td>Chargers in basement ≤ 22 kW each</td><td>Outdoor: ≤ 100 kWh total / zone. On grade: ≤ 35 kWh. Basement: ≤ 18 kWh</td></tr>
<tr><td>Smoke / exhaust ventilation</td><td>Per QCVN 06 — maintain smoke layer ≥ Annex D</td><td>Mandatory mechanical exhaust — maintain smoke layer ≥ Annex D</td><td>Forced mechanical exhaust + gas detection required</td></tr>
<tr><td>Gas detection (H₂ / CO)</td><td>Mandatory — certified equipment</td><td>Mandatory — certified equipment</td><td>Not specified separately (covered by fire detection)</td></tr>
<tr><td>Fire detection</td><td>Automatic fire alarm — mandatory</td><td>Heat + smoke detection mandatory</td><td>Heat + smoke detection; off-gas (H₂/CO) detection</td></tr>
<tr><td>24/7 CCTV monitoring</td><td>Mandatory — linked to staffed control room</td><td>Mandatory — linked to staffed control room</td><td>Mandatory — continuous feed to staffed control room</td></tr>
<tr><td>Power supply</td><td>Sufficient capacity</td><td>Separate circuit; auto-disconnect on fire alarm; emergency manual cutoff</td><td>Separate circuit; emergency cutoff for entire system; lightning protection</td></tr>
<tr><td>Charger / cabinet certification</td><td>N/A</td><td>Compliant with applicable law; certified before installation</td><td>Compliant with applicable law; certified before installation</td></tr>
</tbody></table>

<h2>3. Key design implications</h2>
<h3>3.1 Reclassification when chargers are installed</h3>
<p>A standard EV parking zone where vehicles are only parked (not actively charging) is governed by the existing QCVN 06 compartmentation rules for its occupancy type. As soon as chargers are installed and activated, the zone must be <strong>reclassified as an EV charging zone</strong> — triggering the requirement for: a dedicated fire compartment, a maximum compartment area of 3,000 m² (on grade) or 1,200 m² (basement), mandatory automatic suppression, and dedicated smoke exhaust — even if the chargers are slow (Level 1/2 AC) units.</p>

<h3>3.2 Drencher curtain as an alternative to a fire-rated wall</h3>
<p>Where the required 6 m clearance between EV charging compartments cannot be achieved, Amendment 01:2026 permits a drencher water curtain as an alternative to a full fire-rated wall: two rows of drencher heads spaced 0.5 m apart, with a minimum flow rate of ≥ 1 l/s per metre of curtain width, maintained for ≥ 1 hour.</p>

<h3>3.3 Battery-swap EQ limits are the most restrictive</h3>
<p>Battery-swap stations face the tightest energy quantity (EQ) limits in the regulation, because stored batteries at various states of charge represent the highest risk of thermal runaway propagation. Designers must calculate the total EQ of all batteries that can be simultaneously stored in each zone and verify compliance with the applicable threshold (outdoor / on grade / basement).</p>

<div class="fqs" itemscope itemtype="https://schema.org/FAQPage">
<h2>Frequently Asked Questions</h2>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">Does Amendment 01:2026 apply to existing buildings retrofitting EV chargers?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">Yes, Amendment 01:2026 applies to both new construction and existing buildings being retrofitted with EV chargers or battery-swap stations. Existing buildings are given some accommodation on egress route requirements (§2.10.2.3), but the compartmentation, suppression, ventilation, and detection requirements apply in full. Operators retrofitting existing car parks with chargers must assess whether compartment sizes and fire systems meet the new requirements.</p></div>
</div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">Is NFPA 855 relevant to EV charging zone design in Vietnam?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">NFPA 855 is the primary international standard addressing energy storage systems (ESS) including vehicle charging and battery-swap installations. Where Amendment 01:2026 to QCVN 04 does not provide sufficient detail — for example, on suppression system design for battery-swap stations — NFPA 855 is the recognised supplementary reference, applied under a technical justification report pursuant to Circular 06/2023/TT-BCA.</p></div>
</div>
</div>
<div class="srcbox"><p style="font-weight:600;margin-bottom:0.5rem">References:</p><ul style="margin:0;padding-left:1.2rem"><li>Circular 31/2026/TT-BXD — Amendment 01:2026 to QCVN 04:2021/BXD (§1.4, §2.10, §2.11, §3)</li><li>QCVN 06:2022/BXD and Amendment 01:2023 — National Technical Regulation on Fire Safety for Buildings and Structures</li><li>QCVN 10:2025/BCA — Fire safety requirements for facilities</li><li>NFPA 855 (2023) — Standard for the Installation of Stationary Energy Storage Systems</li></ul><p style="margin-top:0.5rem;font-style:italic;color:#666">This article is for technical reference only. Please consult current legislation and guidance from the competent authority for your specific project.</p></div>
<div class="ctabox"><h3>Need fire safety design for EV charging infrastructure?</h3><p>VIETSAFE E&amp;C provides PCCC design and compliance consulting for EV charging zones, battery-swap stations, and BESS installations under QCVN 04, QCVN 06, and NFPA 855.</p><a href="/en/#contact" class="btnw">Contact us →</a></div>
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

