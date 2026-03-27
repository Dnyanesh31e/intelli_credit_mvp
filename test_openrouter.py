# Intelli-Credit: Enterprise Credit Underwriting Platform

## Hackathon Submission

### Team Information
- **Project Name:** Intelli-Credit Enterprise Platform
- **Submission Date:** March 18, 2026
- **Hackathon:** Enterprise Credit Underwriting Automation

---

## Problem Statement

End-to-end automation of enterprise credit underwriting by transforming raw, unstructured financial data into comprehensive, AI-backed investment/assessment reports.

---

## Solution Overview

Intelli-Credit is a complete web application that guides Credit Analysts through a 4-stage journey:

### Stage 1: Entity Onboarding
- Capture basic entity details (CIN, PAN, Sector, Turnover)
- Input Loan Details (Type, Amount, Tenure, Interest)
- Multi-step form with validation

### Stage 2: Intelligent Data Ingestion
- Secure upload interface for 5 critical document types:
  1. ALM (Asset-Liability Management)
  2. Shareholding Pattern
  3. Borrowing Profile
  4. Annual Reports (P&L, Cashflow, Balance Sheet)
  5. Portfolio Cuts/Performance Data
- Supports PDF, DOCX, XLSX, XLS, PNG, JPG formats

### Stage 3: Automated Extraction & Schema Mapping
- Automatic document classification
- Human-in-the-loop approval/editing
- Dynamic schema configuration
- High-precision data extraction

### Stage 4: Pre-Cognitive Secondary Analysis & Reporting
- Secondary research (News, Legal, Market Sentiment)
- 360-degree entity/sector view
- Explainable recommendation engine
- Comprehensive SWOT analysis
- Downloadable investment report

---

## Key Features

### 1. Multi-Format Document Support
- PDF (with OCR fallback for scanned documents)
- DOCX (Microsoft Word)
- XLSX/XLS (Excel)
- Images (PNG, JPG, JPEG)
- TXT (Plain text)

### 2. Intelligent Classification
- Automatic document type detection
- Keyword-based classification
- Confidence scoring
- Human-in-the-loop editing

### 3. AI-Powered Analysis
- OpenRouter MiniMax M2.5 integration
- Document-specific analysis prompts
- Structured JSON output
- Fallback handling

### 4. Explainable Risk Scoring
- Deterministic rule-based scoring
- Transparent calculations
- Score breakdown with explanations
- Three risk levels: Low/Moderate/High

### 5. Secondary Research Integration
- News analysis with sentiment
- Legal/regulatory checks
- Market sentiment analysis
- Sector trends

### 6. Comprehensive Reporting
- Professional CAM memo generation
- Investment report with SWOT
- Downloadable formats (TXT, JSON)
- Shareable reports

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| LLM | OpenRouter MiniMax M2.5 |
| PDF Processing | PyMuPDF |
| OCR | PaddleOCR |
| Excel | pandas + openpyxl |
| Document | python-docx |
| HTTP Client | requests |
| Language | Python 3.8+ |

---

## Architecture

```
User Upload → File Parser → Text Extraction
    ↓
Document Classifier → Human Approval
    ↓
Schema Mapping → Data Extraction
    ↓
Secondary Research → LLM Analysis
    ↓
Risk Engine → Recommendation
    ↓
Report Generator → Downloadable Report
```

---

## Project Structure

```
intelli_credit_mvp/
├── app.py                    # Simple single-document app
├── app_complete.py           # Complete 4-stage application
├── requirements.txt          # Python dependencies
├── .env                      # API configuration
├── sample_documents/         # Sample test documents
│   ├── sample_annual_report.txt
│   ├── sample_borrowing_profile.txt
│   ├── sample_shareholding.txt
│   ├── sample_alm.txt
│   └── sample_portfolio.txt
└── utils/
    ├── file_parser.py        # Multi-format text extraction
    ├── doc_classifier.py     # Document type classification
    ├── llm_analyzer.py       # LLM integration
    ├── risk_engine.py        # Risk scoring engine
    ├── cam_formatter.py      # CAM memo generation
    ├── entity_manager.py     # Entity data management
    ├── schema_manager.py     # Dynamic schema handling
    ├── secondary_research.py # Secondary research module
    ├── reasoning_engine.py   # Recommendation engine
    └── report_generator.py   # Investment report generator
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- OpenRouter API key (free tier available)

### Quick Start

```bash
# 1. Navigate to project
cd intelli_credit_mvp

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API key in .env file
# (Already configured with sample key)

# 4. Run the application
streamlit run app_complete.py
```

The app will open at `http://localhost:8501`

---

## Demo Flow

### 1. Entity Onboarding (2 min)
- Enter company details (ABC Industries Ltd)
- Fill loan information
- Submit to create entity

### 2. Document Upload (3 min)
- Upload 5 sample documents
- Verify upload progress
- Proceed to classification

### 3. Extraction & Classification (3 min)
- Review auto-classification
- Approve/edit classifications
- Configure schema if needed
- Extract data

### 4. Analysis & Reporting (2 min)
- View recommendation
- Review SWOT analysis
- Examine secondary research
- Download investment report

**Total Demo Time: ~10 minutes**

---

## Success Criteria Met

### Operational Excellence
- ✅ Stable web application
- ✅ Uploads and forms work flawlessly
- ✅ Progress tracking
- ✅ Error handling

### Extraction Accuracy
- ✅ Handles complex financial tables
- ✅ Multi-format support
- ✅ OCR for scanned documents
- ✅ Schema-based extraction

### Analytical Depth
- ✅ Comprehensive secondary research
- ✅ Pre-cognitive risk signals
- ✅ Market sentiment analysis
- ✅ Sector trends integration

### User Experience
- ✅ Intuitive 4-stage journey
- ✅ Raw data to final report
- ✅ Fast processing (10-35 seconds)
- ✅ Downloadable outputs

---

## Key Differentiators

1. **End-to-End Solution**: Complete 4-stage workflow
2. **Human-in-the-Loop**: Approval and editing at each stage
3. **Explainable AI**: Transparent reasoning and recommendations
4. **Multi-Document Intelligence**: Handles 5 different document types
5. **Professional Output**: CAM memo format familiar to credit analysts
6. **Free LLM Integration**: Uses OpenRouter free tier

---

## Screenshots

### Stage 1: Entity Onboarding
- Multi-field form with validation
- Loan details capture
- Clean UI with progress indicators

### Stage 2: Document Upload
- Drag-and-drop interface
- Progress tracking (5/5 documents)
- File type indicators

### Stage 3: Classification
- Auto-classification display
- Confidence scores
- Edit/approve controls

### Stage 4: Analysis Dashboard
- Recommendation card
- SWOT visualization
- Secondary research summary
- Downloadable reports

---

## Future Enhancements

- Database persistence
- User authentication
- Batch document processing
- PDF report export
- Email notifications
- Integration with banking APIs
- Historical tracking
- Custom risk rules

---

## Known Limitations

1. In-memory storage (no database)
2. Single session (no user accounts)
3. LLM rate limits (free tier)
4. No batch processing

---

## Testing

### Test Files Included
- `sample_annual_report.txt` - Financial statements
- `sample_borrowing_profile.txt` - Debt analysis
- `sample_shareholding.txt` - Ownership structure
- `sample_alm.txt` - Asset-liability management
- `sample_portfolio.txt` - Portfolio performance

### Running Tests
```bash
# Test API connection
python test_openrouter.py

# Run application
streamlit run app_complete.py
```

---

## Credits

- Built with Streamlit
- Powered by OpenRouter MiniMax M2.5
- PDF Processing: PyMuPDF
- OCR: PaddleOCR

---

## License

MIT License - Free for hackathon and educational use

---

**Built for Hackathon 2026** 
**Team: Intelli-Credit**
