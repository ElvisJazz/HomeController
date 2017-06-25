# -*- coding: utf-8 -*-
from genericpath import isdir
import os
from os.path import isfile, join

__author__ = 'ElvisJia'


class MusicLoader(object):

	@staticmethod
	def load_music_lists(music_path):
		music_list_dir = os.listdir(music_path)
		return [MusicLoader.list_all_files(join(music_path, music_list)) for music_list in music_list_dir if isdir(join(music_path, music_list))]

	@staticmethod
	def list_all_files(path):
		return [join(path, file) for file in os.listdir(path) if isfile(join(path, file))]

