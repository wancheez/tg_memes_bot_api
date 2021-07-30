from rest_framework.routers import DefaultRouter

from .views import ScheduleTaskView, TaskTypeView

app_name = 'meme_schedules'

router = DefaultRouter()
router.register(r'meme_schedules', ScheduleTaskView)
router.register(r'schedules_types', TaskTypeView)
urlpatterns = router.urls
