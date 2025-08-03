remark dscp
===========

remark dscp

Function
--------



The **remark dscp** command configures an action of re-marking the DSCP priority in IP packets in a traffic behavior.

The **undo remark dscp** command deletes the configuration.



By default, an action of re-marking the DSCP priority in IP packets is not configured in a traffic behavior.


Format
------

**remark dscp** { *dscp-value* | *dscp-name* }

**undo remark dscp**

**undo remark dscp** { *dscp-value* | *dscp-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dscp-value* | Specifies the DSCP priority in IP packets. | The value is an integer that ranges from 0 to 63. A larger value indicates a higher priority. |
| *dscp-name* | Specifies the DSCP priority name in IP packets. | The value can be ef, af11, af12, af13, af21, af22, af23, af31, af32, af33, af41, af42, af43, cs1, cs2, cs3, cs4, cs5, cs6, cs7, or default. |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To provide differentiated services based on the DSCP priority, run the **remark dscp** command to configure the device to re-mark the DSCP priority in IP packets in a traffic behavior.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing DSCP priority re-marking.

**Precautions**

* For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T and CE6863E-48S8CQ, the **remark dscp** command configured in the inbound direction does not take effect for broadcast and multicast packets.
* Traffic behaviors defining remark dscp and remark 8021p can be configured in the same traffic policy and take effect at the same time.
* If you run the **remark dscp** command in the same traffic behavior view multiple times, only the latest configuration takes effect.
* The **remark dscp** command can only change the DSCP priority of packets but not queues where packets are scheduled. To change the queues where packets are scheduled, run the **remark local-precedence** command.
* If a traffic policy containing remark dscp is applied to an interface in the inbound direction and the **qos phb marking dscp enable** command is run to enable mapping from PHBs to DSCP priorities for outgoing packets, the **qos phb marking dscp enable** command takes effect preferentially. If a traffic policy containing remark dscp is applied to an interface in the outbound direction and the **qos phb marking dscp enable** command is run to enable mapping from PHBs to DSCP priorities for outgoing packets, the **remark dscp** command takes effect preferentially.


Example
-------

# Re-mark the DSCP priority in IP packets with 56 in the traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] remark dscp 56

```