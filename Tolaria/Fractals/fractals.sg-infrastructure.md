# fractals.sg — Site Infrastructure

## Current Setup (as of Jul 22, 2026)

### Hosting
- **Origin server:** Hermes VPS (Hostinger KVM 1, IP `153.92.4.147`)
- **Edge:** Cloudflare proxy (CDN, SSL termination, DDoS protection)
- **Web server:** Caddy 2.6.2 — `file_server` at `/var/www/fractals.sg/`
- **SSL:** Let's Encrypt (auto-managed by Caddy)

### DNS
- **Registrar:** Exabytes (.sg domain)
- **Nameservers:** `cortney.ns.cloudflare.com` / `will.ns.cloudflare.com`
- **Cloudflare proxy status:**
  - Proxied (orange cloud): `fractals.sg` A + AAAA, `www` CNAME
  - DNS only (grey cloud): all subdomain records (hermes, crm, vault, workspace, chasr, changelog, geo, stats, n8n, api, dashboard) and all email records (MX, TXT, DKIM, SPF, DMARC)

### Migration History

#### Why we moved
On Jul 19, 2026, a Hostinger `deployStaticWebsite` archive only contained `index.html` (canonical URL fix). The MCP tool wipes and replaces the entire `public_html`, so `pr-playbook/`, `media-playbook/`, `projects/`, `sitemap.xml`, and `robots.txt` were silently deleted. This exposed a fundamental problem with the zip-deploy cycle.

#### Migration steps (Jul 21)
1. Copied site files to `/var/www/fractals.sg/`
2. Added Caddy block for `fractals.sg, www.fractals.sg` with `file_server`
3. Updated DNS A record at Hostinger from `156.67.222.23` → `153.92.4.147`
4. Temporarily removed AAAA record (Let's Encrypt ACME was caching old IPv6)
5. Obtained Let's Encrypt certs for both bare and www domains
6. Re-added AAAA record for VPS IPv6
7. Fixed file permissions (Caddy runs as `caddy` user, files need 644 not 600)

#### Cloudflare setup (Jul 22)
The VPS IP (`153.92.4.147`) was blocked by Google corporate network firewalls (common for VPS hosting ranges). Added Cloudflare proxy so visitors connect to Cloudflare IPs instead.

Steps:
1. Created Cloudflare free account
2. Added fractals.sg, reviewed scanned DNS (25 records)
3. Set proxy toggles: root + www proxied, everything else DNS only
4. Changed nameservers at Exabytes to Cloudflare's (`cortney.ns.cloudflare.com`, `will.ns.cloudflare.com`)
5. Set Cloudflare SSL/TLS to Full (strict)

### File Structure
```
/var/www/fractals.sg/
├── index.html           # Hub page
├── pr-playbook/         # PR & Communications Playbook
├── media-playbook/      # Media Playbook
├── projects/            # Solo-built products
├── sitemap.xml
└── robots.txt
```

### Workflow Changes
- **Before:** Edit → zip → MCP deploy (wipe-and-replace risk)
- **Now:** Edit → `caddy reload` (instant, zero risk)

### Key Lessons
- `deployStaticWebsite` is wipe-and-replace — always archive the full site
- File permissions matter: Caddy runs as `caddy` user, index files need 644
- ACME rate limits extend with each failed attempt; wait them out
- Corporate networks commonly block VPS IP ranges; Cloudflare proxy is the standard fix
