"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
import os
import struct


class BlockRequest(TLObject):
    CONSTRUCTOR_ID = 0x332b49fc
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, id):
        """
        :param InputUser id:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.id = id

    def resolve(self, client, utils):
        self.id = utils.get_input_user(client.get_input_entity(self.id))

    def to_dict(self):
        return {
            '_': 'BlockRequest',
            'id': None if self.id is None else self.id.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\xfcI+3',
            bytes(self.id),
        ))

    @staticmethod
    def from_reader(reader):
        _id = reader.tgread_object()
        return BlockRequest(id=_id)


class DeleteContactRequest(TLObject):
    CONSTRUCTOR_ID = 0x8e953744
    SUBCLASS_OF_ID = 0x524d5ae9

    def __init__(self, id):
        """
        :param InputUser id:

        :returns contacts.Link: Instance of Link.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.id = id

    def resolve(self, client, utils):
        self.id = utils.get_input_user(client.get_input_entity(self.id))

    def to_dict(self):
        return {
            '_': 'DeleteContactRequest',
            'id': None if self.id is None else self.id.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'D7\x95\x8e',
            bytes(self.id),
        ))

    @staticmethod
    def from_reader(reader):
        _id = reader.tgread_object()
        return DeleteContactRequest(id=_id)


class DeleteContactsRequest(TLObject):
    CONSTRUCTOR_ID = 0x59ab389e
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, id):
        """
        :param list[InputUser] id:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.id = id

    def resolve(self, client, utils):
        self.id = [utils.get_input_user(client.get_input_entity(_x)) for _x in self.id]

    def to_dict(self):
        return {
            '_': 'DeleteContactsRequest',
            'id': [] if self.id is None else [None if x is None else x.to_dict() for x in self.id]
        }

    def __bytes__(self):
        return b''.join((
            b'\x9e8\xabY',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(bytes(x) for x in self.id),
        ))

    @staticmethod
    def from_reader(reader):
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _id.append(_x)

        return DeleteContactsRequest(id=_id)


class ExportCardRequest(TLObject):
    CONSTRUCTOR_ID = 0x84e53737
    SUBCLASS_OF_ID = 0x5026710f

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'ExportCardRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'77\xe5\x84',
        ))

    @staticmethod
    def from_reader(reader):
        return ExportCardRequest()

    def on_response(self, reader):
        reader.read_int()  # Vector ID
        count = reader.read_int()
        self.result = [reader.read_int() for _ in range(count)]


class GetBlockedRequest(TLObject):
    CONSTRUCTOR_ID = 0xf57c350f
    SUBCLASS_OF_ID = 0xffba4f4f

    def __init__(self, offset, limit):
        """
        :param int offset:
        :param int limit:

        :returns contacts.Blocked: Instance of either Blocked, BlockedSlice.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.offset = offset
        self.limit = limit

    def to_dict(self):
        return {
            '_': 'GetBlockedRequest',
            'offset': self.offset,
            'limit': self.limit
        }

    def __bytes__(self):
        return b''.join((
            b'\x0f5|\xf5',
            struct.pack('<i', self.offset),
            struct.pack('<i', self.limit),
        ))

    @staticmethod
    def from_reader(reader):
        _offset = reader.read_int()
        _limit = reader.read_int()
        return GetBlockedRequest(offset=_offset, limit=_limit)


class GetContactsRequest(TLObject):
    CONSTRUCTOR_ID = 0xc023849f
    SUBCLASS_OF_ID = 0x38be25f6

    def __init__(self, hash):
        """
        :param int hash:

        :returns contacts.Contacts: Instance of either ContactsNotModified, Contacts.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetContactsRequest',
            'hash': self.hash
        }

    def __bytes__(self):
        return b''.join((
            b'\x9f\x84#\xc0',
            struct.pack('<i', self.hash),
        ))

    @staticmethod
    def from_reader(reader):
        _hash = reader.read_int()
        return GetContactsRequest(hash=_hash)


class GetStatusesRequest(TLObject):
    CONSTRUCTOR_ID = 0xc4a353ee
    SUBCLASS_OF_ID = 0xdf815c90

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'GetStatusesRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'\xeeS\xa3\xc4',
        ))

    @staticmethod
    def from_reader(reader):
        return GetStatusesRequest()


class GetTopPeersRequest(TLObject):
    CONSTRUCTOR_ID = 0xd4982db5
    SUBCLASS_OF_ID = 0x9ee8bb88

    def __init__(self, offset, limit, hash, correspondents=None, bots_pm=None, bots_inline=None, phone_calls=None, groups=None, channels=None):
        """
        :param bool | None correspondents:
        :param bool | None bots_pm:
        :param bool | None bots_inline:
        :param bool | None phone_calls:
        :param bool | None groups:
        :param bool | None channels:
        :param int offset:
        :param int limit:
        :param int hash:

        :returns contacts.TopPeers: Instance of either TopPeersNotModified, TopPeers.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.correspondents = correspondents
        self.bots_pm = bots_pm
        self.bots_inline = bots_inline
        self.phone_calls = phone_calls
        self.groups = groups
        self.channels = channels
        self.offset = offset
        self.limit = limit
        self.hash = hash

    def to_dict(self):
        return {
            '_': 'GetTopPeersRequest',
            'correspondents': self.correspondents,
            'bots_pm': self.bots_pm,
            'bots_inline': self.bots_inline,
            'phone_calls': self.phone_calls,
            'groups': self.groups,
            'channels': self.channels,
            'offset': self.offset,
            'limit': self.limit,
            'hash': self.hash
        }

    def __bytes__(self):
        return b''.join((
            b'\xb5-\x98\xd4',
            struct.pack('<I', (0 if self.correspondents is None or self.correspondents is False else 1) | (0 if self.bots_pm is None or self.bots_pm is False else 2) | (0 if self.bots_inline is None or self.bots_inline is False else 4) | (0 if self.phone_calls is None or self.phone_calls is False else 8) | (0 if self.groups is None or self.groups is False else 1024) | (0 if self.channels is None or self.channels is False else 32768)),
            struct.pack('<i', self.offset),
            struct.pack('<i', self.limit),
            struct.pack('<i', self.hash),
        ))

    @staticmethod
    def from_reader(reader):
        flags = reader.read_int()

        _correspondents = bool(flags & 1)
        _bots_pm = bool(flags & 2)
        _bots_inline = bool(flags & 4)
        _phone_calls = bool(flags & 8)
        _groups = bool(flags & 1024)
        _channels = bool(flags & 32768)
        _offset = reader.read_int()
        _limit = reader.read_int()
        _hash = reader.read_int()
        return GetTopPeersRequest(offset=_offset, limit=_limit, hash=_hash, correspondents=_correspondents, bots_pm=_bots_pm, bots_inline=_bots_inline, phone_calls=_phone_calls, groups=_groups, channels=_channels)


class ImportCardRequest(TLObject):
    CONSTRUCTOR_ID = 0x4fe196fe
    SUBCLASS_OF_ID = 0x2da17977

    def __init__(self, export_card):
        """
        :param list[int] export_card:

        :returns User: Instance of either UserEmpty, User.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.export_card = export_card

    def to_dict(self):
        return {
            '_': 'ImportCardRequest',
            'export_card': [] if self.export_card is None else self.export_card[:]
        }

    def __bytes__(self):
        return b''.join((
            b'\xfe\x96\xe1O',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.export_card)),b''.join(struct.pack('<i', x) for x in self.export_card),
        ))

    @staticmethod
    def from_reader(reader):
        reader.read_int()
        _export_card = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _export_card.append(_x)

        return ImportCardRequest(export_card=_export_card)


class ImportContactsRequest(TLObject):
    CONSTRUCTOR_ID = 0x2c800be5
    SUBCLASS_OF_ID = 0x8172ad93

    def __init__(self, contacts):
        """
        :param list[InputContact] contacts:

        :returns contacts.ImportedContacts: Instance of ImportedContacts.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.contacts = contacts

    def to_dict(self):
        return {
            '_': 'ImportContactsRequest',
            'contacts': [] if self.contacts is None else [None if x is None else x.to_dict() for x in self.contacts]
        }

    def __bytes__(self):
        return b''.join((
            b'\xe5\x0b\x80,',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.contacts)),b''.join(bytes(x) for x in self.contacts),
        ))

    @staticmethod
    def from_reader(reader):
        reader.read_int()
        _contacts = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _contacts.append(_x)

        return ImportContactsRequest(contacts=_contacts)


class ResetSavedRequest(TLObject):
    CONSTRUCTOR_ID = 0x879537f1
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'ResetSavedRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'\xf17\x95\x87',
        ))

    @staticmethod
    def from_reader(reader):
        return ResetSavedRequest()


class ResetTopPeerRatingRequest(TLObject):
    CONSTRUCTOR_ID = 0x1ae373ac
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, category, peer):
        """
        :param TopPeerCategory category:
        :param InputPeer peer:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.category = category
        self.peer = peer

    def resolve(self, client, utils):
        self.peer = utils.get_input_peer(client.get_input_entity(self.peer))

    def to_dict(self):
        return {
            '_': 'ResetTopPeerRatingRequest',
            'category': None if self.category is None else self.category.to_dict(),
            'peer': None if self.peer is None else self.peer.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\xacs\xe3\x1a',
            bytes(self.category),
            bytes(self.peer),
        ))

    @staticmethod
    def from_reader(reader):
        _category = reader.tgread_object()
        _peer = reader.tgread_object()
        return ResetTopPeerRatingRequest(category=_category, peer=_peer)


class ResolveUsernameRequest(TLObject):
    CONSTRUCTOR_ID = 0xf93ccba3
    SUBCLASS_OF_ID = 0xf065b3a8

    def __init__(self, username):
        """
        :param str username:

        :returns contacts.ResolvedPeer: Instance of ResolvedPeer.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.username = username

    def to_dict(self):
        return {
            '_': 'ResolveUsernameRequest',
            'username': self.username
        }

    def __bytes__(self):
        return b''.join((
            b'\xa3\xcb<\xf9',
            TLObject.serialize_bytes(self.username),
        ))

    @staticmethod
    def from_reader(reader):
        _username = reader.tgread_string()
        return ResolveUsernameRequest(username=_username)


class SearchRequest(TLObject):
    CONSTRUCTOR_ID = 0x11f812d8
    SUBCLASS_OF_ID = 0x4386a2e3

    def __init__(self, q, limit):
        """
        :param str q:
        :param int limit:

        :returns contacts.Found: Instance of Found.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.q = q
        self.limit = limit

    def to_dict(self):
        return {
            '_': 'SearchRequest',
            'q': self.q,
            'limit': self.limit
        }

    def __bytes__(self):
        return b''.join((
            b'\xd8\x12\xf8\x11',
            TLObject.serialize_bytes(self.q),
            struct.pack('<i', self.limit),
        ))

    @staticmethod
    def from_reader(reader):
        _q = reader.tgread_string()
        _limit = reader.read_int()
        return SearchRequest(q=_q, limit=_limit)


class UnblockRequest(TLObject):
    CONSTRUCTOR_ID = 0xe54100bd
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, id):
        """
        :param InputUser id:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.id = id

    def resolve(self, client, utils):
        self.id = utils.get_input_user(client.get_input_entity(self.id))

    def to_dict(self):
        return {
            '_': 'UnblockRequest',
            'id': None if self.id is None else self.id.to_dict()
        }

    def __bytes__(self):
        return b''.join((
            b'\xbd\x00A\xe5',
            bytes(self.id),
        ))

    @staticmethod
    def from_reader(reader):
        _id = reader.tgread_object()
        return UnblockRequest(id=_id)
