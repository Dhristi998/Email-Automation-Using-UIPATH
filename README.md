# 📬 Email Summarization Automation with UiPath & Python

## 🔍 Project Description

This project automates the task of reading and summarizing recent emails from a web-based email client (like Gmail) using **UiPath** for browser automation and **Python** for natural language processing (NLP). It extracts email content, summarizes it using a locally-run NLP model (like BART or Pegasus), and saves the summarized data into an Excel file for easy review and reporting. The solution operates **fully offline**, ensuring data privacy and efficient processing without relying on cloud APIs or third-party tools like LangChain.

---

## ⚙️ Step-by-Step Process

### **Step 1: Launch Gmail in Browser**
- UiPath bot opens the Gmail web interface using *Use Application/Browser* activity.
- Automatically logs in using provided credentials (can be securely stored in assets or config files).

### **Step 2: Email Extraction**
- Bot navigates the inbox and iterates through recent or unread emails.
- Extracts essential data: **sender name**, **email subject**, **timestamp**, and **email body**.
- Cleans and formats email content for further processing.

### **Step 3: Hand Over to Python**
- Email body is passed to a local Python script using *Invoke Python Method* activity.
- Python uses a pre-trained transformer model (e.g., `facebook/bart-large-cnn` or `google/pegasus-xsum`) for summarization.
- Summary is returned to UiPath.

### **Step 4: Store Results in Excel**
- UiPath writes the sender, subject, original content, and summary into a structured Excel file using *Write Range*.
- The file is saved locally for reference and can be used for reporting or reviewing summaries.

---

## 🧠 NLP Model & Python Script

- Uses the **Hugging Face Transformers** library.
- Can run completely offline after downloading the model once.
- Ensures high-quality, human-like summaries from long or complex emails.


## ✅ Advantages

- 🔒 **Offline & Secure**: No cloud APIs, all processing is local.
- ⚡ **Time-Saving**: Automatically summarizes multiple emails in seconds.
- 📊 **Structured Output**: Summaries saved in Excel for easy reading and filtering.
- 🧩 **Modular Design**: Python and UiPath are loosely coupled, making customization easy.
- 👩‍💼 **Productivity Boost**: Great for professionals who receive large volumes of emails daily.

---

## 🛠️ Possible Modifications & Extensions

Here are a few ideas to customize or extend this project:

### 1. **Add Email Filters**
- Modify the bot to summarize only emails from specific senders or containing keywords (e.g., “Invoice”, “Urgent”).

### 2. **Sentiment Analysis**
- Use libraries like `TextBlob` or `VADER` to add sentiment scoring to each email.

### 3. **Summarize Attachments**
- Extend functionality using OCR (e.g., `pytesseract`) to extract and summarize text from image/PDF attachments.

### 4. **Email Categorization**
- Use simple machine learning or rule-based classification to tag emails (e.g., Finance, Meetings, Newsletters).

### 5. **Daily Digest Email**
- Automatically send a summarized report back to the user as a daily email.

### 6. **Power BI Dashboard**
- Import Excel data into Power BI to visualize trends like email volume, sentiment, or topics over time.

---

## 📁 Project Structure

```
email-summarizer/
│
├── UiPathProject/
│   ├── Main.xaml
│   └── Config.xlsx
│
├── Python/
│   ├── summarizer.py
│   └── requirements.txt
│
├── Output/
│   └── summarized_emails.xlsx
│
└── README.md
```

---

## 🧪 Requirements

### UiPath:
- UiPath Studio (2022.10+ recommended)
- Python Integration enabled
- Excel activities package

### Python:
- Python 3.8+
- Transformers: `pip install transformers`
- PyTorch: `pip install torch`
- Pandas: `pip install pandas`

---

## 🚀 Get Started

1. Clone the repository.
2. Install required Python packages.
3. Set up your Gmail credentials (manually or via UiPath Orchestrator Assets).
4. Run the UiPath bot (`Main.xaml`).
5. Review the `summarized_emails.xlsx` output file.

---

## 📬 Final Thoughts

This project is a practical example of how automation and AI can combine to reduce digital overload and improve how we interact with communication tools. Whether you're a busy professional, a developer exploring RPA+AI integrations, or an organization aiming for smarter workflows—this solution is a great foundation to build on.

