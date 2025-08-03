dhcpv6 remote-id insert enable
==============================

dhcpv6 remote-id insert enable

Function
--------



The **dhcpv6 remote-id insert enable** command enables the function of appending the remote ID to DHCPv6 relay messages.

The **undo dhcpv6 remote-id insert enable** command disables the function of appending the remote ID to DHCPv6 relay messages.



By default, the function of appending the remote ID to DHCPv6 relay messages is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 remote-id insert enable**

**undo dhcpv6 remote-id insert enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The remote ID carries information about a client and identifies a client. The DHCPv6 server can make decisions about address allocation, parameter setting, and prefix agent according to the remote ID. The remote ID is defined by the vendor. Usually, the remote ID carries the phone number of the caller in dialing, user name, IP address of the peer in a point-to-point connection, and access interface.

**Prerequisites**

The IPv6 function has been enabled using the **ipv6 enable** command in the interface view.


Example
-------

# Enable the function of appending the remote ID to DHCPv6 relay messages on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcpv6 remote-id insert enable

```