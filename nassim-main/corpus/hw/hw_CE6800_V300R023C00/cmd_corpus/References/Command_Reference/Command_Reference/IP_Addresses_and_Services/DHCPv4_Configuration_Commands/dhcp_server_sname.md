dhcp server sname
=================

dhcp server sname

Function
--------

The **dhcp server sname** command configures the name of the server where the DHCP client obtains the startup configuration file.

The **undo dhcp server sname** command deletes the configured name of the server where the DHCP client obtains the startup configuration file.

By default, the name of the server where the DHCP client obtains the startup configuration file is not configured.



Format
------

**dhcp server sname** *sname*

**undo dhcp server sname**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sname** *sname* | Specifies the name of the server where the DHCP client obtains the startup configuration file. | The value is a string of 1 to 63 case-sensitive characters without spaces. When quotation marks are used around the string, spaces are allowed in the string. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

Besides assigning IP addresses, a DHCP server can also provide the required network configuration parameters, such as the startup configuration file name for the DHCP clients. After the name of the server where the DHCP client obtains the startup configuration file is configured using the **dhcp server sname** command, the DHCP client obtains the startup configuration file from this server.

**Prerequisites**

1. IP addresses in the interface address pool have been configured using the **ip address** command.
2. The DHCP server has been enabled on the interface using the **dhcp select interface** command.
3. The startup configuration file name has been configured for the DHCP client using the dhcp server bootfile.

**Follow-up Procedure**

Ensure that the route between the DHCP client and the file server where the DHCP client obtains the startup configuration file is reachable.



Example
-------

# Configure the name of the server where the DHCP client obtains the startup configuration file as Huawei in the interface address pool on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 255.255.255.0
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server bootfile start.ini
[*HUAWEI-100GE1/0/1] dhcp server sname Huawei

```