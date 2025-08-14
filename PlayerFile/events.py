
class EventsGeral:

    def __init__(self, Name_event, value_buy, Effect_Physics, Effect_Mental, Possibility, Time):
        self.Name_event = Name_event
        self.value_buy = float(value_buy)
        self.Effect_Physics = Effect_Physics
        self.Effect_Mental = Effect_Mental 
        self.Possibility = Possibility
        self.Time = Time
    

    def bad_events(): # Name_event, value_buy, Effect_Physics, Effect_Mental, Possibility, Time
        
        return [
            EventsGeral("Gripe", 20.0, -8, 0, 50, 2),
            EventsGeral("Dor de barriga", 9.99, -2, -2, 20, 1),
            EventsGeral("Resfriado", 15.0, -5, 0, 60, 1),
            EventsGeral("Insônia", 0.0, 0, -10, 30, 3),
            EventsGeral("Enxaqueca", 35.0, -15, -5, 15, 1),
            EventsGeral("Alergia", 12.50, -3, -1, 40, 1),
            EventsGeral("Braço Quebrado", 150.0, -25, -10, 5, 14),
            EventsGeral("Intoxicação Alimentar", 50.0, -10, -5, 10, 3),
            EventsGeral("Crise de Ansiedade", 0.0, -2, -20, 8, 1),
            EventsGeral("COVID-19", 100.0, -30, -15, 12, 7)
        ]

        