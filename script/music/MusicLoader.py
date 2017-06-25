# -*- coding: utf-8 -*-
import os
from os.path import isfile, join

__author__ = 'ElvisJia'


class MusicLoader(object):

	@staticmethod
	def load_music_lists(music_path):
		music_list_dir = os.listdir(music_path)
		return [MusicLoader.list_all_files(music_list) for music_list in music_list_dir]

	@staticmethod
	def list_all_files(path):
		return [join(path, file) for file in path if isfile(join(path, file))]

