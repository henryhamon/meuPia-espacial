algoritmo "MissaoMun"
var alt: real
inicio
    ksp_conectar("Nave 1")
    ksp_acelerar(1.0)
    
    enquanto verdadeiro faca
        alt <- ksp_obter_altitude()
        escreva("Altitude: ", alt)
        
        se alt > 10000 entao
             ksp_travar_sas()
        fim_se
    fimenquanto
fimalgoritmo
