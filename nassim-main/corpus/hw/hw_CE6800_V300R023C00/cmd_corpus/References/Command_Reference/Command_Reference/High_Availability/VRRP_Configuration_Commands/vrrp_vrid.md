vrrp vrid
=========

vrrp vrid

Function
--------



The **vrrp vrid** command configures a VRRP backup group.

The **undo vrrp vrid** command deletes a VRRP backup group.



By default, no VRRP backup group is configured.


Format
------

**vrrp vrid** *virtual-router-id* [ **virtual-ip** *virtual-address* ]

**undo vrrp vrid** *virtual-router-id* [ **virtual-ip** *virtual-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| **virtual-ip** *virtual-address* | Specifies the virtual IP address of a VRRP backup group. The virtual IP address and the IP address of the interface where the VRRP backup group resides must be on the same network segment.  If the VRRP backup group is an LBRG member group, you do not need to assign a virtual IP address to the VRRP backup group. | The value is in dotted decimal notation. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A VRRP backup group can be used to implement gateway redundancy without causing networking changes. The VRRP backup group uses the master device to forward traffic along an active link. One virtual IP address serves one separate user group, in which users have the same reliability requirements. This setting helps prevent the default gateway addresses from varying according to location changes of VRRP routers. A maximum of 16 virtual IP addresses can be configured for each VRRP group.A VRRP backup group works in either master/backup or load balancing mode.

* In master/backup mode, a single VRRP backup group works and consists of a master device and one or more backup devices. The master and backup devices have different priorities. The master device has the highest priority among all devices in the backup group. If the network is working properly, the master device transmits all services. If the master device fails, a backup device with a higher priority than others takes over traffic.
* In load balancing mode, two or more VRRP backup groups are set up and their master devices forward traffic. These master devices load-balance traffic for various users.If VRRP backup groups need to work in load balancing mode, repeat this step to configure two or more VRRP backup groups on the interface and assign different VRIDs to them. In addition, virtual IP addresses of VRRP backup groups must be different.

**Follow-up Procedure**

After a VRRP backup group is configured, you can optimize VRRP performance by operations such as changing VRRP packet attributes or the interval at which VRRP packets are sent. This improves VRRP link stability.

**Precautions**



If all virtual IP addresses in a VRRP group are deleted, the system automatically deletes the VRRP group.The VRRP group to be configured as an LBRG must have been assigned a virtual IP address.After this command is run on an interface, when the ARP entries learned by the interface are aged, the device sends ARP aging probe messages with the source IP address being the interface's IP address. The virtual IP address of the interface is not used as the source IP address.A maximum of 16 virtual IP addresses can be configured for each VRID.If multiple vrrp vrid commands are configured in the interface view, the ARP fast reply function does not take effect on the interface.VRRP cannot be configured together with MUX VLAN.




Example
-------

# Configure a virtual IP address for an existing VRRP group.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.10.10.11

```

# Configure a VRRP backup group.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.10.10.10

```