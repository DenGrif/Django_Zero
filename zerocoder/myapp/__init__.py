# # <a href="new">Ссылка на NEW</a>
# Урок номер 2 по изучению фреймворка django и <a href="new">Ссылка на NEW</a>
# <style>
#         body {
#             font-family: Arial, sans-serif;
#             background-color: blue;
#         }
#         aside {
#             padding: 20px;
#             background-color: #fff;
#             box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
#             border-radius: 5px;
#             margin-bottom: 30px;
#         }
#         img {
#             display: block;
#             max-width: 100%;
#             height: auto;
#             margin-bottom: 15px;
#         }
#         span {
#             display: block;
#             text-align: center;
#             font-size: 24px;
#             font-weight: bold;
#             color: #333;
#             margin-bottom: 25px;
#         }
#         ul {
#             list-style-type: none;
#             padding-left: 0;
#             margin-bottom: 0;
#         }
#         li a {
#             display: block;
#             padding: 10px 0;
#             text-decoration: none;
#             color: #007bff;
#             transition: color 0.3s ease;
#         }
#         li a:hover {
#             color: #0056b3;
#         }
#         main {
#             padding: 20px;
#             background-color: #fff;
#             box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
#             border-radius: 5px;
#         }
# </style>

# <span>CatDjango</span>
# <Ul>
#     <li><a href="/">Главная</a></Li>
#     <li><a href="new">Второстепенная</a></Li>
# </ul>

# {% extends 'main/layoute.html' %}
#
# {% block title %}
#     <title>Как начать работать с CatDjango</title>
# {% endblock %}
#
# {% block content %}
# <div class="container">
#     <h1 class="text-center mb-4">Как начать работать с CatDjango</h1>
#
#     <div class="row">
#         <div class="col-md-6">
#             <h3>1. Создайте аккаунт</h3>
#             <p>
#                 Присоединяйтесь к CatDjango, зарегистрировав аккаунт. Это позволит вам сохранять любимые материалы, добавлять комментарии и делиться фотографиями своих кошек с другими пользователями.
#             </p>
#         </div>
#         <div class="col-md-6">
#             <img src="{% static 'main/img/cat_signup.jpg' %}" class="img-fluid rounded" alt="Регистрация на CatDjango">
#         </div>
#     </div>
#
#     <hr class="my-4">
#
#     <div class="row">
#         <div class="col-md-6 order-md-2">
#             <h3>2. Исследуйте контент</h3>
#             <p>
#                 Вдохновляйтесь статьями, советами по разработке Django и разделом, посвящённым уходу за кошками. Наши авторы регулярно добавляют новые материалы для пользователей всех уровней.
#             </p>
#         </div>
#         <div class="col-md-6 order-md-1">
#             <img src="{% static 'main/img/cat_content.jpg' %}" class="img-fluid rounded" alt="Контент CatDjango">
#         </div>
#     </div>
#
#     <hr class="my-4">
#
#     <div class="row">
#         <div class="col-md-6">
#             <h3>3. Делитесь своими находками</h3>
#             <p>
#                 Поделитесь своими проектами на Django, опытом разработки или фотографиями своих питомцев. Мы ценим вклад каждого пользователя!
#             </p>
#         </div>
#         <div class="col-md-6">
#             <img src="{% static 'main/img/cat_share.jpg' %}" class="img-fluid rounded" alt="Делитесь с CatDjango">
#         </div>
#     </div>
#
#     <hr class="my-4">
#
#     <div class="text-center">
#         <h4>Присоединяйтесь к CatDjango и сделайте первый шаг в мир, где кошки и код живут в гармонии!</h4>
#     </div>
# </div>
# {% endblock %}

# < h4 > < / h4 >
# < h5 > < / h5 >
# < p > {{new.text}} < / p >
# < p > Автор: {{new.author.username}} < / p >
# < p > Опубликовано: {{new.pub_date}} < / p >
# < hr >
# ------------------------
# <label for="newsTitle" class="form-label">Заголовок новости</label>
#                     <input type="text" id="newsTitle" name="title" class="form-control" placeholder="Введите заголовок" required>
#
# <label for="newsDescription" class="form-label">Краткое описание новости</label>
#                     <input type="text" id="newsDescription" name="short_description" class="form-control" placeholder="Введите краткое описание" required>
#
# <label for="newsContent" class="form-label">Содержание новости</label>
#                     <textarea id="newsContent" name="content" class="form-control" rows="5" placeholder="Введите текст новости" required></textarea>
#
# <label for="newsDate" class="form-label">Дата публикации</label>
#                     <input type="date" id="newsDate" name="pub_date" class="form-control" required>
#
# <div class="mb-3">
#                     <label for="newsTime" class="form-label">Время публикации</label>
#                     <input type="time" id="newsTime" name="pub_time" class="form-control" required>
#                 </div>
