dhcp client default-route preference
====================================

dhcp client default-route preference

Function
--------



The **dhcp client default-route preference** command configures the default route preference that a DHCP server delivers to a DHCP client.

The **undo dhcp client default-route preference** command restores the default value of the default route preference that a DHCP server delivers to a DHCP client.



By default, the default route preference that a DHCP server delivers to a DHCP client is 60.


Format
------

**dhcp client default-route preference** *preference-value*

**undo dhcp client default-route preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **preference** *preference-value* | Specifies the default route preference. | The value is an integer that ranges from 1 to 255. The default value is 60. A smaller value indicates a higher preference. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A DHCP client can obtain the default route through the DHCP server to dynamically update the routing table. The next-hop address of the default route is the DHCP client's gateway address carried in Option3.The default route that a DHCP server delivers is the open programming route(OPR) with the default preference 60. You can run the **dhcp client default-route preference** command to change the default route preference.


Example
-------

# In the view of interface 100GE1/0/1, set the default route preference that a DHCP server delivers to a DHCP client to 30.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 24
[*HUAWEI-100GE1/0/1] dhcp client default-route preference 30

```