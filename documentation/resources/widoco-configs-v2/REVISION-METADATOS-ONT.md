# Metadatos: ¿ontología (anotaciones) vs `.conf`?

Revisión de las anotaciones OWL que Widoco puede consumir directamente
(`-getOntologyMetadata`, activo por defecto) frente a si el valor vive solo en el `.conf`.
Generado el 15/09/2026 sobre los clones de main en `widoco-next/pruebas/`.

## Resumen: presencia de cada anotación en las OWL (20 repos)

| Propiedad (conf) | Anotación OWL equivalente | En la OWL | Solo en conf | En ninguno |
|---|---|---|---|---|
| ontologyTitle | `dcterms:title` | 19/20 | 1/20 | 0/20 |
| abstract/description | `dcterms:description` | 16/20 | 0/20 | 4/20 |
| authors | `dcterms:creator` | 19/20 | 0/20 | 1/20 |
| contributors | `dcterms:contributor` | 3/20 | 0/20 | 17/20 |
| publisher | `dcterms:publisher` | 1/20 | 19/20 | 0/20 |
| licenseURI | `dcterms:license` | 19/20 | 1/20 | 0/20 |
| citeAs | `schema:citation` | 0/20 | 20/20 | 0/20 |
| ontologyRevisionNumber | `owl:versionInfo` | 20/20 | 0/20 | 0/20 |
| thisVersionURI | `owl:versionIRI` | 19/20 | 1/20 | 0/20 |
| previousVersionURI | `owl:priorVersion` | 9/20 | 7/20 | 4/20 |
| backwardsCompatibleWith | `owl:backwardCompatibleWith` | 0/20 | 0/20 | 20/20 |
| dateCreated | `dcterms:created` | 16/20 | 4/20 | 0/20 |
| dateIssued | `dcterms:issued` | 17/20 | 3/20 | 0/20 |
| dateModified | `dcterms:modified` | 2/20 | 17/20 | 1/20 |
| ontologyPrefix | `vann:preferredNamespacePrefix` | 20/20 | 0/20 | 0/20 |
| ontologyNamespaceURI | `vann:preferredNamespaceUri` | 19/20 | 1/20 | 0/20 |
| introduction | `widoco:introduction` | 0/20 | 0/20 | 20/20 |
| sources | `dcterms:source` | 3/20 | 0/20 | 17/20 |
| seeAlso | `rdfs:seeAlso` | 4/20 | 0/20 | 16/20 |
| DOI | `prism:doi` | 0/20 | 0/20 | 20/20 |

## Detalle por repositorio

### edint-cubo-empleo

- **En la OWL** (8): ontologyTitle, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (12): abstract/description, contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, dateCreated, dateModified, introduction, sources, seeAlso, DOI

### edint-cubo-gasto-comercial

- **En la OWL** (8): ontologyTitle, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (12): abstract/description, contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, dateCreated, dateModified, introduction, sources, seeAlso, DOI

### edint-cubo-turismo

- **En la OWL** (8): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (12): contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, dateCreated, dateIssued, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-agenda

- **En la OWL** (13): ontologyTitle, abstract/description, authors, contributors, licenseURI, ontologyRevisionNumber, thisVersionURI, previousVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI, seeAlso
- **Faltan en la OWL** (7): publisher, citeAs, backwardsCompatibleWith, dateModified, introduction, sources, DOI

### edint-ontologia-alumbrado-publico

- **En la OWL** (14): ontologyTitle, abstract/description, authors, contributors, publisher, licenseURI, ontologyRevisionNumber, thisVersionURI, previousVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI, seeAlso
- **Faltan en la OWL** (6): citeAs, backwardsCompatibleWith, dateModified, introduction, sources, DOI

### edint-ontologia-aparcamiento

- **En la OWL** (9): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateCreated, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (11): contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, dateIssued, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-catastro

- **En la OWL** (12): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateCreated, dateIssued, dateModified, ontologyPrefix, ontologyNamespaceURI, seeAlso
- **Faltan en la OWL** (8): contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, introduction, sources, DOI

### edint-ontologia-censo-locales

- **En la OWL** (10): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (10): contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-censo-vehiculos

- **En la OWL** (11): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, previousVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (9): contributors, publisher, citeAs, backwardsCompatibleWith, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-certificado-energetico

- **En la OWL** (12): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateCreated, dateIssued, dateModified, ontologyPrefix, ontologyNamespaceURI, seeAlso
- **Faltan en la OWL** (8): contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, introduction, sources, DOI

### edint-ontologia-contaminacion-acustica

- **En la OWL** (4): ontologyRevisionNumber, thisVersionURI, previousVersionURI, ontologyPrefix
- **Faltan en la OWL** (16): ontologyTitle, abstract/description, authors, contributors, publisher, licenseURI, citeAs, backwardsCompatibleWith, dateCreated, dateIssued, dateModified, ontologyNamespaceURI, introduction, sources, seeAlso, DOI

### edint-ontologia-fotovoltaica

- **En la OWL** (12): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, previousVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI, sources
- **Faltan en la OWL** (8): contributors, publisher, citeAs, backwardsCompatibleWith, dateModified, introduction, seeAlso, DOI

### edint-ontologia-gestion-residuos

- **En la OWL** (10): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (10): contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-infraestructura

- **En la OWL** (11): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, previousVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (9): contributors, publisher, citeAs, backwardsCompatibleWith, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-organizaciones

- **En la OWL** (11): ontologyTitle, abstract/description, authors, contributors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (9): publisher, citeAs, previousVersionURI, backwardsCompatibleWith, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-servicios-publicos

- **En la OWL** (10): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (10): contributors, publisher, citeAs, previousVersionURI, backwardsCompatibleWith, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-suministro

- **En la OWL** (12): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, previousVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI, sources
- **Faltan en la OWL** (8): contributors, publisher, citeAs, backwardsCompatibleWith, dateModified, introduction, seeAlso, DOI

### edint-ontologia-trafico

- **En la OWL** (11): ontologyTitle, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, previousVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI, sources
- **Faltan en la OWL** (9): abstract/description, contributors, publisher, citeAs, backwardsCompatibleWith, dateModified, introduction, seeAlso, DOI

### edint-ontologia-vehiculos-compartidos

- **En la OWL** (11): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, thisVersionURI, previousVersionURI, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (9): contributors, publisher, citeAs, backwardsCompatibleWith, dateModified, introduction, sources, seeAlso, DOI

### edint-ontologia-zona-regulatoria

- **En la OWL** (9): ontologyTitle, abstract/description, authors, licenseURI, ontologyRevisionNumber, dateCreated, dateIssued, ontologyPrefix, ontologyNamespaceURI
- **Faltan en la OWL** (11): contributors, publisher, citeAs, thisVersionURI, previousVersionURI, backwardsCompatibleWith, dateModified, introduction, sources, seeAlso, DOI

