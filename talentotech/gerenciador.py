# Gerenciador de Tarefas Básico (Código Normal)
tasks = []

def add_task(title, description):
    task = {"title": title, "description": description, "status": "pendente"}
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("Nenhuma tarefa disponível.")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['title']} - {task['status']}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["status"] = "concluído"

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

# Testando o código
add_task("Estudar Python", "Assistir aulas e praticar.")
add_task("Fazer exercícios", "Resolver exercícios do curso.")
view_tasks()
complete_task(0)
delete_task(1)
view_tasks()
