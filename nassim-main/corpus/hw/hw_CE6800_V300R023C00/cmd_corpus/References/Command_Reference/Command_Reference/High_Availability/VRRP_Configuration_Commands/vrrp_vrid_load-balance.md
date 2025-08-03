vrrp vrid load-balance
======================

vrrp vrid load-balance

Function
--------



The **vrrp vrid load-balance** command configures a specified VRRP backup group as a load-balance redundancy group (LBRG).

The **undo vrrp vrid load-balance** command restores an LBRG to a common VRRP backup group.



By default, no LBRG is configured in the system.


Format
------

**vrrp vrid** *virtual-router-id* **load-balance**

**undo vrrp vrid** *virtual-router-id* **load-balance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP backup group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When VRRP is used for gateway redundancy on the live network, the master device has heavy loads, whereas the backup devices have light loads. In traditional VRRP load balancing mode, multiple VRRP backup groups with virtual IP addresses are created and specified as gateways for different users to implement load balancing. To simplify user configurations, create an LBRG and specify it as a gateway for all users to implement load balancing.After you configure an LBRG, the LBRG returns different MAC addresses for ARP request packets from different users. The master device of a specified VRRP backup group forwards the traffic of a specified user.

**Prerequisites**

A VRRP backup group has been created and assigned a virtual IP address using the **vrrp vrid virtual-ip** command.

**Follow-up Procedure**

Run the **vrrp vrid join load-balance-vrrp vrid** command to add a VRRP backup group to the LBRG.

**Precautions**

The VRRP backup group to be configured as an LBRG must have been assigned a virtual IP address.


Example
-------

# Create a VRRP backup group and configure it as an LBRG.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.10.10.10
[*HUAWEI-100GE1/0/1] vrrp vrid 1 load-balance

```