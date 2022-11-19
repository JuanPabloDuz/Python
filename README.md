# GIT STEPS
Go into the directory containing the project.
```bash
git init
git add .
git commit -m "readme"
```
Go to  www.github.com and loggin
Right upper corner and hit create a new repository, then:
```bash
git branch -M main
git remote add origin git@github.com:your_user/your_repo_name.git
git push -u origin main
```

# INSTALLING PYTHON

## INSTALL pyenv for version control
pyenv - is a simple Python version manager tool, which allows you easily switch between multiple versions of Python. You can set local or global system-wide Python versions via the tool.
1- Install dependencies
```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
2- Download and run installation script
```bash
curl https://pyenv.run | bash
```
3- AAd the following entries into your ~/.bashrc
```bash
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

```
4- Restart your shell and validate
```bash
exec $SHELL
pyenv --version
```
5- Install Python and check versions
```bash
pyenv install 3.7.6
pyenv versions
```
6- To change Python version and check effects
```bash
python shell 3.7.6
python --version
```

## REPL
Great place to test things
Access:
```bash
python3.7
```

## PYTHON FILES 

```bash
touch hello.py
echo '#!/usr/bin/env python3.7' >> hello.py
echo 'print("Hello, World!")' >> hello.py
chmod u+x hello.py
./hello.py 

```





