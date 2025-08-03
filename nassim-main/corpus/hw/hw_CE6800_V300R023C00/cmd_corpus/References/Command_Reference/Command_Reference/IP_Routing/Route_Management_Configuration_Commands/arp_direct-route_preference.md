arp direct-route preference
===========================

arp direct-route preference

Function
--------



The **arp direct-route preference** command configures a priority for ARP Vlink direct routes.

The **undo arp direct-route preference** command restores the default priority of ARP Vlink direct routes.



By default, the priority of ARP Vlink direct routes on VBDIF interfaces is 0, and the priority of ARP Vlink direct routes on other interfaces is 255.


Format
------

**arp direct-route preference** *preference-value*

**undo arp direct-route preference** [ *preference-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *preference-value* | Specifies a priority for ARP Vlink direct routes. | The value is an integer ranging from 0 to 255. |



Views
-----

100ge sub-interface view,10GE sub-interface view,1200ge sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, the priority of ARP Vlink direct routes on VBDIF interfaces is 0, and the priority of ARP Vlink direct routes on other interfaces is 255. To change the priority of ARP Vlink direct routes, run the **arp direct-route preference** command. ARP Vlink direct routes can be advertised by different routing protocols. If there are multiple ARP Vlink direct routes advertised by different routing protocols, you can run this command to change the priorities of these routes for route selection.



**Precautions**



The configuration of the **arp direct-route preference** command takes effect only if the **arp direct-route enable** command is run in the system view or interface view.Before running this command in the 100GE sub-interface view, Eth-Trunk sub-interface view, you need to configure the termination encapsulation mode of the sub-interface as Dot1q termination.




Example
-------

# Set the priority of ARP Vlink direct routes on a VLANIF interface to 100.
```
<HUAWEI> system-view
[~HUAWEI] vlan 200
[*HUAWEI-Vlan200] quit
[*HUAWEI] interface vlanif 200
[*HUAWEI-Vlanif200] arp direct-route preference 100

```

# Set the priority of ARP Vlink direct routes on a VBDIF interface to 100.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] quit
[*HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] arp direct-route preference 100

```