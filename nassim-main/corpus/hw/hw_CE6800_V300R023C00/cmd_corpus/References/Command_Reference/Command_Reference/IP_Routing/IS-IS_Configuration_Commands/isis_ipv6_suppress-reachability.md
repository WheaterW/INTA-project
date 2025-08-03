isis ipv6 suppress-reachability
===============================

isis ipv6 suppress-reachability

Function
--------



The **isis ipv6 suppress-reachability** command enables IS-IS to suppress the advertisement of interface addresses so that they can be reused.

The **undo isis ipv6 suppress-reachability** command restores the default setting.



By default, interface addresses can be advertised.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 suppress-reachability** [ **level-1** | **level-1-2** | **level-2** ]

**undo isis ipv6 suppress-reachability**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Suppresses the advertisement of only Level-1 interface addresses. | - |
| **level-1-2** | Suppresses the advertisement of Level-1 and Level-2 interface addresses. | - |
| **level-2** | Suppresses the advertisement of only Level-2 interface addresses.  If no level is specified, the advertisement of Level-1-2 interface addresses is suppressed. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If you want a local interface to be used only for topology connection, you can run the **isis ipv6 suppress-reachability** command to enable IS-IS to suppress the advertisement of the local interface's IP address. This configuration prevents traffic whose destination IP address is the interface's IP address from being sent to the local device. In addition, this configuration also shields the local interface's IP address.


Example
-------

# Suppress the advertisement of the IPv6 address of 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis ipv6 suppress-reachability

```