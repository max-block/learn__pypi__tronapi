from tronapi import Tron

full_node = "https://api.trongrid.io"
solidity_node = "https://api.trongrid.io"
event_server = "https://api.trongrid.io/"


def get_tron() -> Tron:
    return Tron(full_node=full_node, solidity_node=solidity_node, event_server=event_server)
