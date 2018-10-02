from izi.core.loading import get_model

from izi_accounts import names

Account = get_model('izi_accounts', 'Account')


def redemptions_account():
    return Account.objects.get(name=names.REDEMPTIONS)


def lapsed_account():
    return Account.objects.get(name=names.LAPSED)
