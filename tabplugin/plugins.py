from django.utils.translation import gettext_noop
from lms.djangoapps.courseware.tabs import EnrolledTab
from xmodule.tabs import TabFragmentViewMixin

class MyTab(TabFragmentViewMixin, EnrolledTab):
    type = 'mytab'
    title = gettext_noop('MyTab')
    priority = None
    view_name = 'mytab_view'
    is_hideable = True
    
    @classmethod
    def is_enabled(cls, course, user=None):
        """
        Returns true if the tab should be enabled.
        """
        return True