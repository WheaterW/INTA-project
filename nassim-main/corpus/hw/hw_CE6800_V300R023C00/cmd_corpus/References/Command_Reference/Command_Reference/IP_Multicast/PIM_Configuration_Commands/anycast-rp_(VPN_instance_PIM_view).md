anycast-rp (VPN instance PIM view)
==================================

anycast-rp (VPN instance PIM view)

Function
--------



The **anycast-rp** command configures an anycast-rendezvous point (Anycast-RP) and displays the Anycast-RP view or displays an existing Anycast-RP view.

The **undo anycast-rp** command deletes an Anycast-RP.



By default, no Anycast-RP is configured.


Format
------

**anycast-rp** *rp-address*

**undo anycast-rp** *rp-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rp-address* | Specifies an Anycast-RP address. | The value is in dotted decimal notation. This address must be a valid unicast IP address and cannot be an address on the network segment 127.0.0.0/8. |



Views
-----

VPN instance PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a traditional Protocol Independent Multicast-Sparse Mode (PIM-SM) domain, all multicast groups map to one RP. When the network is overloaded or all traffic needs to be forwarded by only one RP, the RP may be overburdened. If the RP fails, routes are converged slowly, or multicast packets are forwarded over non-optimal paths.To resolve this issue, run the anycast-rp command to configure an Anycast-RP in the PIM-SM domain, enabling the network to automatically select a topologically closest RP for each source and receiver. This function releases burdens on RPs, implements RP backup, and optimizes forwarding paths.An Anycast-RP can be implemented in a PIM domain by using the following schemes:

* MSDP Anycast-RP: applies to IPv4 networks.
* PIM Anycast-RP: applies to IPv4 and IPv6 networks.

**Configuration Impact**

If PIM Anycast-RP is configured, after an RP receives a Register message, it checks the source address in the Register message. If the Register message is sent by the source's designated router (DR), the RP forwards the Register message to Anycast-RP peers. If the Register message is sent by an Anycast-RP peer, it does not forward the Register message. In such a manner, Anycast-RP peers can learn source and group information from each other.

**Precautions**

* In IPv4 network deployment, you can choose either of the two schemes. Mixed use of the two schemes is not recommended.
* An Anycast-RP address must be the same as that of the elected RP on an existing network.
* In a single instance, you can configure a maximum of four Anycast-RP addresses on each device.
* Either static or dynamic RPs can be used on a network. Configuring RPs on loopback interfaces is recommended. Configure the same RP address on all devices to be deployed with the Anycast-RP function. If dynamic RPs are used on the network, before configuring an Anycast-RP address, run the **display pim rp-info** command to check the address of the RP on the current network.

Example
-------

# Specify 10.10.10.10 as the Anycast-RP address for the vpn instance and enter the Anycast-RP view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abc
[*HUAWEI-vpn-instance-abc] route-distinguisher 100:1
[*HUAWEI-vpn-instance-abc-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-abc-af-ipv4] quit
[*HUAWEI-vpn-instance-abc] quit
[*HUAWEI] pim vpn-instance abc
[*HUAWEI-pim-abc] anycast-rp 10.10.10.10

```