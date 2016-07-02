''' jankass script for recipe html for veganteaparty.club '''
import json
import math
import re
import sys

recipe_json = json.load(open(sys.argv[1]))

print '''
<!DOCTYPE html>
<html>

<head>
    <title>%(title)s - Vegan Tea Party Club</title>

    <link href="https://fonts.googleapis.com/css?family=Vollkorn|Open+Sans|Unica+One" rel="stylesheet">
    <link href="../static/css/foundation.min.css" rel="stylesheet">
    <link href="../static/css/format.css" rel="stylesheet">

    <meta name=viewport content="width=device-width, initial-scale=1">
    <meta name="twitter:card" content="summary">

    <meta name="og:title" content="%(title)s - Vegan Tea Party Club">
    <meta name="og:description" content="%(description)s">
    <meta name="og:image" content="https://www.veganteaparty.club/../static/images/icon.jpg">

    <meta name="twitter:title" content="%(title)s - Vegan Tea Party Club">
    <meta name="twitter:description" content="%(description)s">
    <meta name="twitter:image" content="https://www.veganteaparty.club/../static/images/icon.jpg">

    <meta name="twitter:creator" content="@tripofmice">
    <meta name="twitter:site" content="@tripofmice">
    <meta name="twitter:image:alt" content="Tea, sandwiches, and cookies">

    <meta name="robots" content="index, follow">

    <!-- Piwik -->
    <script type="text/javascript">
      var _paq = _paq || [];
      _paq.push(["setDomains", ["*.veganteaparty.club"]]);
      _paq.push([\'trackPageView\']);
      _paq.push([\'enableLinkTracking\']);
      (function() {
        var u="//piwik.grimoire.org/piwik/";
        _paq.push([\'setTrackerUrl\', u+\'piwik.php\']);
        _paq.push([\'setSiteId\', 5]);
        var d=document, g=d.createElement(\'script\'), s=d.getElementsByTagName(\'script\')[0];
        g.type=\'text/javascript\'; g.async=true; g.defer=true; g.src=u+\'piwik.js\'; s.parentNode.insertBefore(g,s);
      })();
    </script>
    <noscript><p><img src="//piwik.grimoire.org/piwik/piwik.php?idsite=5" style="border:0;" alt="" /></p></noscript>
    <!-- End Piwik Code -->

</head>
<body>
    <header>
        <div class="block">
            <h2><a href="/">Vegan Tea Party Club</a></h2>
        </div>
    </header>
    <div id="recipe" class="block">
        <div class="recipe-header">
            <h1>%(title)s</h1>
        </div>
        <div id="items">
''' % ({'title': recipe_json['title'],
        'description': recipe_json['description']})

if 'source' in recipe_json:
    print '''
            <div class="section recipe-meta">
                <div class="row">
                    <div class="columns small-4">
                        <!--god only knows the cooking time-->
                        &nbsp;
                    </div>
                    <div class="columns small-4">
                        <a href="%s" target="_blank">Source</a>
                    </div>
                    <div class="columns small-4">
                        <!--makes some quantity-->
                        &nbsp;
                    </div>
                </div>
            </div>
            <div class="section">
                <h3>Ingredients</h3>
                <div class="row">
    ''' % recipe_json['source']
else:
    print '''
            <div class="section recipe-meta">
                <div class="row">
                    <div class="columns small-6">
                        god only knows the cooking time
                    </div>
                    <div class="columns small-6">
                        makes some quantity
                    </div>
                </div>
            </div>
            <div class="section">
                <h3>Ingredients</h3>
                <div class="row">
'''


halfway = int(math.ceil(len(recipe_json['ingredients'])/2)) + 1
for ingredients in [recipe_json['ingredients'][0:halfway],
                    recipe_json['ingredients'][halfway:]]:
    print '''
                    <div class="columns medium-6">
                        <ul>
    '''
    for ingredient in ingredients:
        ingredient = re.sub(r'\{butter\}',
                            '<a href="/recipe/vegan_butter.html">vegan butter</a>',
                            ingredient)
        ingredient = re.sub(r'[\{\}]', '', ingredient)
        print '''
                            <li>%s</li>
        ''' % (ingredient)

    print '''
                        </ul>
                    </div>
    '''


print '''
                </div>
            </div>
            <div class="section">
                <h3>Instructions</h3>
                <ul>
'''


for step in recipe_json['steps']:
    print '''
                    <li>%s</li>
    ''' % step


print '''
                </ul>
            </div>
'''

print '''
        </div>
        <div class="section menu-footer">
            <h2>enjoy</h2>
        </div>
    </div>
    <div class="block options">
        <ul>
            <li><a>print</a></li>
        </ul>
    </div>

    <footer>
        <div class="block">
            <p>by <a href="https://www.mousereeve.com/" target="_blank">Mouse Reeve<a>.</p>
        </div>
    </footer>
    <script type="text/javascript" src="../static/js/vendor/jquery.js"></script>
    <script type="text/javascript" src="../static/js/vendor/foundation.min.js"></script>
</body>
</html>
'''
