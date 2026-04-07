from flask import Flask, render_template, request, jsonify
import csv
from pathlib import Path

app = Flask(__name__)

def load_co2_data():
    """Load CO2 data from CSV file"""
    data = []
    
    # Get the absolute path to the CSV file
    current_dir = Path(__file__).parent
    csv_path = current_dir / 'CO2.csv'
    
    try:
        with open(csv_path, 'r') as file:
            # Read the CSV file
            csv_reader = csv.reader(file)
            
            # Skip the header
            next(csv_reader)
            
            # Process each row
            for row in csv_reader:
                if len(row) >= 3:
                    try:
                        # Clean the data - remove quotes and strip whitespace
                        cleaned_row = [col.strip().strip('"') for col in row]
                        
                        # Parse the data
                        index = int(cleaned_row[0]) if cleaned_row[0] else None
                        co2 = float(cleaned_row[1]) if cleaned_row[1] else None
                        day = int(cleaned_row[2]) if cleaned_row[2] else None
                        
                        if co2 is not None and day is not None:
                            data.append({
                                'index': index,
                                'CO2': co2,
                                'Day': day
                            })
                    except (ValueError, IndexError):
                        continue
        
        return data
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

@app.route('/')
def start():
    """Start page with two options"""
    return render_template('start.html')

@app.route('/graph')
def graph_view():
    """Pure graph view - only chart, no table or filters"""
    all_data = load_co2_data()
    
    # Get summary statistics for the graph page
    if all_data:
        co2_values = [d['CO2'] for d in all_data]
        summary = {
            'total_records': len(all_data),
            'min_co2': min(co2_values),
            'max_co2': max(co2_values),
            'avg_co2': round(sum(co2_values) / len(co2_values), 2)
        }
    else:
        summary = {
            'total_records': 0,
            'min_co2': 0,
            'max_co2': 0,
            'avg_co2': 0
        }
    
    return render_template('graph.html', 
                         data=all_data, 
                         summary=summary)

@app.route('/data')
def data_view():
    """Data view - table with filters and all data management"""
    all_data = load_co2_data()
    
    # Get unique days for the dropdown
    days = sorted(set(d['Day'] for d in all_data))
    
    # Get summary statistics
    if all_data:
        co2_values = [d['CO2'] for d in all_data]
        summary = {
            'total_records': len(all_data),
            'unique_days': len(days),
            'min_co2': min(co2_values),
            'max_co2': max(co2_values),
            'avg_co2': round(sum(co2_values) / len(co2_values), 2),
            'min_day': min(days),
            'max_day': max(days)
        }
        
        # Calculate CO2 level categories based on Latvian guidelines
        # 420-1000 ppm - Good air quality
        # 1000-2000 ppm - Air quality declining
        # >2000 ppm - Poor air quality
        summary['good'] = len([c for c in co2_values if 420 <= c < 1000])
        summary['moderate'] = len([c for c in co2_values if 1000 <= c < 2000])
        summary['poor'] = len([c for c in co2_values if c >= 2000])
    else:
        summary = {
            'total_records': 0,
            'unique_days': 0,
            'min_co2': 0,
            'max_co2': 0,
            'avg_co2': 0,
            'min_day': 0,
            'max_day': 0,
            'good': 0,
            'moderate': 0,
            'poor': 0
        }
    
    return render_template('data.html', 
                         data=all_data, 
                         days=days,
                         summary=summary)

@app.route('/filter', methods=['POST'])
def filter_data():
    """Filter data by day"""
    try:
        selected_day = request.form.get('day', '')
        
        if selected_day:
            selected_day = int(selected_day)
            all_data = load_co2_data()
            
            # Filter data for the selected day
            filtered_data = [d for d in all_data if d['Day'] == selected_day]
            
            # Calculate statistics for filtered data
            if filtered_data:
                co2_values = [d['CO2'] for d in filtered_data]
                stats = {
                    'avg_co2': round(sum(co2_values) / len(co2_values), 2),
                    'min_co2': min(co2_values),
                    'max_co2': max(co2_values)
                }
            else:
                stats = {}
            
            return jsonify({
                'success': True,
                'data': filtered_data,
                'stats': stats,
                'count': len(filtered_data),
                'day': selected_day
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Lūdzu, izvēlieties dienu'
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        })

@app.route('/api/data')
def get_all_data():
    """API endpoint to get all data"""
    data = load_co2_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)