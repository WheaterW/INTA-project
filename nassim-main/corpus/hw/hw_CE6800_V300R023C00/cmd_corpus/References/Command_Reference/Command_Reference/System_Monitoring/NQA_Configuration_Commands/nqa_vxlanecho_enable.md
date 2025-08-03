nqa vxlanecho enable
====================

nqa vxlanecho enable

Function
--------



The **nqa vxlanecho enable** command enables VXLAN ping/tracert.

The **undo nqa vxlanecho enable** command disables VXLAN ping/tracert.



By default, VXLAN ping/tracert is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**nqa vxlanecho enable udp-port** *udpPort* [ **source-ip-interface** { *ifName* | *ifType* *ifNum* } ]

**nqa vxlanecho enable ipv6 udp-port** *udpPort6* [ **source-ip-interface** { *ifName6* | *ifType6* *ifNum6* } ]

**undo nqa vxlanecho enable udp-port** *udpPort* [ **source-ip-interface** { *ifName* | *ifType* *ifNum* } ]

**undo nqa vxlanecho enable ipv6 udp-port** *udpPort6* [ **source-ip-interface** { *ifName6* | *ifType6* *ifNum6* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-ip-interface** *ifName* | Specifies the name of the interface where the source IP address of VXLAN echo request and reply packets resides.  By default, no source IP address or interface is specified. | You are advised to specify this parameter in M-LAG scenarios. |
| *ifType* | Specifies the type of the interface where the source IP address of VXLAN Echo Request and Reply packets resides.  By default, no source IP address or interface is specified. | You are advised to specify this parameter in M-LAG scenarios. |
| *ifNum* | Specifies the number of the interface where the source IP address of VXLAN Echo Request and Reply packets resides.  By default, no source IP address or interface is specified. | You are advised to specify this parameter in M-LAG scenarios. |
| **ipv6** | Indicates an IPv6 address. | - |
| **udp-port** *udpPort* | Specifies a monitoring port number of the VXLAN server for the NQA test. | The value is an integer ranging from 1 to 65535. |
| *udpPort6* | Specifies the listening port number of the IPv6 VXLAN server for the NQA test. | The value is an integer ranging from 1 to 65535. |
| *ifName6* | Specifies the name of the interface where the source IPv6 address of VXLAN echo request and reply packets resides.  You are advised to set this parameter in M-LAG scenarios.  By default, no source IPv6 address or interface is specified. | - |
| *ifType6* | Specifies the type of the interface where the source IPv6 address of VXLAN Echo Request and Reply packets resides.  You are advised to set this parameter in M-LAG scenarios.  By default, no source IPv6 address or interface is specified. | - |
| *ifNum6* | Specifies the number of the interface where the source IPv6 address of VXLAN Echo Request and Reply packets resides.  You are advised to set this parameter in M-LAG scenarios.  By default, no source IPv6 address or interface is specified. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The VXLAN echo capability needs to be enabled and the VXLAN echo listening port number needs to be configured on the responder when the ping vxlan or tracert vxlan operation is required.When you configure the source IP interface, if you do not specify the source IP address when running the ping vxlan or tracert vxlan command, the source IP address of the request packet is obtained from this interface. The source IP address of the response packet is obtained from the interface.

**Configuration Impact**

If the VXLAN echo listening port number is not configured on the responder, the ping vxlan and tracert vxlan configuration initiated by the initiator will time out and fail.If the VXLAN echo listening port number is not enabled on the initiator, the initiator fails to initiate a ping or tracert test when the replyMode is set to 3.


Example
-------

# Enable VXLAN ping/tracert on the responder and set the number of the listening port on the VXLAN server to 2000 for the NQA test.
```
<HUAWEI> system-view
[~HUAWEI] nqa vxlanecho enable udp-port 2000

```

# Enable VXLAN IPv6 ping on the responder and set the number of the listening port on the VXLAN server to 2000 for the NQA test.
```
<HUAWEI> system-view
[~HUAWEI] nqa vxlanecho enable ipv6 udp-port 2000

```