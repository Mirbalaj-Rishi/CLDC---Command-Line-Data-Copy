import sys
import sysconfig

print(f"GIL enabled: {sys._is_gil_enabled()}")
print(f"Free-threading supported: {sysconfig.get_config_var('Py_GIL_DISABLED') == 1}")

if sysconfig.get_config_var('Py_GIL_DISABLED') == 1 and sys._is_gil_enabled() == False:
    print("\nall set\n")
else:
    print("\nGIL is still enabled or/and free-threading is disabled\n")