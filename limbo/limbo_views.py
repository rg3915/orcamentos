class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        e = {
            'n': {'total': Entry.objects.all().count(),
                  'entrada': Entry.objects.filter(is_entry=False).count()
                  },
        }
        context = super(Home, self).get_context_data(**kwargs)
        context['entry'] = e
        return context
        # use: {{ entry.n.total }}
