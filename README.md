# Study Group Recommendations

An intelligent web application that helps students find optimal study groups based on their courses, schedules, and learning needs.

## Features

- **CSV Upload**: Upload student data in CSV format
- **AI-Powered Matching**: Smart grouping based on courses, schedules, and learning needs
- **Interactive UI**: Beautiful, responsive interface
- **No Login Required**: Simple and easy to use

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmad18697/StudyGroupRecommendations.git
   cd StudyGroupRecommendations
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Usage

1. Prepare a CSV file with the following columns:
   - `name`: Student's name
   - `course`: Course name
   - `grade_estimate`: Numeric grade estimate (0-100)
   - `topics_needed`: Comma-separated list of topics
   - `preferred_times`: Comma-separated list of available times

2. Upload the CSV file using the web interface
3. View and download the recommended study groups

## Example CSV

```csv
name,course,grade_estimate,topics_needed,preferred_times
John Doe,CS101,85,"Calculus, Algebra","Mon 10-12, Wed 2-4"
Jane Smith,CS101,92,"Algorithms, Data Structures","Mon 10-12, Thu 3-5"
```

## Technologies Used

- Backend: Python, Flask
- Frontend: HTML5, CSS3, JavaScript
- Data Processing: Pandas
- AI: CrewAI (for intelligent grouping)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
