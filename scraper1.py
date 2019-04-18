from bs4 import BeautifulSoup
import requests
import sqlite3
conn = sqlite3.connect("finale.db")
c=conn.cursor()

az=[]
az_title=[]
c.execute('''CREATE table if not exists azcentral (title text, article text)''')
news=['https://www.azcentral.com/story/news/local/gilbert/2019/04/17/chandler-school-district-perry-high-students-president-trump-maga-gear-harassed-peers/3417172002/','https://www.azcentral.com/story/news/local/southwest-valley-breaking/2019/04/17/antoinette-perez-arrested-suspected-making-threats-against-macys/3495444002/',
'https://www.azcentral.com/story/news/politics/border-issues/2019/04/16/yuma-mayor-doug-nicholls-declares-emergency-over-release-migrant-families/3492054002/',
'https://www.azcentral.com/story/travel/airlines/2019/04/17/phoenix-mesa-gateway-airport-remodeled-private-plane-terminal/3487467002/',
'https://www.azcentral.com/story/news/local/phoenix/2019/04/17/maricopa-county-attorney-bill-montgomery-defends-actions-juan-martinez-sexual-harassment-allegation/3490601002/',
'https://www.azcentral.com/story/news/local/chandler/2019/04/17/community-rallies-around-east-valley-mom-of-three-killed-i-10-crash-stacey-sullivan/3484081002/',
'https://www.azcentral.com/story/entertainment/events/2019/04/17/friends-musical-parody-ross-rachel-and-gang-live-on-phoenix/3381445002/',
'https://www.azcentral.com/story/news/local/2019/04/17/greta-rogers-89-year-old-queen-nba-twitter-keeps-phoenix-honest/3403339002/',
'https://www.azcentral.com/story/opinion/op-ed/robertrobb/2019/04/17/arizona-public-service-election-spending-appoint-corporation-commission/3486942002/',
     'https://www.azcentral.com/story/news/nation/2019/04/17/columbine-shooting-denver-schools-fbi-searches-woman-sol-pais/3494398002/']
for url in news:
    reqs=requests.get(url)
    soup=BeautifulSoup(reqs.content,'html5lib')
    s=soup.findAll('p',attrs={'class':'p-text'})
    d=soup.findAll('h1')
    b=BeautifulSoup(str(d)).get_text()
    ja=BeautifulSoup(str(s)[:-58]).get_text()
    az.append(ja)
    az_title.append(b) 
    c.execute('''INSERT into azcentral values(?,?)''',(b, ja))
    
    conn.commit()


c.execute('''CREATE table if not exists tampabay (title text, article text)''')
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
    ti=(BeautifulSoup(str(tit)).get_text()).replace("\n\n",'')
    titl.append(ti)
    c.execute('''INSERT into tampabay values(?,?)''',(ti,cont.replace("\n\n\n",'')))
    
    conn.commit()




c.execute('''CREATE table if not exists usatoday (title text, article text)''')
us=[]
us_title=[]
news=['https://www.usatoday.com/story/news/nation/2019/04/17/columbine-shooting-denver-schools-fbi-searches-woman-sol-pais/3494398002/',
     'https://www.usatoday.com/story/news/politics/elections/2019/04/17/pete-buttigieg-confronts-sodom-and-gomorrah-hecklers-iowa-rally/3494336002/',
'https://www.usatoday.com/story/money/cars/2019/04/17/new-york-auto-show-2020-toyota-highlander/3476818002/',
'https://www.usatoday.com/picture-gallery/news/world/2019/04/16/inside-notre-dame/3482510002/',
'https://www.usatoday.com/story/life/music/2019/04/17/beyonces-homecoming-diet-has-twitter-shock-somebody-feed-bey/3494445002/',
'https://www.usatoday.com/story/tech/talkingtech/2019/04/16/ps-5-sonys-first-details-point-8-k-support-faster-performance/3483186002/',
'https://www.usatoday.com/videos/news/world/2019/04/16/couple-rescued-croc-infested-beach-after-writing-help-sand/3482693002/',
'https://www.usatoday.com/story/news/politics/2019/04/17/trump-team-game-plan-robert-mueller-400-page-report-thursday/3482153002/',
'https://www.usatoday.com/story/news/politics/2019/04/17/william-barr-directs-judges-deny-bond-hearings-asylum-seekers/3494905002/',
'https://www.usatoday.com/story/opinion/2019/04/17/mueller-report-redactions-congress-public-disclosure-no-secrets-column/3472669002/']
for url in news:
    reqs=requests.get(url)
    soup=BeautifulSoup(reqs.content,'html5lib')
    s=soup.findAll('p',attrs={'class':'p-text'})
    sd=soup.findAll('h1')
    dus=BeautifulSoup(str(s)).get_text()
    us.append(dus)
    du=BeautifulSoup(str(sd)).get_text()
    us_title.append(du)
    c.execute('''INSERT into usatoday values(?,?)''',(du, dus))
    
    conn.commit()






newsdaily=[]
title=[]
c.execute('''CREATE table if not exists newsday (title text, article text)''')
domain=['https://www.newsday.com/long-island/suffolk/brookhaven-calabro-airport-solar-panels-1.29902154','https://www.newsday.com/long-island/obituaries/kim-hardwick-clayton-huey-principal-obituary-1.29909256',
       'https://www.newsday.com/long-island/suffolk/riverhead-luminati-legal-issues-1.29910315','https://www.newsday.com/sports/columnists/neil-best/islanders-penguins-sweep-1.29896366',
       'https://www.newsday.com/long-island/suffolk/patchogue-civil-war-statue-returning-1.29879558','https://www.newsday.com/sports/baseball/yankees/yankees-red-sox-james-paxton-1.29893124',
       'https://www.newsday.com/entertainment/movies/many-saints-of-newark-garden-city-1.29884079','https://www.newsday.com/sports/hockey/islanders/isles-penguins-game-4-1.29877549',
        'https://www.newsday.com/lifestyle/family/census-contest-1.29838095','https://www.newsday.com/long-island/obituaries/cecilia-moloughney-dead-obituary-1.29933531',
       ]
for dom in domain:
    reqs=requests.get(dom)
    soup=BeautifulSoup(reqs.content,'html5lib')
    con=soup.findAll('div',attrs={'id':'contentAccess'})
    tat=soup.findAll('h1')
    cons=BeautifulSoup(str(con))
    s= cons.findAll('p')
    da=BeautifulSoup(str(s[:-3])).get_text()
    da=da.replace('[','')
    da=da.replace(']','')
    newsdaily.append(da)
    d=BeautifulSoup(str(tat)).get_text()
    title.append(d)

    
    c.execute('''INSERT into newsday values(?,?)''',(d,da))
    
    conn.commit()   
    



wp={}
c.execute('''CREATE table if not exists washingtonpost (title text, article text)''')
urs=['https://www.washingtonpost.com/politics/trump-vetoes-resolution-to-end-us-participation-in-yemens-civil-war/2019/04/16/0fabc312-60a1-11e9-bfad-36a7eb36cb60_story.html',
    'https://www.washingtonpost.com/world/notre-dame-fire-updates/2019/04/17/00dbbd84-6091-11e9-bf24-db4b9fb62aa2_story.html','https://www.washingtonpost.com/politics/trump-moves-to-resist-house-inquiries-setting-up-fight-over-congressional-subpoena-powers/2019/04/16/49f4c75c-6057-11e9-9412-daf3d2e67c6d_story.html',
    'https://www.washingtonpost.com/opinions/2019/04/15/mueller-may-be-done-barr-is-just-getting-started/','https://www.washingtonpost.com/opinions/global-opinions/this-scientific-braintrust-is-needed-now-more-than-ever/2019/04/15/885a627a-5fa0-11e9-9ff2-abc984dc9eec_story.html','https://www.washingtonpost.com/opinions/2019/04/16/buttigieg-bump-is-real-mayor-pete-still-has-long-way-go/',
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
    c.execute('''INSERT into washingtonpost values(?,?)''',(t,d))
    
    conn.commit()



c.execute('''CREATE table if not exists nytimes (title text, article text)''')
content=[]
title_ny=[]
urls=["https://www.nytimes.com/2019/04/17/us/politics/mueller-report-release-guide.html","https://www.nytimes.com/2019/04/16/magazine/consumer-financial-protection-bureau-trump.html",'https://www.nytimes.com/2019/04/16/world/europe/why-notre-dame-fire-spread.html',
      'https://www.nytimes.com/2019/04/17/us/politics/julian-castro-2020.html','https://www.nytimes.com/2019/04/16/us/politics/trump-presidency-base.html','https://www.nytimes.com/interactive/2019/04/16/climate/glaciers-melting-alaska-washington.html',
     'https://www.nytimes.com/2019/04/17/opinion/trump-economy-job-growth.html','https://www.nytimes.com/2019/04/17/opinion/mayor-pete-and-the-queering-of-the-american-soul.html','https://www.nytimes.com/2019/04/17/opinion/mayor-pete-and-the-queering-of-the-american-soul.html',
     'https://www.nytimes.com/2019/04/16/opinion/australia-election-nationalism.html','https://www.nytimes.com/2019/04/17/opinion/trump-economy-job-growth.html']
for url in urls:
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html5lib')
    head=soup.findAll('span',attrs={'class':'css-fwqvlz'})
    sa=BeautifulSoup(str(head)).get_text()
    title_ny.append(s)
    s=soup.findAll(attrs={"class":"css-1ygdjhk evys1bk0"})
    d=BeautifulSoup(str(s)).get_text()
    content.append(d)
    c.execute('''INSERT into nytimes values(?,?)''',(str(sa),d))
    
    conn.commit()

c.execute('''CREATE table if not exists nydaily (title text, article text)''')
content_nd=[]
title_nd=[]
urls=['https://www.nydailynews.com/new-york/nyc-crime/ny-man-arrested-gasoline-st-patricks-cathedral-20190418-sg6j6wo5ijezbceahnn4znilmi-story.html',
     'https://www.nydailynews.com/news/national/ny-obituary-cancer-feel-good-20190417-7lkaduritre5le66phf5rlqglu-story.html',
     'https://www.nydailynews.com/new-york/nyc-crime/ny-boy-8-struck-critically-injured-in-queens-20190417-rdwjfkpizfhevoed5njxhruabm-story.html',
     'https://www.nydailynews.com/new-york/ny-judith-clark-paroled-20190417-xihs5hhcz5c7rfbgd4nfh324gq-story.html',
     'https://www.nydailynews.com/new-york/ny-mta-fare-hikes-subway-bus-swipe-metrocard-20190418-xi62mswdevd6jjvprat7dxdmmy-story.html',
     'https://www.nydailynews.com/news/world/ny-julian-assange-wikileaks-ecuador-embassy-london-asylum-feces-walls-20190418-mhfd3bjbu5fefo5ir6trt25voq-story.html',
     'https://www.nydailynews.com/news/world/ny-indias-jet-airways-goes-bankrupt-20190418-scnd7ydzmbeyvm2lwf4yojoocu-story.html',
     'https://www.nydailynews.com/news/crime/ny-mother-son-karate-wisconsin-walmart-naked-arrested-20190413-gvvqufmw5jbqpokmxjbyxen4eu-story.html',
     'https://www.nydailynews.com/news/world/ny-20-carat-okavango-blue-diamond-unveiled-in-botswana-20190418-ghmysn2hqzhtdnzrsj2r7rkvwu-story.html',
     'https://www.nydailynews.com/opinion/ny-edit-judith-clarks-freedom-20190418-jvc6g523szb47kvg42qe3g5qb4-story.html']
for url in urls:
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html5lib')
    text=soup.findAll('p')
    tat=soup.findAll('h1')
    e=BeautifulSoup(str(text)).get_text()
    d=BeautifulSoup(str(tat)).get_text()
    content_nd.append(e)
    title_nd.append(d)
    c.execute('''INSERT into nydaily values(?,?)''',(d, e))
    
    conn.commit()











c.execute('''CREATE table if not exists nola (title text, article text)''')
content_bg=[]
title_bg=[]
urls=['https://www.nola.com/weather/2019/04/tornadoes-possible-thursday-in-new-orleans-metro-as-severe-storms-move-through.html',
     'https://www.nola.com/crime/2019/04/man-accused-of-shooting-neighbor-after-argument-over-music-sheriffs-office.html',
     'https://www.nola.com/pelicans/2019/04/david-griffin-working-the-art-of-the-anthony-davis-deal-on-day-1-of-new-pelicans-era.html',
     'https://www.nola.com/news/2019/04/some-schools-closing-due-to-thursday-storm-threat.html','https://www.nola.com/news/2019/04/gas-leak-closes-orleans-parish-juvenile-court-on-thursday.html',
     'https://expo.nola.com/life-and-culture/g66l-2019/04/21b83c452a7916/with-otra-vez-new-york-chef-brings-his-mexican-cooking-to-new-orleans.html',
     'https://www.nola.com/news/2019/04/state-offices-closed-thursday-due-to-severe-weather-threat.html','https://www.nola.com/crime/2019/04/person-of-interest-sought-in-armed-hold-up-at-chalmette-bar-st-bernard-authorities.html',
     'https://www.nola.com/entertainment/2019/04/beyonce-busts-out-with-behind-the-scenes-film-and-live-album.html','https://www.nola.com/news/2019/04/miss-costa-a-1668-pound-great-white-shark-swims-off-fla-panhandle-report.html']
for url in urls:
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html5lib')
    text=soup.findAll("p")
    tat=soup.findAll('h1')
    e=BeautifulSoup(str(text)).get_text()
    d=BeautifulSoup(str(tat)).get_text()
    content_bg.append(e)
    title_bg.append(d)
    
    c.execute('''INSERT into nola values(?,?)''',(d, e))
    
    conn.commit()
    
    
    
    
    
c.execute('''CREATE table if not exists latime (title text, article text)''')
content_la=[]
title_la=[]
urls=['https://www.latimes.com/politics/la-na-pol-mueller-report-obstruction-russia-investigation-20190418-story.html',
     'https://www.latimes.com/local/lanow/la-me-ln-alora-benitez-missing-20190418-story.html','https://www.latimes.com/local/lanow/la-me-college-admissions-scandal-isackson-20190418-story.html',
     'https://www.latimes.com/local/lanow/la-me-imperial-sues-mwd-colorado-drought-plan-20190418-story.html','https://www.latimes.com/nation/la-na-puerto-rico-population-hurricane-maria-20190418-story.html',
     'https://www.latimes.com/nation/la-na-puerto-rico-population-hurricane-maria-20190418-story.html','https://www.latimes.com/local/lanow/la-me-ln-alora-benitez-missing-20190418-story.html',
     'https://www.latimes.com/local/lanow/la-me-ln-triple-homicide-glendale-20190418-story.html','https://www.latimes.com/opinion/editorials/la-ed-columbine-anniversary-threat-shootings-20190418-story.html',
     'https://www.latimes.com/opinion/editorials/la-ed-william-barr-trump-detain-asylum-seekers-20190418-story.html']
for url in urls:
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html5lib')
    text=soup.findAll("p")
    tat=soup.findAll('h1')
    e=BeautifulSoup(str(text)).get_text()
    d=BeautifulSoup(str(tat)).get_text()
    content_la.append(e)
    title_la.append(d)
    
    c.execute('''INSERT into latime values(?,?)''',(d, e))
    
    conn.commit()

content_st=[]

title_st=[]
c.execute('''CREATE table if not exists seattle (title text, article text)''')
urls=['https://www.seattletimes.com/nation-world/nation-politics/heres-the-redacted-mueller-report-and-what-you-need-to-know-about-it/',
     'https://www.seattletimes.com/seattle-news/politics/with-lawsuits-possible-seattle-city-attorneys-office-takes-over-power-pole-collapse-investigation/',
     'https://www.seattletimes.com/nation-world/president-trump-targets-rep-ilhan-omar-with-a-video-of-twin-towers-burning/','https://www.seattletimes.com/nation-world/nation/deputies-substitute-teacher-downed-vodka-endangered-kids/',
     'https://www.seattletimes.com/life/food-drink/dinner-at-a-movie-yikes-a-downtown-seattle-multiplex-ventures-into-real-food-and-jartails/',
     'https://www.seattletimes.com/nation-world/nation/boy-thrown-from-mall-of-america-balcony-still-hospitalized/','https://www.seattletimes.com/nation-world/opioid-users-call-kratom-a-godsend-the-fda-says-its-a-menace/',
     'https://www.seattletimes.com/entertainment/music/nirvanas-manager-breaks-his-silence-on-kurt-cobain/','https://www.seattletimes.com/seattle-news/northwest/oregon-couples-final-days-captured-in-intimate-aid-in-dying-video/',
     'https://www.seattletimes.com/seattle-news/i-told-you-my-reaction-to-seattle-is-dying-heres-what-you-told-me/']
for url in urls:
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html5lib')
    text=soup.findAll("p")
    tat=soup.findAll('h1')
    e=BeautifulSoup(str(text)[1588:]).get_text()
    d=BeautifulSoup(str(tat)).get_text()
    content_st.append(e)
    title_st.append(d)
    c.execute('''INSERT into seattle values(?,?)''',(d, e))
    
    conn.commit()

    
    
    
    
c.close()    

