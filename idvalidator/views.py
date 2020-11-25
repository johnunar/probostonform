from django.views.generic import FormView

from idvalidator.forms import ContactForm


class IndexView(FormView):
    template_name = 'idvalidator/index.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(IndexView, self).form_valid(form)
