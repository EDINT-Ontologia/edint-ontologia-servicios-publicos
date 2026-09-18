# Checklist: tripletas de metadatos que Widoco toma de la ontología

Fuente: `WIDOCO/src/main/java/widoco/Configuration.java` (`completeOntologyMetadata` +
`completeAgentMetadata`) — anotaciones sobre el IRI de la ontología (o sobre el nodo
agente). Generado el 15/09/2026.

⚠️ Con `-confFile`, `GuiController` desactiva la lectura de la ontología
(`getOntoMetadata=false`). Para combinar conf + ontología hay que añadir
`-getOntologyMetadata` **después** de `-confFile` en la línea de comandos.
Con la lectura activa, **la ontología tiene prioridad** sobre el conf en los campos
comunes (el conf se procesa antes).

## 1. Identificación

| Dato | Anotación recomendada | Aliases que también acepta Widoco | Multilingüe |
|---|---|---|---|
| Título | `dcterms:title` | `dc:title`, `schema:name`, `rdfs:label`, `skos:prefLabel`, `mod:acronym`, `schema:alternateName` | ✓ (por `xml:lang`) |
| Nombre corto (h2) | `rdfs:label` | `skos:prefLabel`, `schema:alternateName`, `mod:acronym` | ✓ |
| Abstract | `dcterms:abstract` | `dc:abstract` | ✓ |
| Descripción | `dcterms:description` | `dc:description`, `schema:description`, `rdfs:comment`, `skos:note` | ✓ |
| Prefijo | `vann:preferredNamespacePrefix` | — | — |
| Namespace URI | `vann:preferredNamespaceUri` | — | — |
| Logo / imagen | `schema:logo` | `foaf:logo`, `schema:image`, `foaf:img`, `foaf:depiction` | — |

## 2. Personas y agentes (creadores, contribuidores, publisher, funders)

El valor puede ser un **literal** (solo nombre) o un **nodo con anotaciones** (recomendado
para llevar URL/institución). Anotaciones del nodo agente aceptadas:

| Dato del agente | Anotaciones |
|---|---|
| Nombre | `foaf:name`, `schema:name`, `vcard:fn`, `rdfs:label` |
| Nombre propio / apellido | `foaf:givenname`/`schema:givenName`, `foaf:family_name`/`schema:familyName`, `vcard:given-name`/`vcard:family-name` |
| Web | `foaf:homepage`, `schema:url`, `vcard:hasURL` |
| Email | `foaf:mbox`, `schema:email`, `vcard:hasEmail` |
| Institución | `schema:affiliation`, `org:memberOf` |

| Rol | Anotación recomendada | Aliases |
|---|---|---|
| Autores | `dcterms:creator` | `dc:creator`, `schema:creator`, `pav:createdBy`, `prov:wasAttributedTo` |
| Contribuidores | `dcterms:contributor` | `dc:contributor`, `schema:contributor`, `pav:contributedBy` |
| Publisher | `dcterms:publisher` | `dc:publisher`, `schema:publisher` |
| Funders | `schema:funder` | `foaf:fundedBy` |

## 3. Versionado

| Dato | Anotación recomendada | Aliases |
|---|---|---|
| Revisión (vX.Y.Z) | `owl:versionInfo` | `schema:schemaVersion`, `pav:version`, `dcterms:hasVersion` |
| IRI de esta versión | `owl:versionIRI` | — |
| Versión anterior | `owl:priorVersion` | `dcterms:replaces`, `prov:wasRevisionOf`, `pav:previousVersion` |
| Compatibilidad | `owl:backwardCompatibleWith` | `owl:incompatibleWith` (ruptura) |

## 4. Fechas

| Dato | Anotación recomendada | Aliases |
|---|---|---|
| Creación | `dcterms:created` | `schema:dateCreated`, `prov:generatedAtTime`, `pav:createdOn` |
| Modificación | `dcterms:modified` | `schema:dateModified`, `pav:lastUpdatedOn` |
| Publicación (issued) | `dcterms:issued` | `schema:dateIssued` |

## 5. Licencia, citación y estado

| Dato | Anotación recomendada | Aliases |
|---|---|---|
| Licencia | `dcterms:license` | `dc:rights`, `schema:license`, `cc:license` |
| Citación (citeAs) | `schema:citation` | `dcterms:bibliographicCitation` |
| Estado | `bibo:status` / `mod:status` | `schema:creativeWorkStatus` |
| DOI | `bibo:doi` | — |

## 6. Contexto y recursos

| Dato | Anotación recomendada | Aliases |
|---|---|---|
| Introducción (por idioma) | `widoco:introduction` (con `xml:lang`) | — |
| Fuentes | `dcterms:source` | `prov:hadPrimarySource` |
| Ver también | `rdfs:seeAlso` | — |
| Extendida (voaf) | `voaf:extends` | — |
| Perfil de descarga | `wdrs:describedBy` | — |
| Repositorio | `schema:codeRepository` | `doap:repository` |
| Funding | `schema:funding` | — |
| Serializaciones alternativas | `widoco:rdfXmlSerialization`, `widoco:turtleSerialization`, `widoco:jsonldSerialization`, `widoco:ntSerialization` | — |

## 7. Propuestas de adopción EDINT (huecos detectados)

- [ ] `dcterms:publisher` con nodo agente FEMP (nombre, URL, institución) — hoy solo en conf (19/20)
- [ ] `schema:citation` — 0/20
- [ ] `widoco:introduction` es/en — 0/20 (hoy solo en confs v2)
- [ ] `dcterms:modified` en cada release — 2/20
- [ ] `dcterms:contributor` — 3/20
- [ ] `dcterms:source` / `rdfs:seeAlso` — 3/20, 4/20
- [ ] `owl:backwardCompatibleWith` / `owl:incompatibleWith` — 0/20
- [ ] `bibo:doi` — 0/20 (requiere Zenodo/CITATION.cff)


---

## Etiquetas de vocabularios importados / extendidos / reutilizados

⚠️ **Limitación de OWLAPI**: las aserciones cuyo sujeto es un IRI suelto
(`<http://.../skos/core> dcterms:title "SKOS"`) **se descartan** al cargar el
modelo (verificado en RDF/XML y Turtle). La anotación debe colgar de la
ontología.

### Forma recomendada: una anotación por vocabulario (multilingüe)

```turtle
<ontología> widoco:vocabularyLabel [
    widoco:vocabularyIRI <http://www.w3.org/2004/02/skos/core> ;
    rdfs:label "SKOS"@es , "SKOS"@en ] .
```
```xml
<widoco:vocabularyLabel>
  <rdf:Description>
    <widoco:vocabularyIRI rdf:resource="http://www.w3.org/2004/02/skos/core"/>
    <rdfs:label xml:lang="es">SKOS</rdfs:label>
    <rdfs:label xml:lang="en">SKOS</rdfs:label>
  </rdf:Description>
</widoco:vocabularyLabel>
```
Sirve para imports, `voaf:extends` y vocabularios reutilizados (el
`vocabularyIRI` es el IRI importado o el namespace reutilizado).

### Forma alternativa: listas nombre/URI (compatibilidad)

```properties
widoco:importedOntologyNames "SKOS;Infraestructura"
widoco:importedOntologyURIs  "http://www.w3.org/2004/02/skos/core;https://edint.es/def/infraestructura"
# ídem extendedOntologyNames/URIs y reusedVocabularyNames/URIs
```

### Orden de resolución (verificado)

1. `widoco:vocabularyLabel` (idioma actual → sin idioma → cualquiera),
2. listas `widoco:*OntologyNames/URIs`,
3. título de la ontología importada (si el import resuelve),
4. **carga del IRI del vocabulario** para leer su título (mappers locales → red,
   timeout 3 s, caché en `~/.widoco/vocabulary-titles.properties`; se desactiva
   con `-noResolveVocabularyTitles`),
5. último segmento completo del IRI, prettificado,
6. el IRI.

Si dos entradas acaban con el mismo label, se desambiguan con el host
(`dimension (purl.org)` / `dimension (vocab.linkeddata.es)`).
