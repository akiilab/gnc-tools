
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

### Settings

### Remote

```shell
# ~/.vimrc
command XX :redir! >> /tmp/xx | sli echon @* | redir end
```

```shell
# ~/.bashrc
function before_xx {
  rm -f /tmp/xx
}

function after_xx {
  file=$1
  mkdir -p $(dirname $file)
  cat /tmp/xx | base64 -d > $file
}

alias BX="before_xx"
alias XX="vimx +XX +qall"
alias AX="after_xx"
```

### Usage

```shell
osascript cp.scpt /path/from/file.py /path/to/file.py
```

feature: support multiple files

