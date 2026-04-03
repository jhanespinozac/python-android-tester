import flet as ft

def main(page: ft.Page):
    # Configuración básica
    page.title = "App Estable - Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # Referencias
    nombre_input = ft.TextField(
        label="Nombre del Proyecto", 
        border_color=ft.Colors.BLUE_700
    )
    texto_resultado = ft.Text(value="Esperando...", size=16)

    def al_hacer_clic(e):
        if not nombre_input.value:
            texto_resultado.value = "❌ Error: Campo vacío"
            texto_resultado.color = ft.Colors.RED
        else:
            texto_resultado.value = f"🚀 Proyecto '{nombre_input.value}' iniciado"
            texto_resultado.color = ft.Colors.GREEN_800
        page.update()

    # --- UI con máxima compatibilidad ---
    
    # Botón usando 'content' para evitar líos de argumentos
    boton = ft.ElevatedButton(
        content=ft.Text("Procesar Ahora", weight=ft.FontWeight.BOLD),
        on_click=al_hacer_clic,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE_700,
        )
    )

    # Card usando un Container interno para el color
    tarjeta_resultado = ft.Card(
        content=ft.Container(
            content=texto_resultado,
            padding=20,
            bgcolor=ft.Colors.BLUE_GREY_50, # Aquí definimos el color de fondo
            border_radius=10
        )
    )

    # Agregar todo a la página
    page.add(
        ft.Text("Prueba de Librerías", size=28, weight=ft.FontWeight.W_800),
        ft.Divider(height=20),
        nombre_input,
        ft.Container(height=10), # Espaciador
        boton,
        ft.Divider(height=40),
        tarjeta_resultado
    )

if __name__ == "__main__":
    # Si quieres probarlo como web app en el navegador: ft.app(target=main, view=ft.AppView.WEB_BROWSER)
    ft.app(target=main)