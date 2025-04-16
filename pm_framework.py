from datetime import datetime

class ProjectManager:
    def __init__(self):
        self.projects = {}
    
    def create_project(self, name):
        if name not in self.projects:
            self.projects[name] = {
                'tasks': [],
                'status': 'En Progreso',
                'created_at': datetime.now(),
                'team_members': []
            }
            return True
        return False
    
    def add_task(self, project_name, task_name, due_date=None, priority='Media'):
        if project_name in self.projects:
            task = {
                'name': task_name,
                'status': 'Pendiente',
                'due_date': due_date,
                'priority': priority,
                'created_at': datetime.now()
            }
            self.projects[project_name]['tasks'].append(task)
            return True
        return False
    
    def update_task_status(self, project_name, task_name, new_status):
        if project_name in self.projects:
            for task in self.projects[project_name]['tasks']:
                if task['name'] == task_name:
                    task['status'] = new_status
                    return True
        return False
    
    def add_team_member(self, project_name, member_name, role):
        if project_name in self.projects:
            member = {
                'name': member_name,
                'role': role,
                'joined_at': datetime.now()
            }
            self.projects[project_name]['team_members'].append(member)
            return True
        return False
    
    def get_project_details(self, project_name):
        return self.projects.get(project_name, None)
    
    def get_all_projects(self):
        return self.projects
