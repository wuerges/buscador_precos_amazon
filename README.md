# Primeiro

Ferramenta trabalha somente com csv:

libreoffice --headless  --convert-to csv planilhas/*.ods


Converter os CSVs para UTF8:

for f in data/* ; do  iconv -f ISO-8859-1 -t UTF8 "$f">/tmp/temp; mv /tmp/temp "$f"  ; done
