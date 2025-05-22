opc = 0
pikachu_Roll = 0
otaku_Roll = 0
pulpo_Roll = 0
anguila_Roll = 0

contRolls = 0
total = 0
ventas = 0
dsct = "soyotaku"
codigo = ""
seguir = True
while seguir:
    print("*"*40)
    print("\tSushiMon Menu's")
    print("*"*40)
    print("[1] Pikachu Roll $4500 \n[2] Otaku Roll $5000 \n[3] Pulpo Venenoso Roll $5200 \n[4] Anguila Eléctrica Roll $4800 \n[5] Terminar pedido \n[6] Salir")
    print("*"*40)
    opc = 0
    while opc < 1 or opc > 6:
        try:
            opc = int(input("Opcion: "))
            if opc < 1 or opc > 6:
                print("Opcion invalida!!!")
        except ValueError:
            print("El valor debe ser numerico. Intentalo denuevo")
    if opc == 1:
            pikachu_Roll += 1
            contRolls += 1
            print("Pikachu Roll agregado con exito!")
    elif opc == 2:
            otaku_Roll += 1
            contRolls += 1
            print("Otaku Roll agregado con exito!")
    elif opc == 3:
            pulpo_Roll += 1
            contRolls += 1
            print("Pulpo Venenoso Roll agregado con exito!.")
    elif opc == 4:
            anguila_Roll += 1
            contRolls += 1
            print("Anguila Electrica Roll agregado con exito!.")
    elif opc == 5:
        x = input("Tiene codigo de descuento?[S/N]: ").lower()
        if x == "s":
            while codigo != "soyotaku":
                codigo = input("Ingrese codigo de descuento: ").lower()
                if codigo != "soyotaku":
                    intento = input("Codigo invalido, desea intentarlo nuevamente?[S/N]: ").lower()
                    if intento == "n":
                        break
        total = (pikachu_Roll * 4500)+(otaku_Roll * 5000)+(pulpo_Roll * 5200)+(anguila_Roll * 4800)
        print("*"*40)
        print(f"TOTAL PRODUCTOS: {contRolls}")
        print("*"*40)
        print(f"[1] Pikachu Roll: {pikachu_Roll} \n[2] Otaku Roll: {otaku_Roll} \n[3] Pulpo Venenoso Roll: {pulpo_Roll} \n[4] Anguila Eléctrica Roll: {anguila_Roll}")
        print("*"*40)
        print(f"Subtotal por pagar: {total}")
            
        if codigo == dsct:
            print(f"Descuento por codigo: {total*0.10}")
            print(f"TOTAL: {total*0.90}")
        else:
            print("No se aplicó descuento.")
            print(f"TOTAL: {total}")
            
        while True:
            reinicio = input("¿Desea realizar un nuevo pedido?[S/N]: ").lower()
            if reinicio == "s":
                print("Listo para ordenar un nuevo pedido!")
                pikachu_Roll = 0
                otaku_Roll = 0
                pulpo_Roll = 0
                anguila_Roll = 0
                contRolls = 0
                total = 0
                ventas = 0
                codigo = ""
                break
            elif reinicio == "n":
                seguir = False
                print("Gracias por su pedido. ¡Hasta pronto!")
                break
            else: 
                print("Opcion Invalida")
    elif opc == 6:
        seguir = False
        print("Gracias por visitar SushiMon. ¡Hasta pronto!")
