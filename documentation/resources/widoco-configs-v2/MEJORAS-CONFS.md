# Valoración de mejoras en los ficheros de configuración

Fecha: 15/09/2026 · A partir de los informes de `widoco-tests/informes-propiedades/`
(38 propiedades × 23 confs) y del estado actual de `widoco-configs-v2/`.

## Resumen

Los informes detectan problemas en cuatro capas distintas. La nueva build (v2) ya
resuelve la parte mecánica; lo que queda son **decisiones editoriales** (que no deben
automatizarse) y **errores en los repos** (fuera de los confs).

| Capa | Ejemplos | ¿Quién lo arregla? |
|---|---|---|
| A. Resuelto por v2 | abstract/description/references/intro desincronizados con `textos_extra`; readme; CodeMirror; post-gen que machacaba | ✅ ya hecho (confs v2 extraen de la doc actual) |
| B. Erratas deterministas en el conf | `citeAs` con doble punto (`v0.2.1..`); tildes en `ontologyName` («Trafico», «Vehiculos compartidos») | 🤖 script de saneo automático |
| C. Decisiones editoriales | licencia BY vs BY-SA; nombres cortos coherentes; abstracts fuera de guía de estilo; versiones divergentes | 👤 decisión por repo, luego editar conf |
| D. Problemas del repo, no del conf | namespaces legacy sin migrar (12); `owl:versionInfo`/tags desactualizados; ontologías rotas; sin CITATION.cff | 🔧 repo (ontología/workflow) |

## Detalle y propuesta por tema

### B — Saneo aplicado directamente a los confs v2 (15/09/2026)

✅ Aplicado en los 20 confs (edición directa, sin lógica en el generador):

1. **`citeAs`**: colapsado `..` final a `.` (7 repos).
2. **`ontologyName`**: tildes corregidas («Tráfico», «Vehículos compartidos»).
3. **`licenseIconURL`** y **`*Serialization`**: eliminados (campo muerto / fuente de
   enlaces rotos según informe 33).
4. **`dateCreated`/`dateModified`**: rellenados desde `dcterms:created/issued/modified`
   de la OWL de cada repo (cubo-empleo, cubo-gasto-comercial, cubo-turismo,
   aparcamiento, catastro). Regeneradas las 20 documentaciones: 0 placeholders.

### C — Decisiones editoriales pendientes (recomendación)

1. **Licencia (informes 10-11)**: el repo dice **CC BY-SA 4.0** (LICENSE) y el conf/la
   ontología dicen **CC BY 4.0**. No es un errata: es una contradicción legal. Decidir
   cuál es la buena y alinear LICENSE ↔ conf ↔ `dcterms:license` en los 23.
2. **`ontologyName` coherente**: adoptar un formato único (recomendado: nombre legible
   capitalizado, «Alumbrado Público», «Censo de Vehículos») para los 4 estilos hoy
   conviviendo. Afecta al `<h2>` de la sección description.
3. **Versionado (`thisVersionURI`/`latestVersionURI`/`ontologyRevisionNumber`)**: hoy
   `thisVersionURI == latestVersionURI == namespaceURI` en los 23, y el `.conf` va por
   delante de los tags en 3 repos y por detrás en otros. Regla recomendada: el conf se
   edita solo en release, con `thisVersionURI = <ns>/<versión>` y
   `ontologyRevisionNumber` = tag git más alto.
4. **`previousVersionURI`**: rellenar donde hay tag y owl:priorVersion (censo-vehiculos,
   contaminacion-acustica, gestion-residuos, oferta-inmobiliaria, certificado-energetico,
   catastro) para que el changelog funcione.
5. **`backwardsCompatibleWith`**: vacío en 23, pero `organizaciones` documenta cambios
   de ruptura. Declarar incompatibilidades explícitas donde las haya.
6. **Abstracts**: aplicar la guía de estilo propuesta (2-3 frases, ~400 car.) y corregir
   SSN→SOSA en calidad-aire (cuando esa ontología exista).
7. **`importedOntologyNames`/`extendedOntologyNames`**: rellenar los 6+5 huecos
   documentados (cubo-*→Data Cube, contaminacion-acustica→medio-ambiente, etc.); corrige
   también el caso oferta-inmobiliaria (catastro en imported en vez de extended).

### D — Del lado del repo (no configurable)

- Migración de namespaces legacy `vocab.linkeddata.es` → `edint.es` (12 repos): hasta
  entonces, `latestVersionURI` del conf promete una URL que la ontología no usa.
- `owl:versionInfo` y tags desincronizados con el conf.
- Ontologías rotas (medio-ambiente, oferta-inmobiliaria) — ver
  `workbench/fix_serializations/`.
- DOI/Zenodo: crear `CITATION.cff` por repo si se quiere DOI por release.

## Acción inmediata propuesta

1. Añadir a `build_confs.py` el saneo B (citeAs, tildes, eliminar licenseIconURL y
   `*Serialization`, inyectar fechas desde la OWL si faltan) → regenerar los 20 confs.
2. Abrir decisión de licencia (BY vs BY-SA) y de formato de `ontologyName` antes de
   tocar nada de la capa C.

Nota: los informes analizan los confs legacy de `clean_configs`; los confs v2 ya
incorporan la capa A y son la base sobre la que aplicar B.
