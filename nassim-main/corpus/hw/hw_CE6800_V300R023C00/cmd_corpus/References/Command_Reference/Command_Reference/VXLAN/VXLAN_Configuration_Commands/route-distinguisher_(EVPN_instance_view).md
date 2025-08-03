route-distinguisher (EVPN instance view)
========================================

route-distinguisher (EVPN instance view)

Function
--------



The **route-distinguisher** command configures a route distinguisher (RD) for a BD EVPN instance.

The **undo route-distinguisher** command deletes the RD of a BD EVPN instance.



By default, no RD is configured for BD EVPN instances.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**route-distinguisher** *route-distinguisher*

**route-distinguisher auto**

**undo route-distinguisher** *route-distinguisher*

**undo route-distinguisher auto**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-distinguisher* | Specifies an RD to be configured for a BD EVPN instance. | The format of an RD can be as follows:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. An AS number is an integer ranging from 0 to 65535, and a user-defined number is an integer ranging from 0 to 4294967295. The AS and user-defined numbers cannot be both 0s. This means that an RD cannot be 0:0. * Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. An AS number is an integer ranging from 65536 to 4294967295, and a user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers ranging from 0 to 65535. A user-defined number is an integer ranging from 0 to 65535. The AS and user-defined numbers cannot be both 0s. This means that an RD cannot be 0.0:0. * 32-bit IP address:2-byte user-defined number. For example, 192.168.122.15:1. An IP address ranges from 0.0.0.0 to 255.255.255.255, and a user-defined number is an integer ranging from 0 to 65535. |
| **auto** | Specifies the RD that is automatically generated. | - |



Views
-----

EVPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After creating an EVPN instance in a BD view, run the **route-distinguisher** command to configure an RD for the BD EVPN instance.Different EVPN instances may have the same route prefix. To allow a peer PE to determine to which EVPN instance a received route belongs, run the **route-distinguisher** command to configure an RD for the EVPN instance on the local PE. The local PE then adds the RD to the route prefix to be sent to the peer PE, and the route prefix becomes a globally unique EVPN route.

**Prerequisites**

An EVPN instance has been created using the **evpn** command in the BD view.

**Precautions**

Running the **undo route-distinguisher** command in the BD-EVPN instance view causes EVPN-related configurations to be deleted.


Example
-------

# Configure an RD 22:1 for EVPN instance in BD 11.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 11
[*HUAWEI-bd11] evpn
[*HUAWEI-bd11-evpn] route-distinguisher 22:1

```