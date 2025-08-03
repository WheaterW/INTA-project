display msdp rpf-peer
=====================

display msdp rpf-peer

Function
--------



The **display msdp rpf-peer** command displays information about all reverse path forwarding (RPF) peers of a specific source's rendezvous point (RP) address, including RPF peer selection rules and RPF route types.




Format
------

**display msdp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **rpf-peer** **original-rp** *original-rp-address*

**display msdp rpf-peer original-rp** *original-rp-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays information about all RPF peers of a specific source's RP address in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Displays information about all RPF peers of a specific source's RP address in all instances. | - |
| **original-rp** *original-rp-address* | original-rp-address specifies a source's RP address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check whether the forwarding path of source active (SA) messages works properly, run the **display msdp rpf-peer** command. Based on the RPF peer information in the command output, you can check each hop in the forwarding path. If the forwarding path works improperly, this command helps you locate faulty nodes.

**Prerequisites**

Multicast Source Discovery Protocol (MSDP) peers have been configured, because only MSDP peers in Up TCP connections can become RPF peers.NOTE:A device does not perform RPF peer checks on SA messages received from any types of the following MSDP peers:

* The MSDP peer address is the source's RP address.
* The MSDP peer is a static RPF peer of the local device.
* The MSDP peer is a unique MSDP peer of the local device.
* The MSDP peer has joined a full-mesh group.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about RPF peers of the source's RP 1.2.3.4 in the public network instance.
```
<HUAWEI> display msdp rpf-peer original-rp 1.2.3.4
 MSDP RPF peer information of VPN-Instance: public net
 MSDP RPF peer information for Original RP: 1.2.3.4
 01. RPF peer: 6.6.6.6
  RPF selection rule: Peer is IGP next hop of best route
  RPF used topology: default
  RPF route type: multicast(static)

```

**Table 1** Description of the **display msdp rpf-peer** command output
| Item | Description |
| --- | --- |
| MSDP RPF peer information of VPN-Instance | Instance in which RPF peer information is displayed. |
| MSDP RPF peer information for Original RP | Source RP address. |
| RPF peer | RPF peer address. |
| RPF selection rule | RPF peer selection rule:   * Peer is IGP next hop of best route: The RPF peer is a next hop of an IGP route. * Peer is in the AS-path to original RP: The RPF peer is on an AS-path to the source's RP address. * Peer is (M)BGP next hop of best route: The RPF peer is a next hop of a/an (M)BGP route. * Peer is (M)BGP advertiser of best route: The RPF peer is a forwarder of a/an (M)BGP route. |
| RPF used topology | RPF used topology:   * default: default topology. * multicast: multicast topology. * topology name (user-defined): unicast topology. |
| RPF route type | RPF route type:   * mbgp: Multicast Border Gateway Protocol (MBGP) route. * unicast(bgp): BGP route. * multicast(static): static multicast route. * unicast: IGP route (unicast route). |