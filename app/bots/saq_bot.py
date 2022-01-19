
class SaqBot:

    def __init__(self, network, parser):
        self.network = network
        self.parser = parser

    def scrape(self, url):
        html = self.network.run(url)
        return self.parser.parse(html)
