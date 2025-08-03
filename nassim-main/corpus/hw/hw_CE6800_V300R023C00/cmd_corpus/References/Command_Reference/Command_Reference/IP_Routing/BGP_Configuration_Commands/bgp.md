bgp
===

bgp

Function
--------



The **bgp** command enables BGP and displays the BGP view, or displays the BGP view directly.

The **undo bgp** command disables BGP.



By default, the BGP is disabled.


Format
------

**bgp** *as-number*

**undo bgp** [ *as-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-number* | Specifies a destination AS number. | For an AS number in integer format, the value ranges from 1 to 4294967295.  For an AS number in dotted notation, it is in the format of x.y, in which x and y are integers, with x ranging from 1 to 65535 and y ranging from 0 to 65535. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP is an inter-AS dynamic routing protocol. BGP is called Internal BGP (IBGP) when it runs within an AS and called External BGP (EBGP) when it runs between ASs.BGP transmits routes between ASs; however, it may not be required in some situations.

* BGP is used only when at least one of the following conditions is met:
* An AS allows data packets to traverse it to reach other ASs.
* An AS has multiple external connections to multiple ISPs and multiple connections to the Internet.
* Data flows entering or leaving ASs must be controlled.
* BGP does not need to be run in the following situations:
* The user is connected to only one ISP.
* The ISP does not need to provide Internet routes for users.
* ASs are connected through default routes.

**Configuration Impact**



After the **bgp** command is run, BGP is enabled.



**Follow-up Procedure**



Run the **peer as-number** command to establish BGP peer relationships between devices on a BGP network.



**Precautions**



Generally, only one local AS number is specified for each device. If BGP multi-instance is configured, another local AS number is specified for BGP multi-instance.By default, an AS number must be specified in the **undo bgp** command.The **undo bgp** command deletes all BGP configurations on the device. Therefore, exercise caution when running this command.The BGP AS number configuration change may affect the route calculation result of the local or remote OSPF VPN process. Because the BGP AS number changes, the local tag of the OSPF VPN process and the tag carried in the LSA advertised by the OSPF VPN process change. When the local tag of the OSPF VPN process is the same as the tag of the received LSA, the LSA does not participate in OSPF route calculation. When a 4-byte AS number is configured for BGP, OSPF does not support automatic tag-based loop prevention.




Example
-------

# Enable BGP and enter the BGP view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100

```