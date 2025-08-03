ipv6 neighbor
=============

ipv6 neighbor

Function
--------



The **ipv6 neighbor** command configures a static entry in the IPv6 neighbor discovery cache.

The **undo ipv6 neighbor** command deletes a static entry from the IPv6 neighbor discovery cache.



By default, no static entry is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 neighbor** *ipv6-address* *mac-address*

**undo ipv6 neighbor** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a static entry. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *mac-address* | Specifies the data link layer address of the static entry. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be a multicast MAC address or an all-F broadcast MAC address. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To filter the illegal packets, you can create static ND entries, binding the destination IPv6 addresses of these packets to nonexistent MAC addresses.

**Prerequisites**

The IPv6 function has been enabled on an interface using the **ipv6 enable** command.

**Configuration Impact**

An ND entry enters the REACHABLE state after being created, indicating that the interface connected to this neighbor is Up. If the interface connected to this neighbor turns Down, the ND entry needs to be deleted.The static ND entries overwrite the ND entries dynamically learnt by routers. That is, static ND entries are of higher priorities than dynamically learnt ND entries.

**Precautions**

* A maximum of 16K static neighbor entries can be configured on an interface.
* If the IPv6 address or MAC address specified in the **ipv6 neighbor** command is incorrect, the device cannot communicate with the neighbor.
* To clear all dynamic neighbor entries, run the **reset ipv6 neighbors dynamic** command.

Example
-------

# Configure static entries in the IPv6 neighbor discovery cache on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 neighbor 2001:db8::1 fe-e0-89

```