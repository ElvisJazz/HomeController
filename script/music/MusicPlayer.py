# -*- coding: utf-8 -*-
import os
from music.MusicLoader import MusicLoader

__author__ = 'ElvisJia'


class MusicPlayer(object):
	music_path = '/home/pi/Music'

	def __init__(self):
		self._music_lists = self.load_music_list()
		self._cur_music_index = 0
		self._cur_music_list_index = 0
		self._cur_music_list = None
		self._cur_music = None
		self._volume_delta = 5

	@staticmethod
	def load_music_list():
		return MusicLoader.load_music_lists(MusicPlayer.music_path)

	@property
	def music_lists(self):
		if not self._music_lists:
			self._music_lists = self.load_music_list()
		return self._music_lists

	def sel_music_list(self, index):
		if index >= len(self.music_lists):
			raise RuntimeError('Wrong index of music lists!')

		self._cur_music_index = index
		self._cur_music_list = self.music_lists[index]

	def play_music(self):
		if self._cur_music_list is None:
			self._cur_music_list = self.music_lists[self._cur_music_index]

		music_url = self._cur_music_list[self._cur_music_index]
		os.system('mocp')
		os.system('mocp -p %s' % music_url)

	def next_music(self):
		self._cur_music_index = (self._cur_music_index + 1) % len(self._cur_music_list)
		self.play_music()

	def pre_music(self):
		self._cur_music_index = (self._cur_music_index - 1) % len(self._cur_music_list)
		self.play_music()

	def pause_music(self):
		os.system('mocp -P')

	def resume_music(self):
		os.system('mocp -U')

	def stop_music(self):
		os.system('mocp -s')

	def volume_up(self):
		os.system('mocp -v %d' % self._volume_delta)

	def volume_down(self):
		os.system('mocp -v %d' % -self._volume_delta)
