## **Simple To-Do Application**

### **Project Overview**
This project is a basic **to-do list application** that allows users to manage tasks efficiently. It is designed to demonstrate Git and GitHub workflows, version control, and collaboration techniques as part of a case study assignment.

The application is written in **Python** and includes functionality to:
- Add tasks
- View tasks
- Remove tasks
- Mark tasks as completed

---

### **Features**
1. **Add a Task**: Users can add tasks to their to-do list.
2. **View Tasks**: Displays all tasks in the list.
3. **Remove a Task**: Deletes a task by its position in the list.
4. **Mark Task as Done**: Marks a task as completed.

---

### **Git Workflow**
The project follows standard Git best practices, including branching, merging, and collaborative development. Below is an outline of the workflow:

1. **Branching Strategy**:
   - `main`: Stable branch with production-ready code.
   - `feature`: Core functionality development.
   - `feature -test`: Testing and enhancements.
   - `feature3`: Bug fixes.
  

2. **Key Milestones**:
   - **Feature Branches**: Used for isolated development of new features.
   - **Pull Requests**: For code reviews and merging changes.
   - **Tagging**: Version `v1.0` marks the initial release.

3. **Merge Strategies**:
   - Fast-Forward, Rebase, and 3-Way Merges (with conflict resolution).

---

### **Setup Instructions**

#### **Prerequisites**
- Python 3.x installed on your system.
- Git installed and configured.

#### **Clone the Repository**
1. Clone the project:
   ```bash
   git clone <repository-url>
   cd simple-todo-app
   ```

#### **Run the Application**
1. Open the terminal in the project directory.
2. Run the Python script:
   ```bash
   python app.py
   ```

---

### **Git Workflow Steps**

#### **Initial Setup**
1. Initialize the repository:
   ```bash
   git init
   ```
2. Add a remote repository:
   ```bash
   git remote add origin <repository-url>
   ```

#### **Development**
1. Create a new branch for features
   ```bash
   git checkout -b feature
   ```
2. Regularly commit changes with meaningful messages:
   ```bash
   git add .
   git commit -m "Add core functionality"
   ```
3. Push changes to the remote branch:
   ```bash
   git push origin feature/initial-development
   ```

#### **Collaboration**
1. Open a pull request on GitHub for merging into `main`.
2. Review, resolve conflicts (if any), and merge changes.

---

### **Challenges Faced**
1. **Merge Conflicts**: Encountered while merging branches but resolved by carefully analyzing differences.
2. **Git LFS Integration**: Required to efficiently manage large files like images.
3. **Pre-Commit Hooks**: Ensuring code style consistency with `flake8`.

---

### **Lessons Learned**
1. Importance of meaningful commit messages for traceability.
2. Best practices for Git branching and collaboration.
3. Managing and resolving merge conflicts effectively.
4. Utilizing Git LFS for large file storage.

---

### **Versioning**
- **v1.0**: Initial release with core functionality.

---

### **Future Enhancements**
1. Add a graphical user interface (GUI) for better user experience.
2. Include persistent storage for tasks (e.g., using a database).
3. Expand functionality to include task deadlines and priority levels.

---

### **Contributors**
- **Kaushal Darji**  
  GitHub: https://github.com/kaushaldarji7182

