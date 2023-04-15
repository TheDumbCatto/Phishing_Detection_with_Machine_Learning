import ipaddress
from os import path
import re
import urllib.request
import urllib.parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import socket
from pandas import read_csv
import requests
from googlesearch import search
import whois
from datetime import date, datetime
import time
from dateutil.parser import parse as date_parse
import math
import aiohttp
import asyncio
import difflib

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

#async def generate_dataset_web_content(url):
#    try:
#        async with aiohttp.ClientSession(conn_timeout=0.3, read_timeout=0.5) as session:
#            async with session.get(url) as response:
#                web_content = await response.text()
#                soup = BeautifulSoup(web_content, 'html.parser')
#                print('Doing shit')
#    except:
#        print('Error')

def generate_data_set(url, tlds, popular_urls):

#    start = time.time()
    data_set = []
    data_set.append(url)
    domain = urlparse(url).netloc

    if not re.match(r"^https?", url):
        url = "http://" + url

    #try:
    #    response = requests.get(url, timeout = 1)
    #    soup = BeautifulSoup(response.text, 'html.parser')
    #except:
    #    response = ""
    #    soup = -999
    ##asyncio.run(generate_dataset_web_content(url))

#
##    domain = re.findall(r"://([^/]+)/?", url)[0]
#    if re.match(r"^www.", domain):
#        domain = domain.replace("www.", "")
#    whois_response = whois.whois(domain)
#
#    rank_checker_response = requests.post("https://www.checkpagerank.net/index.php", {
#        "name": domain
#    })
#
#    try:
#        global_rank = int(re.findall(
#            r"Global Rank: ([0-9]+)", rank_checker_response.text)[0])
#    except:
#        global_rank = -1

    # 1.having_IP_Address
    try:
        ipaddress.ip_address(domain)
        data_set.append(1)
    except:
        data_set.append(0)

    # 2a.having_too_long_domain_length
    domain_len = len(domain)
    if domain_len > 25:
        data_set.append(1)
    else:
        data_set.append(0)

    # 2b.URL_Length
    if len(url) > 54:
        data_set.append(1)
    else:
        data_set.append(0)
#    if len(url) < 20:
#        data_set.append(0)
#    elif len(url) >= 20 and len(url) <= 30:
#        data_set.append(0)
#    else:
#        data_set.append(1)

    # 3.Shortening_Service
    shortening_services = r'''bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|                                                                        
                            yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|
                            short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|
                            doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|
                            db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|
                            q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|
                            x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net'''
    match = re.search(shortening_services, url)
    if match:
        data_set.append(1)
    else:
        data_set.append(0)

    # 4.having_At_Symbol
    if re.findall("@", url):
        data_set.append(1)
    else:
        data_set.append(0)

    # 5.double_slash_redirecting
    double_slash_pos_list = [x.start(0) for x in re.finditer('//', url)]
    if ( not double_slash_pos_list):
        data_set.append(0)
    elif double_slash_pos_list[len(double_slash_pos_list)-1] > 6:
        data_set.append(1)
    else:
        data_set.append(0)

    # 6.having_too_many_hyphens_in_domain
    all_hyphens = re.findall(r'-', url)
    if len(all_hyphens) > 1:
        data_set.append(1)
    else: data_set.append(0)
   # data_set.append(len(re.findall(r'-', url)))
   # if len(re.findall(r"-", url)):
   #     data_set.append(1)
   # else:
   #     data_set.append(0)

    # 7.number_of_sub_Domains
    data_set.append(len(re.findall(r'\.', url)))
#    if len(re.findall(r"\.", url)) == 1:
#        data_set.append(0)
#    elif len(re.findall(r"\.", url)) == 2:
#        data_set.append(0)
#    else:
#        data_set.append(1)

    #### Response time is too long ####
#    # 8.SSLfinal_State
#    try:
#        if response.text:
#            data_set.append(1)
#    except:
#        data_set.append(-1)

#    #### Response time is too long ####
#    # 9.Domain_registeration_length
#    expiration_date = whois_response.expiration_date
#    registration_length = 0
#    try:
#        expiration_date = min(expiration_date)
#        today = time.strftime('%Y-%m-%d')
#        today = datetime.strptime(today, '%Y-%m-%d')
#        registration_length = abs((expiration_date - today).days)
#
#        if registration_length / 365 <= 1:
#            data_set.append(-1)
#        else:
#            data_set.append(1)
#    except:
#        data_set.append(-1)
#
#    # 10.Favicon
#    if soup == -999:
#        data_set.append(-1)
#    else:
#        try:
#            for head in soup.find_all('head'):
#                for head.link in soup.find_all('link', href=True):
#                    dots = [x.start(0)
#                            for x in re.finditer('\.', head.link['href'])]
#                    if url in head.link['href'] or len(dots) == 1 or domain in head.link['href']:
#                        data_set.append(1)
#                        raise StopIteration
#                    else:
#                        data_set.append(-1)
#                        raise StopIteration
#        except StopIteration:
#            pass

    # 8. using weird ports
    try:
        port = domain.split(":")[1]
        if port and (int(port)!=80 and int(port)!=443):
            data_set.append(1)
        else:
            data_set.append(0)
    except:
        data_set.append(0)

    # 9. HTTPS_token
    if re.findall(r"https", domain):
        data_set.append(0)
    else:
        data_set.append(1)

    # 10. randomness_of_URL
    url_tokens = re.split(r';|\/|\?|:|&|=|\+', url) + re.split(r'\.', urlparse(url).netloc)
    max_randomness = 0.0
    for token in url_tokens:
        if(len(token)==0): continue
        randomness = float(max(len(re.split(r'\D', token)), len(re.split(r'[A-Za-z0-9]', token))) * math.log(len(token), 2))
        if (randomness > max_randomness):
            max_randomness = randomness
    data_set.append(max_randomness)

    # 11. having_HTML_tag_in_URL
    unquoted_url = urllib.parse.unquote(url)
    if re.findall(r'<.*>', unquoted_url) or re.findall(r'<.*>', url):
        data_set.append(1)
    else:
        data_set.append(0)

    ###
    popular_domain_tokens = [x.split('.') for x in popular_urls]
    brand_names = set([x[len(x)-2] for x in popular_domain_tokens])
    ###
    # 12. having_brand_name_in_path
    # 13. having_brand_name_in_domain
#
    url_path = urlparse(url).path

    found_brand_name_in_path = False
    found_brand_name_in_domain = False
    for brand_name in brand_names:
        if brand_name + '.' in url_path:
            found_brand_name_in_path = True
        if re.findall(re.escape(brand_name) + r'\.|' + re.escape(brand_name), domain):
            found_brand_name_in_domain = True
    if (found_brand_name_in_path): data_set.append(1)
    else: data_set.append(0)
    if (found_brand_name_in_domain): data_set.append(1)
    else: data_set.append(0)

#    # 15. misspelled_brand_name_in_path
#    # 16. misspelled_brand_name_in_domain
#    fake_brand_name_domain_score = 0.0
#    fake_brand_name_path_score = 0.0
#    for word in url_tokens:
#        # calculate similarity score between word and pre-defined words
#        scores = difflib.get_close_matches(word, brand_names, n=1, cutoff=0.5)
#        if scores:
#            score = difflib.SequenceMatcher(None, word, scores[0]).ratio()
#            if word in domain and score > fake_brand_name_domain_score: fake_brand_name_domain_score = score
#            if word in url_path and score > fake_brand_name_path_score: fake_brand_name_path_score = score
##
#    data_set.append(fake_brand_name_domain_score) 
#    data_set.append(fake_brand_name_path_score)

    # 17. entropy_of_special_characters
    nan_list = ['/','-','.','=',';','?','_','%','@','&']
    entropy = 0
    for nan_char in nan_list:
        total_characters = len(url)
        character_count = url.count(nan_char)
    
        if character_count == 0: continue
        character_probability = character_count / total_characters
        entropy = -character_probability * math.log2(character_probability)
    
    data_set.append(entropy)
#
    # 18. having_suspicious_words_in_URL
    sus_word_list = ['security' ,'login', 'signin', 'bank', 'account', 'update', 'include', 'webs', 'online']
    found_sus_word = False
    for sus_word in sus_word_list:
        if sus_word in url:
            data_set.append(1)
            found_sus_word = True
            break
    if not found_sus_word:
        data_set.append(0)

    # 19. having_TLD_in_domain_name
    domain_tokens = domain.split('.')
    found_TLD_in_domain_name = False
    for tld in tlds:
        if tld in domain_tokens[0:len(domain_tokens)-1]:
            data_set.append(1)
            found_TLD_in_domain_name = True
            break

    if (not found_TLD_in_domain_name): data_set.append(0)

    # 20. having_more_than_1_TLD_in_URL

    tld_count = 0
    for tld in tlds:
        if tld in url:
            tld_count += 1
    if tld_count > 1:
        data_set.append(1)
    else:
        data_set.append(0)

    return data_set

#    # 13. Request_URL
#    i = 0
#    success = 0
#    if soup == -999:
#        data_set.append(-1)
#    else:
#        for img in soup.find_all('img', src=True):
#            dots = [x.start(0) for x in re.finditer('\.', img['src'])]
#            if url in img['src'] or domain in img['src'] or len(dots) == 1:
#                success = success + 1
#            i = i+1
#
#        for audio in soup.find_all('audio', src=True):
#            dots = [x.start(0) for x in re.finditer('\.', audio['src'])]
#            if url in audio['src'] or domain in audio['src'] or len(dots) == 1:
#                success = success + 1
#            i = i+1
#
#        for embed in soup.find_all('embed', src=True):
#            dots = [x.start(0) for x in re.finditer('\.', embed['src'])]
#            if url in embed['src'] or domain in embed['src'] or len(dots) == 1:
#                success = success + 1
#            i = i+1
#
#        for iframe in soup.find_all('iframe', src=True):
#            dots = [x.start(0) for x in re.finditer('\.', iframe['src'])]
#            if url in iframe['src'] or domain in iframe['src'] or len(dots) == 1:
#                success = success + 1
#            i = i+1
#
#        try:
#            percentage = success/float(i) * 100
#            if percentage < 22.0:
#                data_set.append(-1)
#            elif((percentage >= 22.0) and (percentage < 61.0)):
#                data_set.append(0)
#            else:
#                data_set.append(1)
#        except:
#            data_set.append(-1)
#
#    # 14. URL_of_Anchor
#    percentage = 0
#    i = 0
#    unsafe = 0
#    if soup == -999:
#        data_set.append(-1)
#    else:
#        for a in soup.find_all('a', href=True):
#            # 2nd condition was 'JavaScript ::void(0)' but we put JavaScript because the space between javascript and :: might not be
#                # there in the actual a['href']
#            if "#" in a['href'] or "javascript" in a['href'].lower() or "mailto" in a['href'].lower() or not (url in a['href'] or domain in a['href']):
#                unsafe = unsafe + 1
#            i = i + 1
#
#        try:
#            percentage = unsafe / float(i) * 100
#        except:
#            data_set.append(1)
#
#        if percentage < 31.0:
#            data_set.append(1)
#        elif ((percentage >= 31.0) and (percentage < 67.0)):
#            data_set.append(0)
#        else:
#            data_set.append(-1)
#
#    # 15. Links_in_tags
#    i = 0
#    success = 0
#    if soup == -999:
#        data_set.append(-1)
#        data_set.append(0)
#    else:
#        for link in soup.find_all('link', href=True):
#            dots = [x.start(0) for x in re.finditer('\.', link['href'])]
#            if url in link['href'] or domain in link['href'] or len(dots) == 1:
#                success = success + 1
#            i = i+1
#
#        for script in soup.find_all('script', src=True):
#            dots = [x.start(0) for x in re.finditer('\.', script['src'])]
#            if url in script['src'] or domain in script['src'] or len(dots) == 1:
#                success = success + 1
#            i = i+1
#        try:
#            percentage = success / float(i) * 100
#        except:
#            data_set.append(1)
#
#        if percentage < 17.0:
#            data_set.append(-1)
#        elif((percentage >= 17.0) and (percentage < 81.0)):
#            data_set.append(0)
#        else:
#            data_set.append(1)
#
#        # 16. SFH
#        if len(soup.find_all('form', action=True))==0:
#            data_set.append(-1)
#        else :
#            sus_actions = ['', 'about:blank', '#', 'javascript:true']
#            for form in soup.find_all('form', action=True):
#                if form['action'] in sus_actions:
#                    data_set.append(1)
#                    break
#                elif url not in form['action'] and domain not in form['action']:
#                    data_set.append(0)
#                    break
#                else:
#                    data_set.append(-1)
#                    break
#
#    # 17. Submitting_to_email
#    if response == "":
#        data_set.append(-1)
#    else:
#        if re.findall(r"[mail\(\)|mailto:?]", response.text):
#            data_set.append(1)
#        else:
#            data_set.append(-1)
#
##    # 18. Abnormal_URL
##    if response == "":
##        data_set.append(-1)
##    else:
##        if response.text == whois_response:
##            data_set.append(1)
##        else:
##            data_set.append(-1)
#
#    # 19. Redirect
#    if response == "":
#        data_set.append(-1)
#    else:
#        if len(response.history) <= 1:
#            data_set.append(-1)
#        elif len(response.history) <= 2:
#            data_set.append(0)
#        else:
#            data_set.append(1)
#
#    # 20. on_mouseover
#    if response == "":
#        data_set.append(-1)
#    else:
#        if re.findall("<script>.+onmouseover.+</script>", response.text):
#            data_set.append(1)
#        else:
#            data_set.append(-1)
#
#    # 21. RightClick
#    if response == "":
#        data_set.append(-1)
#    else:
#        if re.findall(r"event.button ?== ?2", response.text):
#            data_set.append(1)
#        else:
#            data_set.append(-1)
#
#    # 22. popUpWidnow
#    if response == "":
#        data_set.append(-1)
#    else:
#        if re.findall(r"alert\(", response.text):
#            data_set.append(1)
#        else:
#            data_set.append(-1)
#
#    # 23. Iframe
#    if response == "":
#        data_set.append(-1)
#    else:
#        if re.findall(r"[<iframe>|<frameBorder>]", response.text):
#            data_set.append(1)
#        else:
#            data_set.append(-1)
#
#    # 24. age_of_domain
#    if response == "":
#        data_set.append(-1)
#    else:
#        try:
#            registration_date = re.findall(
#                    r'Registration Date:</div><div class="df-value">([^<]+)</div>', whois_response.text)[0]
#            if diff_month(date.today(), date_parse(registration_date)) >= 6:
#                data_set.append(-1)
#            else:
#                data_set.append(1)
#        except:
#            data_set.append(1)
#
#    # 25. DNSRecord
#    dns = 1
#    try:
#        d = whois.whois(domain)
#    except:
#        dns = -1
#    if dns == -1:
#        data_set.append(-1)
#    else:
#        if registration_length / 365 <= 1:
#            data_set.append(-1)
#        else:
#            data_set.append(1)

#    # 26. web_traffic
#    try:
#        rank = BeautifulSoup(urllib.request.urlopen(
#            "http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']
#        rank = int(rank)
#        if (rank < 100000):
#            data_set.append(-1)
#        else:
#            data_set.append(0)
#    except :
#        data_set.append(1)
#
#    # 27. Page_Rank
#    try:
#        if global_rank > 0 and global_rank < 100000:
#            data_set.append(-1)
#        else:
#            data_set.append(1)
#    except:
#        data_set.append(1)
#
#    # 28. Google_Index
#    site = search(url, 5)
#    if site:
#        data_set.append(1)
#    else:
#        data_set.append(-1)

#    # 29. Links_pointing_to_page
#    if response == "":
#        data_set.append(-1)
#    else:
#        number_of_links = len(re.findall(r"<a href=", response.text))
#        if number_of_links == 0:
#            data_set.append(1)
#        elif number_of_links <= 2:
#            data_set.append(0)
#        else:
#            data_set.append(-1)

#    # 30. Statistical_report
#    url_match = re.search(
#        'at\.ua|usa\.cc|baltazarpresentes\.com\.br|pe\.hu|esy\.es|hol\.es|sweddy\.com|myjino\.ru|96\.lt|ow\.ly', url)
#    try:
#        ip_address = socket.gethostbyname(domain)
#        ip_match = re.search('146\.112\.61\.108|213\.174\.157\.151|121\.50\.168\.88|192\.185\.217\.116|78\.46\.211\.158|181\.174\.165\.13|46\.242\.145\.103|121\.50\.168\.40|83\.125\.22\.219|46\.242\.145\.98|'
#                             '107\.151\.148\.44|107\.151\.148\.107|64\.70\.19\.203|199\.184\.144\.27|107\.151\.148\.108|107\.151\.148\.109|119\.28\.52\.61|54\.83\.43\.69|52\.69\.166\.231|216\.58\.192\.225|'
#                             '118\.184\.25\.86|67\.208\.74\.71|23\.253\.126\.58|104\.239\.157\.210|175\.126\.123\.219|141\.8\.224\.221|10\.10\.10\.10|43\.229\.108\.32|103\.232\.215\.140|69\.172\.201\.153|'
#                             '216\.218\.185\.162|54\.225\.104\.146|103\.243\.24\.98|199\.59\.243\.120|31\.170\.160\.61|213\.19\.128\.77|62\.113\.226\.131|208\.100\.26\.234|195\.16\.127\.102|195\.16\.127\.157|'
#                             '34\.196\.13\.28|103\.224\.212\.222|172\.217\.4\.225|54\.72\.9\.51|192\.64\.147\.141|198\.200\.56\.183|23\.253\.164\.103|52\.48\.191\.26|52\.214\.197\.72|87\.98\.255\.18|209\.99\.17\.27|'
#                             '216\.38\.62\.18|104\.130\.124\.96|47\.89\.58\.141|78\.46\.211\.158|54\.86\.225\.156|54\.82\.156\.19|37\.157\.192\.102|204\.11\.56\.48|110\.34\.231\.42', ip_address)
#        if url_match:
#            data_set.append(-1)
#        elif ip_match:
#            data_set.append(-1)
#        else:
#            data_set.append(1)
#    except:
#        print('Connection problem. Please check your internet connection')
    #print(data_set)
#    end = time.time()
#    print(end - start)
    #return 1
