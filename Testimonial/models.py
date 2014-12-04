from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class Testimonial(CMSPlugin):
    """
    A Testimonial
    """
    title = models.CharField(_("title"), max_length=255)

    page_link = models.ForeignKey(
        Page, verbose_name=_("page"),
        help_text=_("Please select the page "), blank=True,
        null=True, limit_choices_to={'publisher_is_draft': True})

    show_count = models.IntegerField(_("Show Counts"))

    STYLE_CHOICES = (
        ('DEFAULT', 'Default'),
        ('HOME', 'Home'),
    )

    styles = models.CharField(max_length=10,
                                      choices=STYLE_CHOICES,
                                      default='DEFAULT')
    def __str__(self):
        return self.title
