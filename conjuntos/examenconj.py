# ═══════════════════════════════════════════════════════
#   EXAMEN - COMERCIO ELECTRÓNICO Y UNIVERSIDAD
# ═══════════════════════════════════════════════════════

A = {"Ana", "Luis", "Pedro", "Sofía", "María", "Carlos"}
B = {"Sofía", "Carlos", "Julián", "María", "Andrés", "Camila"}

print("=" * 55)
print("   PARTE 1 - COMERCIO ELECTRÓNICO")
print("=" * 55)

# 1. Usuarios registrados en AL MENOS una plataforma (unión)
al_menos_una = A | B
print(f"\n1. Al menos en una plataforma: {sorted(al_menos_una)}")

# 2. Usuarios registrados en AMBAS plataformas (intersección)
ambas = A & B
print(f"\n2. En ambas plataformas: {sorted(ambas)}")

# 3. Diferencias
solo_web = A - B
solo_app = B - A
print(f"\n3a. Solo en tienda web: {sorted(solo_web)}")
print(f"3b. Solo en app móvil:  {sorted(solo_app)}")

# 4. Usuarios en solo UNA plataforma (diferencia simétrica)
solo_una = A ^ B
print(f"\n4. Solo en una plataforma: {sorted(solo_una)}")

# 5. ¿Todos los usuarios de la app están también en la web?
#    Esto es: ¿B es subconjunto de A?
print(f"\n5. ¿Todos los de la app están en la web? {B <= A}")
print(f"   (Si fuera True, la sospecha sería correcta)")

# 6. Campaña de descuentos
#    Condición 1: registrados en ambas plataformas → A & B
#    Condición 2: no son exclusivos de una sola    → no están en A ^ B
#    Ambas condiciones juntas = simplemente A & B
campaña = ambas - solo_una   # quita exclusivos por si acaso
print(f"\n6. Usuarios para campaña de descuentos: {sorted(campaña)}")


print("\n" + "=" * 55)
print("   PARTE 2 - UNIVERSIDAD")
print("=" * 55)

F = {"Ana", "Pedro", "Juan", "Sofía", "Carlos"}
B = {"Sofía", "María", "Luis", "Carlos", "Andrea"}
V = {"Pedro", "Andrea", "Camila", "Juan"}

# 1. Estudiantes en LOS TRES deportes
tres_deportes = F & B & V
print(f"\n1. En los tres deportes: {sorted(tres_deportes)}")

# 2. Estudiantes en SOLO UN deporte
#    Estrategia: está en uno, pero NO en ninguna combinación de dos

# Primero identificamos quienes están en exactamente dos o tres
en_fb = F & B          # fútbol y baloncesto
en_fv = F & V          # fútbol y voleibol
en_bv = B & V          # baloncesto y voleibol
en_dos_o_mas = en_fb | en_fv | en_bv   # cualquiera que esté en al menos dos

# Los de solo uno = están en algún deporte pero no en dos o más
todos = F | B | V
solo_uno = todos - en_dos_o_mas
print(f"\n2. Solo en un deporte: {sorted(solo_uno)}")

# 3. Estudiantes en EXACTAMENTE DOS deportes
#    = están en dos o más, pero NO en los tres
exactamente_dos = en_dos_o_mas - tres_deportes
print(f"\n3. En exactamente dos deportes: {sorted(exactamente_dos)}")

# 4. ¿Algún estudiante no practica ningún deporte?
#    La universidad tiene un listado total de estudiantes
todos_estudiantes = {"Ana", "Pedro", "Juan", "Sofía", "Carlos",
                     "María", "Luis", "Andrea", "Camila"}

sin_deporte = todos_estudiantes - (F | B | V)

if sin_deporte:
    print(f"\n4. Estudiantes sin ningún deporte: {sorted(sin_deporte)}")
else:
    print(f"\n4. Todos practican al menos un deporte ✓")

# 5. ¿Todos los de voleibol están también en fútbol?
#    Esto es: ¿V es subconjunto de F?
print(f"\n5. ¿Todos los de voleibol están en fútbol? {V <= F}")
print(f"   Voleibol: {sorted(V)}")
print(f"   Fútbol:   {sorted(F)}")
if not V <= F:
    falta = V - F
    print(f"   Faltan inscribirse en fútbol: {sorted(falta)}")
