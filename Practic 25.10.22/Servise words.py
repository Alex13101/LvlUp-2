"""Перед публикацией текста или документа обычно
принято удалять или изменять в них служебную информацию.
 В данном упражнении вам необходимо написать программу,
 которая будет заменять все служебные слова в тексте на
 символы звездочек (по количеству символов в словах).
 Вы должны осуществлять регистрозависимый поиск служебных
 слов в тексте, даже если эти слова входят в состав других слов.
  Список служебных слов должен храниться в отдельном файле.
  Сохраните отредактированную версию исходного файла в новом
  файле. Имена исходного файла, файла со служебными словами
   и нового файла должны быть введены пользователем."""

#  считываем все служебные слова
# service
servisce_words = []
with open("Service_wordses.txt", encoding="utf8") as f:
    for l in f.readlines():
        servisce_words.append((l.replace("password", "")))
print(servisce_words)

# заменять слова на звездочки

text = []
with open("Service_wordses.txt", encoding="utf8") as f:
    for l in f.readlines():
        for word in servisce_words:
            l=l.replace(word, "*" * len(word))
        text.append(l)
print(text)
# Записываем текс в исходный файл
with open ("coded_text.txt", encoding="utf8", mode="w") as f:
    for line in text:
        f.write(line)