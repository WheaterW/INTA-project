vrrp vrid backup-forward
========================

vrrp vrid backup-forward

Function
--------



The **vrrp vrid backup-forward** command enables backup devices to forward service traffic.

The **undo vrrp vrid backup-forward** command disables backup devices from forwarding service traffic.



By default, backup devices are disabled from forwarding service traffic.


Format
------

**vrrp vrid** *virtual-router-id* **backup-forward**

**undo vrrp vrid** *virtual-router-id* **backup-forward**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a mobile bearer network, a base station is connected to aggregation devices over the primary and secondary PWs and to NPEs over the active and standby links. A VRRP group is deployed on both NPEs. If the aggregation device on the active link fails, service traffic switches from the active link to the standby link immediately, but a master/backup VRRP switchover is performed between both NPEs after a delay. Therefore, service traffic is lost before the master/backup VRRP switchover is performed. To resolve this issue and meet carrier-class reliability requirements, run the **vrrp vrid backup-forward** command to enable the backup NPE to forward service traffic. After the configuration is complete, the backup NPE forwards service traffic before a master/backup VRRP switchover is performed, which prevents service traffic loss.

**Prerequisites**

A VRRP group has been created using the **vrrp vrid virtual-ip** command in the interface view.

**Configuration Impact**

After the **vrrp vrid backup-forward** command is run, backup devices forward service traffic with a virtual MAC address as a destination MAC address. If a downstream switch broadcasts a packet with a virtual MAC address as a destination MAC address, backup devices also forward this packet. As a result, duplicate traffic is sent. Do not run this command on a non-mobile bearer network to prevent duplicate traffic.

**Precautions**

You can configure backup devices to forward service traffic on the master and backup devices in a VRRP group.


Example
-------

# Create VRRP group 1 on 100GE 1/0/7 and enable backup devices to forward service traffic.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/7
[~HUAWEI-100GE1/0/7] undo portswitch
[*HUAWEI-100GE1/0/7] vrrp vrid 1 virtual-ip 10.1.1.100
[*HUAWEI-100GE1/0/7] vrrp vrid 1 backup-forward

```