from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_realname(realname):
    realname_lst = [
        '강경은','김민성','김수연','김수환','김연준','김영준','김우석','김한솔','남은열','노수지',
        '노용래','노희진','명은호','문희철','박소은','박종선','배성진','원재호','원찬호','이동근',
        '이상현','이재상','이종민','정호제','이진영','이민교',
        ]
    if realname not in realname_lst:
        raise ValidationError(
            _('%(realname)s는(은) SSAFY 7기 서울 1반 소속이 아닙니다.'),
            params={'realname': realname},
        )
