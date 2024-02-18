
# Create RSS feed from mp3 files

```
export STORAGE_PREFIX="https://storage.googleapis.com/...."
```

```bash
for file in ~/Downloads/spanish/*.mp3; do
#    echo "$file"
    afinfo "$file" |grep "estimated duration" |cut -d' '  -f3
done
```