# 구조화 데이터(JSON-LD) 생성 — 메인부터 전 페이지에 일괄 적용.
# build.py 가 페이지마다 호출해 <head> 에 삽입한다.
import html
import json
import re

from .site import (BASE_URL, BRAND, PHONE, RATING_COUNT, RATING_VALUE,
                   REVIEWS)

_BASE = BASE_URL.rstrip("/")


def _script(obj: dict) -> str:
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(obj, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


def _review_nodes():
    """REVIEWS 데이터를 schema.org Review 노드로 변환."""
    nodes = []
    for r in REVIEWS:
        nodes.append({
            "@type": "Review",
            "datePublished": r["date"],
            "author": {"@type": "Person", "name": r["author"]},
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": r["rating"],
                "bestRating": "5",
                "worstRating": "1",
            },
            "name": r["title"],
            "reviewBody": r["body"],
        })
    return nodes


def business_node() -> dict:
    """사이트 공통 LocalBusiness 노드 — 평점·후기 포함."""
    return {
        "@type": ["LocalBusiness", "HealthAndBeautyBusiness"],
        "@id": _BASE + "/#business",
        "name": BRAND,
        "telephone": PHONE,
        "url": _BASE + "/",
        "image": _BASE + "/assets/og-image.png",
        "logo": _BASE + "/assets/icon-512.png",
        "description": "영등포구 전지역 방문 출장마사지·홈타이 예약 안내",
        "address": {
            "@type": "PostalAddress",
            "addressRegion": "서울특별시",
            "addressLocality": "영등포구",
            "addressCountry": "KR",
        },
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": "서울특별시 영등포구",
        },
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday",
            ],
            "opens": "00:00",
            "closes": "23:59",
        },
        "priceRange": "₩90,000 - ₩180,000",
        "currenciesAccepted": "KRW",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": RATING_VALUE,
            "reviewCount": RATING_COUNT,
            "bestRating": "5",
            "worstRating": "1",
        },
        "review": _review_nodes(),
    }


def _website_node() -> dict:
    return {
        "@type": "WebSite",
        "@id": _BASE + "/#website",
        "url": _BASE + "/",
        "name": BRAND + " — 영등포 출장마사지·홈타이 안내",
        "inLanguage": "ko-KR",
        "publisher": {"@id": _BASE + "/#business"},
    }


def _breadcrumb_node(crumbs, title, canonical) -> dict:
    """[(label, href), ...] + 현재 페이지 → BreadcrumbList."""
    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "홈",
        "item": _BASE + "/",
    }]
    pos = 2
    for label, href in crumbs:
        node = {"@type": "ListItem", "position": pos, "name": label}
        if href:
            node["item"] = _BASE + href
        else:
            node["item"] = canonical
        items.append(node)
        pos += 1
    return {
        "@type": "BreadcrumbList",
        "@id": canonical + "#breadcrumb",
        "itemListElement": items,
    }


def _faq_nodes_from_body(body: str):
    """본문 .faq-item(h3 질문 / p 답변)을 FAQPage mainEntity 로 추출."""
    items = re.findall(
        r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>',
        body, flags=re.S,
    )
    entities = []
    for q, a in items:
        q = html.unescape(re.sub(r"<[^>]+>", "", q)).strip()
        a = html.unescape(re.sub(r"<[^>]+>", "", a)).strip()
        if not q or not a:
            continue
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        })
    return entities


def page_jsonld(page: dict, canonical: str, body: str) -> str:
    """페이지별 JSON-LD 묶음을 반환한다.
    - 모든 페이지: WebSite + LocalBusiness(평점·후기) + WebPage + BreadcrumbList
    - FAQ 섹션이 있으면 FAQPage 추가
    """
    is_home = page.get("path", "") == ""
    crumbs = page.get("breadcrumb") or []

    webpage = {
        "@type": "WebPage",
        "@id": canonical + "#webpage",
        "url": canonical,
        "name": page["title"],
        "description": page["desc"],
        "inLanguage": "ko-KR",
        "isPartOf": {"@id": _BASE + "/#website"},
        "about": {"@id": _BASE + "/#business"},
        "primaryImageOfPage": _BASE + "/assets/og-image.png",
    }
    breadcrumb = _breadcrumb_node(crumbs, page["title"], canonical)
    webpage["breadcrumb"] = {"@id": breadcrumb["@id"]}

    graph = [_website_node(), business_node(), webpage, breadcrumb]

    out = [_script({"@context": "https://schema.org", "@graph": graph})]

    faq = _faq_nodes_from_body(body)
    if faq:
        out.append(_script({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "@id": canonical + "#faq",
            "mainEntity": faq,
        }))

    return "\n".join(out) + "\n"


def stars(rating: str) -> str:
    """별점 문자열(★★★★★) 생성."""
    n = int(round(float(rating)))
    return "★" * n + "☆" * (5 - n)


def reviews_block() -> str:
    """후기 페이지에 노출되는 대표 후기 카드 + 종합 평점.
    구조화 데이터(review/aggregateRating)와 동일한 내용을 화면에도 표기한다."""
    cards = []
    for r in REVIEWS:
        cards.append(f"""    <li class="review-card">
      <div class="review-head">
        <span class="review-stars" aria-label="별점 {r['rating']}점">{stars(r['rating'])}</span>
        <span class="review-meta">{r['area']} · {r['theme']} · {r['time']} 이용</span>
      </div>
      <p class="review-title">{r['title']}</p>
      <p class="review-body">{r['body']}</p>
      <p class="review-author">{r['author']} 님 · {r['date']}</p>
    </li>""")
    cards_html = "\n".join(cards)
    return f"""
<section id="list">
<h2>이용자 대표 후기</h2>
<div class="rating-summary">
  <span class="rating-score">{RATING_VALUE}</span>
  <span class="rating-stars" aria-hidden="true">{stars(RATING_VALUE)}</span>
  <span class="rating-count">실제 이용 확인 후기 {RATING_COUNT}건 기준</span>
</div>
<ul class="review-list">
{cards_html}
</ul>
<p class="review-note">후기는 이용이 확인된 예약 건에 한해 등록되며, 낮은 평가도 지우지 않고 그대로 보여드립니다.</p>
</section>
"""
