multicast mvpn
==============

multicast mvpn

Function
--------



The **multicast mvpn** command configures a multicast virtual private network (MVPN) ID.

The **undo multicast mvpn** command deletes an MVPN ID.



By default, no MVPN ID is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast mvpn** *mvpn-id*

**undo multicast mvpn** [ *mvpn-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mvpn-id* | Specifies an MVPN ID in the format of an IPv4 address. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure an MVPN ID, run the **multicast mvpn** command. The MVPN ID is the IP address of the originator Provider Edge (PE) in an MVPN. An MVPN ID can be used as:Specifies the value of the Originator router's IP address field in an A-D route.This object indicates the value of the Administrator field in the VRF Route Import Extended Community attribute carried in BGP VPNv4 routes.If the **multicast mvpn** command is not run, PEs do not send A-D routes, and BGP VPNv4 routes do not carry the VRF Route Import Extended Community attribute.

**Configuration Impact**

If you run this command more than once, the latest configuration overrides the previous one. Changing an MVPN ID may interrupt NG MVPN services. When you run this command again, the system prompts you whether to change the MVPN ID.


Example
-------

# Configure the MVPN ID as 10.1.1.9.
```
<HUAWEI> system-view
[~HUAWEI] multicast mvpn 10.1.1.9

```