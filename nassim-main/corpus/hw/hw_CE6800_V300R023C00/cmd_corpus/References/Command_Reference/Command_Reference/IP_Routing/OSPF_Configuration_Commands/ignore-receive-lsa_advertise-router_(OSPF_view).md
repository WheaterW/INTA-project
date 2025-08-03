ignore-receive-lsa advertise-router (OSPF view)
===============================================

ignore-receive-lsa advertise-router (OSPF view)

Function
--------



The **ignore-receive-lsa advertise-router** command configures the device to discard LSAs of a specified type.

The **undo ignore-receive-lsa advertise-router** command cancels the configuration of discarding LSAs of a specified type.



By default, the device is not configured to discard LSAs of a specified type.


Format
------

**ignore-receive-lsa advertise-router** *adv-rtr-id* [ **lsa-type** *type-value* [ **area** { *area-id* | *area-idipv4* } ] | **link-state-id** *ls-id* ] \*

**undo ignore-receive-lsa advertise-router** *adv-rtr-id* [ **lsa-type** *type-value* [ **area** { *area-id* | *area-idipv4* } ] | **link-state-id** *ls-id* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *adv-rtr-id* | Specifies the router ID of the LSA advertising device. | The value is in dotted decimal notation. |
| **lsa-type** *type-value* | LSA type. | The value is in hexadecimal notation. The value ranges from 0 to ffff. |
| **area** *area-id* | Specifies the area ID in decimal format. | The value is a decimal integer ranging from 0 to 4294967295. |
| *area-idipv4* | Specifies an area ID in IP address format. | The value is in dotted decimal notation. |
| **link-state-id** *ls-id* | Specifies the LSID of an LSA. | The value is in dotted decimal notation. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

1. When abnormal LSAs cause devices on the entire network to repeatedly restart and the LSA that causes protocol restarts is located, you can use this command as a last resort to prevent the devices from constantly restarting. However, incorrect configurations may cause loops.
2. If an LSA is an attack packet, is not supposed to appear in the local area, and causes serious problems such as device restarts, but it does not affect topology path computation, and the attack source cannot be found temporarily, you can run this command to temporarily filter out the LSA.
3. If an LSA is an attack packet, is not supposed to appear in the local area, causes serious problems such as restarts of network-wide devices, and affect topology path computation, you can run the command on all the devices on the network to configure them not to accept the LSA, preventing the LSA from participating in network-wide path computation.(Note: To filter out LSAs that affect topology path computation, they must be filtered out of all LSDBs on the entire network. If they are filtered out of only some of LSDBs, routing loops may occur.)
4. If an LSA is an unreachable residual LSA, the device that advertised the LSA is never reachable, and the LSA does not affect topology path computation, you can configure the device to filter out the LSA after receiving it from a neighbor.

**Configuration Impact**

If this command is incorrectly configured, services cannot be restored even if the **undo** command is run. In this case, you may need to reset the process or neighbor to restore services.To filter out the LSA that affects topology path computation, you must ensure that it is removed from all the LSDBs on the entire network. Otherwise, routing loops may occur.This command is not recommended for LSAs that exist on the network because normal LSAs may be filtered out.

**Precautions**

* This command is not used to defend against attacks. It violates the protocol processing principle and affects services. Therefore, exercise caution when running this command. If an attack source exists, you are advised to isolate the attack source. Attacked LSAs can have any key and cannot be defended by commands.
* If the fault is caused by a bug, you are advised to run this command temporarily. After installing the patch, run the **undo** command immediately, and check whether services are affected. If services are affected, re-establish all neighbor relationships to restore services.

Example
-------

# Discards LSAs advertised by 2.2.2.2.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] ignore-receive-lsa advertise-router 2.2.2.2
Warning: The operation will cause ospf lsdb not correct and can not recover ospf lsdb by undo command,need reset all neighbors to recover lsdb. Continue? [Y/N]:Y
[*HUAWEI-ospf-100]

```