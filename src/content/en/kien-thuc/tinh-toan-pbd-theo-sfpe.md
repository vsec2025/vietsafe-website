---
layout: "layouts/article.njk"
title: "Performance-Based Fire Design (PBD) — Methodology and Calculations per the SFPE Handbook"
description: "A technical overview of Performance-Based Fire Design (PBD) methodology: ASET/RSET framework, design fire characterisation, FDS simulation, Pathfinder egress modelling, and tenability criteria per the SFPE Handbook."
lang: "en"
permalink: "/en/kien-thuc/tinh-toan-pbd-theo-sfpe.html"
date: 2026-05-28
category: "mo-phong"
---


<div class="abox"><p><strong>Performance-Based Design (PBD)</strong> is a fire engineering methodology in which compliance with fire safety objectives is demonstrated through calculation and simulation — rather than prescriptive compliance with fixed dimensional parameters in a code. This article presents the methodological framework as set out in the <strong>SFPE Handbook of Fire Protection Engineering</strong> — the most widely referenced technical reference in the fire engineering field — and the key calculation steps when applying PBD to a project.</p></div>
<div class="trow"><span class="tag">SFPE Handbook</span><span class="tag">Performance-Based Design</span><span class="tag">ASET/RSET</span><span class="tag">Fire Simulation</span><span class="tag">Egress Modelling</span></div>

<h2>1. PBD vs prescriptive design — the fundamental difference</h2>
<p>Prescriptive design applies fixed quantitative requirements from a code — for example, minimum egress corridor width, maximum travel distance to a final exit, or minimum stair count — based on occupancy type and building scale. This approach is straightforward to check, but the parameters embedded in the code are calibrated for typical cases and may not suit buildings with unusual geometry, occupancy, or scale.</p>
<p>PBD is an alternative or complementary method applied when a building cannot meet one or more prescriptive requirements, or when a different design solution needs to be shown to achieve an equivalent level of safety. Rather than checking "does the building satisfy parameter X?", PBD answers the question: <em>"In the identified fire scenario, do occupants have sufficient time to reach safety before conditions in the building become untenable?"</em> The answer is demonstrated by engineering calculation — not by reference to a table of numbers.</p>
<p>In Vietnam, PBD is a permitted design method under QCVN where prescriptive requirements cannot be met, provided the design documentation includes a separate technical justification report and, typically, the endorsement of a panel of experts or the competent authority.</p>

<h2>2. The role of the SFPE Handbook</h2>
<p>The <em>SFPE Handbook of Fire Protection Engineering</em>, published by the Society of Fire Protection Engineers (SFPE), is the comprehensive technical reference for fire engineering calculation methods. It is not a mandatory code or standard, but an engineering reference document — analogous to a structural engineering design manual. The SFPE Handbook content most commonly used in PBD calculations includes:</p>
<ul>
<li>Methods for identifying and characterising design fire scenarios</li>
<li>Calculation models for heat release rate (HRR) by material type and fuel array</li>
<li>Methods for predicting smoke movement, temperature rise and visibility reduction within building spaces</li>
<li>Methods for calculating evacuation time, including detection time, occupant response time and travel time</li>
<li>Tenability criteria (threshold limits for human exposure to heat, toxic gas concentrations and smoke obscuration)</li>
</ul>
<p>In practice, these methods are applied through simulation software — primarily FDS (Fire Dynamics Simulator, developed by NIST) for fire and smoke modelling, and Pathfinder (developed by Thunderhead Engineering) for egress modelling.</p>

<h2>3. The ASET / RSET framework</h2>
<p>The central criterion of PBD is the demonstration that <strong>ASET &gt; RSET</strong> for all design fire scenarios:</p>
<ul>
<li><strong>ASET — Available Safe Egress Time:</strong> the time from ignition until conditions in the building become untenable for occupants — defined by tenability thresholds for temperature, toxic gas concentration and visibility.</li>
<li><strong>RSET — Required Safe Egress Time:</strong> the total time required for all occupants to reach a place of safety — the sum of detection time, alert time, pre-movement time and travel time.</li>
</ul>
<div class="ibox"><strong>Safety margin requirement</strong><p style="font-size:0.85rem;margin:0;color:#555">It is not sufficient to show ASET = RSET. Engineering practice requires a margin of safety — typically ASET ≥ 1.5 × RSET, or ASET − RSET ≥ a defined minimum duration (often 60–120 seconds), depending on the methodology adopted and the authority's requirements.</p></div>

<h2>4. Key calculation steps — PBD methodology</h2>
<h3>4.1 Design fire characterisation</h3>
<p>The design fire is the quantitative description of the fire that the building systems must be able to manage. Key parameters: heat release rate curve (growth phase, steady-state HRR, suppression or decay phase), fuel type and geometry, fire location and initial area. The SFPE Handbook provides HRR data for common materials and occupancies; the design fire is selected conservatively for the specific scenario being evaluated.</p>

<h3>4.2 Fire and smoke simulation (FDS / PyroSim)</h3>
<p>FDS (Fire Dynamics Simulator), developed by the US National Institute of Standards and Technology (NIST), solves the governing equations of fluid dynamics and combustion to simulate smoke movement, temperature distribution and visibility within the building geometry. PyroSim is the most widely used graphical pre-processor for FDS. Outputs are compared against tenability thresholds to determine ASET for each scenario.</p>

<h3>4.3 Egress modelling (Pathfinder)</h3>
<p>Pathfinder models occupant movement — accounting for occupant density, walking speed, door flow capacity and decision-making behaviour — to calculate the total time required for all occupants to reach a safe location. Occupant characteristics (age, mobility, familiarity with the building) are defined in accordance with SFPE guidance. The result is RSET for each scenario.</p>

<h3>4.4 Tenability criteria</h3>
<table class="ctb"><thead><tr><th>Parameter</th><th>Tenability threshold</th><th>Reference</th></tr></thead><tbody>
<tr><td>Air temperature</td><td>≤ 60°C (at 2 m above floor)</td><td>SFPE Handbook / ISO 13571</td></tr>
<tr><td>Radiant heat flux</td><td>≤ 2.5 kW/m²</td><td>ISO 13571</td></tr>
<tr><td>CO concentration</td><td>≤ 1,400 ppm (for short exposure)</td><td>ISO 13571</td></tr>
<tr><td>Visibility in smoke</td><td>≥ 10 m (large spaces) / ≥ 5 m (corridors)</td><td>SFPE / NFPA 92</td></tr>
<tr><td>O₂ concentration</td><td>≥ 15%</td><td>ISO 13571</td></tr>
</tbody></table>

<div class="fqs" itemscope itemtype="https://schema.org/FAQPage">
<h2>Frequently Asked Questions</h2>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">When is PBD required in Vietnam, versus prescriptive design?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">PBD is used when a building cannot satisfy one or more prescriptive requirements of QCVN — for example, a super high-rise that exceeds QCVN 06's height limits, a building with unusually large atria, or an irregular floor plan where prescriptive travel distances cannot be met. PBD is also used when a project proposes an alternative design solution (e.g. a different suppression system type) and must demonstrate equivalent safety. The dossier requires a technical justification report and expert panel endorsement or authority approval.</p></div>
</div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<p class="fqq" itemprop="name">What is the difference between FDS and CFD smoke modelling?</p>
<div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">FDS (Fire Dynamics Simulator) is a specialist CFD (computational fluid dynamics) code developed specifically for fire and smoke scenarios — it includes combustion sub-models, soot generation and radiation heat transfer. General-purpose CFD tools (Fluent, OpenFOAM) can be used for smoke modelling but require more specialist calibration for fire applications. FDS is the internationally recognised standard tool for fire engineering simulation and is accepted by fire authorities in most jurisdictions where PBD is permitted.</p></div>
</div>
</div>
<div class="ctabox"><h3>Need PBD analysis and fire simulation for your project?</h3><p>VIETSAFE E&amp;C provides FDS fire simulation, Pathfinder egress modelling, ASET/RSET analysis, and complete technical justification dossiers for complex and non-standard projects.</p><a href="/en/pbd.html" class="btnw">Learn more about our PBD services →</a></div>
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

