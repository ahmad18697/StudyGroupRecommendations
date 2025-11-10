from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
import pandas as pd
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'data'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload
app.secret_key = 'your-secret-key-here'  # Change this in production
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching for development

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Mock AI analysis function (to be replaced with actual CrewAI integration)
def analyze_student_data(df):
    # This is a placeholder - in production, this would call CrewAI
    groups = []
    
    # Simple grouping by course for demo purposes
    for course, group in df.groupby('course'):
        members = []
        for _, row in group.iterrows():
            members.append({
                'name': row['name'],
                'grade_estimate': int(row['grade_estimate']),
                'topics_needed': [t.strip() for t in row['topics_needed'].split(',')],
                'preferred_times': row['preferred_times']
            })
        
        # Split into groups of 3-5 students
        for i in range(0, len(members), 4):
            group_members = members[i:i+4]
            if len(group_members) >= 2:  # Only create groups with at least 2 members
                groups.append({
                    'group_id': f"G{len(groups) + 1}",
                    'course': course,
                    'members': group_members,
                    'reason': f"Grouped by shared course {course} with {len(group_members)} students"
                })
    
    return {
        'recommended_groups': groups,
        'isolated_students': []
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{int(datetime.now().timestamp())}_{filename}")
        file.save(filepath)
        
        try:
            # Read the CSV file
            df = pd.read_csv(filepath)
            required_columns = ['name', 'course', 'grade_estimate', 'topics_needed', 'preferred_times']
            
            if not all(col in df.columns for col in required_columns):
                return jsonify({'error': 'CSV must contain columns: name, course, grade_estimate, topics_needed, preferred_times'}), 400
            
            # Analyze the data
            results = analyze_student_data(df)
            return jsonify(results)
            
        except Exception as e:
            return jsonify({'error': f'Error processing file: {str(e)}'}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True, use_reloader=True)
