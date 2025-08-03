description (VPN instance view)
===============================

description (VPN instance view)

Function
--------



The **description** command specifies the description of the current VPN instance.

The **undo description** command deletes the description of the current VPN instance.



By default, no description is specified for a VPN instance.


Format
------

**description** *description-information*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description-information* | Specifies the description of a VPN instance. | The value is a string of 1 to 242 case-sensitive characters, spaces supported. |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To record the purpose of creating a VPN instance and the CEs with which the VPN instance is associated, run the **description** command to specify the description of the VPN instance.



**Configuration Impact**



If the **description** command is run more than once, the latest configuration overrides the previous one.




Example
-------

# Specify the description of a VPN instance named vpn1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] description OnlyForAB

```