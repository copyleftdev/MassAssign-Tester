# Concurrent Mass Assignment Exploit Tool

This tool is designed to test for mass assignment vulnerabilities in web applications by sending multiple requests concurrently. It can help security researchers identify potential risks in web applications during penetration tests or security assessments.

## ⚠️ Disclaimer

**Use this tool responsibly and ethically.** Only run it against systems you have permission to test. Unauthorized scanning and data modification is illegal and unethical.

## Requirements

- Python 3.7+
- Libraries: `aiohttp`

To install the necessary libraries, use:

```bash
pip install aiohttp
```

## Usage

```bash
python exploit_tool.py --url <TARGET_URL> --data <ORIGINAL_DATA> --exploit <EXPLOIT_DATA> --concurrent <NUMBER_OF_CONCURRENT_REQUESTS>
```

**Parameters:**

- `TARGET_URL`: The URL endpoint you wish to target.
- `ORIGINAL_DATA`: The expected data in JSON format. Example: `{"username":"user", "password":"pass"}`
- `EXPLOIT_DATA`: The exploit data in JSON format you wish to inject. Example: `{"isAdmin":true}`
- `NUMBER_OF_CONCURRENT_REQUESTS`: The number of concurrent requests you wish to make.

**Example:**

```bash
python exploit_tool.py --url "http://target.com/update_profile" --data '{"username":"user", "password":"pass"}' --exploit '{"isAdmin":true}' --concurrent 10
```

This will send 10 concurrent requests to "http://target.com/update_profile" with the supplied data and exploit data.

## Features

- Utilizes asynchronous I/O to make concurrent requests, allowing for faster testing.
- Easy to use with JSON-formatted input for data and exploit.

## Future Enhancements

- Support for multiple URLs in one run.
- Enhanced logging and reporting.
- Proxy support for using tools like Burp Suite.

---

Save this content as `README.md` in the same directory as your exploit tool. Adjust any details as necessary to fit your specific needs or environment.
