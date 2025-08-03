advertise link-attributes disable
=================================

advertise link-attributes disable

Function
--------



The **advertise link-attributes disable** command configures OSPF to withdraw the advertisement of a specified type of TLV.

The **undo advertise link-attributes disable** command enables OSPF to advertise TLVs of a specified type.



By default, OSPF advertises Local/Remote Interface ID Sub-TLV and Remote IPv4 Address Sub-TLVs.


Format
------

**advertise link-attributes** { **interface-id** | **remote-ip** } **disable**

**undo advertise link-attributes** { **interface-id** | **remote-ip** } **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface-id** | Specifies the Local/Remote Interface ID Sub-TLV. | - |
| **remote-ip** | Specifies the Remote IPv4 Address Sub-TLV. | - |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After OSPF multi-area is enabled and multi-area neighbor relationships are established, OSPF advertises Local/Remote Interface ID Sub-TLV and Remote IPv4 Address Sub-TLVs by default. If you do not want the device to advertise related TLVs, you can run this command.


Example
-------

# Configure OSPF to withdraw the advertisement of the Remote IPv4 Address Sub-TLV.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] advertise link-attributes remote-ip disable

```

# Configure OSPF to withdraw the advertisement of Local/Remote Interface ID Sub-TLV.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] advertise link-attributes interface-id disable

```