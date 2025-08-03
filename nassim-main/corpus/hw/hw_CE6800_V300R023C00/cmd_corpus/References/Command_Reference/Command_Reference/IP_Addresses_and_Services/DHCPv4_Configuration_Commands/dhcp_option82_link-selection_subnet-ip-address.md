dhcp option82 link-selection subnet-ip-address
==============================================

dhcp option82 link-selection subnet-ip-address

Function
--------



The **dhcp option82 link-selection subnet-ip-address** command configures the IP address corresponding to the Sub5 field in Option 82 on a DHCP relay interface.

The **undo dhcp option82 link-selection subnet-ip-address** command deletes the IP address corresponding to the Sub5 field in Option 82 on a DHCP relay interface.



By default, no IP address is configured for the Sub5 field in Option 82.


Format
------

**dhcp option82 link-selection subnet-ip-address** *ip-address*

**undo dhcp option82 link-selection subnet-ip-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address corresponding to the Sub5 field in Option 82. | The value is in dotted decimal notation. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **dhcp option82 link-selection subnet-ip-address** command configures the IP address corresponding to the Sub5 field in Option 82 on an interface of a DHCP relay agent. The DHCP relay agent then fills this IP address in the Sub5 field.

**Prerequisites**

The function of appending the Option 82 field to DHCP messages has been enabled using the **dhcp option82 link-selection insert enable** command.


Example
-------

# Insert the Sub5 field into the Option 82 field of DHCP messages on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp option82 link-selection insert enable
[*HUAWEI-100GE1/0/1] dhcp option82 link-selection subnet-ip-address 10.1.1.1

```