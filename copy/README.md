# Copy File

Currenly, this command only can execute at MacOSX environment and only one file can transfer.

## Text Mode



### Usage

```shell
osascript cp-text.scpt /path/from/file.py /path/to/file.py
```

## Copy and Paste Mode

### Settings

On remote server, append these commands into **.vimrc**.

```shell
# ~/.vimrc
command CCP :redir! >> /tmp/copy_base64 | sil echon @* | redir end
```

On remote server, append these commands into **.bashrc** 

```shell
# ~/.bashrc
function before_copy {
  rm -f /tmp/copy_base64
}

function after_copy {
  file=$1
  md5=$2
  mkdir -p $(dirname $file)
  cat /tmp/copy_base64 | base64 -d > $file
  diff <(md5sum $file | cut -d ' ' -f 1)  <(echo $md5)
}

alias BCP="before_copy"
alias CCP="vimx +CCP +qall"
alias ACP="after_copy"
```

Reload Bash

```shell
bash
```

## Usage

```shell
osascript cp.scpt /path/from/file.py /path/to/file.py
```

