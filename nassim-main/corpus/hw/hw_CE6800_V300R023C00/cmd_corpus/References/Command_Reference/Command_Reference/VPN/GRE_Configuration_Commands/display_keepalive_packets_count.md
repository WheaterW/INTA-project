display keepalive packets count
===============================

display keepalive packets count

Function
--------



The **display keepalive packets count** command displays the numbers of Keepalive messages and Keepalive response messages sent and received by a GRE tunnel interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display keepalive packets count**


Parameters
----------

None

Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After configuring the Keepalive function using the **keepalive** command, you can run the **display keepalive packets count** command to check the numbers of Keepalive messages and Keepalive response messages sent and received by a GRE tunnel interface.

**Prerequisites**

The Keepalive function has been enabled for the GRE tunnel using the **keepalive** command.

**Follow-up Procedure**

If the numbers of Keepalive messages and Keepalive response messages sent and received by a GRE tunnel interface do not change within the specific period, check whether the GRE tunnel works properly.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the numbers of Keepalive messages and Keepalive response messages sent and received by the GRE tunnel interface Tunnel 10.
```
<HUAWEI> system-view
[~HUAWEI] interface Tunnel 10
[*HUAWEI-Tunnel10] tunnel-protocol gre
[*HUAWEI-Tunnel10] commit
[~HUAWEI-Tunnel10] display keepalive packets count
Send 0 keepalive packets to peers, Receive 0 keepalive response packets from peers
Receive 0 keepalive packets from peers, Send 0 keepalive response packets to peers.

```

**Table 1** Description of the **display keepalive packets count** command output
| Item | Description |
| --- | --- |
| Send 0 keepalive packets to peers | 0 Keepalive messages are sent to the peer. |
| Send 0 keepalive response packets to peers | 0 Keepalive response messages are sent to the peer. |
| Receive 0 keepalive response packets from peers | 0 Keepalive response messages are received from the peer. |
| Receive 0 keepalive packets from peers | 0 Keepalive messages are received from the peer. |