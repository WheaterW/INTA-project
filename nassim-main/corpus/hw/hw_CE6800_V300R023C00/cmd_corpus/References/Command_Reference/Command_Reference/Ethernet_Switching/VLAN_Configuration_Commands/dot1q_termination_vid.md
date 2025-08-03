dot1q termination vid
=====================

dot1q termination vid

Function
--------

The **dot1q termination vid** command enables VLAN tag termination for single-tagged packets.

The **undo dot1q termination vid** command disables VLAN tag termination for single-tagged packets.

By default, VLAN tag termination for single-tagged packets is disabled on a sub-interface.



Format
------

**dot1q termination vid** *low-pe-vid*

**undo dot1q termination vid** *low-pe-vid*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vid** *low-pe-vid* | Specifies the start VLAN ID in user packets. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |




Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

* Inter-VLAN communicationVLAN technology is widely used because it helps Layer 2 packets of different users to be separately transmitted. Hosts in a VLAN can communicate with each other, but hosts in different VLANs cannot communicate at Layer 2. The Layer 3 routing technology is required for communication between hosts in different VLANs. The following interfaces can be used to implement inter-VLAN communication:
* VLANIF interfaces on Layer 3 switches- Layer 3 Ethernet sub-interfaces on devicesConventional Layer 3 Ethernet interfaces do not identify VLAN packets. After receiving VLAN packets, they consider the packets invalid and discard them. To implement inter-VLAN communication, create Ethernet sub-interfaces on an Ethernet interface and configure the sub-interfaces to remove tags from VLAN packets.

**Configuration Impact**

After the **dot1q termination vid** command is used, the VLAN tag termination sub-interface processes packets in the following ways:

* After receiving a packet, the inbound interface removes the tag carried in the packet, and then forwards the packet. The outbound interface determines whether the sent packet carries tags.
* Before sending a packet, the outbound interface adds the VLAN information carried in the packet received from the peer end into the packet for forwarding.The VLAN IDs in the tags carried in packets received by a sub-interface must be the low-pe-vid value specified in the **dot1q termination vid** command. Otherwise, the packets will be discarded.After the **dot1q termination vid** command is run on a sub-interface, the encapsulation dot1q-termination configuration is automatically generated on the sub-interface. If you then run the **undo dot1q termination vid** command on this sub-interface, the encapsulation dot1q-termination configuration is deleted from the sub-interface accordingly.

**Precautions**

Each time you run the **dot1q termination vid** command, you are advised to run the commit command. Otherwise, traffic may be interrupted.

If a VLAN range is specified, broadcast, unknown unicast, and multicast (BUM) traffic is replicated in all VLANs in that VLAN range. To ensure that the board is not overburdened by many redundant VLANs, you are advised to plan VLANs appropriately during service deployment.

Example
-------

# Configure Dot1q termination on
100GE
1/0/1.1, specify the VLAN range in the outer tag of user packets to be 100.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1
[*HUAWEI-100GE1/0/1.1] dot1q termination vid 100

```