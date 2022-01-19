# [Native]
import json
import os

# [Project]
from network import SaqNetworkInteractor
from parser import SaqParser
from bots.saq_bot import SaqBot


if __name__ == "__main__":
    product_id = os.environ.get('SAQ_PRODUCT_ID', None)
    assert product_id, 'please set the `SAQ_PRODUCT_ID` parameter in the .env file'

    bot = SaqBot(
        network=SaqNetworkInteractor(),
        parser=SaqParser()
    )

    availability = bot.scrape(f"https://www.saq.com/en/{product_id}")
    print(json.dumps(availability, indent=4, sort_keys=True))
