# Sofía Deutsch-Abenteuer (deutsch.hurlingham.xyz)

Sitio web interactivo y material imprimible de práctica de **Alemán para 3° de primaria**, diseñado con temática de **Dandy's World** (Roblox) para Sofía de cara a su trabajo integrador individual del **jueves 19 de Noviembre** con la profesora **Frau Mónica Briesemeister**.

---

## 🎯 Contenidos y Temas Evaluados

1. **Personalvorstellung (Presentación personal o de otra persona):**
   - Nombre, edad, lugar de residencia, procedencia (*Ich heiße...*, *Ich bin acht Jahre alt*, *Ich wohne in...*, *Ich komme aus...*).
   - Verbos: *sein*, *heißen*, *wohnen*, *haben*, *spielen*.
   - Presentar a otra persona: *"Das ist mein Freund Boxten. Er ist acht Jahre alt."*
2. **Familie (Miembros de la familia):**
   - *der Vater / Papa*, *die Mutter / Mama*, *der Bruder*, *die Schwester*, *der Opa*, *die Oma*, *das Baby*.
3. **Schulsachen & Artikel (Útiles escolares y artículos):**
   - Géneros definidos: **der** (maskulin), **die** (feminin), **das** (neutral).
   - Artículos indefinidos y negación: *ein*, *eine*, *kein*, *keine*.
   - Mini-juego interactivo: *Der, Die oder Das? – Sortierspiel!*
4. **Bauernhoftiere & Adjektive (Animales de la granja y adjetivos):**
   - *der Hund* (Pebble), *die Kuh*, *das Pferd*, *die Katze*, *das Schwein*, *das Schaf*, *die Ente*, *das Huhn / der Hahn*, *die Ziege*.
   - Adjetivos: *groß*, *klein*, *schnell*, *langsam*, *schön*, *lustig*, *freundlich*, *bunt*, *müde*, *lecker*.
5. **Das Datum, Wochentage & Hobbys (La fecha, días y pasatiempos):**
   - Días de la semana: *Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag*.
   - Escribir la fecha: *"Heute ist Donnerstag, der 19. November."*
   - Hobbies: *Fußball spielen, Bilder malen, Bücher lesen, schwimmen, Rad fahren, Musik hören, singen*.
6. **Hör- und Leseverstehen (Comprensión auditiva y lectora):**
   - Cuento: *"Dandy und seine Freunde auf dem Bauernhof"* con botón de audio para escuchar toda la historia narrada en alemán nativo.
   - Preguntas de comprensión y Richtig / Falsch.
   - Quiz integrador final y certificado oficial de felicitaciones.

---

## 🚀 Características Interactivas

- **Pronunciación y Lectura en Alemán (TTS)**: Web Speech API calibrada para `de-DE` con selector de velocidad (🐰 Normal / 🐢 Despacio).
- **Lectura Automática al Acertar**: Al seleccionar la respuesta correcta, el sistema reproduce el audio de la oración completa en alemán y muestra la transcripción destacada.
- **Banco Rotativo Dinámico**: Más de 100 preguntas aleatorias en cada recarga o con el botón `🔄 Mischen`.
- **Personalización de Nombre**: Modal para ingresar el nombre de la alumna/o (por defecto "Sofía") actualizando diálogos, audios y certificado.
- **Diseño Mobile-First**: Barra en dos niveles, navegación por pestañas táctiles con desplazamiento suave, botones con área mínima de 44px y márgenes de seguridad para pantallas modernas.

---

## 🛠️ Stack Tecnológico

- **Backend**: FastAPI + Jinja2 + Python 3.12 (gestionado con `uv`).
- **Contenedores**: Docker multi-stage (`uv:python3.12-bookworm-slim`).
- **Despliegue**: Docker Compose sirviendo en puerto host **8082** (`"${PORT:-8082}:8000"`).
- **CI/CD**: GitHub Actions hacia GitHub Container Registry (`ghcr.io/cacrespo/sofi_deutsch:latest`), preparado para auto-actualización con Watchtower en `deutsch.hurlingham.xyz`.
- **PDF Imprimible**: Generador ReportLab A4 de exactamente 5 páginas con maquetación profesional y gráficos de Dandy's World.

---

## 💻 Desarrollo Local

```bash
# Instalar dependencias con uv
uv sync

# Ejecutar tests
uv run pytest

# Lint y formato
uv run ruff check .
uv run ruff format --check .

# Servidor de desarrollo
uv run python run.py
```
