nssa (OSPF area view)
=====================

nssa (OSPF area view)

Function
--------



The **nssa** command configures an NSSA.

The **undo nssa** command cancels the configuration of an NSSA.



By default, an OSPF area is not configured as an NSSA.


Format
------

**nssa** [ { **default-route-advertise** [ **backbone-peer-ignore** ] } | **no-import-route** | **no-summary** | **set-n-bit** | **suppress-forwarding-address** | **translator-always** | **translator-interval** *interval-value* | **zero-address-forwarding** ] \*

**undo nssa**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **default-route-advertise** | Configure the ABR or ASBR to generate default Type 7 LSAs and advertise them to the NSSA. | - |
| **backbone-peer-ignore** | Prevents the ABR from checking the neighbor status when the ABR generates default Type 7 LSAs and advertises them to the NSSA. Specifically, the ABR generates default Type 7 LSAs and advertises them to the NSSA as long as an interface that is Up exist in the backbone area. | - |
| **no-import-route** | Indicates that no external route is imported to an NSSA. | - |
| **no-summary** | Indicates that an ABR is prevented from sending summary LSAs to the NSSA. | - |
| **set-n-bit** | Indicates that the N-bit is set in DD packets. | - |
| **suppress-forwarding-address** | Sets the forwarding address (FA) of the Type 5 LSA translated by the NSSA ABR to 0.0.0.0. | - |
| **translator-always** | Indicates an ABR in an NSSA as an all-the-time translator. Multiple ABRs in an NSSA can be configured as translators. | - |
| **translator-interval** *interval-value* | Specifies the timeout period of a translator. | The value is an integer ranging from 1 to 120, in seconds. The default value is 40 seconds. |
| **zero-address-forwarding** | Sets the FA of the generated NSSA LSAs to 0.0.0.0 when external routes are imported by the ABR in an NSSA. | - |



Views
-----

OSPF area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you need to import AS external routes to an area and prevent these routes from consuming resources, you can configure the area as an NSSA. The NSSA imports AS external routes and transmits them to the entire OSPF AS.NSSA attributes must be configured on all devices in the NSSA using the **nssa** command. The application scenarios of the parameters are as follows:

* The conditions for generating default Type 7 LSAs and advertising them to the NSSA are as follows:

1. A neighbor in the Full state exists in the backbone area.
2. An interface in the Up state exists in the backbone area, and the default-route-advertise backbone-peer-ignore parameter is configured.
3. The nssa default-route-advertise parameter is configured.
4. The route 0.0.0.0 of another process exists in the local routing table.
5. The OSPF process is bound to a VPN instance, and the **vpn-instance-capability simple** command is not run in the OSPF process view.If condition 1, 2, or 5 is met, the ABR can generate default Type 7 LSAs and advertise them to the NSSA. If conditions 3 and 4 are met, the ASBR can generate default Type 7 LSAs and advertise them to the NSSA.

* If an ASBR also functions as an ABR, you can specify no-import-route in the command to prevent external routes imported using the **import-route** command from being advertised to the NSSA.
* To reduce the number of LSAs to be transmitted to the NSSA, set no-summary on an ABR. This prevents the ABR from transmitting summary LSAs (Type 3 LSAs) to the NSSA.After the **nssa default-route-advertise backbone-peer-ignore no-summary** command is run, an ABR generates both default Type 7 LSAs and default Type 3 LSAs as long as an interface in the Up state exists in the backbone area, regardless of whether a neighbor in the Full state exists. The default Type 3 LSAs take effect preferentially.
* After the set-n-bit keyword is set, the N-bit is set in the DD packets during the synchronization between the local device and neighbors.If there are multiple ABRs in an NSSA, the system automatically selects an ABR as the translator according to certain rules (generally, the device with the largest router ID is selected in the NSSA) to translate Type 7 LSAs into Type 5 LSAs. You can also configure the parameter translator-always on an ABR to specify the ABR as an all-the-time translator. To specify two ABRs for load balancing, configure the parameter translator-always on two ABRs to specify the ABRs as all-the-time translators. This prevents LSA flooding caused by translator role changes.
* The translator-interval parameter is used to ensure smooth translator switching. The interval-value value must be greater than the flooding period.The rules for setting the forwarding address of NSSA LSAs are as follows:

1. The primary IP address of an active interface in the NSSA is selected as the forwarding address of NSSA LSAs. The IP address of an interface suppressed by the **suppress-reachability** command is not selected as the forwarding address of NSSA LSAs.
2. The IP address of the loopback interface is preferred over the IP addresses of other interfaces. If the priorities are the same, the IP address of the interface with a smaller index is preferred.
3. When a new interface with a better IP address is available in the area, the LSA forwarding address is updated after a delay of 10s. When the IP address of the interface that functions as the FA is unavailable, the LSA forwarding address is updated immediately.

**Configuration Impact**

Configuring or deleting NSSA attributes may trigger routing updates in the area. A second configuration of NSSA attributes can be implemented or canceled only after a routing update is complete.

**Precautions**

* According to the FA selection rules of NSSA LSAs, the interface indexes are compared during FA selection. If the interface index changes after the restart, the FA address may change after the restart.
* You are advised to configure a loopback address for the device in the NSSA so that the loopback address can be automatically selected as the FA. If other devices have paths of the same cost to the device in the NSSA, load balancing is performed.
* When the last common area (not a stub area or NSSA) in an OSPF process is deleted, useless Type 5 LSAs on the local device in the area where LSAs are flooded are deleted immediately. The local device, however, still reserves useless Type 5 LSAs from other devices. These useless Type 5 LSAs are deleted only when the aging time reaches 3600s.

Example
-------

# Configure area 1 as an NSSA.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] nssa

```