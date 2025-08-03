port vlan exclude
=================

port vlan exclude

Function
--------



The **port vlan exclude** command specifies VLANs that are not allowed to pass through a peer-link interface.

The **undo port vlan exclude** command cancels the configuration.



By default, packets from all VLANs are allowed to pass through a peer-link interface.


Format
------

**port vlan exclude** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }

**undo port vlan exclude** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Indicates the start VLAN ID. | For the CE6885-LL in low latency mode, the value ranges from 1 to 1023.  For other models, the value ranges from 1 to 4094. |
| **to** *vlan-id2* | Indicates the end VLAN ID. The value of <vlan-id2> must be greater than or equal to the value of <vlan-id1>. | For the CE6885-LL in low latency mode, the value ranges from 1 to 1023.  For other models, the value ranges from 1 to 4094. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an interface is configured as a peer-link interface, it is added to all VLANs by default, and no other services can be configured on the interface. You can run the **port vlan exclude** command to configure the VLANs that are not allowed to pass through the peer-link interface.

**Prerequisites**

The Eth-Trunk interface has been configured as a peer-link interface. If the Eth-Trunk interface is not a peer-link interface, run the peer-link *peer-link-id*command in the Eth-Trunk interface view to configure the Eth-Trunk interface as a peer-link interface.


Example
-------

# Specify the IDs of VLANs that are not allowed to pass through Eth-Trunk interface 2 to 10 to 30.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] quit
[*HUAWEI] interface eth-trunk 2
[*HUAWEI-Eth-Trunk2] peer-link 1
[*HUAWEI-Eth-Trunk2] port vlan exclude 10 to 30

```