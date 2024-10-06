# DisplaySpecifications-Scrapy

## Overview

DisplaySpecifications-Scrapy is a web scraping project designed to extract detailed specifications of various devices from the DisplaySpecifications website. The project leverages Scrapy, a powerful web scraping framework, to navigate through the site and collect data efficiently.

## Complexities

### Dynamic Content Handling
- **Challenge:** Extracting data from dynamically loaded pages.
- **Solution:** Integrated a proxy service (ZenRows) to handle dynamic content and JavaScript rendering, ensuring accurate data extraction.

### Data Structure Variability
- **Challenge:** Inconsistent data structures across different product pages.
- **Solution:** Implemented robust parsing logic to handle variations in the HTML structure, using regular expressions and conditional checks to ensure data integrity.

### Rate Limiting and IP Blocking
- **Challenge:** Avoiding IP blocks and managing rate limits imposed by the target website.
- **Solution:** Utilized a premium proxy service with rotating IPs and managed request rates through Scrapy's built-in settings and middleware.

## Getting Started

### Prerequisites
- Python 3.8+
- Scrapy
- Dotenv
- MongoDB

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/faisal-fida/DisplaySpecifications-Scrapy.git
   cd DisplaySpecifications-Scrapy
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file:
   ```plaintext
   API_KEY=your_api_key_here
   ```

4. Run the scraper:
   ```bash
   scrapy crawl devicespecifications
   ```

## Usage

- The scraper will start at the main page of DisplaySpecifications and navigate through the brand and product listings, extracting detailed specifications and storing them in a MongoDB database.

## Contributing

We welcome contributions from the community. Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify or expand this draft as needed. Let me know if there are any specific aspects or details you would like to emphasize.
