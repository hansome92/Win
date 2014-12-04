from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Testimonial


class TestimonialPlugin(CMSPluginBase):
    model = Testimonial
    name = _("Testimonial")
    render_template = "cms/plugins/Testimonial.html"
    
    def render(self, context, instance, placeholder):

       # child = instance.page_link.get_children()
        child = instance.page_link.get_children()


        context.update({
            'object': instance,
            'placeholder': placeholder,
            'link': instance.page_link,
            'child' : child,
            'showcount' : instance.show_count,
            'styles' : instance.styles,
        #    'child' : child
        })
        return context 
 
plugin_pool.register_plugin(TestimonialPlugin)