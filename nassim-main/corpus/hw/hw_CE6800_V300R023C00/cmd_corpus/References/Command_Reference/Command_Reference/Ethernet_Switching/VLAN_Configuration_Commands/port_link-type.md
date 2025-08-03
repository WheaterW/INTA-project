port link-type
==============

port link-type

Function
--------



The **port link-type** command configures a link type on an Ethernet interface.

The **undo port link-type** command restores the default link type.



The default link type of an interface is access.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**port link-type access**

**port link-type hybrid**

**port link-type trunk**

**undo port link-type**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**port link-type dot1q-tunnel**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hybrid** | Configures the link type of an interface as hybrid. | - |
| **trunk** | Configures the link type of an interface as trunk. | - |
| **dot1q-tunnel** | Configures the link type of an interface as dot1q-tunnel.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **access** | Configures the link type of an interface as access. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Different types of interfaces are applicable to different scenarios:

* An access interface connects to a user host and is usually used on an access link. The frames transmitted on the access link are untagged Ethernet frames. If an access interface is configured with a default VLAN, the interface adds a tag to the packet and sets the VID in the tag to the default VLAN ID.
* A trunk interface is used to connect to another device and is usually used on a trunk link. A trunk interface allows frames from multiple VLANs to pass through.
* A hybrid interface can connect to a user host or another device. A hybrid interface can connect to an access link or a trunk link. A hybrid interface allows frames from multiple VLANs to pass through.
* A Dot1q-tunnel interface is mainly used on carrier networks. It adds another 802.1Q tag to 802.1Q tagged packets to expand VLAN space. In this manner, packets from private VLANs can be transparently transmitted to the public network.

**Precautions**



The port link-type command cannot be configured on physical interfaces that are added to an Eth-Trunk.A Layer 3 interface must be switched to a Layer 2 interface using the **portswitch** command.When you modify the link type of an interface that has VLAN configuration, the VLAN configuration will be deleted.




Example
-------

# Configure the link type of 100GE1/0/1 as trunk.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] port link-type trunk

```