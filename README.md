# Website VIETSAFE E&C — vnsec.com.vn

Trang web giới thiệu **Công ty Cổ Phần VIETSAFE E&C** — tư vấn & thiết kế an toàn cháy nổ PCCC.

## Stack kỹ thuật

- **Hosting**: Vercel (auto-deploy từ GitHub `main`)
- **CMS**: Decap CMS tại `/admin` (cần Netlify Identity)
- **Domain**: `www.vnsec.com.vn`

## Cấu trúc thư mục

```
/
├── index.html          — Trang chủ (toàn bộ nội dung & giao diện)
├── pbd.html            — Trang dịch vụ PBD & Mô phỏng
├── netlify.toml        — Cấu hình Netlify (headers, redirects)
├── robots.txt          — SEO crawl rules
├── sitemap.xml         — XML sitemap
├── admin/
│   ├── index.html      — Decap CMS entry point
│   ├── config.yml      — CMS collections config
│   └── oauth-callback.html
├── kien-thuc/          — Bài viết kỹ thuật PCCC
│   ├── index.html      — Trang danh sách bài viết
│   └── *.html          — Các bài viết
├── hoat-dong/          — Hoạt động công ty
│   └── index.html      — Trang danh sách hoạt động
├── images/
│   └── uploads/        — Ảnh upload qua CMS
└── *.jpg               — Ảnh hero & sector (01–13)
```

## Thay ảnh

Ghi đè file cùng tên rồi push lên GitHub — Vercel tự deploy lại:
- `01-hero.jpg` — Ảnh hero trang chủ
- `02-07-sector-*.jpg` — Ảnh 6 lĩnh vực
- `08-13-project-*.jpg` — Ảnh 6 dự án tiêu biểu

## CMS Biên soạn bài viết

Truy cập: `https://www.vnsec.com.vn/admin`

Yêu cầu: Netlify Identity được kích hoạt trên site Netlify kết nối với repo này.

Collections:
- **Kiến thức PCCC** — bài viết kỹ thuật, pháp lý, tiêu chuẩn
- **Hoạt động công ty** — tin tức, dự án, sự kiện

## Cập nhật lần cuối

2026-06-12 — Fix UTF-8 encoding, nâng cấp CMS config
