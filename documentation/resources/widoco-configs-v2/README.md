# widoco-configs-v2 — Configuraciones para Widoco 1.4.26-EDINT

Sustituye a `../widoco-configs/clean_configs/` + `widoco_post_gen.py` + `textos_extra/`.
La regeneración es **un solo paso, sin post-proceso**.

## Contenido

| Ruta | Descripción |
|---|---|
| `run/widoco-1.4.26-EDINT-jar-with-dependencies.jar` | Jar completo (build de `widoco-next/WIDOCO`, rama `work/edint-extensions`, commit `introduction-<lang>`) |
| `run/generar_doc.sh` | Script de regeneración (un paso) |
| `confs/widoco-edint-<repo>.conf` | Confs extendidos por repo |
| `resources/` | CodeMirror (`codemirror.css/js`, `matchbrackets.js`, `turtle.js`) que las descripciones con ejemplos Turtle necesitan |
| `resources/common/` | Intro y references canónicas EDINT (es/en) — se aplican a **todos** los repos |
| `build_confs.py` | Genera/actualiza los confs extendidos |

## Uso

```bash
./run/generar_doc.sh <ruta/al/repo> [en-es]
```

## Qué aporta nuestra build frente a Widoco 1.4.25 upstream

Claves nuevas en el `.conf` (todas con fallback a las claves globales):

- `abstract-<lang>`, `description-<lang>`, `references-<lang>`, `introduction-<lang>` —
  contenido de la sección en cada idioma. `abstract`/`introduction` son contenido
  interno (la plantilla añade el `<span class="markdown">`); `description`/`references`
  se escriben verbatim tras la línea del `<h2>`.
- `pathToAbstract-<lang>`, `pathToDescription-<lang>`, `pathToReferences-<lang>` — paths por idioma.
- `extraCSS` / `extraJS` — recursos (separados por `;`) que se añaden al `<head>` de los index.
- `extraResources` — ficheros o directorios que se copian a `documentation/resources/`.
- `-omitReadme` (flag) / `omitReadme` (conf) — no genera el `readme.md` genérico.

## Regenerar/actualizar los confs

```bash
python3 build_confs.py <repo-name> <repo-path> confs/widoco-edint-<repo-name>.conf
```

Extrae los textos de la documentación commitada actual del repo
(` <repo-path>/documentation/sections/`), con fallback a
`clean_configs/textos_extra/`, y combina el metadato del conf base
(`clean_configs/widoco-<repo>.conf`).

**Prioridad de fuentes por sección**: `introduction` y `references` usan siempre el
texto canónico de `resources/common/` (común a todos los repos EDINT);
`abstract` y `description` son específicos de cada repo.

## Estado por repo (20 con conf operativo)

- ✅ 18 repos regeneran sin post-proceso (verificado en `widoco-next/pruebas/`).
- 🚫 **Ignorados de momento** (su `ontology.owl` de main no parsea; ver
  `../workbench/fix_serializations/README.md`):
  - `edint-ontologia-medio-ambiente` (individuos autocerrados)
  - `edint-ontologia-oferta-inmobiliaria` (`inverseOf` contra genid anónimo)
- ℹ️ `edint-ontologia-calidad-aire`: sin documentación en main (no tiene conf aquí).
- ℹ️ `edint-ontologia-censo-vehiculos`: clone en `telefonicasc/` (org distinta).
- ℹ️ Cubos: la ontología es `ontology/data-cube.owl` (el script lo resuelve).

## Pendientes conocidos (drift aceptado)

- `index`/`provenance`: mejoras de upstream (dark mode, marked por CDN, mermaid,
  fechas correctas en JSON-LD en lugar de placeholders).
- `crossref`/`overview`/`ns`: anchors de la ontología actual (los refs antiguos
  usaban IRIs previas a la migración); master genera `ns-<lang>.html` separado.
