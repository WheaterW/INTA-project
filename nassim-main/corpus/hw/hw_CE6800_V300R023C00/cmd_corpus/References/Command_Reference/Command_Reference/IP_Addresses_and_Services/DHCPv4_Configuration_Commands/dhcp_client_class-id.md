dhcp client class-id
====================

dhcp client class-id

Function
--------



The **dhcp client class-id** command is used to set the Option60 field in the DHCP request packet sent by the DHCP client.

The **undo dhcp client class-id** command is used to restore the default value of the Option60 field.



By default, no Option60 field is configured under interface view.

By default, the default value of the Option60 field depends on the device type, which is "huawei Device Model" under system view.




Format
------

**dhcp client class-id** *class-id*

**undo dhcp client class-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *class-id* | Indicates the value of the Option60 field. | The value is a string of 1 to 64 case-sensitive characters, spaces supported. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The DHCP server identifies the devices according to the Option60 field in the DHCP request packet. You can run the dhcp client class-id class-id command to customize the Option60 field in the DHCP request packet sent from the DHCP client.The DHCP server identifies the devices according to the Option60 field in the DHCP request packet. You can run the dhcp client class-id class-id command to customize the Option60 field in the DHCP request packet sent from the DHCP client.Configuration information of the Option60 field is saved in the storage device:/dhcp-client.options file. By default, the storage device needs to provide more than 80-byte storage space. You can run the more dhcp-client.options command in the user view to check configuration information of the Option60 field.After you run the dhcp client class-id class-id command in the system view, the device that functions as the DHCP client fills the set Option60 in the DHCP request packet sent from all of the interfaces.


Example
-------

# Set the class-id of a DHCP client to huawei on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp client class-id huawei

```

# Set the class-ID of a DHCP client to huawei.
```
<HUAWEI> system-view
[~HUAWEI] dhcp client class-id huawei

```