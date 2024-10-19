
# Groww to Trendlyne Portfolio Importer

This script generates a holding statement from your Groww portfolio, formatted for easy import and further analysis in Trendlyne.

## Prerequisites

1. **Python**: Ensure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/).
   
2. **Beautiful Soup**: The script requires Beautiful Soup for parsing HTML. You can install it by following the instructions in [this GeeksforGeeks guide](https://www.geeksforgeeks.org/beautifulsoup-installation-python/).

    Alternatively, you can install Beautiful Soup via pip:
    ```bash
    pip install beautifulsoup4
    ```

## Instructions

### Step 1: Log in to Groww
1. Visit [Groww](https://groww.in/login) and log in to your account.

### Step 2: Access Your Stocks Dashboard
1. Navigate to the [Groww Stocks Dashboard](https://groww.in/stocks/user/investments) to view your portfolio.

### Step 3: Copy the HTML of the Page
1. Open your browser's Developer Tools by right-clicking and selecting "Inspect" (or press `Cmd + Option + I` on Mac, or `Ctrl + Shift + I` on Windows/Linux).
2. In the **Elements** tab, copy the entire HTML of the page.

### Step 4: Save the HTML Locally
1. Open the `groww_investment_page.html` file located in the `input` folder.
2. Paste the copied HTML into this file and save it.

### Step 5: Run the Script
1. Open your terminal or command prompt and run the script `create_holding_stmt_for_trendlyne.py`:
    ```bash
    python create_holding_stmt_for_trendlyne.py
    ```

### Step 6: Import the Portfolio into Trendlyne
1. Visit [Trendlyne’s manual import page](https://trendlyne.com/portfolio/import-portfolio/#manual-import).
2. Select your _Account_ and _Current Portfolio_, then click the _Download Excel_ button (no need to download the file).
3. On the right-hand side, choose the generated file from the `output` folder and proceed with the import.

---