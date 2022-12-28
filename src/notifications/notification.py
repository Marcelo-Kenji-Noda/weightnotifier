from winotify import Notification, audio
from datetime import date

def create_toast():
    today = date.today().strftime("%dd/%mm/%YYYY")
    title = f"Adicionar medidas: {today}"
    toast = Notification(
        app_id="windows app",
        title= title,
        msg="Adicione as medidas na planilha!",
        icon="healthyicon.png")

    toast.set_audio(audio.Mail, loop=False)
    toast.add_actions(
        label="Abrir formulário", 
        launch="https://forms.gle/ck5gjqZwT4KazoSz7/")
    toast.show()
    return