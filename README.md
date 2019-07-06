# Rzeczoznawca motocyklowy - Szacowanie ceny motocykla

Celem projektu jest zastosowanie modeli regresji do szacowania (przewidywania) cen
motocykli o podanych parametrach i cechach. W projekcie dokonano ewaluacji różnych modeli regresji i dobrano model optymalny. 
***
Dane użyte do budowy modelu zostały pobrane ze stron znanego portalu aukcyjnego, do ściągnięcia danych ofert użyty został pakiet [scrapy](https://scrapy.org/). 
W projekcie jest już zapisany ściągnięty plik z danymi: `scrapy_motory/motory-2019-04-19.json` - ten plik został użyty do analizy i budowania modeli regresji. 

***

Szczegóły analizy danych i doboru modelu znajdziesz w pliku: [rzeczoznawca_motocyklowy.ipynb](rzeczoznawca_motocyklowy.ipynb)

Znajdziesz tam między innymi:
* implementację przeliczania cen na PLN wg kursów publikowanych przez NBP (pobieranych przez Rest API)
* ewaluację takich modeli regresji jak: LinearRegression, Lasso, BayesianRidge, Ridge, ElasticNet, DecisionTreeRegressor, RandomForestRegressor, KernelRidge, GradientBoostingRegressor, MLPRegressor
* próbę redukcji wymiaru przy użyciu TruncatedSVD
* próbę utworzenia komisji ekspertów - VotingRegressor

***

**Zwycięskim modelem na końcu analizy okazał się [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)**
