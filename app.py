
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []


@app.route("/")
def home():
    status_filter = request.args.get("status", "all")
    priority_filter = request.args.get("priority", "all")

    filtered_tasks = []

    for index, task in enumerate(tasks):
        if status_filter == "pending" and task["completed"]:
            continue
        if status_filter == "completed" and not task["completed"]:
            continue
        if priority_filter != "all" and task["priority"] != priority_filter:
            continue

        filtered_tasks.append({"id": index, **task})

    return render_template(
        "index.html",
        tasks=filtered_tasks,
        status_filter=status_filter,
        priority_filter=priority_filter,
    )


@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task", "").strip()
    priority = request.form.get("priority", "medium").lower()

    if priority not in ["low", "medium", "high"]:
        priority = "medium"

    if task_name:
        tasks.append({
            "name": task_name,
            "priority": priority,
            "completed": False,
        })

    return redirect(url_for("home"))


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = not tasks[task_id]["completed"]

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
