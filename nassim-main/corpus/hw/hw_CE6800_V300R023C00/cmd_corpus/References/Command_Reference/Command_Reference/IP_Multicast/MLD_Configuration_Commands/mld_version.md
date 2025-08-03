mld version
===========

mld version

Function
--------



The **mld version** command specifies the version of Multicast Listener Discovery (MLD) running on an interface.

The **undo mld version** command restores the default configuration.



By default, an interface runs MLDv2.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld version** *version*

**undo mld version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *version* | Specifies the version of Multicast Listener Discovery (MLD). | MLD version:   * 1:MLDv1 * 2:MLDv2 |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

All Routers on the same subnet must support the same MLD version. The device does not adapt to the MLD version automatically.


Example
-------

# Configure MLDv1 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld version 1

```