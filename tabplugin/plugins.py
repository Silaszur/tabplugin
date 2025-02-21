from django.conf import settings
from django.utils.translation import ugettext_noop

from lms.djangoapps.courseware.tabs import EnrolledTab
from xmodule.tabs import TabFragmentViewMixin

class MyTab(TabFragmentViewMixin, EnrolledTab):
    type = 'mytab'
    title = ugettext_noop('MyTab')
    priority = None
    view_name = 'mytab_view'
    is_hideable = True

    @classmethod
    def is_enabled(cls, course, user=None):
        """
        Returns true if the specified user has staff access.
        """
        return True
       
