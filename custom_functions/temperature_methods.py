# Estas son las funciones que van a reemplazar a las de student_grade_methods.py en laboratory.py

# Funcion para hallar el promedio de temperatura en los departamentos

def promedio_temperature(temperature):

    temperature_sum = 0
    temperature_count = len(temperature)


    for tempe in temperature:
        temperature_sum += tempe


    final_temperature = temperature_sum / temperature_count

    return final_temperature


# Funcion para hallar la temperatura mas caliente o la mejor en los departamentos


def temperature_best(temperature):


    best_temperature = temperature[0]


    for tempe in temperature:

        if tempe > best_temperature:
            best_temperature = tempe


    return best_temperature


