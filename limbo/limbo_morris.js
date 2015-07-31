{% for k, v in proposals.items %}
    { label: '{{ k }}', value: {{ v }} },
{% endfor %}
