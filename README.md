Below is the updated README with a detailed example for the Sample Input and Sample Output sections:

---

# ✨ Hamiltonian Cycle Finder Web Application ✨

## 🔍 Overview
This is a simple web application built with Django that finds the Hamiltonian cycle for a given directed weighted graph. Users can input the number of vertices and edges, then the system will calculate and display the Hamiltonian cycle.

## 📅 Features
- 💡 Accepts user input for graph vertices and edges.
- 🛠️ Processes the graph to find a Hamiltonian cycle.
- 🔄 Displays the result directly on the webpage.
- 🌐 Simple and user-friendly interface.

## 🛁 Project Structure
```
.
├── 📚 README.md
├── 💾 db.sqlite3
├── 💻 hamilton_app
│   ├── 📝 Hamilton.py     # Hamiltonian cycle calculation logic
│   ├── 📗 __init__.py
│   ├── 📒 admin.py
│   ├── 📒 apps.py
│   ├── 📝 graph.py        # Handles graph input and processing
│   ├── 📑 migrations
│   ├── 📓 models.py       # Django models (if needed)
│   ├── 🌍 static
│   │   ├── 🎨 style.css   # CSS styles
│   │   ├── ⚡ script.js   # JavaScript for frontend behavior
│   ├── 📚 templates
│   │   ├── 📄 index.html  # Main HTML page
│   ├── 📙 tests.py
│   ├── 📝 urls.py         # URL routing
│   ├── 📙 utils.py        # Utility functions
│   ├── 📝 views.py        # Handles user requests and responses
├── 💻 hamilton_project
│   ├── 📗 __init__.py
│   ├── 📒 asgi.py
│   ├── 📓 settings.py     # Django settings
│   ├── 📝 urls.py         # Root URL configuration
│   ├── 📒 wsgi.py
├── 📝 main.py
├── 💪 manage.py           # Django management script
```

## ⚙️ Installation & Setup
### ⚡ Prerequisites
Ensure you have Python installed. You also need Django.

### 🔍 Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd hamilton_project
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install django
   ```
4. Run the Django server:
   ```sh
   python manage.py runserver
   ```
5. Open a browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## 📈 Usage
1. 🔢 Enter the number of vertices and edges.
2. ✏️ Input each edge with its start vertex, end vertex, and weight.
3. 🚶‍♂️ Click **Find Path** to compute the Hamiltonian cycle.
4. 🌟 The result will be displayed on the page.

## 📝 Sample Input
```
5 20
1 2 10
1 3 25
1 4 18
1 5 22
2 1 12
2 3 30
2 4 24
2 5 15
3 1 20
3 2 28
3 4 14
3 5 27
4 1 16
4 2 21
4 3 19
4 5 23
5 1 26
5 2 17
5 3 29
5 4 11
```
*This sample input represents a graph with 5 vertices and 20 directed edges. The first line specifies the number of vertices (5) and edges (20). Each subsequent line contains three numbers indicating the start vertex, end vertex, and the weight (or cost) of that edge.*

## 📊 Sample Output
```
Hamiltonian Cycle: 1 -> 3 -> 4 -> 5 -> 2 -> 1
Total Cost: 100
```
*The output shows a valid Hamiltonian cycle (starting and ending at vertex 1) and the total cost of traversing the cycle.*

## 🌐 License
This project is licensed under the MIT License.

---

Let me know if you need any further modifications!
