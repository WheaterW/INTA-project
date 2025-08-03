pim vpn-instance
================

pim vpn-instance

Function
--------



The **pim vpn-instance** command enables PIM and displays the PIM view of a VPN instance.

The **undo pim vpn-instance** command clears all configurations in the PIM view, releases resources occupied by PIM, and restores the initial state.



By default, PIM is not enabled.


Format
------

**pim vpn-instance** *vpn-instance-name*

**undo pim vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

PIM parameters can be configured only after PIM is enabled, and global PIM parameters can be configured only in the PIM view of the VPN instance.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the VPN instance view.

**Precautions**

Running the **undo pim** command interrupts PIM services. Therefore, exercise caution when using this command.


Example
-------

# Enable PIM and enter the PIM view of a VPN instance named mytest.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance mytest
[*HUAWEI-vpn-instance-mytest] ipv4-family
[*HUAWEI-vpn-instance-mytest-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-mytest-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-instance-mytest-af-ipv4] quit
[*HUAWEI-vpn-instance-mytest] quit
[*HUAWEI] pim vpn-instance mytest
[*HUAWEI-pim-mytest]

```