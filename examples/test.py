from examples import get_tron

tron = get_tron()


print(tron.trx.get_block("latest"))
