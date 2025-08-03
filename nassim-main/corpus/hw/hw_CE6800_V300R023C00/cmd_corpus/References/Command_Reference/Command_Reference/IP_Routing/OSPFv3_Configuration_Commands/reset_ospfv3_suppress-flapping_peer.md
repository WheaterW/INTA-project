reset ospfv3 suppress-flapping peer
===================================

reset ospfv3 suppress-flapping peer

Function
--------



The **reset ospfv3 suppress-flapping peer** command configures an interface to exit OSPFv3 neighbor relationship flapping suppression.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ospfv3** *process-id* **suppress-flapping** **peer** [ *interface-name* | *interface-type* *interface-number* ]

**reset ospfv3** *process-id* **suppress-flapping** **peer** [ *interface-name* | *interface-type* *interface-number* ] **notify-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the interface number. | - |
| **notify-peer** | Instructs neighbors to exit from OSPF neighbor relationship flapping suppression too. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the fault that causes OSPFv3 neighbor relationship flapping is rectified, you can run the **reset ospfv3 suppress-flapping peer** command to configure an OSPFv3 interface to exit the neighbor relationship flapping suppression. Interfaces exit from flapping suppression in the following scenarios:

* The suppression timer expires.
* The OSPFv3 process is reset.
* The **reset ospfv3 suppress-flapping peer** command is run to configure the device to exit flapping suppression.
* The **reset ospfv3 peer** command is run to restart the OSPFv3 neighbor.
* OSPFv3 neighbor relationship flapping suppression is disabled globally using the suppress-flapping peer disable (OSPFv3) command.If notify-peer is specified when the command is run on a device, the device sends Hello packets in which HelloInterval and RouterDeadInterval are 0s to its neighbors to instruct the neighbors to exit OSPFv3 neighbor relationship flapping suppression too. If the neighbors fail to receive such Hello packets, the function of notify-peer does not take effect. To configure the neighbors to exit OSPFv3 neighbor relationship flapping suppression, run the **reset ospfv3 suppress-flapping peer** command on them.

Example
-------

# Configure interfaces to exit OSPFv3 neighbor relationship flapping suppression.
```
<HUAWEI> reset ospfv3 1 suppress-flapping peer

```