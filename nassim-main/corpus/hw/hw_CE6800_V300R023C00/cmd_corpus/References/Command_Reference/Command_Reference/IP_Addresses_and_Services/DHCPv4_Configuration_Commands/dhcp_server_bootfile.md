dhcp server bootfile
====================

dhcp server bootfile

Function
--------

The **dhcp server bootfile** command configures the name of the startup configuration file for a DHCP client.

The **undo dhcp server bootfile** command deletes the configured name of the startup configuration file for a DHCP client.

By default, the startup configuration file name is not configured for a DHCP client.



Format
------

**dhcp server bootfile** *bootfile*

**dhcp server bootfile cipher** *bootfile-cipher*

**undo dhcp server bootfile**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bootfile* | Specifies the name of the startup configuration file for a DHCP client. | The value is a string of 1 to 127 case-sensitive characters. If the string is enclosed in quotation marks, spaces are allowed in the string. |
| **cipher** *bootfile-cipher* | Specifies the name of the startup configuration file of a DHCP client as a ciphertext one. | The value is a string of case-sensitive characters. The entered ciphertext character string can be in explicit or ciphertext format. The ciphertext is a character string starting and ending with %@%# or %+%#. If the string is enclosed in quotation marks, spaces are allowed in the string.   * When you enter an explicit password, the value is a string of 1 to 127 characters. * When you enter a ciphertext password, the value is a string of 32 to 268 characters. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

Besides assigning IP addresses, a DHCP server can also provide the required network configuration parameters, such as the startup configuration file name for the DHCP clients. After the name of the startup configuration file is configured using the **dhcp server bootfile** command, the Offer and ACK packets sent from the DHCP server carry this file name. The DHCP client can acquire the startup configuration file from the specified server based on the file name.

**Prerequisites**

* IP addresses in the interface address pool have been configured using the **ip address** command.
* The DHCP server has been enabled on the interface using the **dhcp select interface** command.


Example
-------

# Configure the name of the startup configuration file as start.ini for the DHCP client on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 255.255.255.0
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server bootfile start.ini

```