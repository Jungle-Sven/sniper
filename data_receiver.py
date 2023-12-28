from dotenv import load_dotenv
import os


'''this is a class to get new trading pairs, pools from solana, etc
v1 will use birdeye api'''
class DataReceiver:

    def __init__(self):
        self.birdeye_api_key = None
        self.read_api()

    def read_api(self):
        load_dotenv()
        self.birdeye_api_key = os.getenv('BIRDEYE_API_KEY')
        print(self.birdeye_api_key)

    def get_list(self):
        url = "https://public-api.birdeye.so/public/tokenlist?sort_by=v24hUSD&sort_type=desc"

        headers = {
            "x-chain": "solana",
            "X-API-KEY": ""
        }

        response = requests.get(url, headers=headers)
       
    def run(self):
        pass


if __name__ == "__main__":
    test = DataReceiver()
    test.run()
        



