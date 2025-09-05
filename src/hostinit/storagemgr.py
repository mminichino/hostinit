##
##

import logging
import warnings
from overrides import override
from hostinit.cli import CLI
from hostinit.storage import StorageManager

warnings.filterwarnings("ignore")
logger = logging.getLogger()


class StorageMgrCLI(CLI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @override()
    def local_args(self):
        self.parser.add_argument('-p', '--partition', action='store', help="Get partition for device")
        self.parser.add_argument('-D', '--disk', action='store_true', help="Get disk device")
        self.parser.add_argument('-S', '--swap', action='store_true', help="Get swap device")
        self.parser.add_argument('-R', '--root', action='store_true', help="Get root device")
        self.parser.add_argument('-n', '--number', action='store', help="Partition number", type=int, default=0)

    def run(self):
        if self.options.partition:
            device = StorageManager().get_partition(self.options.partition, self.options.number)
            if device:
                print(device)
        elif self.options.disk:
            device = StorageManager().get_device(self.options.number)
            if device:
                print(device)
        elif self.options.swap:
            device = StorageManager().get_device(2)
            if device:
                print(device)
        elif self.options.root:
            device = StorageManager().get_device(1)
            if device:
                print(device)


def main(args=None):
    cli = StorageMgrCLI(args)
    cli.run()
