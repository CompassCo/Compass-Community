from django.db import models

class Fcuser(models.Model):
	username = models.CharField(max_length=64, verbose_name='사용자')
	password = models.CharField(max_length=64, verbose_name='비밀번호')

	# 관리자 페이지 첫 화면에 보여지는 유저명
	def __str__(self):
		return self.username

	class Meta:
		db_table = 'fastcampus_fcuser'
		verbose_name = '패스트캠퍼스 사용자'
		verbose_name_plural = '패스트캠퍼스 사용자'
	
