# Gitignore Creator

Simple command line tool for downloading and combining multiple
gitignore templates from the
[Github gitignore repo](https://github.com/github/gitignore).

## Installation

If you want to install the command system wide then clone the repo and
run the command:

```
sudo pip install .
```

This will add a new command `gitignore-creator`. If you do not want to
install system wide then you can just run `python gitignore-creator`
from within the cloned repo.

## Usage

Run the command

```
gitignore-creator Python OSX
```

This will create a file `.gitignore` in the current directory that
contains the latest version of the `Python.gitignore` and
`OSX.gitignore` templates.

If you want to output to a different file just add the `--output`
option and provide a full or relative path. For example:

```
gitignore-creator Python OSX --output testing.gitignore
```

will create a file `testing.gitignore` containing the latest version
of the `Python.gitignore` and `OSX.gitignore` templates.

If you want to output to stdout then set the output file to `-`. For
example:

```
gitignore-creator Python OSX --output -
```

That will print out the following on stdout

```
 ____        _   _                 
|  _ \ _   _| |_| |__   ___  _ __  
| |_) | | | | __| '_ \ / _ \| '_ \ 
|  __/| |_| | |_| | | | (_) | | | |
|_|    \__, |\__|_| |_|\___/|_| |_|
       |___/                       

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask instance folder
instance/

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# IPython Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# dotenv
.env

# virtualenv
venv/
ENV/

# Spyder project settings
.spyderproject

# Rope project settings
.ropeproject

  ___  ______  __
 / _ \/ ___\ \/ /
| | | \___ \\  / 
| |_| |___) /  \ 
 \___/|____/_/\_\
                 

.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon

# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk
```
