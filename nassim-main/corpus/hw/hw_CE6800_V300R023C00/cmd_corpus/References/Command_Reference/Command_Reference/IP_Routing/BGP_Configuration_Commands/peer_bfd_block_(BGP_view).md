peer bfd block (BGP view)
=========================

peer bfd block (BGP view)

Function
--------



The **peer bfd block** command prevents a peer from inheriting the BFD function of its peer group.

The **undo peer bfd block** command restores the default configuration.



By default, a peer inherits the BFD function from its peer group.


Format
------

**peer** *ipv4-address* **bfd** **block**

**undo peer** *ipv4-address* **bfd** **block**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BFD provides millisecond-level fault detection. It helps BGP to detect faults in neighboring devices or links more quickly, and instructs BGP to recalculate routes for correct packet forwarding. If a peer group is configured with BFD, all members of the peer group will establish BFD sessions. The **peer bfd block** command can be used to prevent a peer from inheriting the BFD function from its peer group.

**Prerequisites**



A BFD session has been established.



**Configuration Impact**



After the **peer bfd block** command is run on a peer, the corresponding BFD session on the peer is deleted. As a result, fast link fault detection cannot be implemented.



**Precautions**



The **peer bfd block** command and the peer bfd enable command are mutually exclusive. After the **peer bfd block** command is run, related BFD sessions are automatically deleted.




Example
-------

# Prevent the peer from inheriting the BFD function of its peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 192.168.1.1 as-number 100
[*HUAWEI-bgp] peer 192.168.1.1 bfd block

```