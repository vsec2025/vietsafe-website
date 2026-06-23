---
layout: "layouts/article.njk"
title: "Tính toán Thiết kế theo Hiệu năng (PBD) theo SFPE Handbook"
description: "Tổng quan về thiết kế PCCC theo hiệu năng (Performance-Based Design) theo SFPE Handbook: kịch bản cháy thiết kế, mô phỏng cháy khói, tính ASET/RSET, và khi nào công trình cần áp dụng phương pháp này."
lang: "vi"
permalink: "/kien-thuc/tinh-toan-pbd-theo-sfpe.html"
date: 2026-05-28
category: "mo-phong"
---



<div class="abox"><p>Thiết kế theo hiệu năng (Performance-Based Design — PBD) là phương pháp thiết kế PCCC dựa trên việc chứng minh công trình đáp ứng các mục tiêu an toàn cụ thể bằng tính toán và mô phỏng, thay vì chỉ tuân theo các thông số định lượng cố định trong quy chuẩn. Bài viết này trình bày khung phương pháp luận theo SFPE Handbook — tài liệu kỹ thuật được tham chiếu phổ biến nhất trong lĩnh vực kỹ thuật PCCC — và các bước tính toán chính khi áp dụng PBD cho một công trình.</p></div>

<div class="trow"><span class="tag">SFPE Handbook</span><span class="tag">Performance-Based Design</span><span class="tag">ASET/RSET</span><span class="tag">Mô phỏng cháy</span><span class="tag">Mô phỏng thoát nạn</span></div>

<h2>1. PBD khác gì với thiết kế theo quy định (prescriptive)?</h2>
<p>Thiết kế theo quy định (prescriptive design) áp dụng các yêu cầu định lượng có sẵn trong quy chuẩn — ví dụ chiều rộng lối thoát nạn tối thiểu, khoảng cách tới lối ra gần nhất, hoặc số lượng cầu thang thoát nạn — dựa trên loại công năng và quy mô công trình. Phương pháp này có ưu điểm là đơn giản, dễ kiểm tra, nhưng các thông số trong quy chuẩn được xây dựng cho các trường hợp điển hình và có thể không phù hợp với công trình có hình dạng, công năng hoặc quy mô đặc biệt.</p>
<p>PBD là phương pháp thay thế hoặc bổ sung, áp dụng khi công trình không đáp ứng một hoặc một số yêu cầu định lượng của quy chuẩn, hoặc khi cần chứng minh một giải pháp thiết kế khác đạt mức an toàn tương đương. Thay vì kiểm tra "có đáp ứng thông số X không", PBD trả lời câu hỏi "trong kịch bản cháy được xác định, người sử dụng công trình có đủ thời gian thoát ra trước khi điều kiện môi trường trở nên nguy hiểm không". Câu trả lời được chứng minh bằng tính toán kỹ thuật, không phải bằng việc đối chiếu một bảng số liệu.</p>
<p>Tại Việt Nam, PBD được quy định là một phương pháp được phép áp dụng trong các trường hợp công trình không đáp ứng yêu cầu của QCVN, với điều kiện hồ sơ thiết kế phải có luận chứng kỹ thuật riêng và thường cần ý kiến của hội đồng chuyên gia hoặc cơ quan có thẩm quyền.</p>

<h2>2. Vai trò của SFPE Handbook</h2>
<p>SFPE Handbook of Fire Protection Engineering, do Society of Fire Protection Engineers (Hiệp hội Kỹ sư Phòng cháy Hoa Kỳ) biên soạn, là tài liệu kỹ thuật tổng hợp các phương pháp tính toán dùng trong kỹ thuật PCCC. Đây không phải một quy chuẩn hay tiêu chuẩn bắt buộc áp dụng, mà là tài liệu tham khảo kỹ thuật (engineering reference) — tương tự vai trò của một sổ tay tính toán kết cấu trong ngành xây dựng.</p>
<p>Các nội dung trong SFPE Handbook thường được sử dụng khi tính toán PBD bao gồm:</p>
<ul>
<li>Phương pháp xác định và mô tả kịch bản cháy thiết kế (design fire scenarios)</li>
<li>Các mô hình tính toán tốc độ giải phóng nhiệt (heat release rate) theo loại vật liệu và bố trí cháy</li>
<li>Phương pháp tính lan truyền khói, nhiệt độ và tầm nhìn trong không gian công trình</li>
<li>Phương pháp tính thời gian thoát nạn, bao gồm thời gian phát hiện, thời gian phản ứng và thời gian di chuyển</li>
<li>Các ngưỡng giới hạn chịu đựng của con người (tenability criteria) đối với nhiệt độ, nồng độ khí độc và tầm nhìn trong khói</li>
</ul>
<p>Trong thực hành, các nội dung này được áp dụng thông qua phần mềm mô phỏng — phổ biến nhất là FDS (Fire Dynamics Simulator) cho mô phỏng cháy và khói, và Pathfinder hoặc các phần mềm tương tự cho mô phỏng di chuyển thoát nạn.</p>

<h2>3. Quy trình tính toán PBD</h2>
<h3>3.1. Xác định mục tiêu an toàn và tiêu chí chấp nhận</h3>
<p>Bước đầu tiên là xác định mục tiêu thiết kế cần đạt được — thông thường là bảo đảm an toàn tính mạng cho người sử dụng công trình, hỗ trợ hoạt động chữa cháy và cứu nạn, và hạn chế thiệt hại tài sản. Từ mục tiêu này, các tiêu chí chấp nhận định lượng được xác định, ví dụ: nhiệt độ tại vùng đầu người không vượt quá một giá trị nhất định, nồng độ CO không vượt ngưỡng gây nguy hiểm trong thời gian thoát nạn, và tầm nhìn trong khói đủ để người sử dụng định hướng tới lối thoát.</p>

<h3>3.2. Xây dựng kịch bản cháy thiết kế</h3>
<p>Kịch bản cháy thiết kế (design fire scenario) mô tả vị trí phát sinh cháy, loại vật liệu cháy, tốc độ phát triển của đám cháy theo thời gian (đường cong heat release rate), và trạng thái của các hệ thống PCCC trong công trình tại thời điểm xảy ra cháy — ví dụ hệ thống chữa cháy tự động hoạt động hoặc không hoạt động, cửa ngăn cháy đóng hoặc mở. Việc lựa chọn kịch bản cần phản ánh các tình huống có khả năng xảy ra và mang tính bất lợi hợp lý cho công trình, không phải kịch bản cực đoan nhất về lý thuyết.</p>

<h3>3.3. Mô phỏng cháy và khói — tính ASET</h3>
<p>Với kịch bản cháy đã xác định, mô hình hóa được thực hiện bằng phần mềm FDS để tính toán sự lan truyền của khói, nhiệt và khí độc trong không gian công trình theo thời gian. Kết quả mô phỏng cho phép xác định thời điểm các tiêu chí chấp nhận (nhiệt độ, tầm nhìn, nồng độ khí độc) bị vượt ngưỡng tại từng vị trí trong công trình. Thời điểm sớm nhất mà điều kiện môi trường trở nên không còn an toàn cho người sử dụng được gọi là ASET (Available Safe Egress Time) — thời gian thoát nạn khả dụng.</p>

<h3>3.4. Mô phỏng thoát nạn — tính RSET</h3>
<p>Song song, mô hình thoát nạn được xây dựng bằng phần mềm như Pathfinder để mô phỏng quá trình người sử dụng di chuyển từ vị trí ban đầu tới lối thoát nạn an toàn. Thời gian này — RSET (Required Safe Egress Time) — bao gồm tổng của thời gian phát hiện cháy, thời gian cảnh báo và phản ứng của người sử dụng (pre-movement time), và thời gian di chuyển thực tế tới khu vực an toàn. Các thông số đầu vào như mật độ người, đặc điểm vận động (bao gồm người có khả năng vận động hạn chế nếu có), và độ quen thuộc với công trình đều ảnh hưởng đến kết quả tính toán.</p>

<h3>3.5. So sánh ASET và RSET</h3>
<p>Điều kiện an toàn được coi là thỏa mãn khi ASET lớn hơn RSET với một hệ số an toàn (margin of safety) phù hợp — hệ số này phản ánh các yếu tố bất định trong dữ liệu đầu vào và mô hình tính toán. Nếu ASET nhỏ hơn hoặc gần bằng RSET, phương án thiết kế cần được điều chỉnh — ví dụ tăng số lượng hoặc chiều rộng lối thoát nạn, bổ sung hệ thống hút khói, hoặc thay đổi bố trí công năng — và lặp lại quá trình tính toán cho đến khi đạt yêu cầu.</p>

<table class="ctb"><tr><th>Bước</th><th>Nội dung</th><th>Công cụ thường dùng</th></tr>
<tr><td>1</td><td>Xác định mục tiêu và tiêu chí chấp nhận</td><td>Tham chiếu SFPE Handbook, BS 7974</td></tr>
<tr><td>2</td><td>Xây dựng kịch bản cháy thiết kế</td><td>Phân tích công năng, tải trọng cháy</td></tr>
<tr><td>3</td><td>Mô phỏng cháy và khói — tính ASET</td><td>FDS / PyroSim</td></tr>
<tr><td>4</td><td>Mô phỏng thoát nạn — tính RSET</td><td>Pathfinder / STEPS</td></tr>
<tr><td>5</td><td>So sánh ASET–RSET, hiệu chỉnh thiết kế</td><td>Lặp lại bước 2–4 nếu cần</td></tr>
<tr><td>6</td><td>Lập báo cáo luận chứng kỹ thuật</td><td>Tổng hợp kết quả, kết luận</td></tr>
</table>

<h2>4. Khi nào công trình cần tính toán PBD</h2>
<p>PBD thường được áp dụng cho các trường hợp sau:</p>
<ul>
<li>Công trình có chiều cao hoặc khối tích vượt giới hạn áp dụng trực tiếp của quy chuẩn (nhà siêu cao tầng)</li>
<li>Không gian lớn, trần cao, khó áp dụng các thông số ngăn cháy hoặc hút khói theo quy định cứng (sảnh atrium, ga tàu, nhà ga sân bay, trung tâm thương mại)</li>
<li>Công trình có hình dạng mặt bằng hoặc bố trí lối thoát nạn không điển hình</li>
<li>Công năng hỗn hợp với mật độ sử dụng hoặc đặc điểm người sử dụng đa dạng</li>
<li>Trường hợp chủ đầu tư đề xuất giải pháp thiết kế khác với quy chuẩn nhưng cần chứng minh mức an toàn tương đương</li>
</ul>
<p>Trong các trường hợp này, báo cáo luận chứng kỹ thuật PBD là một phần của hồ sơ thiết kế trình thẩm duyệt, bên cạnh các tài liệu thiết kế PCCC thông thường.</p>

<div class="ibox"><strong>Lưu ý</strong><p style="font-size:0.85rem;margin:0;color:#555">Nội dung trên mang tính giới thiệu phương pháp luận, không thay thế cho việc tính toán cụ thể cho từng công trình. Kết quả tính toán PBD phụ thuộc vào dữ liệu đầu vào, giả định kịch bản, và yêu cầu của cơ quan thẩm duyệt đối với từng dự án.</p></div>

<div class="fqs" itemscope itemtype="https://schema.org/FAQPage">
<h2>Câu hỏi thường gặp</h2>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"><p class="fqq" itemprop="name">PBD có thể thay thế hoàn toàn thiết kế theo quy chuẩn không?</p><div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">Không. PBD thường được áp dụng cho các nội dung cụ thể mà công trình không đáp ứng quy chuẩn, trong khi các yêu cầu khác của quy chuẩn vẫn phải tuân thủ. PBD là phương pháp bổ sung, không phải phương pháp thay thế toàn bộ hệ thống quy chuẩn hiện hành.</p></div></div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"><p class="fqq" itemprop="name">ASET và RSET là gì?</p><div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">ASET (Available Safe Egress Time) là thời gian từ khi phát sinh cháy đến khi điều kiện môi trường tại một vị trí trở nên nguy hiểm, xác định từ mô phỏng cháy khói. RSET (Required Safe Egress Time) là thời gian cần thiết để người sử dụng di chuyển đến khu vực an toàn, xác định từ mô phỏng thoát nạn. Điều kiện an toàn được chứng minh khi ASET lớn hơn RSET với hệ số an toàn phù hợp.</p></div></div>
<div class="fqi" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question"><p class="fqq" itemprop="name">SFPE Handbook có phải là tiêu chuẩn bắt buộc áp dụng tại Việt Nam không?</p><div class="fqa" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"><p itemprop="text">SFPE Handbook là tài liệu tham khảo kỹ thuật, không phải quy chuẩn hay tiêu chuẩn bắt buộc. Khi áp dụng PBD tại Việt Nam, phương pháp tính toán theo SFPE Handbook thường được sử dụng làm cơ sở kỹ thuật trong báo cáo luận chứng, nhưng việc chấp thuận kết quả vẫn thuộc thẩm quyền của cơ quan thẩm duyệt theo từng dự án.</p></div></div>
</div>

<div class="ctabox"><h3>Dự án của bạn cần tính toán PBD?</h3><p>VIETSAFE E&amp;C thực hiện mô phỏng cháy khói (FDS), mô phỏng thoát nạn (Pathfinder), phân tích ASET/RSET và lập báo cáo luận chứng kỹ thuật cho công trình của bạn.</p><a href="/pbd.html" class="btnw">Xem dịch vụ PBD &amp; Mô phỏng →</a></div>


