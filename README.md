# RoutedBits Python Library

A Python library for all things RoutedBits.

## Getting Started

Install this library via Git:

```
pip install https://github.com/routedbits/routedbits-python.git
```

Install after cloning this repository:

```
git clone https://github.com/routedbits/routedbits-python.git
cd routedbits-python
pip install .
```

Use in requirements.txt

```
routedbits @ git+https://github.com/routedbits/routedbits-python.git
```

## Usage

1) Retrieve the current list of nodes:

```python
from routedbits import RoutedBits

a = RoutedBits()
a.nodes() # Returns a list of dicts
```

2) Retrieve a router by its friendly name:

```python
from routedbits import RoutedBits

a.RoutedBits()
a.nodes(name="dal1")

print(a)

"""
{'city': 'Dallas, TX, US', 'flag': '🇺🇸', 'fqdn': 'router.dal1.routedbits.com', 'hostname': 'router.dal1', 'name': 'dal1', 'tunnel_ipv4_address': '172.20.19.68', 'tunnel_ipv6_address': {'link_local': 'fe80::207', 'ula': 'fdb1:e72a:343d::5'}, 'wireguard_public_key': '8clbJPxK5ylOhFDNGdn/CL5zRWQdf7rXbLeF7j8czFI='}
"""
```

## Development

If you update any dependencies required outside of development,
be sure to update the requirements in [pyproject.toml](pyproject.toml)

This project is Linted via workflow by `black` and `flake8`. To install them
and lint before pushing to GitHub:

```
$ pip install black flake8
$ black .
$ flake8
```
