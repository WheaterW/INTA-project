hostname
========

hostname

Function
--------



The **hostname** command enables the OSPF dynamic hostname function.

The **undo hostname** command disables the OSPF dynamic hostname function.



By default, the OSPF dynamic hostname function is disabled.


Format
------

**hostname** [ *host-name* ]

**undo hostname**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *host-name* | Specifies the OSPF hostname. | The value is a string of 1 to 255 characters. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To facilitate network planning, configure hostnames to identify devices. After you run the **hostname** command to configure a dynamic hostname for a router, a device configured with a dynamic hostname generates a Router Information (RI) Opaque LSA. You can view the mapping between the router ID and hostname of the device through the RI Opaque LSA.The rules based on which RI Opaque LSAs are generated on ASBRs are as follows:

* If the device is an ASBR:
* If an ASBR is connected to an NSSA or a stub area, the ASBR generates and floods Type 10 RI Opaque LSAs (Type 10 RI LSAs) to the NSSA or stub area.
* If an ASBR is connected to a common area (non-NSSA or non-stub area), the ASBR generates and floods AS RI LSAs (Type 11 RI LSAs).
* If an ASBR is connected to an NSSA or a stub area but not to a common area, the ASBR does not generate AS-wide RI Opaque LSAs.
* If the device is an ABR or an intra-area device, it floods RI Opaque LSAs to its connected area.After all devices flood RI Opaque LSAs, you can run the **display ospf hostname-table** command on the devices that learn RI Opaque LSAs to view the mapping between router IDs and hostnames.

**Prerequisites**

The Opaque LSA capability has been enabled using the **opaque-capability enable** command.

**Precautions**

If you specify in this command, is advertised as the dynamic hostname. If no is specified in this command, the hostname specified in the **sysname** command is advertised as the dynamic hostname.


Example
-------

# Configure OSPF hostname BLR and enable the OSPF dynamic hostname function.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] opaque-capability enable
[*HUAWEI-ospf-100] hostname BLR

```