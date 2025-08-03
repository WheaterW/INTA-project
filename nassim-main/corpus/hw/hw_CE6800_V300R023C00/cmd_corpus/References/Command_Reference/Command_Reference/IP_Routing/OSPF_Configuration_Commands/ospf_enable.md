ospf enable
===========

ospf enable

Function
--------



The **ospf enable** command enables OSPF on the interface.

The **undo ospf enable** command disables OSPF from the interface.



By default, OSPF is not enabled on interfaces.


Format
------

**ospf enable** [ *process-id* ] **area** { *area-id* | *areaidipv4* }

**undo ospf enable** [ *process-id* ] **area** { *area-id* | *areaidipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The·value·is·an·integer·ranging·from·1·to·4294967295.·The·default·value·is·1. |
| **area** *area-id* | Specifies an area ID in the format of a decimal integer. | The value is an integer ranging from 0 to 4294967295. |
| *areaidipv4* | Specifies an area ID in the format of an IP address. | The value is in dotted decimal notation. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **ospf enable** command enables OSPF on an interface and its configuration takes precedence over the **network** command configuration.The **undo ospf enable** command disables OSPF from an interface. After this command is run, the network configuration on the interface takes effect automatically.

**Configuration Impact**

Switching between the **ospf enable** command and the **network** command causes the protocol status of the interface to go down or up.To prevent service loss or system breakdown caused by the number of enabled IGP interfaces exceeding the specified specification during system running, the system controls the number of enabled IGP interfaces. An alarm is generated in the following situations:

* The number of IGP-enabled interfaces is greater than the independent IGP specification, that is, the number of IS-IS interfaces plus the number of OSPF interfaces x 4 / 3 > independent IGP specification.
* The number of IGP-enabled interfaces is not greater than the independent IGP specification but greater than the combined IGP specification. In addition, the number of BGP-enabled interfaces is greater than the combined BGP specification.The independent IGP specification is greater than the combined specification. The idependent IGP specifications, combined specifications, and combined BGP specifications vary according to products. For details, contact Huawei engineers.

**Precautions**

The area specified in the **ospf enable** command must have been created. Otherwise, the configuration does not take effect.The configured interface and the OSPF process must be in the same VPN.

* The **ospf enable** command can be configured on an interface before an OSPF process is created. The interface specified in the **ospf enable** command and the created OSPF process must be in the same VPN.
* If a process is created before the **ospf enable** command is run on an interface, the process of the interface and existing process must belong to the same VPN. Otherwise, the **ospf enable** command cannot be run.
* If no OSPF process is created, interfaces that belong to different VPN instances cannot be added to the same OSPF process.


Example
-------

# Enable the interface in the specified OSPF area.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0

```