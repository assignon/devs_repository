from rest_framework import routers
from works.views import Works_view, Description_view, Skills_view


router = routers.DefaultRouter()
router.register('works', Works_view)
router.register('description', Description_view)
router.register('skills', Skills_view)
