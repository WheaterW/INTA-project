igmp
====

igmp

Function
--------



The **igmp** command displays the IGMP view of the public network instance or VPN instance.

The **undo igmp** command deletes the IGMP view and all configurations in the IGMP view.



By default,no IGMP view is not enabled.


Format
------

**igmp**

**igmp vpn-instance** *vpn-instance-name*

**undo igmp**

**undo igmp vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IGMP parameters globally, you must run the igmp to enter the IGMP view of the public network instance or VPN instance.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Precautions**

Running the **undo igmp** command may interrupt IGMP services. Therefore, exercise caution when running this command.For security purposes, after the **configuration re-authentication enable** command is configured, you must enter the password and pass the authentication before running the **undo igmp** command.


Example
-------

# Enter the IGMP view of the public network instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] igmp

```

# Enter the IGMP view of a VPN instance named vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] route-distinguisher 1:100
[*HUAWEI-vpn-instance-vrf1] multicast routing-enable
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] igmp vpn-instance vrf1

```