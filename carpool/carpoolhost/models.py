from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Member(models.Model):
    #등록가능한 멤버리스트를 관리한다
    #field

    membernumber=models.PositiveIntegerField(help_text='사번',primary_key=True)
    membername=models.CharField(max_length=10,help_text='이름')
    register_tf=models.BooleanField(help_text='등록여부')

    class Meta:
        ordering = ['membername']

    def __str__(self):
        """String for representing the Model object."""
        return self.membername

class RegMember(models.Model):
    #field
    #등록한 멤버리스트를 관리한다.
    membernumber=models.OneToOneField(Member,on_delete=models.CASCADE,null=True )
    memberemail=models.EmailField(help_text='비밀번호 찾기용 이메일')
    memberpw=models.CharField(max_length=50)
    datetime_of_reg=models.DateTimeField(auto_now_add=True)
    datetime_of_update=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['membernumber']

    def __str__(self):
        """String for representing the Model object."""
        return self.memberemail

class Host(models.Model):
    #field
    hostnumber=models.AutoField(primary_key=True)
    host=models.ForeignKey(Member,on_delete=models.SET_NULL, null=True)
    date_of_host=models.DateField(default=timezone.now,help_text='탑승일자')
    HOURS_STATUS=(
        ('17','오후 5시'),
        ('18','오후 6시'),
        ('19', '오후 7시'),
        ('20', '오후 8시'),
        ('21', '오후 9시'),
        ('22', '오후 10시'),
        ('23', '오후 11시'),
        ('24', '자정'),
        ('01', '새벽 1시'),
    )
    MINUTES_STATUS=(
        ('00', '정각'),
        ('15', '15분'),
        ('30','30분'),
        ('45','45분'),
    )
    hour_of_host=models.CharField(max_length=2,choices=HOURS_STATUS,default='06',help_text='탑승 시각')
    minutes_of_host=models.CharField(max_length=2,choices=MINUTES_STATUS,default='00',help_text='탑승 분')
    ending_tf=models.BooleanField(default=False,help_text='Host 종료여부')
    how_many_guest=models.PositiveSmallIntegerField(
        help_text='탑승인원',
        default=3,
        validators=[MaxValueValidator(10),
                    MinValueValidator(1)]
    )
    datetime_of_reg = models.DateTimeField(auto_now_add=True)
    datetime_of_update = models.DateTimeField(auto_now=True)
    where_to_go = models.CharField(max_length=40,help_text='목적지',blank=True)
    car_num = models.CharField(max_length=10,help_text='차량번호',blank=True)

class Client(models.Model):
    clientnumber=models.AutoField(primary_key=True,help_text='탑승신청 고유번호')
    hostnumber=models.ForeignKey(Host,on_delete=models.SET_NULL,help_text='호스트 고유번호',null=True)
    clientmembernumber=models.ForeignKey(Member,on_delete=models.SET_NULL,help_text='탑승자 사번',null=True)
    datetime_of_reg=models.DateTimeField(auto_now_add=True)
    datetime_of_update=models.DateTimeField(auto_now=True)