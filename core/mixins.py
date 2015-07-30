from django.contrib.auth.decorators import login_required
from django.db.models import Q


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class CounterMixin(object):

    def get_context_data(self, **kwargs):
        context = super(CounterMixin, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class FirstnameSearchMixin(object):

    def get_queryset(self):
        queryset = super(FirstnameSearchMixin, self).get_queryset()
        q = self.request.GET.get('search_box')
        if q:
            return queryset.filter(
                Q(first_name__icontains=q) |
                Q(company__icontains=q))
        return queryset
