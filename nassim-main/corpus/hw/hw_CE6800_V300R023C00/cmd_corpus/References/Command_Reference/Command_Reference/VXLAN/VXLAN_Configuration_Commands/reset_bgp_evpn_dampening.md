reset bgp evpn dampening
========================

reset bgp evpn dampening

Function
--------



The **reset bgp evpn dampening** command clears BGP EVPN route dampening information and releases suppressed routes.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bgp instance** *instance-name* **evpn** **dampening**

**reset bgp instance** *instance-name* **evpn** **dampening** { **mac-route** | **prefix-route** } *prefix*

**reset bgp evpn dampening**

**reset bgp evpn dampening** { **mac-route** | **prefix-route** } *prefix*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Clears route dampening information about a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without any spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **mac-route** | Indicates MAC advertisement routes. | - |
| **prefix-route** | Indicates IP prefix routes. | - |
| *prefix* | Specifies the prefix of an EVPN route. | EVPN route prefixes are classified into the following types:  MAC advertisement route, in the format of E:M:H-H-H:L:X.X.X.X or E:M:H-H-H:L: [X:X::X:X]:   * E: ID of the VLAN to which the MAC address belongs. * M: The value is 48, indicating the length of the MAC address. * H-H-H: MAC address. H is a 4-digit hexadecimal number, such as 00e0 or fc01. If you enter less than four digits, 0s are padded ahead. For example, e0 is displayed as 00e0. * L: The value is 0, indicating the mask length of the IP address corresponding to the MAC address. * X.X.X.X: IP address corresponding to the MAC address. Currently, only 0.0.0.0 is supported. * X:X::X:X: IPv6 address corresponding to the MAC address.   IP prefix route, in the format of L:X.X.X.X:M or L:[X:X::X:X]:M:   * L: Currently, the value can only be 0. * X.X.X.X: IP address of the host. * M: mask of the host IP address. * X:X::X:X: host IPv6 address. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Route dampening can address route instability. In most cases, BGP EVPN is used on complex networks where routes change frequently. To prevent the adverse impact of continuous route flapping, BGP EVPN uses route dampening to suppress unstable routes.The **reset bgp evpn dampening** command clears dampening information about specified BGP EVPN routes on the public network and releases specified suppressed routes. If no parameter is specified, dampening information about all BGP EVPN routes on the public network is cleared and all suppressed routes are released.

**Prerequisites**

If you do not know which routes are suppressed, you can run the **display bgp evpn all routing-table dampened** command to view the suppressed routes.

**Configuration Impact**

After the reset bgp dampening command is run, suppressed routes are released. If the status of some routes still changes frequently, route flapping may occur. Routing flapping consumes a large number of bandwidth and CPU resources.


Example
-------

# Clear BGP EVPN route dampening information and release suppressed routes.
```
<HUAWEI> reset bgp evpn dampening

```