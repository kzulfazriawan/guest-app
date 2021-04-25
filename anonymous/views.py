from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView


# Create your views here.


class ViewHome(TemplateView):
    template_name = 'homepage/index.html'

    def dispatch(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_superuser:
            return redirect('/admin')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        return context


class ViewPostGuest(View):
    def post(self, requests):
        """

        :param requests:
        :return:
        """
        pass
