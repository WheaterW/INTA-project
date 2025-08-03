dhcp snooping server record
===========================

dhcp snooping server record

Function
--------



The **dhcp snooping server record** command enables DHCP server detection.

The **undo dhcp snooping server record** command disables DHCP server detection.



By default, DHCP server detection is disabled.


Format
------

**dhcp snooping server record**

**undo dhcp snooping server record**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If bogus DHCP servers exist on the network, they send incorrect information to DHCP clients, such as the incorrect gateway address, incorrect DNS server, and incorrect IP address. As a result, DHCP clients cannot access the network or access incorrect networks.After DHCP server detection is enabled, a DHCP snooping device checks and stores all information about DHCP servers in the DHCP Reply messages, such as DHCP server address and DHCP client port number, in logs. Based on the logs, the network administrator checks for bogus DHCP servers on the network to maintain the network.When the CHADDR field in the DHCP Request message received by the DHCP snooping device is the same as the MAC address of a DHCP server connected to the trusted interface, the DHCP snooping device discards the message.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.


Example
-------

# Enable DHCP server detection.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] dhcp snooping server record

```