<div align="center">

# 📈 Massive API to Snowflake Ticker Sync

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-Connector-29B5E8?logo=snowflake&logoColor=white)](https://www.snowflake.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated data pipeline script that extracts active stock ticker reference data from the **Massive API**, appends daily partition timestamps, and dynamically loads the records into a **Snowflake** data warehouse.

</div>

---

## 🚀 Features

- **Automated Pagination:** Seamlessly loops through multi-page API responses using Massive's `next_url` cursor pagination.
- **Built-in Rate Limiting:** Includes deliberate throttling (`time.sleep`) between API requests to prevent hitting rate limits.
- **Dynamic Table Provisioning:** Automatically creates or verifies the destination table schema in Snowflake based on incoming payload fields.
- **Typed Column Mapping:** Maps source JSON types to proper Snowflake SQL data types (`VARCHAR`, `BOOLEAN`, `TIMESTAMP_NTZ`).
- **Bulk Insert Execution:** Leverages parameterised bulk inserts (`executemany`) for fast, secure ingestion.
- **Environment-Driven Config:** Fully configurable via secure environment variables (`.env`).

---

## 📁 Project Structure

```text
├── .env                  # Environment variables (not tracked in git)
├── requirements.txt      # Python package dependencies
├── sync_tickers.py       # Main script execution logic
└── README.md             # Project documentation
```

---

## 🛠️️ Prerequisites & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/massive-snowflake-sync.git
   cd massive-snowflake-sync
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Or install manually: `pip install requests python-dotenv snowflake-connector-python`)*

---

## ⚙️ Configuration

Create a `.env` file in the root directory of the project. Fill in your Massive API credentials and your Snowflake connection details:

```env
# Massive API Configuration
MASSIVE_API_KEY=your_massive_api_key_here

# Snowflake Connection Configuration
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account_identifier
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema
SNOWFLAKE_ROLE=your_role

# Optional: Target Table Override (Defaults to 'stock_tickers')
SNOWFLAKE_TABLE=stock_tickers
```

---

## 📊 Snowflake Schema Mapping

The pipeline automatically maps incoming record attributes to the following Snowflake schema:

| Column Name | Snowflake Data Type | Description |
| :--- | :--- | :--- |
| `TICKER` | `VARCHAR` | Unique stock ticker symbol |
| `NAME` | `VARCHAR` | Company or asset full name |
| `MARKET` | `VARCHAR` | Market category (e.g., `stocks`) |
| `LOCALE` | `VARCHAR` | Geographic market locale |
| `PRIMARY_EXCHANGE` | `VARCHAR` | Primary exchange code (e.g., `XNYS`) |
| `TYPE` | `VARCHAR` | Security type classification |
| `ACTIVE` | `BOOLEAN` | Current active status flag |
| `CURRENCY_NAME` | `VARCHAR` | Trading currency |
| `CIK` | `VARCHAR` | SEC Central Index Key |
| `COMPOSITE_FIGI` | `VARCHAR` | Financial Instrument Global Identifier |
| `SHARE_CLASS_FIGI` | `VARCHAR` | Share class specific FIGI |
| `LAST_UPDATED_UTC` | `TIMESTAMP_NTZ` | Last update timestamp from the provider |
| `DS` | `VARCHAR` | Partition load date (`YYYY-MM-DD`) |

---

## 🏃 Usage

Execute the pipeline script directly from your terminal:

```bash
python sync_tickers.py
```

### Execution Lifecycle:
1. **Extract:** Requests active stock tickers from the Massive API (paged at 1,000 records per request).
2. **Transform:** Injects a dynamic processing date (`ds`) into every record.
3. **Load:** Connects to Snowflake, auto-generates the table if missing, and performs a bulk-insert operation.

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git origin push feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.