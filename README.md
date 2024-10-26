# SQL-Injection-Tool
# SQL Injection Testing Tool

This project is a **SQL Injection Testing Tool** designed to automate the process of testing web applications for SQL injection vulnerabilities. It leverages Python, the `requests` library, and customizable payloads to attempt SQL injections through HTTP GET and POST requests, helping cybersecurity professionals and developers identify potential security weaknesses.

## Features

- **Automated SQL Injection Testing**: Runs through a list of common SQL injection payloads to identify vulnerabilities.
- **Error-based and Time-based Detection**: Detects vulnerabilities by analyzing error messages and response delays.
- **Supports GET and POST Requests**: Adjusts automatically to use GET or POST based on form configurations.
- **Customizable Payloads**: Users can modify or extend the payload list in `payloads.txt` to suit specific testing needs.
- **Response Logging**: Logs responses for each payload attempt to aid in debugging and analysis.

## Project Structure

- **sql_injection.py**: Main script to perform SQL injection testing. It identifies input fields, injects payloads, and checks responses for SQL errors or time delays.
- **get_request_module.py**: Contains functions to send GET or POST requests based on the specified parameters.
- **payloads.txt**: A list of SQL injection payloads used by the tool to test for potential vulnerabilities.

## Requirements

- Python 3.7+
- `requests` library
- `BeautifulSoup` (for HTML parsing)

Install dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Dark5301/SQL-Injection-Tool.git
   cd SQL-Injection-Tool
   ```

2. **Prepare Payloads**:
   Customize `payloads.txt` if additional or specific payloads are desired.

3. **Run the Tool**:
   Execute the tool in a terminal and provide the target URL:
   ```bash
   python3 sql_injection.py
   ```

4. **Analyze Results**:
   The tool will print any detected vulnerabilities along with the payloads that triggered them.

## Notes

- **Ethical Usage**: This tool is for educational and ethical testing purposes only. Unauthorized testing on live systems is illegal and unethical.
- **DVWA Testing**: This tool was tested against Damn Vulnerable Web Application (DVWA) for educational validation. Configure DVWA on `low` security level for optimal results.

## Contributing

Feel free to open issues, suggest improvements, or submit pull requests to enhance the tool!

## License

This project is open-source and available under the [MIT License](LICENSE).
