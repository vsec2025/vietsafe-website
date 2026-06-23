---
layout: "layouts/article.njk"
title: "PCCC cho Hệ thống Lưu trữ Pin BESS — Áp dụng NFPA 855 tại Việt Nam"
description: "Hướng dẫn thiết kế PCCC cho hệ thống lưu trữ pin BESS theo NFPA 855: phân loại EQ, phát hiện thermal runaway, hệ thống suppression và luận chứng kỹ thuật theo Luật PCCC 55/2024."
lang: "vi"
permalink: "/kien-thuc/pccc-bess-nfpa-855.html"
date: 2026-06-11
category: "ky-thuat"
---

<div class="abox"><p><strong>PCCC cho hệ thống lưu trữ pin BESS (Battery Energy Storage System)</strong> áp dụng tiêu chuẩn NFPA 855 kết hợp QCVN 01:2021/BCA. BESS là công trình đặc thù vì nguy cơ cháy pin lithium-ion (thermal runaway) khác hoàn toàn với cháy thông thường — yêu cầu hệ thống phát hiện nhiệt sớm, suppression chuyên dụng, và quy trình chữa cháy riêng.</p></div>
<div class="trow"><span class="tag">NFPA 855</span><span class="tag">BESS Fire Safety</span><span class="tag">Thermal Runaway</span><span class="tag">QCVN 01</span><span class="tag">Lithium-ion</span><span class="tag">ESS</span></div>
<h2>1. Tại sao BESS cần giải pháp PCCC riêng?</h2>
<p>Hệ thống lưu trữ pin BESS đang bùng nổ tại Việt Nam theo làn sóng năng lượng tái tạo. Tuy nhiên, hầu hết QCVN hiện hành <strong>không có điều khoản cụ thể</strong> cho nguy cơ cháy pin lithium-ion. Điểm nguy hiểm nhất là hiện tượng <strong>thermal runaway</strong>: một tế bào pin quá nhiệt kích hoạt tế bào kế cận, tạo chuỗi phản ứng khó dập tắt, giải phóng khí độc HF và CO ngay cả khi không có ngọn lửa nhìn thấy.</p>
<div class="ibox"><strong>📌 Thực tế sự cố</strong><p style="font-size:0.85rem;margin:0;color:#555">Nhiều vụ cháy BESS lớn (Arizona 2019, Liverpool 2021) cho thấy sprinkler thông thường không đủ kiểm soát thermal runaway — cần phát hiện nhiệt sớm và làm mát kéo dài sau sự cố.</p></div>
<h2>2. Tiêu chuẩn áp dụng cho PCCC BESS tại Việt Nam</h2>
<table class="ctb"><thead><tr><th>Tiêu chuẩn</th><th>Nội dung</th><th>Loại BESS</th></tr></thead><tbody>
<tr><td><strong>NFPA 855 (2023)</strong></td><td>Yêu cầu lắp đặt ESS tĩnh: phân khoang, ventilation, suppression, emergency response</td><td>Tất cả</td></tr>
<tr><td><strong>NFPA 13</strong></td><td>Hệ thống sprinkler tự động — mật độ phun cho buồng BESS</td><td>Container/indoor</td></tr>
<tr><td><strong>NFPA 72</strong></td><td>Hệ thống báo cháy và early-warning detection</td><td>Tất cả</td></tr>
<tr><td><strong>UL 9540A</strong></td><td>Test method cho thermal runaway fire propagation</td><td>Lithium-ion</td></tr>
<tr><td><strong>QCVN 01:2021/BCA</strong></td><td>Yêu cầu PCCC cơ bản theo pháp luật Việt Nam</td><td>Tất cả</td></tr>
</tbody></table>
<h2>3. Yêu cầu thiết kế theo NFPA 855</h2>
<h3>3.1 Phân loại và giới hạn năng lượng (EQ)</h3>
<ul><li><strong>EQ ≤ 20 kWh/buồng:</strong> miễn giảm — áp dụng hộ gia đình</li><li><strong>EQ 20–600 kWh:</strong> phân khoang, ventilation, detection và suppression theo Chương 12</li><li><strong>EQ &gt; 600 kWh:</strong> yêu cầu luận chứng kỹ thuật và phân tích rủi ro</li></ul>
<h3>3.2 Phát hiện cháy sớm — 3 lớp</h3>
<ul><li>Cảm biến nhiệt tế bào (cell-level thermal monitoring) — tích hợp trong BMS</li><li>Phát hiện khí: CO, H₂, HF — nhận biết thermal runaway từ sớm</li><li>Báo khói/nhiệt thông thường (NFPA 72) — lớp cuối cùng</li></ul>
<h3>3.3 Hệ thống suppression</h3>
<ul><li><strong>Nước phun sương (water mist):</strong> làm mát hiệu quả — phổ biến nhất</li><li><strong>Khí sạch (CO₂, FK-5-1-12):</strong> cho buồng kín nhỏ</li><li><strong>Sprinkler ESFR/CMSA:</strong> cho kho BESS lớn theo NFPA 13 + NFPA 855</li></ul>
<h2>4. Thủ tục PCCC theo Luật PCCC 55/2024</h2>
<p>Theo các bản tin gần đây, thủ tục PCCC đang được điều chỉnh theo hướng đơn giản hóa và tăng cường hậu kiểm. Trong bối cảnh đó, đối với dự án BESS, chủ đầu tư thường được khuyến nghị: (1) xây dựng hồ sơ PCCC tham chiếu NFPA 855 và QCVN liên quan; (2) lập luận chứng kỹ thuật so sánh với QCVN; (3) chuẩn bị hồ sơ để xuất trình khi cơ quan chức năng yêu cầu; (4) có kế hoạch kiểm tra định kỳ và ứng cứu khẩn cấp chuyên biệt. Quy định và thời điểm áp dụng cụ thể đề nghị tham khảo văn bản pháp luật hiện hành.</p>
<div class="fqs" itemscope itemtype="https://schema.org/FAQPage">
<h2>Câu hỏi thường gặp</h2>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"><p class="fqq" itemprop="name">BESS lắp trên mái nhà áp dụng NFPA 855 như thế nào?</p><div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">Theo NFPA 855 Chương 15, BESS lắp ngoài trời và trên mái cần tuân thủ khoảng cách an toàn đến lối thoát nạn và kết cấu tòa nhà. Tại Việt Nam cần lập luận chứng kỹ thuật theo Luật PCCC 55/2024 để cơ quan thẩm định xem xét nếu có yêu cầu.</p></div></div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"><p class="fqq" itemprop="name">Thermal runaway khác cháy thông thường như thế nào?</p><div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">Thermal runaway là phản ứng nhiệt hóa học tự duy trì trong tế bào pin, tạo nhiệt, khí độc HF, CO và ngọn lửa ngay cả không có oxy. Cần làm mát liên tục nhiều giờ để ngăn lan dây chuyền, lực lượng chữa cháy cần SCBA đặc biệt.</p></div></div>
</div>
<div class="srcbox" style="margin:1.5rem 0;padding:1rem 1.2rem;border-left:3px solid #c0392b;background:#faf6f6;font-size:0.9rem;line-height:1.6"><p style="font-weight:600;margin-bottom:0.5rem">Tổng hợp từ các nguồn:</p><ul style="margin:0;padding-left:1.2rem"><li>Tiêu chuẩn NFPA 855, NFPA 850 về hệ thống lưu trữ năng lượng (BESS) và QCVN liên quan.</li><li>Cổng Thông tin điện tử Chính phủ — quy định về thủ tục PCCC: <a href="https://vanban.chinhphu.vn" target="_blank" rel="noopener">vanban.chinhphu.vn</a></li><li>Báo Tuổi Trẻ: <a href="https://tuoitre.vn" target="_blank" rel="noopener">tuoitre.vn</a>; Báo Thanh Niên: <a href="https://thanhnien.vn" target="_blank" rel="noopener">thanhnien.vn</a></li></ul><p style="margin-top:0.5rem;font-style:italic;color:#666">Nội dung mang tính tham khảo kỹ thuật, không thay thế cho tư vấn pháp lý chính thức. Đề nghị tham khảo văn bản pháp luật hiện hành và hướng dẫn của cơ quan chức năng.</p></div>
<div class="ctabox"><h3>Cần tư vấn PCCC chuyên sâu?</h3><p>Đội ngũ kỹ sư VIETSAFE E&amp;C hỗ trợ từ luận chứng kỹ thuật đến mô phỏng và hồ sơ.</p><a href="/#contact" class="btnw">Liên hệ ngay →</a></div>
