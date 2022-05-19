import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="amisbackend",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="amisbackend_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from amisbackend.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export amisbackend_KEY=value
export amisbackend_KEY="@int 42"
export amisbackend_KEY="@jinja {{ this.db.uri }}"
export amisbackend_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
amisbackend_ENV=production amisbackend run
```

Read more on https://dynaconf.com
"""
