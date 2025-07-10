# utilise le code suivant pour stocker dans un fichier txt
# les informations title, instructions, ingredients et nutrients
# de chaque recette de cuisine présente dans la liste des urls
# PS recipe_scrapers vient de https://github.com/hhursev/recipe-scrapers

# crée ensuite un script de lecture du fichier
# et une classe Recipe
# qui représente une recette extraite d'une url

# PS : commence ton TP avec une ou deux urls pour ensuite faire le processus sur les 100 urls présentes

from recipe_scrapers import scrape_me
"""
urls = ['https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/'
    , 'https://www.allrecipes.com/recipe/22162/uglies/', 'https://www.allrecipes.com/recipe/140286/homemade-dog-food/',
        'https://www.allrecipes.com/the-10-minute-recipe-i-make-once-a-week-11742451',
        'https://www.allrecipes.com/recipe/16248/easy-homemade-chili/',
        'https://www.allrecipes.com/recipe/16383/basic-crepes/',
        'https://www.allrecipes.com/recipe/234933/how-to-make-perfect-polenta/',
        'https://www.allrecipes.com/recipe/58942/absolute-best-liver-and-onions/',
        'https://www.allrecipes.com/recipe/7177/bread-pudding-ii/',
        'https://www.allrecipes.com/recipe/51301/sarahs-applesauce/',
        'https://www.allrecipes.com/recipe/9870/easy-sugar-cookies/',
        'https://www.allrecipes.com/recipe/17481/simple-white-cake/',
        'https://www.allrecipes.com/recipe/228774/emergency-chicken/',
        'https://www.allrecipes.com/recipe/223042/chicken-parmesan/',
        'https://www.allrecipes.com/recipe/6761/tasty-buns/', 'https://www.allrecipes.com/recipe/35149/corn-dogs/',
        'https://www.allrecipes.com/recipe/11867/death-by-garlic/',
        'https://www.allrecipes.com/recipe/71484/i-dont-know/', 'https://www.allrecipes.com/recipe/24448/my-favorites/',
        'https://www.allrecipes.com/recipe/20586/homemade-vanilla-pudding/',
        'https://www.allrecipes.com/recipe/11899/basic-pasta/',
        'https://www.allrecipes.com/recipe/222006/disneys-ratatouille/',
        'https://www.allrecipes.com/recipe/222352/jamies-sweet-and-easy-corn-on-the-cob/',
        'https://www.allrecipes.com/red-white-and-blue-cheesecake-bites-recipe-7554460',
        'https://www.allrecipes.com/recipe/21006/fried-cornmeal-mush/',
        'https://www.allrecipes.com/recipe/85129/fleischkuechle-flesh-keek-luh/',
        'https://www.allrecipes.com/recipe/221972/chef-johns-cioppino/',
        'https://www.allrecipes.com/recipe/15983/grannys-cherokee-casserole/',
        'https://www.allrecipes.com/recipe/30918/irish-boiled-dinner-corned-beef/',
        'https://www.allrecipes.com/recipe/269742/soul-food-seasoning/',
        'https://www.allrecipes.com/recipe/10857/dishpan-cookies-i/',
        'https://www.allrecipes.com/recipe/233122/perfect-fried-green-tomatoes/',
        'https://www.allrecipes.com/garlic-butter-grilled-cheese-hotdog-recipe-11763786',
        'https://www.allrecipes.com/recipe/218619/easy-bok-choy/',
        'https://www.allrecipes.com/recipe/229290/homemade-baking-powder-recipe/',
        'https://www.allrecipes.com/italian-penicillin-soup-recipe-8751324',
        'https://www.allrecipes.com/recipe/17072/thirty-minute-meal/',
        'https://www.allrecipes.com/recipe/242401/homemade-worcestershire-sauce/',
        'https://www.allrecipes.com/recipe/139453/lucky-and-rippys-favorite-dog-food/',
        'https://www.allrecipes.com/easy-summer-dump-cake-recipe-11759738',
        'https://www.allrecipes.com/recipe/285393/bialys/', 'https://www.allrecipes.com/recipe/16304/husbands-delight/',
        'https://www.allrecipes.com/recipe/146125/chicken-julienne/',
        'https://www.allrecipes.com/recipe/17891/golden-sweet-cornbread/',
        'https://www.allrecipes.com/father-in-law-favorite-shrimp-recipe-11748331',
        'https://www.allrecipes.com/recipe/57176/gunk-on-noodles/',
        'https://www.allrecipes.com/recipe/14415/cobb-salad/',
        'https://www.allrecipes.com/recipe/11352/three-ingredient-peanut-butter-cookies/',
        'https://www.allrecipes.com/recipe/257242/norwegian-butter-sauce-sandefjordsmor/',
        'https://www.allrecipes.com/recipe/34450/italian-seasoning-i/',
        'https://www.allrecipes.com/recipe/213015/daves-georgia-black-eyed-peas/',
        'https://www.allrecipes.com/recipe/81942/new-york-knish-yo/',
        'https://www.allrecipes.com/recipe/53683/perfect-lemon-curd/',
        'https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio/',
        'https://www.allrecipes.com/recipe/13961/baked-vegetables-i/',
        'https://www.allrecipes.com/recipe/8380474/dynamite-rice/',
        'https://www.allrecipes.com/recipe/214931/oven-roasted-asparagus/',
        'https://www.allrecipes.com/recipe/228333/cuban-inspired-millet/',
        'https://www.allrecipes.com/recipe/228823/quick-beef-stir-fry/',
        'https://www.allrecipes.com/recipe/11758/baked-ziti-i/',
        'https://www.allrecipes.com/recipe/228755/braunschweiger-potato-hash/',
        'https://www.allrecipes.com/recipe/26159/kolachky/',
        'https://www.allrecipes.com/recipe/240206/simple-broccolini/',
        'https://www.allrecipes.com/recipe/238510/homemade-arepas/',
        'https://www.allrecipes.com/my-husbands-favorite-hot-dog-recipe-11764543',
        'https://www.allrecipes.com/recipe/221361/traditional-sauerbraten/',
        'https://www.allrecipes.com/recipe/83097/authentic-german-potato-salad/',
        'https://www.allrecipes.com/summer-barbecue-casserole-recipe-11748413',
        'https://www.allrecipes.com/recipe/228641/chef-johns-popovers/',
        'https://www.allrecipes.com/recipe/15432/angel-food-cake-iii/',
        'https://www.allrecipes.com/article/my-grandmas-chicken-wings-recipe/',
        'https://www.allrecipes.com/recipe/11713/the-cheese-thing/',
        'https://www.allrecipes.com/recipe/241074/easy-garlic-kale/',
        'https://www.allrecipes.com/recipe/14064/easy-guacamole/',
        'https://www.allrecipes.com/recipe/190276/easy-shakshuka/',
        'https://www.allrecipes.com/recipe/256888/chef-johns-pate-de-campagne/',
        'https://www.allrecipes.com/recipe/109810/italian-style-swiss-chard/',
        'https://www.allrecipes.com/recipe/24272/buttery-soft-pretzels/',
        'https://www.allrecipes.com/recipe/257961/neeps-and-tatties/',
        'https://www.allrecipes.com/recipe/258755/simple-custard/',
        'https://www.allrecipes.com/recipe/8909/chicken-and-rice/',
        'https://www.allrecipes.com/recipe/20487/old-fashioned-lemonade/',
        'https://www.allrecipes.com/recipe/24059/creamy-rice-pudding/',
        'https://www.allrecipes.com/recipe/259162/ratatouille-provencale/',
        'https://www.allrecipes.com/recipe/158140/spaghetti-sauce-with-ground-beef/',
        'https://www.allrecipes.com/recipe/10412/welsh-cookies/',
        'https://www.allrecipes.com/recipe/229870/thats-good-moosh/',
        'https://www.allrecipes.com/recipe/275183/homemade-grain-free-dog-food/',
        'https://www.allrecipes.com/recipe/22749/the-best-banana-pudding/',
        'https://www.allrecipes.com/recipe/46653/taco-seasoning-i/',
        'https://www.allrecipes.com/recipe/50223/homemade-crispy-seasoned-french-fries/',
        'https://www.allrecipes.com/recipe/164920/easy-dinner-hash/',
        'https://www.allrecipes.com/recipe/11215/benne-wafers/',
        'https://www.allrecipes.com/recipe/223051/chef-johns-colcannon/',
        'https://www.allrecipes.com/recipe/24332/ultimate-twice-baked-potatoes/',
        'https://www.allrecipes.com/recipe/216159/perfect-chicken/',
        'https://www.allrecipes.com/recipe/258879/kewa-datshi-bhutanese-dish/',
        'https://www.allrecipes.com/recipe/10402/the-best-rolled-sugar-cookies/',
        'https://www.allrecipes.com/tang-pie-recipe-11759885']
"""
"""
        try:
            scraper = scrape_me(url)
            titre = scraper.title()
            instructions = scraper.instructions()
            ingredients = scraper.ingredients()
            nutrients = scraper.nutrients()

            f.write(f"--- Recette {i} ---\n")

        except Exception as e:
            print(f"❌  Erreur sur {url} : {e}")

"""

import json
from recipe_scrapers import scrape_me

urls = ['https://www.marmiton.org/recettes/menu-de-la-semaine.aspx',
        'https://www.marmiton.org/recettes/recette_carottes-vichy_17717.aspx'
    , 'https://www.marmiton.org/recettes/selection_asie.aspx', 'https://www.marmiton.org/recettes/selection_cuisine_corse.aspx', 'https://www.marmiton.org/recettes/selection_alsace.aspx', 'https://www.marmiton.org/recettes/selection_afrique.aspx', 'https://www.marmiton.org/recettes/recette_mille-feuilles_33004.aspx', 'https://www.marmiton.org/recettes/recette_gratin-dauphinois_13809.aspx', 'https://www.marmiton.org/recettes/recette_bugnes_16033.aspx', 'https://www.marmiton.org/recettes/recette_cookies-maison_86989.aspx', 'https://www.marmiton.org/recettes/recette_coq-au-vin-maison_25755.aspx', 'https://www.marmiton.org/recettes/recette_tartiflette-facile_15733.aspx', 'https://www.marmiton.org/recettes/selection_recettes_bretonnes.aspx', 'https://www.marmiton.org/recettes/recette_spaghetti-bolognaise_19840.aspx', 'https://www.marmiton.org/recettes/recette_la-poule-au-riz-de-la-mere-michele_36729.aspx', 'https://www.marmiton.org/recettes/recette_cacasse-a-cul-nu-ardennes_18541.aspx', 'https://www.marmiton.org/recettes/recette_veritable-moelleux-au-chocolat_12825.aspx', 'https://www.marmiton.org/recettes/recette_les-vrais-quenelles-natures-lyonnaises_46374.aspx', 'https://www.marmiton.org/recettes/recette_tian-provencal_36194.aspx', 'https://www.marmiton.org/recettes/recette_creme-brulee_11491.aspx', 'https://www.marmiton.org/recettes/recette_tourtons-des-alpes-ou-de-champsaur_27676.aspx', 'https://www.marmiton.org/recettes/recette_steak-tartare_18121.aspx', 'https://www.marmiton.org/recettes/recette_financiers_13690.aspx', 'https://www.marmiton.org/recettes/recette_gougeres-au-fromage_20095.aspx', 'https://www.marmiton.org/recettes/selection_soupe.aspx', 'https://www.marmiton.org/recettes/selection_sud-ouest.aspx', 'https://www.marmiton.org/recettes/recette_moules-au-roquefort_36429.aspx', 'https://www.marmiton.org/recettes/recette_tarte-a-la-tomate-et-a-la-moutarde_20978.aspx', 'https://www.marmiton.org/recettes/selection_hiver.aspx', 'https://www.marmiton.org/recettes/recette_andouillette-sauce-moutarde_19759.aspx', 'https://www.marmiton.org/recettes/recette_courgette-farcie_11173.aspx', 'https://www.marmiton.org/recettes/recette_pancakes-faciles-et-rapides_81518.aspx', 'https://www.marmiton.org/recettes/top-internautes-dessert.aspx', 'https://www.marmiton.org/recettes/selections.aspx', 'https://www.marmiton.org/recettes/selection_indienne.aspx', 'https://www.marmiton.org/recettes/recette_moules-marinieres_13214.aspx', 'https://www.marmiton.org/recettes/recette_gougeres-faciles_13241.aspx', 'https://www.marmiton.org/recettes/recette_madeleines-faciles_17700.aspx', 'https://www.marmiton.org/recettes/recette_coleslaw-facile_28532.aspx', 'https://www.marmiton.org/recettes/recette_pate-a-crepes_12372.aspx', 'https://www.marmiton.org/recettes/recette_rougail-saucisse_22851.aspx', 'https://www.marmiton.org/recettes/recette_mayonnaise-maison_26184.aspx']


recipes = []

for url in urls:
    try:
        scraper = scrape_me(url)
        recipe_data = {
            "titre": scraper.title(),
            "instructions": scraper.instructions(),
            "ingredients": scraper.ingredients(),
            "nutrients": scraper.nutrients()
        }
        recipes.append(recipe_data)
        print(f"✔️ {recipe_data['titre']} ajouté")
    except Exception as e:
        print(f"❌ Erreur sur {url} : {e}")

# Sauvegarde dans un fichier JSON propre
with open("recipes.txt", "w", encoding="utf-8") as f:
    json.dump(recipes, f, ensure_ascii=False, indent=2)
