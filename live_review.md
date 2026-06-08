# In-Depth Website Review: BobSteeger.com

This report provides a technical and content-focused review of the live website at `bobsteeger.com` as of April 11, 2026.

## 1. Technical Architecture
- **Host Platform:** Blogger (Google hosted).
- **Domain Mapping:** `bobsteeger.com` is mapped via CNAME to `bobsteeger.blogspot.com`.
- **Template System:** Blogger "Simple" Template (Layout V2).
- **Asset Delivery:** Most assets (CSS/JS) are delivered via `resources.blogblog.com` and `www.blogger.com` CDNs.

## 2. SEO & Visibility
- **Title Tags:** Optimized for personal branding (e.g., "Bob Steeger", "Bob Steeger: Online Resume").
- **Meta Descriptions:** Present and aligned with professional positioning ("Product Executive & Business Systems Architect").
- **Semantic HTML:** Uses `<header>`, `<nav>`, and `<article>` structures typical of Blogger's templates.
- **Social Integration:** OpenGraph (`og:`) tags are configured for URL, Title, and Description, ensuring clean previews on LinkedIn/Twitter.
- **Sitemaps:** The site exposes both `sitemap.xml` (posts) and `sitemap-pages.xml` (static pages), aiding search engine indexing.

## 3. Design & User Experience
- **Theme:** A modified "Simple" Blogger theme with a distinctive orange/black/white professional palette.
- **Typography:** Relies on Arial/Helvetica/FreeSans but renders cleanly.
- **Responsiveness:** Uses Blogger's responsive mobile view (`viewport` metatag present).
- **Layout:** High-impact "hero" section on the home page with a clear value proposition followed by structured "Where I Operate" sections.

## 4. Content Analysis
- **Home Page:** Serves as a high-level landing page focusing on "Driving Durable Growth" and "Business Systems Architecture."
- **Online Resume:** A comprehensive, single-page professional history. It is data-dense but readable, featuring bulleted successes at AWS, Verizon, and AOL.
- **Blog Content:** Currently features a single anchor post from March 2026, suggesting a recent site refresh or focused content strategy.

## 5. Portability & Archive Status
The site has been successfully exported to the `live/` folder.
- **Pages Captured:** Home, Online Resume, Blog Post.
- **Localization:** Key CSS bundles and Javascript widgets have been downloaded and paths updated to relative references.
- **Note:** Some dynamic features (like the Blogger Navbar iframe or comment systems) require an active connection to Blogger and may not fully function in a local static preview.
