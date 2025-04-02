import flet as ft


def main(page: ft.Page):
    page.title = "Guardar datos como cookies"

    # Guardar un valor (como una cookie)
    page.client_storage.set("mi_cookie", "valor_guardado")

    # Leer el valor más tarde
    valor_guardado = page.client_storage.get("mi_cookie")

    page.add(ft.Text(f"Valor de la 'cookie': {valor_guardado}"))

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080)

