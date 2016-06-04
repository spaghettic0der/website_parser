from website_parser import WebsiteParser
from parser_properties import ParserProperties


def main():
    properties = ParserProperties()
    properties.source_url = "http://deadlocker.no-ip.org/ismaxawake/"
    properties.tags_to_download = ["img", "h2"]
    parser = WebsiteParser(properties)
    pass


if __name__ == "__main__":
    main()
