from rest_framework import routers
from works.views import Works_view


router = routers.DefaultRouter()
router.register('works', Works_view)
