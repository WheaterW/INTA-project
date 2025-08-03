reset ospf suppress-flapping peer
=================================

reset ospf suppress-flapping peer

Function
--------



The **reset ospf suppress-flapping peer** command configures an interface to exit OSPF neighbor relationship flapping suppression.




Format
------

**reset ospf** *process-id* **suppress-flapping** **peer** [ *interface-name* [ **all-areas** | **area** { *area-id* | *area-id-ipv4* } ] | *interface-type* *interface-number* [ **all-areas** | **area** { *area-id* | *area-id-ipv4* } ] ]

**reset ospf** *process-id* **suppress-flapping** **peer** [ *interface-name* [ **all-areas** | **area** { *area-id* | *area-id-ipv4* } ] | *interface-type* *interface-number* [ **all-areas** | **area** { *area-id* | *area-id-ipv4* } ] ] **notify-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| **all-areas** | Clears statistics of all OSPF areas. | - |
| **area** *area-id* | Specifies an area ID in the format of a decimal integer. | The value is an integer ranging from 0 to 4294967295. |
| *area-id-ipv4* | Specifies an area ID in the format of an IP address. | The value is in dotted decimal notation. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | - |
| **notify-peer** | Instructs neighbors to exit from OSPF neighbor relationship flapping suppression too. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Interfaces exit from flapping suppression in the following scenarios:

* The suppression timer expires.
* The corresponding OSPF process is reset.
* The **reset ospf suppress-flapping peer** command is run.
* An OSPF neighbor is reset using the **reset ospf peer** command.
* OSPF neighbor relationship flapping suppression is disabled globally using the suppress-flapping peer disable command in the OSPF view.If notify-peer is specified when the **reset ospf suppress-flapping peer** command is run on a device, the device sends Hello packets in which HelloInterval and RouterDeadInterval are 0s to its neighbors to instruct the neighbors to exit from OSPF neighbor relationship flapping suppression too. If the neighbors fail to receive such Hello packets, the function of notify-peer does not take effect. To configure the neighbors to exit OSPF neighbor relationship flapping suppression, run the **reset ospf suppress-flapping peer** command on them.The OSPF process or the specified interface exits from flapping suppression in the following scenarios:
* The suppression timer expires.
* The OSPF process is reset.
* The **reset ospf suppress-flapping peer** command is run.
* An OSPF neighbor is reset using the **reset ospf peer** command.
* OSPF neighbor relationship flapping suppression is disabled globally using the suppress-flapping peer disable (OSPF) command.If notify-peer is specified when the **reset ospf suppress-flapping peer** command is run on a device, the device sends Hello packets in which HelloInterval and RouterDeadInterval are 0s to its neighbors to instruct the neighbors to exit from OSPF neighbor relationship flapping suppression too. If the neighbors fail to receive such Hello packets, the function of notify-peer does not take effect. To configure the neighbors to exit OSPF neighbor relationship flapping suppression, run the **reset ospf suppress-flapping peer** command on them.

Example
-------

# Configure interfaces to exit OSPF neighbor relationship flapping suppression.
```
<HUAWEI> reset ospf 1 suppress-flapping peer

```

# Configure an OSPF multi-area adjacency interface to exit OSPF neighbor relationship flapping suppression.
```
<HUAWEI> reset ospf 1 suppress-flapping peer 100GE1/0/1 area 1

```