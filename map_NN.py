from flask import Flask, render_template
import folium

app = Flask(__name__)


@app.route('/')
def index():
    map_nizhny_novgorod = folium.Map(location=[56.326887, 44.005986],
                                     zoom_start=8, min_zoom=11, max_zoom=20)

    places = [
        {
            "name": "Кремль",
            "description": "Историческая крепость с прекрасным видом на Волгу.",
            "location": [56.32854154443085, 44.002311240261186]},
        {
            "name": "Стрелка",
            "description": "Место, где Волга впадает в Оку,"
                           " отличное для прогулок и отдыха.",
            "location": [56.33502428254962, 43.97606847991595]},
        {
            "name": "Чкаловская лестница",
            "description": "Известная лестница с 560 ступенями, ведущая к Волге.",
            "location": [56.3305762179773, 44.009503659812914]},
        {
            "name": "Нижегородская ярмарка",
            "description": "Центральный выставочный центр Нижнего Новгорода",
            "location": [56.328492644568, 43.96124942676731]},
        {
            "name": "Парк Швейцария",
            "description": "Один из крупнейших парков города, "
                           "отличное место для прогулок.",
            "location": [56.278789752399426, 43.974851013270836]},
    ]

    sber_place = {
        'name': "ПАО Сбербанк",
        'description': "Моя будущая работа",
        'location': [56.32219007143675, 44.01012612592627]
    }

    fg = folium.FeatureGroup(name="Отобразить интересные места",
                             show=True).add_to(
        map_nizhny_novgorod)
    fg_sber = folium.FeatureGroup(name='место работы', show=True).add_to(
        map_nizhny_novgorod)

    for place in places:
        folium.Marker(
            location=place["location"],
            popup=f"<b>{place['name']}</b><br>{place['description']}").add_to(
            fg)

    folium.Marker(
        location=sber_place['location'],
        popup=f"<b>{sber_place['name']}</b><br>{sber_place['description']}"
    ).add_to(fg_sber)

    folium.TileLayer(
        'cartodbpositron',
        attr='Map tiles by Carto,'
             ' under CC BY 3.0. Data by OpenStreetMap, under ODbL').add_to(
        map_nizhny_novgorod)
    folium.TileLayer(
        'cartodbdark_matter',
        attr='Map tiles by Carto,'
             ' under CC BY 3.0. Data by OpenStreetMap, under ODbL').add_to(
        map_nizhny_novgorod)

    folium.TileLayer('openstreetmap',
                     attr='Map data © OpenStreetMap contributors'
                     ).add_to(map_nizhny_novgorod)

    folium.LayerControl().add_to(map_nizhny_novgorod)

    map_nizhny_novgorod.save('templates/map.html')
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)
