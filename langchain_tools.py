from langchain.tools import Tool
from datetime import datetime

def get_project_tools(project_manager, calendar_manager):
    tools = [
        Tool(
            name="create_project",
            func=project_manager.create_project,
            description="Crea un nuevo proyecto. Parámetros: name (str)"
        ),
        Tool(
            name="add_task",
            func=project_manager.add_task,
            description="Agrega una tarea a un proyecto. Parámetros: project_name (str), task_name (str), due_date (datetime), priority (str)"
        ),
        Tool(
            name="update_task_status",
            func=project_manager.update_task_status,
            description="Actualiza el estado de una tarea. Parámetros: project_name (str), task_name (str), new_status (str)"
        ),
        Tool(
            name="add_team_member",
            func=project_manager.add_team_member,
            description="Agrega un miembro al equipo del proyecto. Parámetros: project_name (str), member_name (str), role (str)"
        ),
        Tool(
            name="get_project_details",
            func=project_manager.get_project_details,
            description="Obtiene los detalles de un proyecto. Parámetros: project_name (str)"
        ),
        Tool(
            name="add_calendar_event",
            func=calendar_manager.add_event,
            description="Agrega un evento al calendario. Parámetros: title (str), start_time (datetime), end_time (datetime), description (str)"
        ),
        Tool(
            name="get_calendar_events",
            func=calendar_manager.get_events,
            description="Obtiene todos los eventos del calendario"
        )
    ]
    return tools
