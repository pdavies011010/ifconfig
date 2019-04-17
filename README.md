# Network Interface Script

The code here was done as part of a challenge, I may delete this repo (or make 
it private) at some point in the future.

## Setup
Turns out getting network interface data is tricky, especially if you want to
make it cross platfor. To achieve this, I used the `psutil` library. You should
be able to do the following to create a virtual environment and install
`psutil`:

```bash
$ mkvirtualenv ifconfig
$ pip install -r requirements.txt
```

Running it should look something like this:
(Note: this is not real data, it has been anonymized)
```
$ python ifconfig.py

bridge0: MAC: 6a:00:00:ad:42:00
en0: IPv4: 10.0.0.123/255.255.255.0, IPv6: fe80::c4e:123f:ea92:a3c0%en0/ffff:ffff:ffff:ffff::, MAC: 00:00:00:00:00:00
en1: MAC: 00:00:00:00:00:00
en2: MAC: 00:00:00:00:00:00
lo0: IPv4: 127.0.0.1/255.0.0.0, IPv6: fe80::1%lo0/ffff:ffff:ffff:ffff::
```
