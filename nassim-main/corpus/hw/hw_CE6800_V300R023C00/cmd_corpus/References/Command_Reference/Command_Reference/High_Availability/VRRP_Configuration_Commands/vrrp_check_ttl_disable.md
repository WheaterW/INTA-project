vrrp check ttl disable
======================

vrrp check ttl disable

Function
--------



The **vrrp check ttl disable** command disables the check of TTL values in VRRP Advertisement packets.

The **undo vrrp check ttl disable** command enables the check of TTL values in VRRP Advertisement packets.



By default, TTL values in VRRP Advertisement packets are checked.


Format
------

**vrrp check ttl disable**

**undo vrrp check ttl disable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

As defined in relevant standards , the system checks TTL values in received VRRP Advertisement packets and drops the VRRP Advertisement packets if the TTL values are not 255.When a Huawei device interworks with a non-Huawei device, checking TTL values in VRRP Advertisement packets may cause the packets to be incorrectly dropped, because the TTL values in the VRRP Advertisement packets sent by non-Huawei devices may not be 255. To prevent this issue, run the vrrp un-check ttl command to disable the system from checking the TTL values in the VRRP Advertisement packets.

**Configuration Impact**

After the vrrp un-check ttl command is run, the TTL values of all VRRP Advertisement packets received by a specified interface are not checked.

**Precautions**

The configuration may cause attacks from invalid packets. Therefore, exercise caution when running the vrrp un-check ttl command.


Example
-------

# Disable the check of TTL values in VRRP Advertisement packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] vrrp vrid 1 virtual-ip 10.10.10.10
[*HUAWEI-100GE1/0/1] vrrp check ttl disable

```