snmp-agent blacklist ip-block disable
=====================================

snmp-agent blacklist ip-block disable

Function
--------



The **snmp-agent blacklist ip-block disable** command disables the blacklist function for an IP address.

The **undo snmp-agent blacklist ip-block disable** command enables the blacklist function for an IP address.



By default, the blacklist function for an IP address is enabled.


Format
------

**snmp-agent blacklist ip-block disable**

**undo snmp-agent blacklist ip-block disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If SNMP connection fails, run the undo snmp-agent blacklist ip-block disable command to put and keep the user's or community's IP address on an SNMP blacklist. During this period, the user cannot establish a connection.If a blacklisted IP address fails to establish a connection for the first time, the system locks the IP address for 8 seconds. If the connection attempt continuously fails, the locking period increases to 16 seconds and then 32 seconds. When the locking period reaches 32 seconds and the connection attempt still fails, the system locks the IP address for 5 minutes. The IP address is automatically unlocked when the 5-minute locking period expires.


Example
-------

# Disable the blacklist function for an IP address.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent blacklist ip-block disable

```