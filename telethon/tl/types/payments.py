"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
import os
import struct


class PaymentForm(TLObject):
    CONSTRUCTOR_ID = 0x3f56aea3
    SUBCLASS_OF_ID = 0xa0483f19

    def __init__(self, bot_id, invoice, provider_id, url, users, can_save_credentials=None, password_missing=None, native_provider=None, native_params=None, saved_info=None, saved_credentials=None):
        """
        :param bool | None can_save_credentials:
        :param bool | None password_missing:
        :param int bot_id:
        :param Invoice invoice:
        :param int provider_id:
        :param str url:
        :param str | None native_provider:
        :param DataJSON | None native_params:
        :param PaymentRequestedInfo | None saved_info:
        :param PaymentSavedCredentials | None saved_credentials:
        :param list[User] users:

        Constructor for payments.PaymentForm: Instance of PaymentForm.
        """
        super().__init__()

        self.can_save_credentials = can_save_credentials
        self.password_missing = password_missing
        self.bot_id = bot_id
        self.invoice = invoice
        self.provider_id = provider_id
        self.url = url
        self.native_provider = native_provider
        self.native_params = native_params
        self.saved_info = saved_info
        self.saved_credentials = saved_credentials
        self.users = users

    def to_dict(self):
        return {
            '_': 'PaymentForm',
            'can_save_credentials': self.can_save_credentials,
            'password_missing': self.password_missing,
            'bot_id': self.bot_id,
            'invoice': None if self.invoice is None else self.invoice.to_dict(),
            'provider_id': self.provider_id,
            'url': self.url,
            'native_provider': self.native_provider,
            'native_params': None if self.native_params is None else self.native_params.to_dict(),
            'saved_info': None if self.saved_info is None else self.saved_info.to_dict(),
            'saved_credentials': None if self.saved_credentials is None else self.saved_credentials.to_dict(),
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users]
        }

    def __bytes__(self):
        assert ((self.native_provider or self.native_provider is not None) and (self.native_params or self.native_params is not None)) or ((self.native_provider is None or self.native_provider is False) and (self.native_params is None or self.native_params is False)), 'native_provider, native_params parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'\xa3\xaeV?',
            struct.pack('<I', (0 if self.can_save_credentials is None or self.can_save_credentials is False else 4) | (0 if self.password_missing is None or self.password_missing is False else 8) | (0 if self.native_provider is None or self.native_provider is False else 16) | (0 if self.native_params is None or self.native_params is False else 16) | (0 if self.saved_info is None or self.saved_info is False else 1) | (0 if self.saved_credentials is None or self.saved_credentials is False else 2)),
            struct.pack('<i', self.bot_id),
            bytes(self.invoice),
            struct.pack('<i', self.provider_id),
            TLObject.serialize_bytes(self.url),
            b'' if self.native_provider is None or self.native_provider is False else (TLObject.serialize_bytes(self.native_provider)),
            b'' if self.native_params is None or self.native_params is False else (bytes(self.native_params)),
            b'' if self.saved_info is None or self.saved_info is False else (bytes(self.saved_info)),
            b'' if self.saved_credentials is None or self.saved_credentials is False else (bytes(self.saved_credentials)),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(bytes(x) for x in self.users),
        ))

    @staticmethod
    def from_reader(reader):
        flags = reader.read_int()

        _can_save_credentials = bool(flags & 4)
        _password_missing = bool(flags & 8)
        _bot_id = reader.read_int()
        _invoice = reader.tgread_object()
        _provider_id = reader.read_int()
        _url = reader.tgread_string()
        if flags & 16:
            _native_provider = reader.tgread_string()
        else:
            _native_provider = None
        if flags & 16:
            _native_params = reader.tgread_object()
        else:
            _native_params = None
        if flags & 1:
            _saved_info = reader.tgread_object()
        else:
            _saved_info = None
        if flags & 2:
            _saved_credentials = reader.tgread_object()
        else:
            _saved_credentials = None
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return PaymentForm(bot_id=_bot_id, invoice=_invoice, provider_id=_provider_id, url=_url, users=_users, can_save_credentials=_can_save_credentials, password_missing=_password_missing, native_provider=_native_provider, native_params=_native_params, saved_info=_saved_info, saved_credentials=_saved_credentials)


class PaymentReceipt(TLObject):
    CONSTRUCTOR_ID = 0x500911e1
    SUBCLASS_OF_ID = 0x590093c9

    def __init__(self, date, bot_id, invoice, provider_id, currency, total_amount, credentials_title, users, info=None, shipping=None):
        """
        :param datetime.datetime | None date:
        :param int bot_id:
        :param Invoice invoice:
        :param int provider_id:
        :param PaymentRequestedInfo | None info:
        :param ShippingOption | None shipping:
        :param str currency:
        :param int total_amount:
        :param str credentials_title:
        :param list[User] users:

        Constructor for payments.PaymentReceipt: Instance of PaymentReceipt.
        """
        super().__init__()

        self.date = date
        self.bot_id = bot_id
        self.invoice = invoice
        self.provider_id = provider_id
        self.info = info
        self.shipping = shipping
        self.currency = currency
        self.total_amount = total_amount
        self.credentials_title = credentials_title
        self.users = users

    def to_dict(self):
        return {
            '_': 'PaymentReceipt',
            'date': self.date,
            'bot_id': self.bot_id,
            'invoice': None if self.invoice is None else self.invoice.to_dict(),
            'provider_id': self.provider_id,
            'info': None if self.info is None else self.info.to_dict(),
            'shipping': None if self.shipping is None else self.shipping.to_dict(),
            'currency': self.currency,
            'total_amount': self.total_amount,
            'credentials_title': self.credentials_title,
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users]
        }

    def __bytes__(self):
        return b''.join((
            b'\xe1\x11\tP',
            struct.pack('<I', (0 if self.info is None or self.info is False else 1) | (0 if self.shipping is None or self.shipping is False else 2)),
            TLObject.serialize_datetime(self.date),
            struct.pack('<i', self.bot_id),
            bytes(self.invoice),
            struct.pack('<i', self.provider_id),
            b'' if self.info is None or self.info is False else (bytes(self.info)),
            b'' if self.shipping is None or self.shipping is False else (bytes(self.shipping)),
            TLObject.serialize_bytes(self.currency),
            struct.pack('<q', self.total_amount),
            TLObject.serialize_bytes(self.credentials_title),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.users)),b''.join(bytes(x) for x in self.users),
        ))

    @staticmethod
    def from_reader(reader):
        flags = reader.read_int()

        _date = reader.tgread_date()
        _bot_id = reader.read_int()
        _invoice = reader.tgread_object()
        _provider_id = reader.read_int()
        if flags & 1:
            _info = reader.tgread_object()
        else:
            _info = None
        if flags & 2:
            _shipping = reader.tgread_object()
        else:
            _shipping = None
        _currency = reader.tgread_string()
        _total_amount = reader.read_long()
        _credentials_title = reader.tgread_string()
        reader.read_int()
        _users = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _users.append(_x)

        return PaymentReceipt(date=_date, bot_id=_bot_id, invoice=_invoice, provider_id=_provider_id, currency=_currency, total_amount=_total_amount, credentials_title=_credentials_title, users=_users, info=_info, shipping=_shipping)


class PaymentResult(TLObject):
    CONSTRUCTOR_ID = 0x4e5f810d
    SUBCLASS_OF_ID = 0x8ae16a9d

    def __init__(self, updates):
        """
        :param Updates updates:

        Constructor for payments.PaymentResult: Instance of either PaymentResult, PaymentVerficationNeeded.
        """
        super().__init__()

        self.updates = updates

    def to_dict(self):
        return {
            '_': 'PaymentResult',
            'updates': None if self.updates is None else self.updates.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\r\x81_N',
            bytes(self.updates),
        ))

    @staticmethod
    def from_reader(reader):
        _updates = reader.tgread_object()
        return PaymentResult(updates=_updates)


class PaymentVerficationNeeded(TLObject):
    CONSTRUCTOR_ID = 0x6b56b921
    SUBCLASS_OF_ID = 0x8ae16a9d

    def __init__(self, url):
        """
        :param str url:

        Constructor for payments.PaymentResult: Instance of either PaymentResult, PaymentVerficationNeeded.
        """
        super().__init__()

        self.url = url

    def to_dict(self):
        return {
            '_': 'PaymentVerficationNeeded',
            'url': self.url
        }

    def __bytes__(self):
        return b''.join((
            b'!\xb9Vk',
            TLObject.serialize_bytes(self.url),
        ))

    @staticmethod
    def from_reader(reader):
        _url = reader.tgread_string()
        return PaymentVerficationNeeded(url=_url)


class SavedInfo(TLObject):
    CONSTRUCTOR_ID = 0xfb8fe43c
    SUBCLASS_OF_ID = 0xad3cf146

    def __init__(self, has_saved_credentials=None, saved_info=None):
        """
        :param bool | None has_saved_credentials:
        :param PaymentRequestedInfo | None saved_info:

        Constructor for payments.SavedInfo: Instance of SavedInfo.
        """
        super().__init__()

        self.has_saved_credentials = has_saved_credentials
        self.saved_info = saved_info

    def to_dict(self):
        return {
            '_': 'SavedInfo',
            'has_saved_credentials': self.has_saved_credentials,
            'saved_info': None if self.saved_info is None else self.saved_info.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'<\xe4\x8f\xfb',
            struct.pack('<I', (0 if self.has_saved_credentials is None or self.has_saved_credentials is False else 2) | (0 if self.saved_info is None or self.saved_info is False else 1)),
            b'' if self.saved_info is None or self.saved_info is False else (bytes(self.saved_info)),
        ))

    @staticmethod
    def from_reader(reader):
        flags = reader.read_int()

        _has_saved_credentials = bool(flags & 2)
        if flags & 1:
            _saved_info = reader.tgread_object()
        else:
            _saved_info = None
        return SavedInfo(has_saved_credentials=_has_saved_credentials, saved_info=_saved_info)


class ValidatedRequestedInfo(TLObject):
    CONSTRUCTOR_ID = 0xd1451883
    SUBCLASS_OF_ID = 0x8f8044b7

    def __init__(self, id=None, shipping_options=None):
        """
        :param str | None id:
        :param list[ShippingOption] | None shipping_options:

        Constructor for payments.ValidatedRequestedInfo: Instance of ValidatedRequestedInfo.
        """
        super().__init__()

        self.id = id
        self.shipping_options = shipping_options

    def to_dict(self):
        return {
            '_': 'ValidatedRequestedInfo',
            'id': self.id,
            'shipping_options': [] if self.shipping_options is None else [None if x is None else x.to_dict() for x in self.shipping_options]
        }

    def __bytes__(self):
        return b''.join((
            b'\x83\x18E\xd1',
            struct.pack('<I', (0 if self.id is None or self.id is False else 1) | (0 if self.shipping_options is None or self.shipping_options is False else 2)),
            b'' if self.id is None or self.id is False else (TLObject.serialize_bytes(self.id)),
            b'' if self.shipping_options is None or self.shipping_options is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.shipping_options)),b''.join(bytes(x) for x in self.shipping_options))),
        ))

    @staticmethod
    def from_reader(reader):
        flags = reader.read_int()

        if flags & 1:
            _id = reader.tgread_string()
        else:
            _id = None
        if flags & 2:
            reader.read_int()
            _shipping_options = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _shipping_options.append(_x)

        else:
            _shipping_options = None
        return ValidatedRequestedInfo(id=_id, shipping_options=_shipping_options)
