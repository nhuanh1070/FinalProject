from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Film import Film

films = []
films.append(Film("F1", "anyone but you", "Tình cảm", 103, "Mỹ", "Will Gluck",
                  "Hai người xa lạ bị cuốn vào một tình huống trớ trêu và buộc phải giả làm một cặp đôi. Ban đầu, cả hai chỉ lợi dụng nhau để đạt được mục đích cá nhân, nhưng dần dần họ nhận ra sự gắn kết không ngờ tới. Những tình huống hài hước, lãng mạn và hiểu lầm liên tục xảy ra, tạo nên câu chuyện hấp dẫn. Bộ phim mang đến không khí tươi sáng, nhẹ nhàng với những khoảnh khắc đáng nhớ. Liệu tình yêu giả có thể trở thành thật hay không?",
                  "Phụ đề tiếng Việt", "25/03/2024", "18", "9:30", 5,"anyone_but_you.jpg"))

films.append(Film("F2", "john wick 4", "Hành động", 169, "Mỹ", "Chad Stahelski",
                  "John Wick tiếp tục bị thế giới sát thủ truy đuổi và lần này, kẻ thù của anh mạnh mẽ hơn bao giờ hết. Anh phải tìm kiếm đồng minh và lập kế hoạch để đối đầu với những tổ chức quyền lực. Những pha hành động mãn nhãn, các trận đấu căng thẳng và những âm mưu đen tối khiến bộ phim đầy cuốn hút. Sự pha trộn giữa bạo lực, chiến thuật và cảm xúc giúp John Wick 4 trở thành phần phim không thể bỏ lỡ. Liệu anh có thể giành lại tự do hay bị cuốn mãi vào vòng xoáy bạo lực?",
                  "Lồng tiếng", "24/03/2024", "18+", "20:00", 10,"JohnWick.jpg"))

films.append(Film("F3", "the marvels", "Siêu anh hùng", 130, "Mỹ", "Nia DaCosta",
                  "Captain Marvel, Ms. Marvel và Monica Rambeau bất ngờ bị liên kết với nhau khi sử dụng sức mạnh, buộc họ phải hợp tác để ngăn chặn mối đe dọa vũ trụ. Sự kết hợp giữa ba nữ siêu anh hùng mang đến những pha hành động mãn nhãn và nhiều tình huống hài hước. Bộ phim không chỉ nói về sức mạnh mà còn tập trung vào tình bạn, gia đình và sự trưởng thành. Các nhân vật phải vượt qua thử thách cá nhân để phối hợp ăn ý trong trận chiến. Với hình ảnh đẹp mắt và nội dung hấp dẫn, đây là một trong những bom tấn siêu anh hùng đáng mong đợi.",
                  "Phụ đề tiếng Việt", "22/03/2024", "PG-13", "17:30", 8,"TheMarvels.jpg"))

films.append(Film("F4", "oppenheimer", "Chính kịch", 180, "Mỹ", "Christopher Nolan",
                  "Bộ phim khắc họa cuộc đời của J. Robert Oppenheimer, người đứng sau Dự án Manhattan, nơi phát triển bom nguyên tử. Thành công của ông đã thay đổi hoàn toàn lịch sử chiến tranh, nhưng cũng khiến ông rơi vào sự dằn vặt và đấu tranh nội tâm. Bộ phim mang đến những góc nhìn sâu sắc về trách nhiệm của khoa học và đạo đức trong chiến tranh. Cách kể chuyện của Christopher Nolan khiến người xem bị cuốn hút vào những xung đột chính trị và tâm lý của nhân vật. Oppenheimer không chỉ là một bộ phim tiểu sử mà còn là một tác phẩm điện ảnh đầy tính triết lý.",
                  "Phụ đề tiếng Việt", "21/03/2024", "R", "19:00", 12,"oppenheimer.jpg"))

films.append(Film("F5", "inside out 2", "Hoạt hình", 100, "Mỹ", "Kelsey Mann",
                  "Riley giờ đã lớn và bắt đầu bước vào tuổi dậy thì, mang theo nhiều cảm xúc mới đầy phức tạp. Những cảm xúc quen thuộc như Vui Vẻ, Buồn Bã, Giận Dữ phải học cách chung sống với những cảm xúc mới như Lo Lắng, Xấu Hổ. Sự hỗn loạn trong tâm trí Riley khiến cô gặp nhiều thử thách trong cuộc sống hàng ngày. Bộ phim tiếp tục khai thác thế giới nội tâm một cách sáng tạo và giàu cảm xúc. Đây không chỉ là câu chuyện dành cho trẻ em mà còn chứa đựng nhiều thông điệp ý nghĩa về tâm lý con người.",
                  "Lồng tiếng", "26/03/2024", "PG", "14:00", 15,"inside_out_two.jpg"))

films.append(Film("F6", "dune: part two", "Khoa học viễn tưởng", 166, "Mỹ", "Denis Villeneuve",
                  "Paul Atreides tiếp tục hành trình của mình để giành lại công lý cho gia đình và bảo vệ hành tinh Arrakis. Khi gia nhập tộc người Fremen, anh phải đối mặt với những thách thức khắc nghiệt của sa mạc và những kẻ thù mạnh mẽ. Tình yêu, lòng trung thành và trách nhiệm trở thành những yếu tố quan trọng trong cuộc chiến này. Bộ phim mang đến những cảnh quay hoành tráng, kết hợp với âm nhạc và hình ảnh mãn nhãn. Đây là phần phim đầy hấp dẫn, tiếp tục mở rộng thế giới Dune kỳ vĩ.",
                  "Phụ đề tiếng Việt", "27/03/2024", "PG-13", "21:00", 7,"Dune.jpg"))

films.append(Film("F7", "avatar: the way of water", "Khoa học viễn tưởng", 192, "Mỹ", "James Cameron",
                  "Jake Sully và gia đình anh phải rời bỏ quê hương và tìm đến một bộ tộc sống dưới nước. Họ học cách sinh tồn và thích nghi với môi trường mới, nhưng nguy hiểm vẫn luôn rình rập. Kẻ thù cũ của họ quay trở lại với những âm mưu tàn bạo hơn. Phim mang đến hình ảnh mãn nhãn về thế giới Pandora với kỹ xảo tiên tiến. Đây là một cuộc phiêu lưu đầy cảm xúc về gia đình, lòng trung thành và bảo vệ thiên nhiên.",
                  "Phụ đề tiếng Việt", "28/03/2024", "PG-13", "18:30", 9,"Avatar.jpg"))

films.append(Film("F8", "spider-man: no way home", "Siêu anh hùng", 148, "Mỹ", "Jon Watts",
                  "Peter Parker vô tình mở ra cánh cổng đa vũ trụ khi nhờ Doctor Strange giúp đỡ. Điều này dẫn đến sự xuất hiện của các phản diện từ những vũ trụ khác nhau. Cậu buộc phải chiến đấu để bảo vệ thế giới, đồng thời học cách chấp nhận hậu quả của quyết định mình. Bộ phim mang đến sự kết hợp giữa hành động, hài hước và những khoảnh khắc xúc động. Cao trào của phim là sự hội tụ của nhiều phiên bản Spider-Man, làm hài lòng người hâm mộ.",
                  "Lồng tiếng", "29/03/2024", "PG-13", "20:00", 6,"Spiderman.jpg"))

films.append(Film("F9", "the conjuring: The Devil Made Me Do It", "Kinh dị", 112, "Mỹ", "Michael Chaves",
                  "Ed và Lorraine Warren điều tra một vụ án giết người liên quan đến hiện tượng quỷ ám đáng sợ. Lần đầu tiên trong lịch sử, một kẻ sát nhân tuyên bố rằng hắn bị quỷ điều khiển để gây án. Những hiện tượng siêu nhiên ngày càng ám ảnh và nguy hiểm hơn bao giờ hết. Bộ phim mang đến những pha hù dọa căng thẳng cùng bầu không khí rùng rợn đặc trưng. Đây là một trong những phần đáng sợ nhất của vũ trụ Conjuring, khiến khán giả thót tim đến giây cuối cùng.",
                  "Phụ đề tiếng Việt", "30/03/2024", "R", "22:00", 5,"TheConjuring.jpg"))

films.append(Film("F10", "fast x", "Hành động", 141, "Mỹ", "Louis Leterrier",
                  "Dominic Toretto và gia đình của anh phải đối mặt với một kẻ thù mới từ quá khứ, kẻ mang trong mình mối hận thù sâu sắc. Những cuộc rượt đuổi tốc độ cao, các vụ nổ hoành tráng và những pha hành động mạo hiểm tiếp tục đẩy loạt phim Fast & Furious lên một tầm cao mới. Bộ phim không chỉ mang đến những pha hành động mãn nhãn mà còn khai thác sâu hơn về tình cảm gia đình và sự trung thành. Những nhân vật cũ trở lại và nhiều bí ẩn mới được tiết lộ, làm tăng thêm kịch tính cho phần phim này. Fast X là một phần quan trọng trong loạt phim, hứa hẹn sẽ mở ra những hướng đi mới đầy bất ngờ.",
                  "Lồng tiếng", "31/03/2024", "PG-13", "16:00", 10,"FastX.jpg"))

print ("Danh sách phim:")
for film in films:
    print(film)
jff=JsonFileFactory()
filename= "../../dataset/film.json"
jff.write_data(films,filename)