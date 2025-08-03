bgp instance
============

bgp instance

Function
--------



The **bgp instance** command enables BGP and enter the BGP multi-instance view.

The **undo bgp instance** command disables BGP.



By default, the BGP is disabled.


Format
------

**bgp** *as-number* **instance** *instance-name*

**undo bgp** *as-number* **instance** *instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *as-number* | Specifies a destination AS number. | For an AS number in integer format, the value ranges from 1 to 4294967295.  For an AS number in dotted notation, it is in the format of x.y, in which x and y are integers, with x ranging from 1 to 65535 and y ranging from 0 to 65535. |
| **instance** *instance-name* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP is an inter-AS dynamic routing protocol. BGP is called Internal BGP (IBGP) when it runs within an AS and called External BGP (EBGP) when it runs between ASs.BGP transmits routes between ASs; however, it may not be required in some situations.BGP is used only when at least one of the following conditions is met:

* An AS allows packets to traverse it to reach other ASs.
* An AS has multiple external connections to multiple ISPs and multiple connections to the Internet.
* Data flows entering or leaving an AS must be controlled.

BGP is not required in the following situations:

* Users are connected to only one ISP.
* The ISP does not need to provide Internet routes for users.
* ASs are connected using default routes.

**Configuration Impact**



After the **bgp** command is run, BGP is enabled.



**Follow-up Procedure**



Run the **peer as-number** command to establish BGP peer relationships between devices on a BGP network.



**Precautions**



Generally, only one local AS number is specified for each device. When BGP multi-instance is configured, a multi-instance local AS number is specified.Exercise caution when using the **undo bgp** command because it will delete all BGP configurations on a device.




Example
-------

# Enable BGP and enter the BGP multi-instance view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance instance100

```