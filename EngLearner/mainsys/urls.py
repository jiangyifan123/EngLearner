from django.urls import path, include
from .views import *

urlpatterns = [
	path(r'', lessonView.as_view(), name = "lesson_index"),
	path(r'read/', readView.as_view(), name = "read"),
	path(r'listen/', listenView.as_view(), name = "listen"),
	path(r'words/', wordsView.as_view(), name = "words"),
	path(r'write/', writeView.as_view(), name = "write"),
	path(r'add_words/', words_View.as_view(), name = "add_words"),
	path(r'set_words/', set_words_View.as_view(), name = "set_words"),
	path(r'word_index/', word_indexView.as_view(), name = "word_index"),
	path(r'test/', test_View.as_view(), name = "test"),
	path(r'upload_pos/', upload_pos, name = "upload_pos"),
	path(r'write_detail/', write_detailView.as_view(), name = "write_detail"),
	path(r'write_add/', write_addView.as_view(), name = "write_add"),
	path(r'save_write/', save_write, name = "save_write"),
	path(r'update_read/', update_read_books, name = "update_read"),
	path(r'read_detail/', read_detailView.as_view(), name = "read_detail"),
	path(r'listen_detail/', listen_detail, name = "listen_detail"),
	# path(r'update_listen/', get_listen_data, name = "update_listen"),
]
