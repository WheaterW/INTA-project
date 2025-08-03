ospfv3 advertise max-cost
=========================

ospfv3 advertise max-cost

Function
--------



The **ospfv3 advertise max-cost** command configures a device to change the costs of all its OSPF LSA to be advertised to the maximum value.

The **undo ospfv3 advertise max-cost** command cancels this configuration.



By default, a device does not change the cost of any of its OSPFv3 LSAs to be advertised to the maximum value.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 advertise max-cost**

**undo ospfv3 advertise max-cost**


Parameters
----------

None

Views
-----

maintenance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In an M-LAG scenario where an M-LAG member device needs to be maintained, run the **ospfv3 advertise max-cost** command to configure the device to change the costs of all its OSPFv3 LSAs to be advertised to the maximum value so that the other devices on the network can be instructed not to use this device to forward data. In this way, service traffic can be switched to the other M-LAG member device in advance. To switch the service traffic back to the original M-LAG member device after maintenance is complete, run the **undo ospfv3 advertise max-cost** command to restore the original costs of these OSPFv3 LSAs. Using the **ospfv3 advertise max-cost** command and its undo form in this scenario prevents traffic loss.

**Precautions**

After the **ospfv3 advertise max-cost** command is run, the device changes the costs of all OSPFv3 LSAs to be advertised to the maximum values. The costs of Router-LSAs (Type 1) will be increased to 65535, whereas the costs of Inter-Area-Prefix-LSAs (Type 3), Inter-Area-Router-LSAs (Type 4), AS-External-LSAs (Type 5), and NSSA-LSAs (Type 7) are all increased to 16711680.


Example
-------

# Configure a device to change the costs of all its OSPFv3 LSAs to be advertised to the maximum value.
```
<HUAWEI> system-view
[~HUAWEI] maintenance
[~HUAWEI-maintenance] ospfv3 advertise max-cost

```