# CLI Tool Dev
Dans cet exo, aucune depédance externe n'est requise. 
1. cloonez le repo: `git clone https://github.com/ynoule/exo2-python.git`
2. Accédez au projet : `cd exo2-python`
3. Créer votre environnement virtuel: `python -m venv .venv`
4. Activez votre environnement virtuel: `source .venv/bin/activate`

## Exécution des commandes python pour tester add; list and delete. 
1. ouvrez dans votre terminal le fichier tasks.json
. Exécutez la commande: `python -m task_manager.cli add "Test1: Adding task1"`
###### Le fichier `tasks.json` devrait mse mettre à jour et contenir le code suivant:
```
[
    {
        "id": 1,
        "description": "Test1: Adding task",
        "priority": 1
    }
]
```
2. Listez les tâches: `python -m task_manager.cli list`
###### Dans votre terminal, vous aure la sortie: `{'id': 1, 'description': 'Test1: Adding task', 'priority': 1}`
3. Supprimez la tâche: `python -m task_manager.cli delete 1`
###### Le fichier `tasks.json` devrait maintenant être vide.

## Visualisation du fichier log
Le fichier log `task_manager.log` présent dans le dossier `logs` à la racine du projet contient les messages de log générés par l'application.
```
2025-03-21 11:45:30,203 - DEBUG - Loaded tasks successfully.
2025-03-21 11:45:30,203 - DEBUG - Tasks saved.
2025-03-21 11:45:30,203 - INFO - Task added: {'id': 1, 'description': 'Buy groceries', 'priority': 1}
2025-03-21 11:45:30,203 - INFO - Task added: {'id': 1, 'description': 'Buy groceries', 'priority': 1}
2025-03-21 11:46:03,136 - DEBUG - Loaded tasks successfully.
2025-03-21 11:46:21,070 - DEBUG - Loaded tasks successfully.
2025-03-21 11:46:21,070 - DEBUG - Tasks saved.
2025-03-21 11:46:21,070 - INFO - Task with ID 1 deleted.
2025-03-21 11:46:21,070 - INFO - Task 1 deleted.
2025-03-21 11:46:26,589 - DEBUG - Loaded tasks successfully.
2025-03-21 11:46:31,732 - DEBUG - Loaded tasks successfully.
2025-03-21 11:46:31,732 - WARNING - Task with ID 1 not found.
2025-03-21 11:46:31,732 - WARNING - Task 1 not found.
2025-03-21 11:46:50,011 - DEBUG - Loaded tasks successfully.
2025-03-21 11:46:50,011 - DEBUG - Tasks saved.
2025-03-21 11:46:50,011 - INFO - Task added: {'id': 1, 'description': 'Test1: Adding task', 'priority': 1}
2025-03-21 11:46:50,011 - INFO - Task added: {'id': 1, 'description': 'Test1: Adding task', 'priority': 1}
2025-03-21 11:46:55,738 - DEBUG - Loaded tasks successfully.
2025-03-21 11:47:03,553 - DEBUG - Loaded tasks successfully.
2025-03-21 11:47:03,554 - DEBUG - Tasks saved.
2025-03-21 11:47:03,554 - INFO - Task added: {'id': 1, 'description': 'Test task', 'priority': 2}
2025-03-21 11:47:03,554 - DEBUG - Loaded tasks successfully.
2025-03-21 11:47:03,554 - DEBUG - Loaded tasks successfully.
2025-03-21 11:47:03,554 - DEBUG - Tasks saved.
2025-03-21 11:47:03,554 - INFO - Task added: {'id': 1, 'description': 'Task to delete', 'priority': 1}
2025-03-21 11:47:03,554 - DEBUG - Loaded tasks successfully.
2025-03-21 11:47:03,554 - DEBUG - Tasks saved.
2025-03-21 11:47:03,554 - INFO - Task added: {'id': 2, 'description': 'Task to keep', 'priority': 1}
2025-03-21 11:47:03,554 - DEBUG - Loaded tasks successfully.
2025-03-21 11:47:03,554 - DEBUG - Tasks saved.
2025-03-21 11:47:03,554 - INFO - Task with ID 1 deleted.
2025-03-21 11:47:03,554 - DEBUG - Loaded tasks successfully.
2025-03-21 11:47:03,554 - DEBUG - Loaded tasks successfully.
2025-03-21 11:47:03,554 - WARNING - Task with ID 999 not found.
2025-03-21 11:59:32,451 - DEBUG - Loaded tasks successfully.
2025-03-21 11:59:32,452 - DEBUG - Tasks saved.
2025-03-21 11:59:32,452 - INFO - Task added: {'id': 2, 'description': 'Test1: Adding task', 'priority': 1}
2025-03-21 11:59:32,452 - INFO - Task added: {'id': 2, 'description': 'Test1: Adding task', 'priority': 1}
2025-03-21 11:59:46,829 - DEBUG - Loaded tasks successfully.
2025-03-21 11:59:46,829 - DEBUG - Tasks saved.
2025-03-21 11:59:46,830 - INFO - Task with ID 2 deleted.
2025-03-21 11:59:46,830 - INFO - Task 2 deleted.
2025-03-21 12:00:18,473 - DEBUG - Loaded tasks successfully.

```
