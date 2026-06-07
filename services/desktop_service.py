import pyautogui
import time
from pyvda import VirtualDesktop, get_virtual_desktops

def switch_to_desktop(desktop: int):
    # Dapatkan jumlah virtual desktop saat ini
    current_desktops = len(get_virtual_desktops())

    if desktop > current_desktops:
        # Pindah ke desktop paling akhir sebelum membuat desktop baru
        VirtualDesktop(current_desktops).go()
        time.sleep(0.5)

        # Buat desktop baru sampai jumlahnya sesuai target
        # Ingat: pembuatan desktop (win+ctrl+d) otomatis berpindah ke desktop tersebut
        for _ in range(current_desktops, desktop):
            pyautogui.hotkey("win", "ctrl", "d")
            time.sleep(0.5)
    else:
        # Jika desktop sudah ada, kita bisa langsung lompat ke desktop tersebut dengan pyvda
        target_desktop = VirtualDesktop(desktop)
        target_desktop.go()
        time.sleep(0.5)