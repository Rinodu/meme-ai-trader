import sys

from .config import ConfigError, Settings


try:
    settings = Settings.from_env()
except ConfigError as error:
    print(f"configuration error: {error}", file=sys.stderr)
    raise SystemExit(2) from error

print(f"mode={settings.mode} birdeye_enabled={settings.birdeye_enabled}")
