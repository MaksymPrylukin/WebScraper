import os
import json
import requests
from bs4 import BeautifulSoup

product_code = input("Provide product code: ")
page = 1
next = True
headers = {
    'Host': 'www.ceneo.pl',
    'Cookie': 'sv3=1.0_a81fcbce-3ccc-11f1-8454-b867372b2641; urdsc=1; userCeneo=ID=007a6884-c026-404a-9a33-1cc807bb09eb; __RequestVerificationToken=B3NworpVpaoJiiA_TC12Xekh5cShIXiyu9IM1XDvCdjDFzlb2UULAJr2YAFpKm9ssK_kVkXleMKF00V9gcAUZNjA2BYtfr29ePXBDAQOUh41; ai_user=kG+la|2026-04-20T15:21:51.979Z; __utmf=364726cdbe2e8437518b57e7b5f0d525_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; ga4_ga=GA1.2.a81fcbce-3ccc-11f1-8454-b867372b2641; _gcl_au=1.1.1125057594.1776698515; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWk5ajBBUWk5ajBBR3lBQkJQTENiRXNBUF9nQUFBQUFCNVlLTHREN0Q3ZExXRmd3SHhuWUtzUU1JMWY4ZUNBWW9RQUJBYUJBU0FCU0FLUUlJUUdra0FRSkFTZ0JBQUNBQUlBS0NSQklRQU1BQUNBQ0VBQVFJQUFJUUFFQUFDUUFRZ0tBQUFFaUFBUUFBQVlBQUFpQ0lBQUFRQUlnRUlFRUJFQW1RaEFBQUlBRUZBQWpBQUVJQUFBQUFBQUFBQUFBd0FBQUFBQ0FBSUFBQUFBZ0NBQUFJQUFBQUFBQUVBQVFCZ0lFQUFBQUFFQUFBQUFBQUFBQVFBQUFCQUFBQUFJS0xnQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRkZ3a0FHQUFJS0xob0FNQUFRVVhFUUFZQUFnb3VLZ0F3QUJCUmNaQUJnQUNDaTQ2QURBQUVGRnlFQUdBQUlLTGtvQU1BQVFVWEtRQVlBQWdvdVdnQXdBQkJSY0EuSUtMdEQ3RDdkTFdGZ3dIeG5ZS3NRTUkxZjhlQ0FZb1FBQkFhQkFTQUJTQUtRSUlRR2trQVFKQVNnQkFBQ0FBSUFLQ1JCSVFBTUFBQ0FDRUFBUUlBQUlRQUVBQUNRQVFnS0FBQUVpQUFRQUFBWUFBQWlDSUFBQVFBSWdFSUVFQkVBbVFoQUFBSUFFRkFBakFBRUlBQUFBQUFBQUFBQUF3QUFBQUFDQUFJQUFBQUFnQ0FBQUlBQUFBQUFBRUFBUUJnSUVBQUFBQUVBQUFBQUFBQUFBUUFBQUJBQUFBQUlBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.InAaduJ2L40PW65zL5NuN18JRMOXaToPPzNXI199PoU%3D; FPLC=MPGNIlP6KYDxzydgAHHis7MMojMtQbnT5zwFWHkqqeT0e6kKNyaXGgSrzK6CcbOL09ElOVwK7STqNCI7Pw%2BDAJf2EiSzmtDi7pnfOzn4fCqgVrI%3D; nps3=SessionStartTime=1776698531,SurveyId=68; ai_session=JveOV|1776698513394|1776698532464.6; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A12.761Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%22a81fcbce-3ccc-11f1-8454-b867372b2641%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A12.761Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22mI8n7o4JCaM4wrGOFB8x%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A12.761Z%22%7D; _tt_enable_cookie=1; _ttp=01KPNQR96RCCMZBMD36WS0CEZV_.tt.1; _fbp=fb.1.1776698533358.837513177925320977; ttcsid=1776698533086::flvW2_VrpxNIOZ5LKYAT.1.1776698543103.0::1.-2155.0::0.0.0.0::0.0.0; ttcsid_CNK74OBC77U1PP7E4UR0=1776698533085::qkYEkGYla8iuH1ZcyrRq.1.1776698543105.1; ga4_ga_K2N2M0CBQ6=GS2.2.s1776698513$o1$g1$t1776698560$j33$l0$h1322320712',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
}
all_opinions = []
while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        print(type(page_dom))
        if page == 1:
            product_name = page_dom.select_one("h1.product-top__product-info__name").get_text(strip=True)
        print(product_name)

        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")
        print(type(opinions))
        print(len(opinions))
        all_opinions = page_dom.find_all("div", {"class": "js_product-review:not(.user-post--highlight)"})
        opinions = [r for r in all_opinions if "user-post--highlight" not in r.get('clas', [])]

        all_opinions = []
        for opinion in opinions:
            single_opinion = {
                'opinion_id': opinion['data-entry-id'],
                'author': opinion.select_one('span.user-post__author-name').get_text().strip(),
                'recommendation': opinion.select_one('span.user-post__author-recommendation > em').get_text().strip() if opinion.select_one('span.user-post__author-recommendation > em') else None,
                'score': opinion.select_one('span.user-post__score-count').get_text().strip(),
                'content': opinion.select_one('	div.user-post__text').get_text().strip(),
                'pros': [p.get_text() for p in opinion.select('div.review-feature__item--positive')],
                'cons': [c.get_text() for c in opinion.select('div.review-feature__item--negative')],
                'like': opinion.select_one('button.vote-yes > span').get_text().strip(),
                'dislike': opinion.select_one('button.vote-no > span').get_text().strip(),
                'publish_date': opinion.select_one('span.user-post__published > time:nth-child(1)[datetime]').['datetime'].strip(),
                'purchase_date': opinion.select_one('span.user-post__published > time:nth-child(2)[datetime]').['datetime'].strip() if opinion.select_one('span.user-post__published > time:nth-child(2)[datetime]') else None,
            }
            all_opinions.append(single_opinion)

    next = True if page_dom.select_one('button.pagination__next') else False
    if next: page += 1

    if not os.path.exists("./opinions"):
        os.mkdir("./opinions")
    with open(f"./{product_code}.json", "w", encoding="UTF-8") as jf:
        json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
