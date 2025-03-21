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
