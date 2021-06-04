
import requests
import pandas as pd

url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/jc4xD4IwEAXgn9QHpQXGQg1QUXBAoYtpojFNLDoYB3-91ZgYB9G76ZLv5R7RpCd6NFd7MBd7Gs3xcWu-5UGNEgVUoyoGMW8o7eQ6QMI8GDzIC1FGcQ0gSkJUMitlnC6Aiv-Xx5cR-JXfEP1Jijb3pJFZCuoX7AWmKj7BRIfBl4zfL5KlmkGELAyUoBQrTjpnR-vsbb8jZ9f1sK27A6NCXAk!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/'

r = requests.get(url)

r.text

df = pd.read_html(r.text)