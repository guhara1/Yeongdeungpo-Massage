# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://yeongdeungpo-massage.netlify.app"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 네이버 서치어드바이저 사이트 소유확인 코드(메인·전 페이지 <head> 삽입)
NAVER_VERIFY = "eb196d9f5e0ef425bd110168d3400e07d1bf1c14"

# 구조화 데이터(JSON-LD)용 평점·후기 데이터.
# aggregateRating/review 는 운영 중 실제 누적 후기를 반영해 갱신한다.
RATING_VALUE = "4.9"
RATING_COUNT = "327"

# 페이지에 노출되는 대표 후기 = 구조화 데이터 review 와 1:1로 일치시킨다.
REVIEWS = [
    {
        "author": "김O진", "rating": "5", "date": "2026-05-21",
        "area": "여의도동", "theme": "스웨디시", "time": "심야",
        "title": "심야인데 도착이 정확했어요",
        "body": "야근 끝나고 자정 넘어 예약했는데 안내해 준 시간에 딱 맞춰 오셨어요. 압도 처음에 말한 대로 맞춰주셔서 다음 날 몸이 가벼웠습니다.",
    },
    {
        "author": "이O수", "rating": "5", "date": "2026-05-09",
        "area": "영등포동", "theme": "아로마테라피", "time": "저녁",
        "title": "오피스텔 출입 안내가 편했습니다",
        "body": "처음 방문 예약이라 걱정했는데 공동현관 출입까지 미리 안내해 주셔서 수월했어요. 아로마 향도 과하지 않아 좋았고 관리 후 바로 잠들었습니다.",
    },
    {
        "author": "박O영", "rating": "5", "date": "2026-04-28",
        "area": "당산동", "theme": "타이마사지", "time": "오후",
        "title": "스트레칭 후 개운함이 확실",
        "body": "어깨가 늘 뭉쳐 있었는데 타이로 풀고 나니 목 돌리기가 한결 편해졌어요. 진행 내내 조용하고 정중했습니다. 재예약 의사 있어요.",
    },
    {
        "author": "정O아", "rating": "5", "date": "2026-04-15",
        "area": "문래동", "theme": "커플 관리", "time": "주말",
        "title": "커플로 같이 받기 좋았어요",
        "body": "기념일에 둘이 같이 받았습니다. 두 분이 동시에 진행해 주셔서 분위기도 좋고 시간도 알차게 썼어요. 예약 상담도 친절했습니다.",
    },
    {
        "author": "최O호", "rating": "4", "date": "2026-03-30",
        "area": "신길동", "theme": "발마사지", "time": "저녁",
        "title": "발 피로가 많이 풀렸습니다",
        "body": "하루 종일 서서 일해 다리가 무거웠는데 발 위주로 받고 한결 가벼워졌어요. 주차 안내만 조금 더 빨랐으면 좋았겠다 싶어 별 하나 뺐습니다.",
    },
    {
        "author": "한O경", "rating": "5", "date": "2026-03-12",
        "area": "대림동", "theme": "홈케어", "time": "오전",
        "title": "부모님 대리 예약도 매끄러웠어요",
        "body": "어머니 선물로 대리 예약했는데 연락 과정이 깔끔했고 어머니가 아주 만족하셨어요. 다음엔 제가 직접 받아보려 합니다.",
    },
]

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("영등포 출장마사지", "/massage/", [
        ("출장마사지 안내", "/massage/#service"),
        ("홈타이 안내", "/massage/#hometai"),
        ("전지역 방문 안내", "/massage/#coverage"),
        ("지하철역 인근 안내", "/massage/#stations"),
        ("예약 가능 시간", "/massage/#hours"),
        ("코스 선택 안내", "/massage/#course"),
        ("이용 전 확인사항", "/massage/#check"),
        ("위생·안전 안내", "/massage/#safety"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("지역별 안내", "/yeongdeungpo/", [
        ("영등포구 전체", "/yeongdeungpo/"),
        ("영등포동", "/yeongdeungpo/yeongdeungpo-dong/"),
        ("여의도동", "/yeongdeungpo/yeouido-dong/"),
        ("당산동", "/yeongdeungpo/dangsan-dong/"),
        ("도림동", "/yeongdeungpo/dorim-dong/"),
        ("문래동", "/yeongdeungpo/mullae-dong/"),
        ("양평동", "/yeongdeungpo/yangpyeong-dong/"),
        ("양화동", "/yeongdeungpo/yanghwa-dong/"),
        ("신길동", "/yeongdeungpo/singil-dong/"),
        ("대림동", "/yeongdeungpo/daerim-dong/"),
    ]),
    ("지하철역별 안내", "/yeongdeungpo/stations/", [
        ("역 전체", "/yeongdeungpo/stations/"),
        ("영등포역", "/yeongdeungpo/stations/yeongdeungpo-station/"),
        ("신길역", "/yeongdeungpo/stations/singil-station/"),
        ("대방역", "/yeongdeungpo/stations/daebang-station/"),
        ("문래역", "/yeongdeungpo/stations/mullae-station/"),
        ("영등포구청역", "/yeongdeungpo/stations/yeongdeungpo-gu-office-station/"),
        ("당산역", "/yeongdeungpo/stations/dangsan-station/"),
        ("대림역", "/yeongdeungpo/stations/daerim-station/"),
        ("양평역", "/yeongdeungpo/stations/yangpyeong-station/"),
        ("영등포시장역", "/yeongdeungpo/stations/yeongdeungpo-market-station/"),
        ("여의도역", "/yeongdeungpo/stations/yeouido-station/"),
        ("여의나루역", "/yeongdeungpo/stations/yeouinaru-station/"),
        ("신풍역", "/yeongdeungpo/stations/sinpung-station/"),
        ("선유도역", "/yeongdeungpo/stations/seonyudo-station/"),
        ("국회의사당역", "/yeongdeungpo/stations/national-assembly-station/"),
        ("샛강역", "/yeongdeungpo/stations/saetgang-station/"),
    ]),
    ("테마별 안내", "/themes/", [
        ("전체 테마", "/themes/"),
        ("스웨디시", "/themes/swedish/"),
        ("로미로미", "/themes/lomilomi/"),
        ("타이마사지", "/themes/thai/"),
        ("중국마사지", "/themes/chinese/"),
        ("아로마테라피", "/themes/aroma/"),
        ("홈케어", "/themes/homecare/"),
        ("호텔식마사지", "/themes/hotel-style/"),
        ("발마사지", "/themes/foot/"),
        ("스포츠·경락", "/themes/sports/"),
        ("스킨케어", "/themes/skincare/"),
        ("왁싱", "/themes/waxing/"),
        ("커플 관리", "/themes/couple/"),
        ("24시간", "/themes/24hours/"),
        ("수면 가능", "/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
