# -*- coding: utf-8 -*-
import subprocess
from music.MusicLoader import MusicLoader

__author__ = 'ElvisJia'


class MusicPlayer(object):
	music_path = '/home/pi/Music'

	def __init__(self):
		self._music_lists = self.load_music_list()
		self._cur_music_list_index = 0
		self._cur_music_list = None
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

		subprocess.Popen(['mocp'])
		subprocess.Popen(['mocp', '-c'])
		cmd = ['mocp', '-a']
		cmd.extend([music for music in self._cur_music_list])
		subprocess.Popen(cmd)

	def play_music(self):
		subprocess.Popen(['mocp', '-p'])

	def next_music(self):
		subprocess.Popen(['mocp', '-f'])

	def pre_music(self):
		subprocess.Popen(['mocp', '-r'])

	def pause_music(self):
		subprocess.Popen(['mocp', '-P'])

	def resume_music(self):
		subprocess.Popen(['mocp', '-U'])

	def stop_music(self):
		subprocess.Popen(['mocp', '-s'])

	def volume_up(self):
		subprocess.Popen(['mocp', '-v', '%d' % self._volume_delta])

	def volume_down(self):
		subprocess.Popen(['mocp', '-v', '%d' % -self._volume_delta])
