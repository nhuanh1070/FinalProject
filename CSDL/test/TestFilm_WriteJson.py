from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Film import Film

films=[]
films.append(Film("F1","Anyone but you","Tình cảm",103,
                  "Phụ đề tiếng Việt","25/03/2024","18","9:30",5))
films.append(Film("F2", "John Wick 4", "Hành động", 169,
                  "Lồng tiếng", "24/03/2024", "18+", "20:00", 10))
films.append(Film("F3", "The Marvels", "Siêu anh hùng", 130,
                  "Phụ đề tiếng Việt", "22/03/2024", "PG-13", "17:30", 8))
films.append(Film("F4", "Oppenheimer", "Chính kịch", 180,
                  "Phụ đề tiếng Việt", "21/03/2024", "R", "19:00", 12))
films.append(Film("F5", "Inside Out 2", "Hoạt hình", 100,
                  "Lồng tiếng", "26/03/2024", "PG", "14:00", 15))
films.append(Film("F6", "Dune: Part Two", "Khoa học viễn tưởng", 166,
                  "Phụ đề tiếng Việt", "27/03/2024", "PG-13", "21:00", 7))
films.append(Film("F7", "Avatar: The Way of Water", "Khoa học viễn tưởng", 192,
                  "Phụ đề tiếng Việt", "28/03/2024", "PG-13", "18:30", 9))
films.append(Film("F8", "Spider-Man: No Way Home", "Siêu anh hùng", 148,
                  "Lồng tiếng", "29/03/2024", "PG-13", "20:00", 6))
films.append(Film("F9", "The Conjuring: The Devil Made Me Do It", "Kinh dị", 112,
                  "Phụ đề tiếng Việt", "30/03/2024", "R", "22:00", 5))
films.append(Film("F10", "Fast X", "Hành động", 141,
                  "Lồng tiếng", "31/03/2024", "PG-13", "16:00", 10))
print ("Danh sách phim:")
for film in films:
    print(film)
jff=JsonFileFactory()
filename="../dataset/film.json"
jff.write_data(films,filename)