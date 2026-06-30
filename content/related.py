# 롱테일 내부링크 컴포넌트 — 지역·역·테마 페이지 하단에 문맥형 링크를 붙인다.
# 페이지명(name)을 앵커 텍스트에 녹여 롱테일 검색의도와 일치시킨다.
# 키워드 나열이 아니라 "주제형 안내 링크"로 구성해 도어웨이를 피한다.


def _render(name: str, intro: str, links) -> str:
    items = "\n".join(
        f'  <li><a href="{href}"><span class="rl-q">{label}</span>'
        f'<span class="rl-go">바로가기 →</span></a></li>'
        for label, href in links
    )
    return f"""
<section class="related-links" aria-label="{name} 관련 안내">
<h2>{name} 이런 주제로 많이 찾으세요</h2>
<p>{intro}</p>
<ul class="rl-grid">
{items}
</ul>
</section>
"""


def area_links(name: str) -> str:
    """지역(동) 페이지용 롱테일 내부링크."""
    links = [
        (f"{name} 출장마사지 코스별 요금", "/courses/#price"),
        (f"{name} 24시간 심야 방문 예약", "/themes/24hours/"),
        (f"{name} 홈타이 스웨디시 안내", "/themes/swedish/"),
        (f"{name} 아로마 커플 관리", "/themes/couple/"),
        (f"{name} 인근 지하철역 출장 안내", "/yeongdeungpo/stations/"),
        (f"{name} 이용 후기·평점 보기", "/reviews/"),
        (f"{name} 처음 이용 방문 가이드", "/guide/#first"),
        ("영등포구 전지역 지역 안내", "/yeongdeungpo/"),
    ]
    return _render(
        name,
        f"{name}에서 자주 찾는 주제를 모았습니다. 원하시는 안내로 바로 이동하세요.",
        links,
    )


def station_links(name: str) -> str:
    """지하철역 페이지용 롱테일 내부링크."""
    links = [
        (f"{name} 인근 출장마사지 코스 요금", "/courses/#price"),
        (f"{name} 숙소·오피스텔 심야 방문", "/themes/24hours/"),
        (f"{name} 홈타이 스웨디시 안내", "/themes/swedish/"),
        (f"{name} 호텔식 마사지 안내", "/themes/hotel-style/"),
        (f"{name} 주변 지역별 방문 안내", "/yeongdeungpo/"),
        (f"{name} 이용 후기·평점 보기", "/reviews/"),
        (f"{name} 예약 방법 안내", "/reservation/#how"),
        ("영등포 지하철역 전체 안내", "/yeongdeungpo/stations/"),
    ]
    return _render(
        name,
        f"{name} 인근에서 자주 찾는 주제를 모았습니다. 원하시는 안내로 바로 이동하세요.",
        links,
    )


def theme_links(name: str) -> str:
    """테마 페이지용 롱테일 내부링크."""
    links = [
        (f"{name} 코스별 요금 안내", "/courses/#price"),
        (f"{name} 24시간 심야 예약", "/themes/24hours/"),
        (f"{name} 영등포구 지역별 방문", "/yeongdeungpo/"),
        (f"{name} 역세권 인근 방문 안내", "/yeongdeungpo/stations/"),
        (f"{name} 이용 후기·평점 보기", "/reviews/"),
        (f"{name} 예약 방법 안내", "/reservation/#how"),
        (f"{name} 처음 이용 가이드", "/guide/#first"),
        ("전체 관리 테마 한눈에 보기", "/themes/"),
    ]
    return _render(
        name,
        f"{name}와 함께 자주 찾는 주제를 모았습니다. 원하시는 안내로 바로 이동하세요.",
        links,
    )
