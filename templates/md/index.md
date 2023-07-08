# Recipes

{% for dir in index | sort %}
## {{ dir }}
{% for file in index[dir] %}
    - [{{ index[dir][file] }}]({{ file }})
{% endfor %}
{% endfor %}

