from django.apps import AppConfig


class NewsPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NewsPortal'

    def ready(self):
        import NewsPortal.signals

        from .tasks import send_mails
        from .scheduler import weekly_scheduler
        print('started')

        weekly_scheduler.add_job(
            id='mail_send',
            func=send_mails,
            trigger='interval',
            seconds=10,

        )