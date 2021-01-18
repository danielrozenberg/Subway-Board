These files are compiled using protoc (apt install protobuf-compiler) and
mypy-protobuf (pip install mypy-protobuf):

```
protoc --proto_path=server/third_party/proto \
  --python_out=server/third_party/proto \
  --mypy_out=server/third_party/proto \
  gtfs-realtime.proto nyct-subway.proto
```
