ipv6 nd collect host enable
===========================

ipv6 nd collect host enable

Function
--------



The **ipv6 nd collect host enable** command enables a device to flood ND entries or proxy ND entries through EVPN routes.

The **undo ipv6 nd collect host enable** command disables a device from flooding ND entries or proxy ND entries through EVPN routes.



By default, a device is not enabled to flood ND entries or proxy ND entries through EVPN routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd collect host enable**

**undo ipv6 nd collect host enable**


Parameters
----------

None

Views
-----

VBDIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

NS multicast suppression is an effective method of alleviating the pressure on NS messages. The basic principle of NS multicast suppression is that a device prefers to implement proxy ND upon received NS messages. After NS multicast suppression is enabled, upon receipt of an NS message, the device checks whether the message contains information about the end user. If so, the device simply implements proxy ND or converts multicast streams to unicast streams. If not, the device forwards the NS message based on the original process.After NS multicast suppression is enabled, in Layer 3 interworking scenarios, run the **ipv6 nd collect host enable** command in the VBDIF interface view to enable the flooding of ND entries generated on a device through EVPN routes.When another device receives the flooded ND entries or proxy ND entries, a proxy ND table is generated on the local. In this manner, when the device receives NS messages again, it searches the local proxy ND table first. If a matching entry exists, the device simply implements proxy ND or converts multicast streams to unicast streams.

**Prerequisites**

* In Layer 2 interworking scenarios, NS multicast suppression has been enabled using the ipv6 nd multicast-suppress { proxy-reply [ unknown-options-unicast ] | unicast-forward } [ mismatch-discard ] enable command in the BD view.
* In Layer 3 interworking scenarios, NS multicast suppression has been enabled using the ipv6 nd multicast-suppress { proxy-reply [ unknown-options-unicast ] | unicast-forward } [ mismatch-discard ] enable command in the BD view and then IPv6 is enabled using the **ipv6 enable** command in the VBDIF interface view.

Example
-------

# Enable the flooding of proxy ND entries generated on a device through EVPN routes in a Layer 3 interworking scenario.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] ipv6 nd multicast-suppress proxy-reply enable
[*HUAWEI-bd10] commit
[~HUAWEI-bd10] quit
[~HUAWEI] interface Vbdif 10
[*HUAWEI-Vbdif10] ipv6 enable
[*HUAWEI-Vbdif10] ipv6 nd collect host enable

```