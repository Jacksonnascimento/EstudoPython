import aleato as a # as coloca apelido 
import media as m

lista = a.geraListaInteiro(4)

media = m.media(lista)
mediana = m.mediana(lista)


print("Minha lista: " + str(lista))
print("A média da minha lista é " + str(media))
print("A mediana da minha lista é " + str(mediana))
