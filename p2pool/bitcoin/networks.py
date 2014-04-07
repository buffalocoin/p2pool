import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(
    buffalocoin=math.Object(
        P2P_PREFIX='25262526'.decode('hex'),
        P2P_PORT=25085,
        ADDRESS_VERSION=25,
        RPC_PORT=25086,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'buffalocoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//3153600,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=30, # s targetspacingBA
        SYMBOL='BFL',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'buffalocoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/buffalocoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.buffalocoin'), 'buffalocoin.conf'),#        BLOCK_EXPLORER_URL_PREFIX='http://exp.buffalocoin.info/block/',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        BLOCK_EXPLORER_URL_PREFIX='',
#        ADDRESS_EXPLORER_URL_PREFIX='http://exp.buffalocoin.info/address/',
#        TX_EXPLORER_URL_PREFIX='http://exp.buffalocoin.info/tx/',
#        BLOCK_EXPLORER_URL_PREFIX='http://exp.buffalocoin.info/block/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
