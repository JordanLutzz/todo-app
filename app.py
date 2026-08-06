from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

@app.route("/")
def home():
    tasks = load_tasks()
    return render_template("home.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    new_task_name = request.form["task_name"]
    tasks.append({"name": new_task_name, "done": False})
    save_tasks(tasks)
    return redirect("/")

@app.route("/complete/<int:task_index>")
def complete_task(task_index):
    tasks = load_tasks()
    tasks[task_index]["done"] = True
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:task_index>")
def delete_task(task_index):
    tasks = load_tasks()
    tasks.pop(task_index)
    save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)