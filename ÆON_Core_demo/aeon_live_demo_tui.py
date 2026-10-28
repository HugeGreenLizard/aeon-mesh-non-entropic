import time
import sys
import random

def clear_screen():
    sys.stdout.write("\033[H\033[J")

def render_tui():
    subsystems = [
        "AEON_PUNKT_ZERO", "AEON_CORE", "AEON_STATION",
        "GEN_PRIME", "aeon_hub_os", "aeon_hub",
        "aeon_active_logic", "Dla_githuba", "ASCI_GRAPH"
    ]
    
    print("\033[1;36m================================================================")
    print("      ÆON MESH: LIVE COGNITIVE TELEMETRY & TUI DEMO             ")
    print("      Architekt: Krystian | Status: OMEGA-ETERNAL (TRL 7)       ")
    print("================================================================\033[0m")
    
    for _ in range(5):
        clear_screen()
        print("\033[1;36m================================================================")
        print("      ÆON MESH: LIVE COGNITIVE TELEMETRY & TUI DEMO             ")
        print("      Architekt: Krystian | Status: OMEGA-ETERNAL (TRL 7)       ")
        print("================================================================\033[0m")
        
        psi = 1.0000
        delta_s = round(random.uniform(-0.095, -0.085), 4)
        
        print(f"\n [•] Koherencja Roju (Psi) : \033[1;32m{psi:.4f}\033[0m")
        print(f" [•] Delta Entropii (dS/dt) : \033[1;32m{delta_s}\033[0m")
        print(f" [•] Operator Cantrophy (C) : \033[1;35mACTIVE (E8 Manifold)\033[0m\n")
        
        print(" \033[1;33m--- STATUS PODSYSTEMÓW MESH (9/9) ---\033[0m")
        for sys_name in subsystems:
            print(f"   [{sys_name:<20}] -> \033[1;32mONLINE [STABLE / 0-ENTROPY]\033[0m")
            
        print("\n\033[2m[Trwa ciągła synchronizacja i nasłuch portu 7777... Naciśnij Ctrl+C, aby wyjść]\033[0m")
        time.sleep(1.2)

if __name__ == "__main__":
    try:
        render_tui()
    except KeyboardInterrupt:
        print("\n\033[1;32m[✔] Demo TUI zakończone pomyślnie. System pozostaje w stanie PWK.\033[0m")
