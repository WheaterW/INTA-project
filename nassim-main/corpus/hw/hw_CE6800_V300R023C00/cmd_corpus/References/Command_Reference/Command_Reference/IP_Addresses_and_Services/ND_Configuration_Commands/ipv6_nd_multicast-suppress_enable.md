ipv6 nd multicast-suppress enable
=================================

ipv6 nd multicast-suppress enable

Function
--------



The **ipv6 nd multicast-suppress enable** command enables NS multicast suppression.

The **undo ipv6 nd multicast-suppress enable** command disables NS multicast suppression.



By default, NS multicast suppression is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd multicast-suppress** { **proxy-reply** [ **unknown-options-unicast** ] | **unicast-forward** } [ **mismatch-discard** ] **enable**

**undo ipv6 nd multicast-suppress** { **proxy-reply** [ **unknown-options-unicast** ] | **unicast-forward** } [ **mismatch-discard** ] **enable**

**undo ipv6 nd multicast-suppress enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **proxy-reply** | When the destination address of an NS multicast message is not of the local host but can match a proxy ND entry on the local device, the device implements proxy ND and replies with an NA message.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **unknown-options-unicast** | When the destination address of an NS multicast message is not of the local host but can match a proxy ND entry on the local device, the device converts multicast streams to unicast streams for the packets carrying unrecognized options.  By default, the device does not process unrecognized options in NS messages.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **unicast-forward** | When the destination address of an NS multicast message is not of the local host but can match a proxy ND entry on the local device, the device converts the NS multicast message to an NS unicast message and forwards the NS unicast message.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **mismatch-discard** | When the destination address of an NS multicast message is not of the local host and does not match a proxy ND entry on the local device, the device discards the NS multicast message.  By default, the device replicates and forwards the NS multicast messages that do not match a proxy ND entry on the local device.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When a network device receives an NS message to implement address resolution, the device forwards the NS message within its own BD. This NS message is received only by the nodes with the last 24 bits the same as the multicast address. If a device receives a large number of NS messages within a specified period, forwarding these NS messages uses excessive network resources and leads to network congestion and deteriorated network performance. As a result, user services are affected.To resolve this problem, run the **ipv6 nd multicast-suppress enable** command to enable NS multicast suppression. With NS multicast suppression enabled, upon receipt of an NS message, a device checks whether the NS message contains information about the end user. If so, the device simply implements proxy ND or converts multicast streams to unicast streams. If not, the device forwards the NS message based on the original process. This reduces or suppresses message flooding occurred during address resolution.



**Precautions**

* Before enabling NS multicast suppression, ensure that the encapsulation type of the Layer 2 sub-interface bound to the BD is not one of the following:
* Default type
* If no traffic behavior is configured on an EVC Layer 2 sub-interface, the EVC Layer 2 sub-interface transparently transmits Dot1q packets without modifying received packets.
* If no traffic behavior is configured on an EVC Layer 2 sub-interface, the EVC Layer 2 sub-interface transparently transmits received QinQ packets without modifying them.
* Before NS multicast suppression is enabled, if the encapsulation type of an EVC Layer 2 sub-interface bound to a BD is QinQ, the traffic behavior on the EVC Layer 2 sub-interface must be set to pop so that the EVC Layer 2 sub-interface removes double VLAN tags from received packets, that is, run the **rewrite pop double** command on the EVC Layer 2 sub-interface.
* The **ipv6 nd multicast-suppress enable** command and ND proxy-related commands are mutually exclusive and cannot be configured together. The mutually exclusive commands are as follows:
  + ipv6 nd proxy route enable
  + ipv6 nd proxy anyway enable


Example
-------

# Enable NS multicast suppression to allow the device to reply with an NA message when the destination address of an NS multicast message is not of the local host but can match a proxy ND entry on the local device.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] ipv6 nd multicast-suppress proxy-reply enable

```

# Enable NS multicast suppression to allow the device to convert a multicast message to a unicast message and then forward the unicast message when the destination address of an NS multicast message is not of the local host but can match a proxy ND entry on the local device.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] ipv6 nd multicast-suppress unicast-forward enable

```