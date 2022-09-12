import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("real.avsc", "rb").read())

# Serialize your avro
writer = DataFileWriter(open("real.avro", "wb"), DatumWriter(), schema)
# uncomment this section to append new data into the schema
# writer.append({"name": "Alyssa", "favorite_number": 256})
writer.close()

# deserialize avro
# reader = DataFileReader(open("users.avro", "rb"), DatumReader())
# for user in reader:
#     print user
# reader.close()
