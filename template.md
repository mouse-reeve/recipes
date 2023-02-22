## Recipe: {{ recipe.title }}
{% if recipe.notes %}{{ recipe.notes }}  
{% endif %}{% if recipe.preptime %}Prep time: {{ recipe.preptime }}  
{% endif %}{% if recipe.baketime %}Bake time: {{ recipe.baketime }}  
{% endif %}{% if recipe.totaltime %}Total time: {{ recipe.totaltime }}  
{% endif %}{% if recipe.quantity %}Quantity: {{ recipe.quantity }}  {% endif %}

### Ingredients{% for entry in recipe.ingredients %}{% if entry is string %}
 - {{ entry|ingredient_display }}{% else %}{% for key in entry %}
 - {{ key }}{% for ingredient in entry[key] %}
    - {{ ingredient|ingredient_display }}{% endfor %}{% endfor %}{% endif %}{% endfor %}

### Steps{% for entry in recipe.steps %}{% if entry is string %}
 - {{ entry }}{% else %}{% for key in entry %}
 - {{ key }}{% for substep in entry[key] %}
    - {{ substep }}{% endfor %}{% endfor %}{% endif %}{% endfor %}

{% if recipe.source %}> Source: {{ recipe.source }}{% endif %}
