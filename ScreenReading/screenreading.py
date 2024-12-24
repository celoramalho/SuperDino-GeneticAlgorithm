import mss
import pygetwindow as gw


def get_chrome_window():
    # Localiza a janela do Chrome pelo título
    for window in gw.getAllWindows():
        if "Chrome" in window.title:
            return window
    return None

with mss.mss() as sct:
    monitor = {"top": 100, "left": 100, "width": 800, "height": 600}
    screenshot = sct.grab(monitor)
    img = np.array(screenshot)
    # Agora você pode processar a imagem com OpenCV ou outra biblioteca.