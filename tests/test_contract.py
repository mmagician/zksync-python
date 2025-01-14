from unittest import TestCase

from web3 import HTTPProvider, Web3, Account

from zksync_sdk.zksync import ZkSync


class TestZkSyncContract(TestCase):
    private_key = "0xcfcf55abae35cfd18caeb3975688d3dcb4834dac21d9c03ca0b670a00028df4c"

    def setUp(self) -> None:
        self.account = Account.from_key(self.private_key)
        w3 = Web3(HTTPProvider(
            endpoint_uri="https://rinkeby.infura.io/v3/bcf42e619a704151a1b0d95a35cb2e62"))
        self.zksync = ZkSync(account=self.account,
                             web3=w3,
                             zksync_contract_address="0x82F67958A5474e40E1485742d648C0b0686b6e5D")

    def test_deposit_eth(self):
        tx = self.zksync.deposit_eth(self.account.address, 2 * 10 ** 13)
        assert tx['transactionHash']

    def test_full_exit(self):
        tx = self.zksync.full_exit(1, "0x3B00Ef435fA4FcFF5C209a37d1f3dcff37c705aD")
        assert tx['transactionHash']

    def test_auth_facts(self):
        tx = self.zksync.auth_facts(self.account.address, 2)
        assert tx
