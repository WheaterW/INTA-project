static-rpf-peer
===============

static-rpf-peer

Function
--------



The **static-rpf-peer** command configures a Multicast Source Discovery Protocol (MSDP) peer as a static Reverse Path Forwarding (RPF) peer. The source active (SA) messages sent by the static RPF peer are free from the RPF check.

The **undo static-rpf-peer** command restores the default configuration.



By default, no MSDP peer is configured as a static RPF peer.


Format
------

**static-rpf-peer** *peer-address* **rp-policy** *ip-prefix-name*

**static-rpf-peer** *peer-address*

**undo static-rpf-peer** *peer-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of a static RPF peer. | The address is in dotted decimal notation. |
| **rp-policy** *ip-prefix-name* | Specifies the filtering policy based on Rendezvous Point (RP) addresses. The filtering policy is used to filter SA messages based on RP addresses. ip-prefix-name specifies the name of the filtering policy. | The name is a string of 1 to 169 characters. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent SA messages from being circularly forwarded between MSDP peers, MSDP performs the RPF check on the received SA message. MSDP strictly controls the incoming SA messages. The SA message that does not comply with the RPF rules are discarded.To protect the SA messages transmitted between MSDP peers from being discarded because of RPF rules and reduce redundant traffic, you can specify MSDP peers as static RPF peers. The SA messages received from a static RPF peer need not be checked according to RPF rules.

**Prerequisites**

The **multicast routing-enable** command is run in the public network instance view or VPN instance view.MSDP peers have been configured.

**Configuration Impact**

You can specify multiple remote static RPF peers for the router by using the **static-rpf-peer** command repeatedly.

**Precautions**

The methods of configure multiple static RPF peers for a Router are as follows:

* All the peers are configured with rp-policy: When SA messages sent by a static RPF peer in the active state reaches the local router, the local router filters the SA messages according to specified rp-policy specified on the peers, and receives only the SA messages passing the filtering.
* None of the peers is configured with rp-policy: The local router receives all the SA messages from the static RPF peers in the active state.

Example
-------

# In the public network instance, configure 192.168.3.2 as a static RPF peer, with the source RP address range being 192.168.0.0/16.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix list-df permit 192.168.0.0 16 greater-equal 16 less-equal 32
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 192.168.3.2 connect-interface Vlanif1
[*HUAWEI-msdp] static-rpf-peer 192.168.3.2 rp-policy list-df

```