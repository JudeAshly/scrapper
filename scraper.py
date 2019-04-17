from bs4 import BeautifulSoup
import requests
content=[]
urls=["https://www.nytimes.com/2019/04/17/us/politics/mueller-report-release-guide.html","https://www.nytimes.com/2019/04/16/magazine/consumer-financial-protection-bureau-trump.html",'https://www.nytimes.com/2019/04/16/world/europe/why-notre-dame-fire-spread.html',
      'https://www.nytimes.com/2019/04/17/us/politics/julian-castro-2020.html','https://www.nytimes.com/2019/04/16/us/politics/trump-presidency-base.html','https://www.nytimes.com/interactive/2019/04/16/climate/glaciers-melting-alaska-washington.html',
     'https://www.nytimes.com/2019/04/17/opinion/trump-economy-job-growth.html','https://www.nytimes.com/2019/04/17/opinion/mayor-pete-and-the-queering-of-the-american-soul.html','https://www.nytimes.com/2019/04/17/opinion/mayor-pete-and-the-queering-of-the-american-soul.html'
     'https://www.nytimes.com/2019/04/16/opinion/australia-election-nationalism.html','https://www.nytimes.com/2019/04/17/opinion/trump-economy-job-growth.html']
for url in urls:
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html5lib')
    #head=soup.find(attrs={"class":"balancedHeadline"})
    #print(head)
    s=soup.findAll(attrs={"class":"css-1ygdjhk evys1bk0"})
    [s.extract() for s in soup('a')]
    b=str(s).replace('</p>,',"\n")
    d=b.replace('</p>','')
    c=d.replace('<!-- -->','')
    u=c.replace("""<p class="css-1ygdjhk evys1bk0">""",'')
    content.append(u)
    

wp={}
urlr=['https://www.washingtonpost.com/politics/trump-vetoes-resolution-to-end-us-participation-in-yemens-civil-war/2019/04/16/0fabc312-60a1-11e9-bfad-36a7eb36cb60_story.html',
    'https://www.washingtonpost.com/world/notre-dame-fire-updates/2019/04/17/00dbbd84-6091-11e9-bf24-db4b9fb62aa2_story.html','https://www.washingtonpost.com/politics/trump-moves-to-resist-house-inquiries-setting-up-fight-over-congressional-subpoena-powers/2019/04/16/49f4c75c-6057-11e9-9412-daf3d2e67c6d_story.html',
    'https://www.washingtonpost.com/opinions/2019/04/15/mueller-may-be-done-barr-is-just-getting-started/','https://www.washingtonpost.com/opinions/global-opinions/this-scientific-braintrust-is-needed-now-more-than-ever/2019/04/15/885a627a-5fa0-11e9-9ff2-abc984dc9eec_story.html','https://www.washingtonpost.com/opinions/2019/04/16/buttigieg-bump-is-real-mayor-pete-still-has-long-way-go/'
    'https://www.washingtonpost.com/weather/2019/04/16/tornado-was-bearing-down-bar-packed-with-college-students-its-owner-explains-why-they-were-kicked-out/',
     'https://www.washingtonpost.com/sports/2019/04/17/draymond-greens-mother-rips-warriors-jabs-kevin-durant-after-historic-collapse/','https://www.washingtonpost.com/local/obituaries/david-brion-davis-pulitzer-winning-historian-who-reshaped-study-of-slavery-dies-at-92/2019/04/16/9727b2e8-6050-11e9-9ff2-abc984dc9eec_story.html','https://www.washingtonpost.com/news/powerpost/paloma/the-cybersecurity-202/2019/04/17/the-cybersecurity-202-why-a-hacking-operation-by-a-proto-state-in-ukraine-could-spell-trouble-for-the-u-s/5cb67b171ad2e5345893fe14/']
for ur in urs:
    reqs=requests.get(ur)
    soup=BeautifulSoup(reqs.content,'html5lib')
    sa=soup.findAll('p')    
    su=soup.findAll('h1')
    
    t=BeautifulSoup(str(su)).get_text()
    d=BeautifulSoup(str(sa)).get_text()
    wp[t]=d

new=['https://www.tampabay.com/sports/2019/04/17/seven-sad-seasons-most-disappointing-moments-in-tampa-bay-sports-history/','https://www.tampabay.com/sports/2019/04/17/lightning-becomes-first-presidents-trophy-winner-to-be-swept-in-first-round/',
'https://www.tampabay.com/news/pinellas/crime/john-jonchuck-guilty-of-first-degree-murder-in-2015-death-of-his-daughter-phoebe-20190416/',
'https://www.tampabay.com/florida-politics/2019/04/17/is-floridas-tough-on-crime-era-vanishing/',
'https://www.tampabay.com/transportation/partners-propose-seven-day-ferry-service-linking-hillsborough-macdill-tampa-st-pete-20190416/',
'https://www.tampabay.com/fun/first-look-hagrid-ride-brings-fluffy-the-three-headed-dog-to-universal-orlando-20190416/',
'https://www.tampabay.com/sports/2019/04/17/seven-sad-seasons-most-disappointing-moments-in-tampa-bay-sports-history/',
'https://www.tampabay.com/music/this-weekends-best-concerts-in-tampa-bay-santana-leon-bridges-whitesnake-20190417/',
'https://www.tampabay.com/movies/what-movies-are-in-tampa-bay-theaters-this-week-breakthrough-penguins-high-life-20190417/',
'https://www.tampabay.com/nation-world/66-minutes-the-frantic-race-to-save-notre-dame-20190417/']
tam=[]
titl=[]
for url in new:
    reqs=requests.get(url)
    soup=BeautifulSoup(reqs.content,'html5lib')
    tit=soup.find('h1')
    cou=soup.find('article')
    cont=BeautifulSoup(str(cou)).get_text().replace('�','')
    tam.append(cont)
    titl.append(BeautifulSoup(str(tit)).get_text())

newsdaily=[]
titl=[]

domain=['https://www.newsday.com/long-island/suffolk/brookhaven-calabro-airport-solar-panels-1.29902154','https://www.newsday.com/long-island/obituaries/kim-hardwick-clayton-huey-principal-obituary-1.29909256',
       'https://www.newsday.com/long-island/suffolk/riverhead-luminati-legal-issues-1.29910315','https://www.newsday.com/sports/columnists/neil-best/islanders-penguins-sweep-1.29896366',
       'https://www.newsday.com/long-island/suffolk/patchogue-civil-war-statue-returning-1.29879558','https://www.newsday.com/sports/baseball/yankees/yankees-red-sox-james-paxton-1.29893124',
       'https://www.newsday.com/entertainment/movies/many-saints-of-newark-garden-city-1.29884079']
for dom in domain:
    reqs=requests.get(dom)
    soup=BeautifulSoup(reqs.content,'html5lib')
    con=soup.findAll('div',attrs={'id':'contentAccess'})
    tat=soup.findAll('h1')
    cons=BeautifulSoup(str(con))
    s= cons.findAll('p')
    c=BeautifulSoup(str(s[:-3])).get_text()
    c=c.replace('[','')
    c=c.replace(']','')
    newsdaily.append(c)
    titl.append(BeautifulSoup(str(tat)).get_text())


az=[]
title=[]
news=['https://www.azcentral.com/story/news/local/gilbert/2019/04/17/chandler-school-district-perry-high-students-president-trump-maga-gear-harassed-peers/3417172002/','https://www.azcentral.com/story/news/local/southwest-valley-breaking/2019/04/17/antoinette-perez-arrested-suspected-making-threats-against-macys/3495444002/',
'https://www.azcentral.com/story/news/politics/border-issues/2019/04/16/yuma-mayor-doug-nicholls-declares-emergency-over-release-migrant-families/3492054002/',
'https://www.azcentral.com/story/travel/airlines/2019/04/17/phoenix-mesa-gateway-airport-remodeled-private-plane-terminal/3487467002/',
'https://www.azcentral.com/story/news/local/phoenix/2019/04/17/maricopa-county-attorney-bill-montgomery-defends-actions-juan-martinez-sexual-harassment-allegation/3490601002/',
'https://www.azcentral.com/story/news/local/chandler/2019/04/17/community-rallies-around-east-valley-mom-of-three-killed-i-10-crash-stacey-sullivan/3484081002/',
'https://www.azcentral.com/story/entertainment/events/2019/04/17/friends-musical-parody-ross-rachel-and-gang-live-on-phoenix/3381445002/',
'https://www.azcentral.com/story/news/local/2019/04/17/greta-rogers-89-year-old-queen-nba-twitter-keeps-phoenix-honest/3403339002/',
'https://www.azcentral.com/story/opinion/op-ed/robertrobb/2019/04/17/arizona-public-service-election-spending-appoint-corporation-commission/3486942002/']
for url in news:
    reqs=requests.get(url)
    soup=BeautifulSoup(reqs.content,'html5lib')
    s=soup.findAll('p',attrs={'class':'p-text'})
    d=soup.findAll('h1')
    b=BeautifulSoup(str(d)).get_text()
    ja=BeautifulSoup(str(s)[:-58]).get_text()
    az.append(ja)
    tis.append(b)
    
    

        
    




