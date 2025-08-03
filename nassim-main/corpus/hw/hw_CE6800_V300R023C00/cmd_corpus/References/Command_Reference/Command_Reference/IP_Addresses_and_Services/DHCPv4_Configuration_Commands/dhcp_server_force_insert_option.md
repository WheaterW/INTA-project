dhcp server force insert option
===============================

dhcp server force insert option

Function
--------

The **dhcp server force insert option** command configures a DHCP server to forcibly insert an Option field specified in the interface address pool to a DHCP Response packet that it sends to a DHCP client.

The **undo dhcp server force insert option** command deletes the Option field forcibly inserted to a DHCP Response packet that a DHCP server sends to a DHCP client.

By default, a DHCP server does not forcibly insert an Option field to a DHCP Response packet that it sends to a DHCP client.



Format
------

**dhcp server force insert option** *code* &<1-254>

**undo dhcp server force insert option** *code* &<1-254>



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *code* | Specifies the code for a forcibly replied option. You can configure a DHCP server to forcibly reply one or more options. | The value is an integer that ranges from 1 to 254. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

In general, when a DHCP client applies for an IP address from a DHCP server, parameters contained in the DHCP Request packet specify the options the client requires. The DHCP server inserts the required options to a DHCP Response packet.

Sometimes, a device, functioning as a DHCP server, receives a DHCP Request packet that contains no parameter specifying the options the client requires. However, the client still wants to obtain the options configured on the interface address pool. Run the
**dhcp server force insert option** command to configure the DHCP server to forcibly insert an Option field to a DHCP Response packet.

**Prerequisites**

* IP addresses in the interface address pool have been configured using the **ip address** command.
* The device has been configured to assign IP addresses in the interface address pool using the **dhcp select interface** command.
* The Option field has been configured in the interface address pool using the **dhcp server option** command in the interface view.


Example
-------

# Configure a DHCP server to forcibly insert Option 4 to a DHCP Response packet on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server option 4 hex 11
[*HUAWEI-100GE1/0/1] dhcp server force insert option 4

```