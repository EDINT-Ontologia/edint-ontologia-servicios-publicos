#!/usr/bin/env python3
"""build_confs.py — Genera los confs extendidos para Widoco 1.4.26-EDINT.

Las claves nuevas soportadas por nuestra build (ver ../WIDOCO, rama
work/edint-extensions) son:

  abstract-<lang>       contenido interno de la sección (la plantilla añade
                        el <span class="markdown"> ... </span>)
  introduction-<lang>   ídem
  description-<lang>    contenido verbatim tras la línea del <h2>
  references-<lang>     ídem
  extraResources        ficheros/dir a copiar en documentation/resources/
  extraCSS / extraJS    recursos a incluir en el <head> de los index
  omitReadme            no generar el readme.md genérico

Fuentes del contenido, por prioridad:
  1. <repo>/documentation/sections/<section>-<lang>.html  (documentación
     commitada actual; en producción, el propio repo)
  2. clean_configs/textos_extra/<repo>/...  (fallback legacy)

Uso:
    python3 build_confs.py <repo-name> <repo-path> <salida.conf>
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLEAN = Path("/backup/pc1/data/FEMP/widoco-configs/clean_configs")
SECTIONS = (
    ("abstract", "inner"),
    ("introduction", "inner"),
    ("description", "verbatim"),
    ("references", "verbatim"),
)


def esc_props(value: str) -> str:
    """Escapa un valor multi-línea al formato java.util.Properties (una única
    línea lógica con secuencias \\n; el espacio inicial se escapa)."""
    v = value.replace("\\", "\\\\").replace("\n", "\\n")
    if v.startswith(" "):
        v = "\\ " + v[1:]
    return v


def read_section(path: Path):
    """Devuelve (h2_line, body) de una sección generada/post-procesada."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.lstrip().startswith("<h2"):
            return line, "".join(lines[i + 1:])
    return None, text


def inner_content(h2_line: str, body: str) -> str:
    """Contenido interno del <span class="markdown"> de una sección. El span
    de apertura puede estar en la línea del <h2> (abstract) o en el body
    (introduction), según el jar que generó el fichero."""
    if h2_line is not None and '<span class="markdown">' in h2_line:
        s = body
    else:
        s = body.lstrip("\n")
        prefix = '<span class="markdown">'
        if s.startswith(prefix):
            s = s[len(prefix):]
        else:
            return s
    if s.endswith("</span>\n"):
        s = s[: -len("</span>\n")]
    elif s.endswith("</span>"):
        s = s[: -len("</span>")]
    return s


def main() -> int:
    repo, repo_path, out_path = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    base = {}
    for line in (CLEAN / f"widoco-{repo}.conf").read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            base[k] = v

    sec_dir = repo_path / "documentation" / "sections"
    tex_dir = CLEAN / "textos_extra" / repo
    common_dir = HERE / "resources" / "common"
    new = {}
    for lang in ("en", "es"):
        for section, kind in SECTIONS:
            # introduction y references son comunes a todos los repos EDINT:
            # el texto canónico de resources/common tiene prioridad
            src = None
            for cand in (common_dir / f"{section}-{lang}.html",
                         sec_dir / f"{section}-{lang}.html",
                         tex_dir / f"{section}-{lang}.html"):
                if cand.exists():
                    src = cand
                    break
            if src is None:
                continue
            if src.parent in (sec_dir, common_dir):
                h2_line, body = read_section(src)
            else:
                h2_line, body = None, src.read_text(encoding="utf-8")
            content = inner_content(h2_line, body) if kind == "inner" else body
            new[f"{section}-{lang}"] = content

    # Recursos CodeMirror si algún texto los usa (descripciones con ejemplos)
    cm = ["codemirror.css", "codemirror.js", "matchbrackets.js", "turtle.js"]
    needs_cm = any("CodeMirror" in v for v in new.values())
    extra_css, extra_js, extra_res = [], [], []
    res_dir = HERE / "resources"
    if needs_cm and res_dir.is_dir():
        for cmf in cm:
            if (res_dir / cmf).exists():
                extra_res.append(f"{res_dir / cmf}")
                (extra_css if cmf.endswith(".css") else extra_js).append(f"resources/{cmf}")

    with open(out_path, "w", encoding="utf-8") as out:
        for k, v in base.items():
            out.write(f"{k}={v}\n")
        out.write("omitReadme=true\n")
        if extra_res:
            out.write(f"extraResources={';'.join(extra_res)}\n")
            out.write(f"extraCSS={';'.join(extra_css)}\n")
            out.write(f"extraJS={';'.join(extra_js)}\n")
        for k, v in new.items():
            out.write(f"{k}={esc_props(v)}\n")
    print(f"{out_path}: {len(new)} claves de sección" + (f" +{len(extra_res)} extraResources" if extra_res else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
