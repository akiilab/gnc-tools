
# GNU

## Login

Auto login to the remote server.

Required:

- Citrix Viewer
- Python Library: **selenium**

```shell
./login.sh -q username password
```

The browser will not be promted out if the **-q** flag is set.

## Copy File

Currenly, this command only can execute at MacOSX environment and only one file can transfer.

```shell
osascript cp.scpt /path/from/file.py /path/to/file.py
```

feature: support multiple files




