redirect interface
==================

redirect interface

Function
--------



The **redirect interface** command configures an action of redirecting packets to an interface in a traffic behavior.

The **undo redirect** interface command deletes the redirection configuration.



By default, the action of redirecting packets to an interface is not configured in a traffic behavior.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**redirect interface tunnel** *tunnel-id*

**undo redirect interface tunnel** *tunnel-id*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**redirect interface** { *interface-type* *interface-number* | *interface-name* } [ **fail-action** **forward** ]

**undo redirect**

**undo redirect interface** { *interface-type* *interface-number* | *interface-name* } [ **fail-action** **forward** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **fail-action** | Specifies the action to be taken when the interface to which packets are redirected is Down. | - |
| **tunnel** *tunnel-id* | Specifies the ID of a GRE tunnel interface to which packets are redirected.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 0 to 4095. |
| *interface-type* | Specifies the type of the interface to which packets are redirected. | - |
| *interface-number* | Specifies the number of the interface to which packets are redirected. | - |
| *interface-name* | Specifies the name of the interface to which packets are redirected. | - |
| **forward** | Forwards packets according to the original forwarding process. | - |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the redirect interface command to configure an action of redirecting packets to an interface in a traffic behavior. For example, packets can be redirected to a firewall for security check.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing redirection to an interface.

**Precautions**

* A traffic policy containing the redirection action cannot be applied to the outbound direction.
* Generally, when a packet is redirected to an outbound interface, the outbound interface needs to be added to the VLAN corresponding to the packet.
* Packets can be redirected to physical interfaces and Eth-trunk interfaces.
* Traffic entering a Layer 2 sub-interface cannot be redirected to a Layer 2 Ethernet outbound interface.


Example
-------

# Configure an action of redirecting packets to 100GE 1/0/1 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] redirect interface 100GE 1/0/1

```