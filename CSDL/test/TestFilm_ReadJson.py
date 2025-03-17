from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Film import Film

jff=JsonFileFactory()
filename= "../../dataset/film.json"
films=jff.read_data(filename,Film)
print("Danh sách film sau khi loading:")
for film in films:
    print(film)