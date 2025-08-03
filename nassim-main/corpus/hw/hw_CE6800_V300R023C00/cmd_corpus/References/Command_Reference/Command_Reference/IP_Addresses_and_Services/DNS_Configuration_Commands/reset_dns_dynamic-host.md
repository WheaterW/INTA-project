reset dns dynamic-host
======================

reset dns dynamic-host

Function
--------



The **reset dns dynamic-host** command deletes dynamic DNS entries saved in the domain name cache.




Format
------

**reset dns dynamic-host** [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After confirming the action of clearing DNS entries, you can run the **reset** command to clear them.

**Precautions**

Clear dynamic DNS entries with caution because they cannot be restored after being cleared.


Example
-------

# Clear dynamic DNS entries of vpn1 from the domain name cache.
```
<HUAWEI> reset dns dynamic-host vpn-instance vpn1

```

# Clear dynamic DNS entries from the domain name cache.
```
<HUAWEI> reset dns dynamic-host

```