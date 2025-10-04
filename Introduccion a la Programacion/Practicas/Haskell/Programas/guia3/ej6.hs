{--
problema bisiesto (anio : Z) : Bool {
    requiere: {True}
    asegura: {(res = false) ↔ (anio no es multiplo de 4, o bien, anio es multiplo de 100 pero no de 400)}
}
--}

type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto a = not (mod a 4 /= 0 || (mod a 100 == 0 && mod a 400 /= 0))