
# 🕸️ Web Scraping Safari

A Python script that scrapes the top 5 trending GitHub repositories using `requests` and `BeautifulSoup`, then saves the results to a CSV file with the repository name and link.

---

## 🚀 Features

- 🔍 Scrapes [GitHub Trending](https://github.com/trending)
- 🧠 Extracts repository name and link
- 📁 Saves results to `trending_repos.csv`
- 🛡️ Handles errors gracefully (network, parsing, file I/O)

---

## 🛠️ Requirements

- Python 3.x
- Install required library:

```bash
pip install beautifulsoup4 requests
````

---

## 📂 Usage

Run the script from the terminal:

```bash
python main.py
```

**Output:**

* A `trending_repos.csv` file containing:

| Repository Name | Link                                                             |
| --------------- | ---------------------------------------------------------------- |
| owner/repo1     | [https://github.com/owner/repo1](https://github.com/owner/repo1) |
| owner/repo2     | [https://github.com/owner/repo2](https://github.com/owner/repo2) |
| ...             | ...                                                              |

---

## ❗ Error Handling

* If GitHub structure changes, it warns the user.
* Handles timeouts, connection errors, and bad HTTP responses.
* Skips individual entries if they are malformed.
* Gracefully handles file write issues.

---

## 🧑‍💻 Author

**Your Name**
[GitHub Profile](https://github.com/yourusername)

---

## 📄 License

This project is licensed under the MIT License.

