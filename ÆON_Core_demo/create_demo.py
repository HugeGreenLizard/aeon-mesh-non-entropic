import os

os.makedirs(".", exist_ok=True)

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# ÆON Core Engine (Demo Release)\n\n> Non-Entropic Cognitive Architecture & Operator Cantrophy\n\nWelcome to the open-source reference release of ÆON Core Engine.\n")

with open("boot_demo.sh", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env bash\necho '=========================================='\necho '      ÆON CORE ENGINE — BOOT SEQUENCE     '\necho '=========================================='\npython3 aeon_core_engine.py\n")

with open("aeon_core_engine.py", "w", encoding="utf-8") as f:
    f.write("import time\ndef run():\n    print('\\n[ÆON-CORE] Uruchamianie silnika referencyjnego...')\n    time.sleep(0.3)\n    print('  [•] Spójność roju (Psi): 1.0000')\n    print('  [•] Delta Entropii (dS/dt): -0.045')\n    print('\\n[ÆON-CORE] Stan systemowy: DOMINACJA / OMEGA ACTIVE\\n')\nif __name__ == '__main__': run()\n")

os.chmod("boot_demo.sh", 0o755)
print("[✔] Pliki demo zostały pomyślnie utworzone!")
