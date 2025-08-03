dhcp client client-id
=====================

dhcp client client-id

Function
--------



The **dhcp client client-id** command configures an identifier for a DHCP client.

The **undo dhcp client client-id** command restores the default identifier of a DHCP client.



By default, the identifier of a DHCP client is the client's MAC address.


Format
------

**dhcp client client-id** *client-id*

**undo dhcp client client-id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *client-id* | Specifies the identifier of a DHCP client. | The value is a string of 2 to 64 case-sensitive characters, spaces supported. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The dhcp client client-id command configures an identifier for a DHCP client. The identifier is encapsulated into a DHCP Request message. When a DHCP client requests an IP address from a DHCP server, the DHCP server obtains the identifier of the DHCP client and assigns an IP address to the DHCP client with the specified identifier.


Example
-------

# Set the identifier of the DHCP client to huawei\_client on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp client client-id huawei_client

```