ipv6 route-static track bfd-session admindown invalid
=====================================================

ipv6 route-static track bfd-session admindown invalid

Function
--------



The **ipv6 route-static track bfd-session admindown invalid** command prevents an IPv6 static route from being selected if the BFD session associated with it is in the AdminDown state.

The **undo ipv6 route-static track bfd-session admindown invalid** command restores the default configuration.



By default, an IPv6 static route can still be selected by the Router even though the BFD session associated with it is in the AdminDown state.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 route-static track bfd-session session-name** *bfd-name* **admindown** **invalid**

**undo ipv6 route-static track bfd-session** [ **session-name** *bfd-name* ] **admindown** **invalid**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **session-name** *bfd-name* | Specifies a BFD session associated with an IPv6 static route. | The value is a string of 1 to 64 case-insensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, an IPv6 static route can still be selected by the Huawei devices even though the BFD session associated with it is in the AdminDown state, but not by non-Huawei devices. As a result, the Huawei devices cannot interwork with non-Huawei devices.To address this problem, run the **ipv6 route-static track bfd-session admindown invalid** command to configure the Router not to select the IPv6 static route if the BFD session associated with it is in the AdminDown state.

**Prerequisites**

The BFD session specified by bfd-name has been created.

**Precautions**

The **undo ipv6 route-static track bfd-session admindown invalid** command deletes the association between all IPv6 static routes and BFD sessions in the AdminDown state.After the **undo bfd** command is run, the BFD parameters bound to the static route are deleted. As a result, the static route status may change and services may be interrupted.


Example
-------

# Prevent the IPv6 static route from participating in route selection if the BFD session (bfda) associated with it is in the AdminDown state.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd bfda bind peer-ipv6 2001:db8:1::1
[*HUAWEI-bfd-session-bfda] discriminator local 20
[*HUAWEI-bfd-session-bfda] discriminator remote 10
[*HUAWEI-bfd-session-bfda] quit
[*HUAWEI] ipv6 route-static track bfd-session session-name bfda admindown invalid

```