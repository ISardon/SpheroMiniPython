#roll(A,V,S): A = angulo, V = velocidad, S = duracion
async def start_program():
    await set_stabilization(True)   # Engage motor drive
    await set_heading(0)            # Zero the heading so 0° is forward
#ida
    await roll(0,60,0.66)           #1 forward
    await roll(90,5,0.66)           #2 right
    await roll(0,60,0.66)           #3 forward`
    await roll(270,20,0.66)         #4 left
    await roll(0,45,0.66)           #5 forward
    await roll(90,90,1)             #6 right
    await roll(0,60,0.66)           #7 forward
#vuelta
    await roll(270,170,0.8)         #8 left
    await roll(180,60,0.66)         #9 backward
    await roll(90,20,0.66)          #10 right
    await roll(180,50,0.8)          #11 backward
    await roll(270,60,0.66)         #12 left
    await roll(180,60,0.66)         #13 backward
    await roll(90,60,0.66)          #14 right
    await roll(180,90,0.66)         #15 backward
    await roll(270,60,0.66)         #16 left
    await roll(0,60,0.66)           #17 forward
