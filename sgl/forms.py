from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    regionid = SelectField(
        '縣市',
        choices=[
            ('1', '台北市'),
            ('2', '基隆市'),
            ('3', '新北市'),
            ('4', '新竹市'),
            ('5', '新竹縣'),
            ('6', '桃園市'),
            ('7', '苗栗縣'),
            ('8', '台中市'),
            ('10', '彰化縣'),
            ('11', '南投縣'),
            ('12', '嘉義市'),
            ('13', '嘉義縣'),
            ('14', '雲林縣'),
            ('15', '台南市'),
            ('17', '高雄市'),
            ('19', '屏東縣'),
            ('21', '宜蘭縣'),
            ('22', '台東縣'),
            ('23', '花蓮縣'),
            ('24', '澎湖縣'),
            ('25', '金門縣'),
            ('26', '連江縣'),
        ],
        validators=[DataRequired()],
    )

    # TODO
    # sections = SelectMultipleField(
    #     '鄉鎮',
    #     choices=[(None, '請選擇')],
    #     validators=[DataRequired()],
    # )

    kind = SelectField(
        '類型',
        choices=[
            ('0', '不限'),
            ('1', '整層住家'),
            ('2', '獨立套房'),
            ('3', '分租套房'),
            ('4', '雅房'),
            ('24', '其他'),
        ],
        validators=[DataRequired()],
    )

    rentprice_min = IntegerField(
        '最低租金',
        default=0,
        validators=[DataRequired()],
    )

    rentprice_max = IntegerField(
        '最高租金',
        default=0,
        validators=[DataRequired()],
    )

    area_min = IntegerField(
        '最低坪數',
        default=0,
        validators=[DataRequired()],
    )

    area_max = IntegerField(
        '最高坪數',
        default=0,
        validators=[DataRequired()],
    )
