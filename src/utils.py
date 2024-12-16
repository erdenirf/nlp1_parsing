from bs4 import BeautifulSoup

def parse_html(html: str) -> dict:
    """Parse HTML to dict.

    Args:
        html (str): HTML to parse.

    Returns:
        dict: Parsed data.
    """
    soup = BeautifulSoup(html, 'lxml')

    def categories(soup: BeautifulSoup) -> str:
        tags = soup.find_all('a', class_='tag__link')
        return ", ".join([tag.get_text(strip=True) for tag in tags])
    
    def tags(soup: BeautifulSoup, default: str = "N/A") -> str:
        tags = soup.find('span', class_='b-singlepost-tags-items')
        if tags is not None:
            return tags.get_text(strip=True)
        tags = soup.find('div', class_='aentry-tags')
        if tags is not None:
            return tags.get_text(strip=True)
        return default
    
    def title(soup: BeautifulSoup, default: str = "N/A") -> str:
        title = soup.find('h1')
        if title is not None:
            return title.get_text(strip=True)
        return default
    
    def body(soup: BeautifulSoup, default: str = "N/A") -> str:
        body = soup.find('article', class_='entry-content')
        if body is not None:
            return body.get_text(strip=True, separator=" ")
        body = soup.find('div', class_='aentry-post__content')
        if body is not None:
            return body.get_text(strip=True, separator=" ")
        return default

    return {
        "date": soup.find('time').get_text(strip=True),
        "title": title(soup),
        "categories": categories(soup),
        "tags": tags(soup),
        "url": soup.find('link', attrs={'rel': 'canonical'}).get('href').strip(),
        "body": body(soup),
    }
