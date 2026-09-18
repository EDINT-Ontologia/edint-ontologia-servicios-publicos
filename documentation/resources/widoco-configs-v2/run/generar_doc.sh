#!/usr/bin/env bash
# generar_doc.sh — Regenera la documentación de un repo EDINT con nuestra
# build de Widoco 1.4.26 (rama work/edint-extensions).
#
# No requiere post-proceso: los contenidos por idioma, los recursos CodeMirror
# y la omisión del readme están en el conf extendido.
#
# Uso:
#   ./generar_doc.sh <ruta/al/repo> [lang]
#
# Ejemplo:
#   ./generar_doc.sh ~/repos/edint-ontologia-alumbrado-publico en-es

set -euo pipefail

REPO="${1:?Uso: $0 <ruta/al/repo> [lang]}"
LANG_OPT="${2:-en-es}"
HERE="$(cd "$(dirname "$0")" && pwd)"
JAR="$HERE/widoco-1.4.26-EDINT-jar-with-dependencies.jar"
CONF="$HERE/../confs/widoco-$(basename "$(cd "$REPO" && pwd)").conf"

[ -f "$CONF" ] || { echo "ERROR: no existe $CONF (genéralo con build_confs.py)" >&2; exit 1; }
[ -d "$REPO/ontology" ] || { echo "ERROR: $REPO/ontology no existe" >&2; exit 1; }

# ontología: ontology.owl o, en los cubos, data-cube.owl
ONTO="$REPO/ontology/ontology.owl"
[ -f "$ONTO" ] || ONTO=$(find "$REPO/ontology" -maxdepth 2 -name "*.owl" | head -1)
[ -n "$ONTO" ] && [ -f "$ONTO" ] || { echo "ERROR: sin .owl en $REPO/ontology" >&2; exit 1; }

echo ">> Regenerando documentación de $(basename "$REPO") con Widoco 1.4.26-EDINT"

# 1) Publicar las fuentes KOS/tesauros: copiar kos/ (raíz del repo) a
#    documentation/kos/, que es donde el índice enlaza (kosHTML=kos/skos-es.html)
#    y donde viven las páginas HTML del tesauro. No se borra nada existente.
#    OJO: en sistemas de ficheros insensibles a mayúsculas (p. ej. sshfs),
#    "Readme.md" y "README.md" son el mismo fichero: se copia preservando el
#    nombre de la raíz y se avisa si ya existe una variante en el destino.
if [ -d "$REPO/kos" ]; then
    mkdir -p "$REPO/documentation/kos"
    for src in "$REPO"/kos/*; do
        [ -f "$src" ] || continue
        name="$(basename "$src")"
        [ -f "$REPO/documentation/kos/$name" ] && continue
        for dst in "$REPO/documentation/kos/"*; do
            [ -f "$dst" ] || continue
            dname="$(basename "$dst")"
            if [ "${dname,,}" = "${name,,}" ] && [ "$dname" != "$name" ]; then
                echo "   AVISO: '$name' y '$dname' difieren solo en mayúsculas (mismo fichero en FS insensible)"
            fi
        done
    done
    cp -R "$REPO/kos/." "$REPO/documentation/kos/"
    echo ">> kos/ copiado a documentation/kos/"
fi

java -jar "$JAR" \
    -ontFile "$ONTO" \
    -outFolder "$REPO/documentation" \
    -confFile "$CONF" \
    -getOntologyMetadata \
    -lang "$LANG_OPT" \
    -rewriteAll \
    -omitReadme

echo ">> Hecho (kos/ copiado a documentation/kos/ y documentación regenerada)"
