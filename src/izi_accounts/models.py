from izi.core.loading import is_model_registered

from izi_accounts import abstract_models

if not is_model_registered('izi_accounts', 'AccountType'):
    class AccountType(abstract_models.AccountType):
        pass


if not is_model_registered('izi_accounts', 'Account'):
    class Account(abstract_models.Account):
        pass


if not is_model_registered('izi_accounts', 'Transfer'):
    class Transfer(abstract_models.Transfer):
        pass


if not is_model_registered('izi_accounts', 'Transaction'):
    class Transaction(abstract_models.Transaction):
        pass


if not is_model_registered('izi_accounts', 'IPAddressRecord'):
    class IPAddressRecord(abstract_models.IPAddressRecord):
        pass
