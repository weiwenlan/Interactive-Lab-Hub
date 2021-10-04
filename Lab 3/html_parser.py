import codecs
from bs4 import BeautifulSoup

file = codecs.open("templates/index.html", 'r')
file_string = file.read()
file_html_soup = BeautifulSoup(file_string, 'html.parser')

todo_items_html = file_html_soup.find_all("li", {"class": "to-do-list-item"})
todo_items_list = [x.text for x in todo_items_html]


def construct_to_do_list_speech(list_of_todos):
    intro_phrase = "Good morning! "
    todo_length_phrase = "You have " + str(len(list_of_todos)) + " items on you to-do list today. "
    todo_item_start_phrase = "Here they are: "
    joined_todo_items_phrase = ", ".join(list_of_todos) + ". "
    closing_phrase = "I know you can do it! Have a wonderful day! "

    return intro_phrase + todo_length_phrase + todo_item_start_phrase + joined_todo_items_phrase + closing_phrase


print(construct_to_do_list_speech(todo_items_list))
