peer description (VPN instance MSDP view/MSDP view of a public network instance)
================================================================================

peer description (VPN instance MSDP view/MSDP view of a public network instance)

Function
--------



The **peer description** command adds description text for a Multicast Source Discovery Protocol (MSDP) peer.

The **undo peer description** command restores the default configuration.



By default, no description text is added for an MSDP peer.


Format
------

**peer** *peer-address* **description** *text*

**undo peer** *peer-address* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The address is in dotted decimal notation. |
| *text* | Specifies the description text. | The description text is a string of 1 to 80 case-sensitive characters, spaces supported. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To easily identify an MSDP peer, you can run the peer description command to add description text for the peer.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.MSDP peers have been configured.


Example
-------

# In the public network instance, add a description ClientA for the MSDP peer with the IP address 10.10.7.6.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface LoopBack1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.7.6 connect-interface LoopBack 1
[*HUAWEI-msdp] peer 10.10.7.6 description ClientA

```