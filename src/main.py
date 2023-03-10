from winotify import Notification, audio
from datetime import date

def main():
    today = date.today().strftime("%d/%m/%Y")
    title = f"Adicionar medidas: {today}"
    toast = Notification(
        app_id="Weight App",
        title= title,
        msg="Adicione as medidas na planilha!",
        icon=r"C:\Users\kenji\dev\weightNotifier\src\static\1350095.png")

    toast.set_audio(audio.Mail, loop=False)
    toast.add_actions(
        label="Abrir formulário", 
        launch="https://forms.gle/ck5gjqZwT4KazoSz7/")
    toast.show()
    return

if __name__ == '__main__':
    main()