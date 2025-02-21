# -*- coding: utf-8 -*-

from web_fragments.fragment import Fragment
from openedx.core.djangoapps.plugin_api.views import EdxFragmentView
from importlib.resources import files


from web_fragments.fragment import Fragment

# Create your views here.


class MyTabView(EdxFragmentView):
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        return files(__package__).joinpath(path).read_text(encoding="utf-8")
    
    def render_to_fragment(self, request, course_id, **kwargs):
        html = self.resource_string("static/html/myxblock.html")
        frag = Fragment(str(html.format(self=self)))
        frag.add_css(str(self.resource_string("static/css/myxblock.css")))
        frag.add_javascript(str(self.resource_string("static/js/src/myxblock.js")))
        frag.initialize_js('MyXBlock')
        return frag

