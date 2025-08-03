vxlan-overlay local-preference enable
=====================================

vxlan-overlay local-preference enable

Function
--------



The **vxlan-overlay local-preference enable** command configures a device to forward all traffic or VXLAN network-side traffic matching a route only to the local outbound interface (non-VXLAN outbound interface).

The **undo vxlan-overlay local-preference enable** command disables the device from forwarding all traffic or VXLAN network-side traffic only to local outbound interfaces (non-VXLAN outbound interfaces) after the traffic matches a route.



By default, the device forwards VXLAN traffic through all outbound interfaces in load balancing mode after the traffic matches a route with multiple next hops.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan-overlay** { **network** | **all** } **local-preference** **enable**

**undo vxlan-overlay** { **network** | **all** } **local-preference** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **network** | After VXLAN network-side traffic matches a route, the traffic is forwarded only to the local outbound interface (non-VXLAN outbound interface). | - |
| **all** | After all traffic matches the route, the traffic is forwarded only to the local outbound interface (non-VXLAN outbound interface). | - |



Views
-----

ECMP load balancing view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the next-hop outbound interfaces of Layer 3 traffic entering the local device are a combination of VXLAN and non-VXLAN tunnels working in load balancing mode, Layer 3 traffic is load balanced between the VXLAN and non-VXLAN tunnels by default. If you do not want the local device to forward all traffic or traffic from VXLAN tunnels to VXLAN tunnels serving as next hops, run this command.

**Precautions**

On the CE6863H-48S6CQ, CE6863H-48S6CQ-K, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6881H-48T6CQ and CE6881H-48T6CQ-K:

* This command and the **local-preference enhanced** command are mutually exclusive globally and cannot be configured together.
* The load-balancing ucmp and **load-balancing ucmp** commands are mutually exclusive globally and cannot be configured together.

On the CE6866-48S8CQ-P, CE6866-48S8CQ-K, CE6860-HAM and CE6860-SAN:

* When two global traffic policies exist, the **vxlan-overlay local-preference enable** command cannot be configured to forward VXLAN network-side traffic that matches a route only to the local outbound interface (non-VXLAN outbound interface).
* This command and the **load-balance ecmp rail-group enable** command are mutually exclusive globally and cannot be configured together.
* This command and the **flow-matrix** command are mutually exclusive globally and cannot be configured together.
* This command and the **load-balancing ucmp** command are mutually exclusive globally and cannot be configured together.

On the CE6885 and CE6885-SAN:

* When two global traffic policies exist, the **vxlan-overlay local-preference enable** command cannot be configured to forward VXLAN network-side traffic that matches a route only to the local outbound interface (non-VXLAN outbound interface).
* This command and the **load-balance ecmp rail-group enable** command are mutually exclusive globally and cannot be configured together.
* This command and the **load-balancing ucmp** command are mutually exclusive globally and cannot be configured together.

On the CE8851-32CQ8DQ-P, CE8851-32CQ8DQ-K, CE8850-HAM and CE8850-SAN:

* When two global traffic policies exist, the **vxlan-overlay local-preference enable** command cannot be configured to forward VXLAN network-side traffic that matches a route only to the local outbound interface (non-VXLAN outbound interface).
* This command and the **load-balancing adaptive-routing** command are mutually exclusive globally and cannot be configured together.
* This command and the **adaptive-routing enable** command are mutually exclusive globally and cannot be configured together.
* This command and the **load-balance ecmp rail-group enable** command are mutually exclusive globally and cannot be configured together.
* This command and the **flow-matrix** command are mutually exclusive globally and cannot be configured together.
* This command and the **load-balancing ucmp** commands are mutually exclusive globally and cannot be configured together.

On the CE8855:

* When two global traffic policies exist, the **vxlan-overlay local-preference enable** command cannot be configured to forward VXLAN network-side traffic that matches a route only to the local outbound interface (non-VXLAN outbound interface).
* This command and the **load-balancing adaptive-routing** command are mutually exclusive globally and cannot be configured together.
* This command and the **adaptive-routing enable** command are mutually exclusive globally and cannot be configured together.
* This command and the **load-balance ecmp rail-group enable** command are mutually exclusive globally and cannot be configured together.
* This command and the **load-balancing ucmp** command are mutually exclusive globally and cannot be configured together.


Example
-------

# Configure a VXLAN network-side or user-side interface to forward traffic only to the local outbound interface (non-VXLAN outbound interface) after the traffic matches a route.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] vxlan-overlay all local-preference enable

```

# Configure the device to forward VXLAN network-side traffic only to the local outbound interface (non-VXLAN outbound interface) after the traffic matches a route.
```
<HUAWEI> system-view
[~HUAWEI] load-balance ecmp
[~HUAWEI-ecmp] vxlan-overlay network local-preference enable

```