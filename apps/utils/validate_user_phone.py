from apps.models import User
from apps.utils.verification import check, send


def validate_phone(phone, code=None, fake_verification=False):
    if phone.startswith('+'):
        phone = phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        if code is None:
            send(phone, fake_verification)
            return {'success': True, 'password': True, 'phone': phone}
        if code.isdigit() and phone and check(phone, code, fake_verification):
            # if not check(phone, code, fake_verification):
            #     return {'success': False, 'message': "Wrong code"}
            try:
                user = User.objects.get(phone__iexact=phone)
            except User.DoesNotExist:
                return {'success': False, 'message': "User doesn't exist"}
            except User.MultipleObjectsReturned:
                user = User.objects.filter(phone__iexact=phone).first()
            return {'success': True, 'user': user}
        return {'success': False, 'message': "Wrong code"}