# Created at 2024/11/21 下午7:33
from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True, description='主键')
    username = fields.CharField(max_length=32, unique=True, description='用户名')
    nickname = fields.CharField(max_length=32, index=True, description='昵称')
    password = fields.CharField(max_length=128, description='密码')
    openid = fields.CharField(max_length=128, unique=True, description='微信openid')
    avatar = fields.CharField(max_length=256, description='头像')
    status = fields.IntField(default=1, description='状态')
    mobile = fields.CharField(max_length=11, unique=True, description='手机号')
    email = fields.CharField(max_length=64, unique=True, description='邮箱')
    country = fields.CharField(max_length=32, description='国家')
    province = fields.CharField(max_length=32, description='省份')
    city = fields.CharField(max_length=32, description='城市')
    gender = fields.IntField(default=0, description='性别')
    created_at = fields.DatetimeField(auto_now_add=True, description='创建时间')
    updated_at = fields.DatetimeField(auto_now=True, description='更新时间')
    deleted_at = fields.DatetimeField(null=True, description='删除时间')

    class Meta:
        table = 'user_info'
        description = '用户信息'

    def __repr__(self):
        return f'<User {self.username}, ID: {self.id}>'

    __str__ = __repr__

