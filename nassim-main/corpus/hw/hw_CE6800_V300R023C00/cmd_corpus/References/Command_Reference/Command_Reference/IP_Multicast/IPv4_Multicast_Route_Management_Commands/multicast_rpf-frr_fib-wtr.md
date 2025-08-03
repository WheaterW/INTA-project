multicast rpf-frr fib-wtr
=========================

multicast rpf-frr fib-wtr

Function
--------



The **multicast rpf-frr fib-wtr** command sets the wait-to-restore (WTR) time of multicast forwarding entries.



By default, the WTR time of multicast forwarding entries is 10 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast rpf-frr fib-wtr** *wtr-time*

**undo multicast rpf-frr fib-wtr**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *wtr-time* | Specifies the WTR time. | The value is an integer that ranges from 10 to 280. The default value is 10. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After PIM FRR is configured, a multicast routing entry with two inbound interfaces (primary and backup inbound interfaces) is generated. If the primary inbound interface fails (the link status or BFD status is Down), the corresponding multicast group accepts and forwards the multicast streams received from the backup inbound interface to quickly restore multicast services. If the primary inbound interface recovers (the link status or BFD status is Up) when the multicast routing entry has not been updated to an entry with a single inbound interface, the device waits for a time to restore (WTR) period before accepting and forwarding multicast streams received from the primary inbound interface. If the device accepts and forwards multicast streams received from the primary inbound interface when the upstream device is not ready, multicast traffic is interrupted. WTR can prevent this problem.The time required for the recovery of the multicast traffic received from the primary inbound interface is closely related to the number of multicast groups and CPU load. Therefore, you need to adjust the WTR time based on the number of multicast groups and CPU load. In the case of CPU light load (the CPU usage is lower than 50%), recommended configurations are as follows:

| Number of Multicast Groups | WTR Time (in Seconds) |
| --- | --- |
| 1â2000 | 10 (default value) |
| 2001â4000 | 20 |
| 4001â8000 | 40 |
| 8001â16000 | 80 |

For a multicast group for which the **rpf-frr** command is run in the PIM view, to ensure that traffic on the backup inbound interface is not interrupted during the WTR period, the device adjusts the delay for sending Prune messages to the upstream device. To ensure that traffic on the primary inbound interface recovers as soon as possible, the device adjusts the maximum delay for delivering new link forwarding entries and the delay for delivering forwarding entries of the backup inbound interface. The delays are adjusted to proper values in typical scenarios based on the configured WTR time, meet the performance requirement of minimizing packet loss during WTR switchback, and do not need to be manually modified. If adjustment is required in special cases, refer to the following suggestions:

| Command | Function | Configuration Suggestions |
| --- | --- | --- |
| rpf-prune-delay | Sets the delay for sending Prune messages to the upstream device. | Set the same value in all PIM views, and ensure that the value is greater than the WTR time. |
| rpf-switch-delay mode sm max-time | Sets the maximum delay for delivering new link forwarding entries. | Set the same value in all PIM views, and ensure that the value is less than the WTR time. |
| backup-rpf-switchover-delay | Sets the delay for delivering forwarding entries of the backup inbound interface. | Set the same value in all PIM views, and ensure that the value is greater than the WTR time. |

Improper configuration of the preceding delays may cause a large number of packets to be lost during the WTR period or when traffic is switched back to the primary inbound interface after the WTR period ends.


Example
-------

# Set the WTR time of PIM FRR forwarding entries to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast rpf-frr fib-wtr 20

```