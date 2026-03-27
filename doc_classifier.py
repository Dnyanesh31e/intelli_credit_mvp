# Intelli-Credit MVP

**AI-powered multi-document credit appraisal assistant** for hackathon demonstration.

---

## 🎯 Overview

Intelli-Credit automates credit document analysis by:
- Extracting text from multiple file formats (PDF, DOCX, TXT, Images)
- Classifying document types using intelligent keyword matching
- Analyzing content with OpenRouter MiniMax M2.5 LLM
- Applying deterministic risk scoring
- Generating professional CAM-style credit memos

---

## ✨ Features

- 📄 Multi-format support (PDF, DOCX, TXT, PNG, JPG)
- 🔍 OCR for scanned documents (PaddleOCR)
- 🤖 AI-powered analysis (OpenRouter MiniMax M2.5)
- ⚖️ Explainable risk scoring (8 deterministic rules)
- 📝 Professional CAM memo generation
- 🎨 Modern UI with progress tracking
- ⬇️ Export to .txt format

---

## 📋 Supported Document Types

1. **Annual Return (MGT-7)** - Governance and compliance analysis
2. **Financial Results** - Financial statement analysis
3. **Debt Covenant Disclosure** - Debt and lender risk assessment
4. **Unknown Credit Documents** - Best-effort analysis

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenRouter API key (already configured in `.env`)

### Installation

```bash
# 1. Navigate to project
cd intelli_credit_mvp

# 2. Install dependencies (may take 5-10 minutes)
pip install -r requirements.txt

# 3. Test API connection
python test_openrouter.py

# 4. Run the application
streamlit run app.py
```

**Windows Users:** Simply double-click `run.bat` to start!

The app will open in your browser at `http://localhost:8501`

---

## 📖 Usage

1. **Upload Document** - Drag and drop or browse for a file
2. **Click Analyze** - System processes automatically
3. **View Results** - See classification, risk score, and insights
4. **Review CAM Memo** - Read the generated credit appraisal memo
5. **Download** - Export memo as .txt file

---

## 🏗️ Project Structure

```
intelli_credit_mvp/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # API configuration (configured)
├── .env.example               # Template for setup
├── README.md                  # This file
├── COMPLETE_PROJECT_INFO.md   # Detailed documentation
│
├── utils/
│   ├── file_parser.py         # Multi-format text extraction
│   ├── doc_classifier.py      # Document type classification
│   ├── llm_analyzer.py        # OpenRouter LLM integration
│   ├── risk_engine.py         # Risk scoring engine
│   └── cam_formatter.py       # CAM memo generation
│
└── Scripts/
    ├── test_openrouter.py     # API connection test
    ├── run.bat                # Windows quick start
    └── test_api.bat           # Quick API test
```

---

## 🔧 Technology Stack

- **UI:** Streamlit
- **LLM:** OpenRouter MiniMax M2.5 (free tier)
- **PDF Processing:** PyMuPDF
- **OCR:** PaddleOCR
- **Document Support:** python-docx
- **HTTP Client:** requests
- **Language:** Python 3.8+

---

## ⚖️ Risk Scoring

**Base Score:** 50

**Risk Adjustments:**
- +10: Asset cover < 1.2
- +15: Covenant breach detected
- +10: Auditor qualification
- +8: Multiple risk flags (≥3)
- +8: High debt-to-equity (>2.0)
- +6: Governance anomalies
- -5: Strong positive signals (≥2)
- -5: Clean compliance record

**Risk Levels:**
- 0-34: Low Risk → Approve
- 35-64: Moderate Risk → Review
- 65-100: High Risk → Reject

---

## 🧪 Testing

### Test API Connection
```bash
python test_openrouter.py
```

Expected output: Successful connection with model response

### Test with Sample Document
1. Start the app: `streamlit run app.py`
2. Upload a credit document
3. Click "Analyze Document"
4. Verify results display correctly

---

## 📞 Troubleshooting

### "Python not found"
Install Python from [python.org](https://www.python.org/downloads/) and add to PATH

### "Module not found"
```bash
pip install -r requirements.txt --upgrade
```

### "API Key Missing"
Verify `.env` file exists with `OPENROUTER_API_KEY` set

### "Port already in use"
```bash
streamlit run app.py --server.port 8502
```

---

## 📚 Documentation

- **README.md** (this file) - Quick start and overview
- **COMPLETE_PROJECT_INFO.md** - Comprehensive documentation with all features, architecture, and technical details

---

## 🎬 Demo Flow

1. Show clean UI
2. Upload document (e.g., annual return)
3. Click "Analyze Document"
4. Show progress tracking
5. Highlight classification results
6. Show risk score with color coding
7. Preview CAM memo
8. Download memo

---

## 🎯 Key Differentiators

✅ Multi-document intelligence (not single-purpose parser)  
✅ Document-specific analysis (tailored prompts per type)  
✅ Unified CAM output (consistent professional format)  
✅ Explainable risk scoring (transparent calculations)  
✅ Credit workflow aware (analyst-friendly terminology)  

---

## ⏱️ Performance

- Text Extraction: 1-3 seconds
- OCR (if needed): 5-15 seconds
- Classification: <1 second
- LLM Analysis: 5-15 seconds
- Risk Scoring: <1 second
- Total: 10-35 seconds per document

---

## 📝 License

MIT License - Free for hackathon and educational use

---

## 🎉 Status

✅ Code Complete  
✅ API Configured  
✅ Ready for Demo  

**Built for Hackathon 2026**
