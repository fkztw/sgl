from flask_wtf import FlaskForm
from wtforms import fields, widgets
from wtforms.validators import DataRequired


class MultiCheckboxField(fields.SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class QueryForm(FlaskForm):
    is_new_list = fields.SelectField(
        '最新刊登',
        default='1',
        choices=[
            ('0', '否'),
            ('1', '是'),
        ],
        validators=[DataRequired()],
    )
    regionid = fields.SelectField(
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

    kind = fields.SelectField(
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

    rentprice_min = fields.IntegerField(
        '最低租金',
        default=0,
        validators=[DataRequired()],
    )
    rentprice_max = fields.IntegerField(
        '最高租金',
        default='',
    )

    patternMore = fields.SelectMultipleField(
        '格局',
        default='0',
        choices=[
            ('0', '不限'),
            ('1', '1 房'),
            ('2', '2 房'),
            ('3', '3 房'),
            ('4', '4 房'),
            ('5', '5 房以上'),
        ],
    )

    area_min = fields.IntegerField(
        '最低坪數',
        default=0,
        validators=[DataRequired()],
    )
    area_max = fields.IntegerField(
        '最高坪數',
        default='',
    )

    shape = fields.SelectMultipleField(
        '房屋型態',
        default='0',
        choices=[
            ('0', '不限'),
            ('1', '公寓'),
            ('2', '電梯大樓'),
            ('3', '透天厝'),
            ('4', '別墅'),
        ],
    )

    floor_min = fields.IntegerField(
        '最低樓層',
        default=0,
        validators=[DataRequired()],
    )
    floor_max = fields.IntegerField(
        '最高樓層',
        default=0,
        validators=[DataRequired()],
    )

    sex = fields.SelectField(
        '性別',
        choices=[
            ('0', '不限'),
            ('1', '男'),
            ('2', '女'),
        ],
        validators=[DataRequired()],
    )

    option = MultiCheckboxField(
        '提供設備',
        default=[],
        choices=[
            ('tv', '電視'),
            ('cold', '冷氣'),
            ('icebox', '冰箱'),
            ('hotwater', '熱水器'),
            ('naturalgas', '天然瓦斯'),
            ('four', '第四台'),
            ('broadband', '網路'),
            ('washer', '洗衣機'),
            ('bed', '床'),
            ('wardrobe', '衣櫃'),
            ('sofa', '沙發'),
        ],
    )

    other = MultiCheckboxField(
        '其他條件',
        default=[],
        choices=[
            ('cartplace', '有車位'),
            ('lift', '有電梯'),
            ('balcony_1', '有陽台'),
            ('cook', '可開伙'),
            ('pet', '可養寵物'),
            ('tragoods', '近捷運'),
            ('lease', '可短期租賃'),
        ],
    )

    hasimg = fields.SelectField(
        '是否有房屋圖片',
        choices=[
            ('0', '不限'),
            ('1', '是'),
        ],
    )

    not_cover = fields.SelectField(
        '是否排除頂樓加蓋',
        choices=[
            ('0', '不限'),
            ('1', '是'),
        ],
    )

    role = fields.SelectField(
        '是否限定屋主刊登',
        choices=[
            ('0', '不限'),
            ('1', '是'),
        ],
    )

    submit = fields.SubmitField('查詢')
