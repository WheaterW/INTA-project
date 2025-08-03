router-id-extend private enable
===============================

router-id-extend private enable

Function
--------



The **router-id-extend private enable** command configures a device to add the router ID that is a private extended community attribute to locally generated EVPN routes.

The **undo router-id-extend private enable** command disables a device from adding the router ID attribute to locally generated EVPN routes.



By default, a device does not add the router ID to EVPN routes when the EVPN routes are generated locally.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**router-id-extend private enable**

**undo router-id-extend private enable**


Parameters
----------

None

Views
-----

Global EVPN configuration view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To configure a device to add the router ID attribute to locally generated EVPN routes, run the **router-id-extend private enable** command.When both IPv4 VXLAN and IPv6 VXLAN tunnels are to be established between two devices, the local device sends two EVPN routes to the remote device. Each of the two EVPN route carries the local device's IP address, one address with the IPv4 VXLAN tunnel identifier and the other address with the IPv6 VXLAN tunnel identifier. Upon receipt of the EVPN routes, the remote device adds the received IP addresses with different VXLAN tunnel identifiers to the ingress replication list during the process of establishing the IPv4 and IPv6 VXLAN tunnels. Consequently, the remote device forwards two copies of BUM traffic to the local device, causing the local device to receive unneeded duplicate traffic. To address this problem, run the **router-id-extend private enable** command to configure the local device to add the router ID attribute to EVPN routes. Upon receipt the routes, the remote device finds that the EVPN routes carry the same router ID and determines that they are from the same device. In this case, the remote device adds the local device's IP address only with the IPv4 VXLAN tunnel identifier to the ingress replication list, so that the remote device forwards only one copy of each BUM packet to the local device.


Example
-------

# Enable routes to carry the router ID extended attribute.
```
<HUAWEI> system-view
[~HUAWEI] evpn
[*HUAWEI-evpn] router-id-extend private enable

```