turno_mañana = {"Dr. López", "Dra. Gómez", "Dr. Torres", "Dra. Ruiz", "Dr. Mendez"}
turno_noche  = {"Dra. Ruiz", "Dr. Mendez", "Dr. Castro", "Dra. Vega"}

especialistas = {
    "Dr. López":   {"cardiología", "medicina interna"},
    "Dra. Gómez":  {"pediatría", "medicina interna"},
    "Dr. Torres":  {"cirugía", "traumatología"},
    "Dra. Ruiz":   {"cardiología", "cirugía"},
    "Dr. Mendez":  {"neurología", "medicina interna"},
    "Dr. Castro":  {"pediatría", "cirugía"},
    "Dra. Vega":   {"neurología", "cardiología"},
}
#¿Qué médicos trabajan en ambos turnos?
ambos_turnos= turno_mañana.intersection(turno_noche)

#¿Qué médicos trabajan solo de noche?
solo_noche= turno_noche - turno_mañana

#¿Cuántos médicos en total tiene el hospital?
total_medicos= turno_mañana | turno_noche
print("Cantidad medicos hospital: ", len(total_medicos))

#Para una cirugía de emergencia se necesita alguien con {"cirugía"}. ¿Qué médicos del turno de noche pueden atenderla? (itera sobre el turno de noche y verifica con subconjunto)


requerimiento = {"cirugía"}
cirugia_emergencia = []
for doctor in turno_noche:
    if requerimiento <= especialistas[doctor]:  # subconjunto
        cirugia_emergencia.append(doctor)   


#¿Qué especialidades únicas ofrece el hospital en total?

especialidad_unica=[]
for doctor, especialidad in especialistas.items():
    for especia in especialidad:
        if especia not in especialidad_unica:
            especialidad_unica.append(especia)

#  Con set (una línea)
especialidades_unicas = set()
for especialidad in especialistas.values():
    especialidades_unicas |= especialidad   # va acumulando todas en un solo set
