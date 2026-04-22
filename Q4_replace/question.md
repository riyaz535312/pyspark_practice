repleace 'python' string in the column values with "PySpark" case sensitive

case sensitive
pyhton != Python != PYTHON

regexp_replace("col", r"\bpython\b", "pyspark")
\b -word boundary

pyspark is good
cpython is fast      ✅ correct
python3 is popular   ✅ correct
