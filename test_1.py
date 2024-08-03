import flet as fl


def main(page: fl.Page):
    page.title = "Mon appli"

    def quand_onclique(e):
        label.value = "Service"
        page.update()

    label = fl.Text("Bonjour")
    button = fl.ElevatedButton("Appuyer ici!")
    button.on_click = quand_onclique

    page.add(label, button)


fl.app(target=main)