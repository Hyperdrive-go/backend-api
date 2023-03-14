from api.models import Contract, Erc721Collection
from django.core.management.base import BaseCommand
from api.utils.contract_utils import get_or_create_contract


class Command(BaseCommand):
    help = "Refresh new contracts and insert to collections"

    def handle(self, *args, **kwargs):
        for con in Contract.objects.filter():
            contract = Contract.objects.get(id=con.id)
            erc721Collection = Erc721Collection.objects.filter(primary_contract_id=con.id)
            # not found insert
            if not erc721Collection:
                get_or_create_contract(address=contract.address)
