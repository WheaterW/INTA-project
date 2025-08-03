ipv6 address auto link-local
============================

ipv6 address auto link-local

Function
--------



The **ipv6 address auto link-local** command enables the generation of a link-local address for an interface.

The **undo ipv6 address auto link-local** command cancels the configuration.



By default, no link-local addresses are generated automatically for an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 address auto link-local**

**undo ipv6 address auto link-local**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Link-local addresses are used for communication between nodes on the local link during neighbor discovery and stateless auto-configuration. The data packets that use the link-local address as the source or destination address are not forwarded to other links. That is, the link-local address is valid only on the local link.To generate an address that is used only on the local link, run the ipv6 address auto link-local command to configure the automatic generation of a link-local address for an interface.


Example
-------

# Configure a link-local address automatically generated for an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address auto link-local

```