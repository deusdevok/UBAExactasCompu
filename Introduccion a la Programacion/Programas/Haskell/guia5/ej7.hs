import Test.HUnit

type Texto = [Char]
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker id [] = False
existeElLocker id ((i, _):ls) 
    | id == i = True
    | otherwise = existeElLocker id ls

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker id ((i, (d, u)):ls) 
    | id == i = u
    | otherwise = ubicacionDelLocker id ls

estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker id ((i, (d, u)):ls)
    | id == i = d
    | otherwise = estaDisponibleElLocker id ls

ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker id ((i, (d, u)):ls) 
    | id == i && d = (i, (False, u)) : ls
    | id == i && not d = (i, (d, u)) : ls
    | otherwise = (i, (d, u)) : ocuparLocker id ls

lockers :: [Locker]
lockers = [
    (1, (True, "Pabellon 1")),
    (2, (True, "Pabellon 1")),
    (3, (False, "Pabellon 2")),
    (4, (True, "Pabellon 2"))
    ]

testSuiteExisteElLocker = [
    "existe" ~: (existeElLocker 1 lockers) ~?= True,
    "no existe" ~: (existeElLocker 5 lockers) ~?= False
    ]

testSuiteUbicacionLocker = [
    "primer locker en lista" ~: (ubicacionDelLocker 1 lockers) ~?= "Pabellon 1",
    "tercer locker en lista" ~: (ubicacionDelLocker 3 lockers) ~?= "Pabellon 2"
    ]

testSuiteEstaDisponibleLocker = [
    "disponible" ~: (estaDisponibleElLocker 1 lockers) ~?= True,
    "no disponible" ~: (estaDisponibleElLocker 3 lockers) ~?= False
    ]

testSuiteOcuparLocker = [
    "ocupar locker disponible" ~: (ocuparLocker 1 lockers) ~?= [
                                                            (1, (False, "Pabellon 1")),
                                                            (2, (True, "Pabellon 1")),
                                                            (3, (False, "Pabellon 2")),
                                                            (4, (True, "Pabellon 2"))
                                                            ],
    "ocupar locker no disponible" ~: (ocuparLocker 3 lockers) ~?= [
                                                            (1, (True, "Pabellon 1")),
                                                            (2, (True, "Pabellon 1")),
                                                            (3, (False, "Pabellon 2")),
                                                            (4, (True, "Pabellon 2"))
                                                            ]
    ]

todosLosTest = testSuiteExisteElLocker ++ testSuiteUbicacionLocker ++ testSuiteEstaDisponibleLocker ++ testSuiteOcuparLocker

correrTests = runTestTT (test todosLosTest)