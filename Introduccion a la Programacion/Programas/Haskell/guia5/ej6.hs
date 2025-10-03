type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

elNombre :: Contacto -> Nombre
elNombre = fst

elTelefono :: Contacto -> Telefono
elTelefono = snd

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((n, t):contactos) 
    | n == nombre = True
    | otherwise = enLosContactos nombre contactos

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto c [] = [c]
agregarContacto (n, t1) ((m, t2):lc) 
    | n == m = (n, t1) : lc
    | otherwise = (m, t2) : agregarContacto (n, t1) lc