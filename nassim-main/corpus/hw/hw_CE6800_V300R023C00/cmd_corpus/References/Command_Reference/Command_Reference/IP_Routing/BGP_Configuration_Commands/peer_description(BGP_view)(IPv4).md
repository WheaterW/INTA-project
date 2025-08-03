peer description(BGP view)(IPv4)
================================

peer description(BGP view)(IPv4)

Function
--------



The **peer description** command configures a description for a peer.

The **undo peer description** command deletes the description of a peer.



By default, no description is configured for a peer.


Format
------

**peer** *ipv4-address* **description** *description-text*

**undo peer** *ipv4-address* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *description-text* | Specifies a description. | The value is a string of 1 to 255 characters. Letters, digits, and spaces are supported. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The peer description can be used to configure a description for a peer, which facilitates management of peers or peer groups. The description records information about the peer, such as the VPN instance to which the peer belongs, and devices that establish peer relationships with the peer.

**Implementation Procedure**

The description configured by using the **peer description** command for a peer is displayed from the first non-space character.

**Configuration Impact**

If the **peer description** command is run multiple times to configure a description for a peer, the latest configuration overwrites the previous one.

**Follow-up Procedure**

Run the display bgp peer verbose command to view the description of a peer configured using the **peer description** command.


Example
-------

# Configure a description for a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] peer 10.1.1.1 description ISP1

```