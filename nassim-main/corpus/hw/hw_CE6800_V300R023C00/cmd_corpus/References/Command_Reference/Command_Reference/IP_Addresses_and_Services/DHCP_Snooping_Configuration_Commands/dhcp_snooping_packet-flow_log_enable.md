dhcp snooping packet-flow log enable
====================================

dhcp snooping packet-flow log enable

Function
--------



The **dhcp snooping packet-flow log enable** command enables the log function for DHCP message exchange.

The **undo dhcp snooping packet-flow log enable** command disables the log function for DHCP message exchange.



By default, the log function for DHCP message exchange is disabled.


Format
------

**dhcp snooping packet-flow log enable**

**undo dhcp snooping packet-flow log enable**


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

After the **dhcp snooping packet-flow log enable** command is run to enable the log function for DHCP message exchange on a device, the device records each received DHCP message in the DHCPSNP/6/SNP\_RCV\_MSG log, which contains DHCPv4 and DHCPv6 message information and can be used in scenarios such as intelligent O&M. The network analyzer uses this log to intelligently analyze why users fail to obtain IP addresses.

**Prerequisites**

DHCP snooping has been enabled using the **dhcp snooping enable** command.


Example
-------

# Enable the log function for DHCP message exchange.
```
<HUAWEI> system-view
[~HUAWEI] dhcp snooping packet-flow log enable

```