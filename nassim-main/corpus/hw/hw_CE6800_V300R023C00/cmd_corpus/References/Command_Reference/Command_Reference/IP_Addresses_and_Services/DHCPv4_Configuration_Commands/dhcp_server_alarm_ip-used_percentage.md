dhcp server alarm ip-used percentage
====================================

dhcp server alarm ip-used percentage

Function
--------

The **dhcp server alarm ip-used percentage** command configures the percentage of the alarms indicating that the addresses in an interface address pool are used up, and the percentage of the clear alarms.

The **undo dhcp server alarm ip-used percentage** command restores the default percentages of the alarms and clear alarms.

By default, the percentage of the alarms indicating that the addresses in an interface address pool are used up is 100%, and the percentage of the clear alarms is 50%.



Format
------

**dhcp server alarm ip-used percentage** *alarm-resume-percentage* *alarm-percentage*

**undo dhcp server alarm ip-used percentage**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *alarm-resume-percentage* | Specifies the percentage of the clear alarms. | The value is an integer that ranges from 1 to 100. The default value is 50. |
| *alarm-percentage* | Specifies the percentage of the alarms indicating that the addresses in an address pool are used up. | The value is an integer in the range from 1 to 100, in percentage. The default value is 100. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

When the addresses in an interface address pool are used up, alarms are sent to notify the administrator.

**Prerequisites**

1. IP addresses in the interface address pool have been configured using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

The percentage of the clear alarms cannot exceed that of the alarms.



Example
-------

# Configure the percentage of the alarms indicating that the addresses in an interface address pool are used up, and the percentage of the clear alarms in the interface address pool of the interface
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server alarm ip-used percentage 80 90

```