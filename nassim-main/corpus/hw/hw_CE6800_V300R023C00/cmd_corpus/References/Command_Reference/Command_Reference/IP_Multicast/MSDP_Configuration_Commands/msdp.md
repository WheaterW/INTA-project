msdp
====

msdp

Function
--------



The **msdp** command enables the Multicast Source Discovery Protocol (MSDP) and displays the MSDP view of the public network instance or the VPN instance.

The **undo msdp** command clears all configurations in the MSDP view, releases resources occupied by MSDP, and restores the initial state.



By default, MSDP is not enabled.


Format
------

**msdp vpn-instance** *vpn-instance-name*

**msdp**

**undo msdp vpn-instance** *vpn-instance-name*

**undo msdp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MSDP peer parameters can be configured only after MSDP is enabled, and MSDP peer parameters can be configured only in the MSDP view. To enable MSDP and enter the MSDP view, run the **msdp** command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

Note:Running the **undo msdp** command interrupts MSDP services. Therefore, exercise caution when using this command.


Example
-------

# Enable MSDP and enter the MSDP view of a VPN instance named mytest.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance mytest
[*HUAWEI-vpn-mytest] ipv4-family
[*HUAWEI-vpn-mytest-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-mytest-af-ipv4] multicast routing-enable
[*HUAWEI-vpn-mytest-af-ipv4] quit
[*HUAWEI-vpn-mytest] quit
[*HUAWEI] msdp vpn-instance mytest
[*HUAWEI-msdp-mytest]

```

# Enable MSDP and enter the MSDP view of the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp]

```