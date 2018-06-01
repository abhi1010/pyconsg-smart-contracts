# Run Smart Contracts using Python


This is a very simple project for managing smart contracts using Python.

PyCon presentation can be found at [bit.ly/pyconsg-ico](http://bit.ly/pyconsg-ico)

## Setup

```bash
virtualenv -p python3.6 ve
source ve/bin/activate
pip install -r requirements.txt
```

## Running it

You should first try and run `direction.py`. It is an extremely simple version
where the code is written in a simplified manner. It uses `web3.py`


Next, you can view `gas.py`. It builds upon `direction.py` by simplifying
some steps like _deployment_ and _waiting for transaction to complete_ on the blockchain.

## Next steps

Start with the releases on [github: ico-runner](https://github.com/abhi1010/ico-runner/releases).

1. The first release is based on [TokenMarketNet's ICO](https://github.com/TokenMarketNet/ico).
2. The second release is based on the ever famous [OpenZeppelin's framework](https://github.com/OpenZeppelin/openzeppelin-solidity).

Both the releases are step by step guide; if you follow the _scripts_ folder.

