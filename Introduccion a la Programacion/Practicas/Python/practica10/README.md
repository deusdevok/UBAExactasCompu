# Como correr tests y coverage

## Instrucciones para test y coverage

- Crear entorno virtual: `python -m venv venv`

- Activar entorno virtual: `.\venv\Scripts\activate`

- Coverage: `coverage run --branch --include=p10.py test_p10.py`

- Reporte en consola: `coverage report -m` (`-m` muestra *Missing*)

- Para usar en vscode con extension (coverage gutters): `coverage xml`

- Reporte HTML: `coverage html`