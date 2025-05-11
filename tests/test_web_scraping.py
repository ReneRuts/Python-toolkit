from src.web_scraping import is_valid_url, fetch_html, parse_html, scrape_with_selenium

def test_is_valid_url():
    valid_url = "https://www.howest.be"
    invalid_url = "htp://www.howest.be"
    assert is_valid_url(valid_url)
    assert not is_valid_url(invalid_url)

def test_fetch_html():
    url = "https://www.howest.be"
    html = fetch_html(url)
    assert html is not None
    assert "</html>" in html 

def test_parse_html():
    url = "https://www.howest.be"
    html_content = fetch_html(url)
    parsed_data = parse_html(html_content)
    assert parsed_data['title'] == 'Howest, de Hogeschool West-Vlaanderen'
    assert len(parsed_data['headers']) > 0  

def test_web_scraping_with_requests():
    url = "https://www.howest.be"
    html = fetch_html(url)
    data = parse_html(html) if html else None
    assert data is not None
    assert "Howest" in data["title"]
    assert len(data["headers"]) > 0