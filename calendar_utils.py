import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

class CalendarManager:
    def __init__(self):
        self.events = []
    
    def add_event(self, title, start_time, end_time, description=""):
        event = {
            'title': title,
            'start_time': start_time,
            'end_time': end_time,
            'description': description
        }
        self.events.append(event)
        return event
    
    def get_events(self):
        return self.events
    
    def display_calendar(self):
        st.subheader("Agenda de Eventos")
        
        # Formulario para agregar eventos
        with st.expander("Agregar Nuevo Evento"):
            col1, col2 = st.columns(2)
            with col1:
                title = st.text_input("Título del Evento")
                start_time = st.date_input("Fecha de Inicio")
                start_hour = st.time_input("Hora de Inicio")
            with col2:
                description = st.text_area("Descripción")
                end_time = st.date_input("Fecha de Fin")
                end_hour = st.time_input("Hora de Fin")
            
            if st.button("Agregar Evento"):
                if title and start_time and end_time:
                    start_datetime = datetime.combine(start_time, start_hour)
                    end_datetime = datetime.combine(end_time, end_hour)
                    self.add_event(title, start_datetime, end_datetime, description)
                    st.success("Evento agregado exitosamente!")
        
        # Mostrar eventos
        if self.events:
            st.subheader("Eventos Programados")
            events_df = pd.DataFrame(self.events)
            st.dataframe(events_df)
        else:
            st.info("No hay eventos programados.")
