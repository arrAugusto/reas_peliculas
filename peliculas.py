# Sistema de recomendación de películas basado en calificaciones previas

# Peliculas en base de datos de las cuales se haran recomendaciones
peliculas = {
    "Inception": ["Ciencia Ficción", "Acción"],
    "Titanic": ["Romance", "Drama"],
    "The Matrix": ["Ciencia Ficción", "Acción"],
    "Avengers": ["Acción", "Aventura"],
    "La La Land": ["Romance", "Musical"],
    "Interestelar": ["Ciencia Ficción", "Drama"]
}

#Peliculas vistas
calificaciones_usuario = {
    "Inception": 5,
    "The Matrix": 4,
    "Avengers": 3
}

# funcion recomendar peliculas se hacen ciclos para verficiacr peliculas que podria recomendar

def recomendar_pelicula(historial, peliculas):
    # Encontrar los géneros más preferidos del usuario
    generos_preferidos = {}
    
    for pelicula, calificacion in historial.items():
        if pelicula in peliculas:
            for genero in peliculas[pelicula]:
                generos_preferidos[genero] = generos_preferidos.get(genero, 0) + calificacion
    
    # Ordenar los géneros según preferencia
    generos_ordenados = sorted(generos_preferidos, key=generos_preferidos.get, reverse=True)
    
    # Buscar una película recomendada basada en los géneros favoritos
    for pelicula, generos in peliculas.items():
        if pelicula not in historial:  # Evitar recomendar películas ya vistas
            if any(genero in generos_ordenados for genero in generos):
                return pelicula
    
    return "No hay recomendaciones disponibles"

# Get recomendacion
recomendacion = recomendar_pelicula(calificaciones_usuario, peliculas)

# recomendada
print("Película recomendada:", recomendacion)
