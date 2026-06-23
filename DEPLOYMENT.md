# 11ty Migration - Deployment Guide

## Project Status

✅ 11ty project is ready for deployment
- Build: `npm run build` generates 17 HTML files
- 14 article pages (7 VI + 7 EN) migrated
- Listing pages created
- Vercel config ready

## Next Steps

### 1. Create GitHub Repository

```bash
# Option A: New repo for 11ty version
git remote add origin https://github.com/vsec2025/vietsafe-11ty.git
git branch -M main
git push -u origin main

# Option B: New branch in existing repo
git remote add origin https://github.com/vsec2025/vietsafe-website.git
git branch -M 11ty-migration
git push -u origin 11ty-migration
```

### 2. Setup Vercel

1. Go to https://vercel.com/
2. Click "Add New..." → "Project"
3. Import from GitHub (select the repo)
4. Framework: **11ty** (or Custom)
5. Build command: `npm run build`
6. Output directory: `_site`
7. Deploy!

### 3. Update Domain

In Vercel project settings:
- Add custom domain: `www.vnsec.com.vn`
- Update DNS records (your domain provider)

## What's in the Box

```
vietsafe-11ty/
├── src/
│   ├── content/           # All markdown content
│   │   ├── vi/           # Vietnamese pages
│   │   │   ├── index.md
│   │   │   ├── kien-thuc-index.md
│   │   │   └── kien-thuc/*.md (7 articles)
│   │   └── en/           # English pages
│   │       ├── index.md
│   │       ├── kien-thuc-index.md
│   │       └── kien-thuc/*.md (7 articles)
│   └── _includes/
│       ├── layouts/      # Page templates
│       ├── components/   # Header, footer
│       └── css-bundle.njk
├── .eleventy.js          # Config
├── vercel.json           # Vercel deployment config
└── package.json          # Dependencies

_site/                    # Build output (17 HTML files)
```

## Development Workflow

### Edit Content
```bash
# Edit markdown files in src/content/
# Changes automatically reflected in _site/ on build
```

### Build & Preview
```bash
npm run build      # One-time build
npm run serve      # Local dev server (http://localhost:8080)
```

### Add New Article
1. Create `src/content/vi/kien-thuc/slug.md`
2. Add frontmatter (title, description, date, category, permalink)
3. Add content
4. Create corresponding `src/content/en/kien-thuc/slug.md`
5. Update listing pages (`kien-thuc-index.md`)
6. Commit & push

## Benefits Over Old HTML

✅ **No code duplication** — header/footer/CSS once, used everywhere
✅ **Add articles in seconds** — just create markdown file
✅ **Easy to maintain** — change CSS once, applies to all pages
✅ **Automatic builds** — Vercel rebuilds on every push
✅ **Version control** — clean git history
✅ **SEO-friendly** — static HTML with proper hreflang

## Troubleshooting

### Build fails with "Output conflict"
- Two files have same permalink
- Check `src/content/` for duplicates

### Local serve not working
```bash
npm install -g @11ty/eleventy
npm run serve
```

### Need to add more pages
- Add to `src/content/vi/` and `src/content/en/`
- Update listing pages
- Commit & push
- Vercel auto-rebuilds

---

**Ready to go live!** Questions? Check `.eleventy.js` or run `npm run debug` for verbose output.
