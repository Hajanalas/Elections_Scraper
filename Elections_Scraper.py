"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Jana Halasova
email: hajanalas@gmail.com
discord: janah.444
"""
import csv
import sys
from bs4 import BeautifulSoup as Bs
from requests import get


def get_location_url_part2(url: str) -> list:
    parsed_html = Bs(get(url).text, features="html.parser")
    all_a_tags = parsed_html.find_all("a")
    location_url_part2 = list()
    for a_tag in all_a_tags:
        if (a_tag.attrs["href"] not in location_url_part2 and "vyber" in
                a_tag.attrs["href"]):
            location_url_part2.append(a_tag.attrs["href"])
    return location_url_part2


def get_whole_location_url(location_url_part2: list) -> list:
    url_part1 = "https://volby.cz/pls/ps2017nss/"
    whole_location_url = [url_part1 + url_part2 for url_part2 in
                          location_url_part2]
    return whole_location_url


def get_code_of_location(url: str) -> int:
    code_of_location = int(url[-18:-12])
    return code_of_location


def parse_location_html(url: str):
    parsed_location_html = Bs(get(url).text, features="html.parser")
    return parsed_location_html


def get_name_of_location(parsed_location_html) -> str:
    all_h3_tags = parsed_location_html.find_all("h3")
    name_of_location = ""
    for tag in all_h3_tags:
        if "Obec:" in tag.get_text():
            name_of_location = tag.get_text()[7:].strip()
    return name_of_location


def get_registered_voters(parsed_location_html) -> str:
    td_tag = parsed_location_html.find("td", {"headers": "sa2"})
    registered_voters = td_tag.get_text().replace("\xa0", " ")
    return registered_voters


def get_issued_envelopes(parsed_location_html) -> str:
    td_tag = parsed_location_html.find("td", {"headers": "sa3"})
    issued_envelopes = td_tag.get_text().replace("\xa0", " ")
    return issued_envelopes


def get_valid_votes(parsed_location_html) -> str:
    td_tag = parsed_location_html.find("td", {"headers": "sa6"})
    valid_votes = td_tag.get_text().replace("\xa0", " ")
    return valid_votes


def get_votes_for_parties(parsed_location_html) -> list:
    td_tags = (parsed_location_html.find_all("td", {"headers": "t1sa2 t1sb3"})
               + parsed_location_html.find_all("td", {"headers": "t2sa2 t2sb3"}
                                               ))
    votes_for_parties = [tag.get_text().replace("\xa0", " ") for tag in td_tags
                         if tag.get_text() != "-"]
    return votes_for_parties


def header_csv(parsed_location_html) -> list:
    header = ["code", "location", "registered", "envelopes", "valid"]
    td_tags = parsed_location_html.find_all("td", {"class": "overflow_name"})
    list_of_political_parties = [tag.get_text() for tag in td_tags]
    for party in list_of_political_parties:
        header.append(party)
    return header


def get_complete_location_data(code_of_location, name_of_location,
                               registered_voters, issued_envelopes,
                               valid_votes, votes_for_parties):
    data = list()
    for i in (code_of_location, name_of_location, registered_voters,
              issued_envelopes, valid_votes):
        data.append(i)
    for ii in votes_for_parties:
        data.append(ii)
    return data


def save_to_csv(file_name: str, header: list, data: list):
    csv_file = open(file_name, mode="w", encoding="utf-8", newline="")
    file_writer = csv.writer(csv_file, delimiter=",")
    file_writer.writerow(header)
    file_writer.writerows(data)
    csv_file.close()


def main():
    if len(sys.argv) != 3:
        print("""Pro spuštění chybí argument 'odkaz' a/nebo argument 'jméno'.
Zkontrolujte rovněž, zda jste argumenty zadali ve správném pořadí
a zda argument 'odkaz' obsahuje správnou URL adresu. Podrobnější
informace naleznete v souboru 'README.md'.""")
        sys.exit(1)
    else:
        url = sys.argv[1]
        url_part2 = get_location_url_part2(url)
        whole_url = get_whole_location_url(url_part2)
        print(f"STAHUJI DATA Z VYBRANÉ URL: {sys.argv[1]}")
        data = list()
        for url in whole_url:
            code_of_location = get_code_of_location(url)
            parsed_location_html = parse_location_html(url)
            name_of_location = get_name_of_location(parsed_location_html)
            registered_voters = get_registered_voters(parsed_location_html)
            issued_envelopes = get_issued_envelopes(parsed_location_html)
            valid_votes = get_valid_votes(parsed_location_html)
            votes_for_parties = get_votes_for_parties(parsed_location_html)
            complete_data = get_complete_location_data(code_of_location,
                                                       name_of_location,
                                                       registered_voters,
                                                       issued_envelopes,
                                                       valid_votes,
                                                       votes_for_parties)
            data.append(complete_data)
        print(f"UKLÁDÁM DO SOUBORU: {sys.argv[2]}")
        header = header_csv(parse_location_html(whole_url[0]))
        save_to_csv(sys.argv[2], header, data)
        print(f"UKONČUJI Elections_Scraper")


if __name__ == '__main__':
    main()
