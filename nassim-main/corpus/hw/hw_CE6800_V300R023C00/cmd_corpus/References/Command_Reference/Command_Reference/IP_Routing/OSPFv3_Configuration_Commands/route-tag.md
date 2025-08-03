route-tag
=========

route-tag

Function
--------



The **route-tag** command sets the VPN route tag for imported VPN routes.

The **undo route-tag** command restores the default setting.



By default, the first two bytes of a tag value are fixed at 0xD000, and the last two bytes are the local BGP AS number. For example, if the local BGP AS number is 100, the default tag value in decimal notation is 3489661028; if the BGP AS number is greater than 65535, the tag value is 0, and you can manually change the tag value. If BGP is not configured, the default tag value is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**route-tag** *tag-value*

**undo route-tag**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tag-value* | Specifies the VPN route tag. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **route-tag** command applies only to VPN scenarios. It is used as the tag value in Type 5 LSAs and Type 7 LSAs to prevent external loops when a CE is dual-homed to PEs. On a network where a CE is connected to two PEs, PE1 generates Type 5 LSAs and Type 7 LSAs based on imported BGP routes and sends them to the CE. The CE then sends the LSAs to PE2. Because OSPFv3 routes have a higher priority than BGP routes, PE2 replaces BGP routes with OSPFv3 routes, causing a routing loop. After the **route-tag** command is run, if the PE finds that the tag value of an LSA is the same as the local tag value, the PE ignores the LSA during route calculation to prevent routing loops.The priorities of the tag set through the **route-tag** command and the tag set through other commands are as follows:

* If a route-policy or route-filter is configured using the **import-route** command and the **apply tag** command is configured in the policy, the tag value configured in the policy has the highest priority.
* If a route-policy or route-filter is configured in the **import-route** command but the **apply tag** command is not configured in the policy, but the tag parameter is specified in the **import-route** command, the tag parameter has the highest priority.
* If a route-policy or route-filter is configured in the **import-route** command, the **apply tag** command is not configured in the policy, and the tag parameter is not specified in the **import-route** command, the priority is as follows:

1. If the current process is bound to a VPN instance and the **vpn-instance-capability simple** command is not run, the value of route-tag is used. The values of route-tag are as follows:(1) If the **route-tag** command is configured, the configured value is used.(2) If the **route-tag** command is not configured, the default value is used.(3) If route-tag disable is configured, the value of route-tag is 0.
2. If the current process is not bound to any VPN instance or is bound to a VPN instance and the **vpn-instance-capability simple** command is executed, the default value is used.(1) If the **default tag** command is configured, the configured value is used.(2) If the **default tag** command is not configured, the default value 1 is used.

* If no route-policy or route-filter is configured in the **import-route** command but the tag parameter is specified in the **import-route** command, the tag parameter has the highest priority.
* If no route-policy or route-filter is configured in the **import-route** command and the tag parameter is not specified in the **import-route** command, the priority is as follows:

1. If the current process is bound to a VPN instance and the **vpn-instance-capability simple** command is not run, the value of route-tag is used. The values of route-tag are as follows:(1) If the **route-tag** command is configured, the configured value is used.(2) If the **route-tag** command is not configured, the default value is used.(3) If route-tag disable is configured, the value of route-tag is 0.
2. If the current process is not bound to any VPN instance or is bound to a VPN instance and the **vpn-instance-capability simple** command is executed, the default value is used.(1) If the **default tag** command is configured, the configured value is used.(2) If the **default tag** command is not configured, the default value 1 is used.

**Precautions**

* It is recommended that PEs in the same area be configured with the same route tag.
* Different OSPFv3 processes can be configured with the same tag value.
* The route tag is not transmitted in BGP extended community attributes. It is configured and takes effect only on the PEs that receive BGP routes and generate Type 5 and Type 7 LSAs.
* This command can be executed only in an OSPFv3 VPN process and takes effect only when the **vpn-instance-capability simple** command is not run in the OSPFv3 VPN process.

Example
-------

# Set the VPN route tag in OSPFv3 process 100 to 100.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv6-family
[*HUAWEI-vpn-instance-huawei-af-ipv4] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ospfv3 100 vpn-instance huawei
[*HUAWEI-ospfv3-100] route-tag 100

```