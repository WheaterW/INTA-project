mld snooping send-query enable
==============================

mld snooping send-query enable

Function
--------



The **mld snooping send-query enable** command enables the device to send MLD Query messages to non-router interfaces when the network topology changes.

The **undo mld snooping send-query enable** command disables the device from sending MLD Query messages to non-router interfaces when the network topology changes.



By default, the device is disabled from sending MLD Query messages to non-router interfaces when the network topology changes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping send-query enable**

**undo mld snooping send-query enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Allows the device to send MLD Query messages to non-router ports in response to network topology changes. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the network topology changes, the device receives a topology change event. By default, the device does not send MLD general Query messages in this case. The network topology change triggers ring network protocol recalculation, but multicast data messages cannot be switched to the new path immediately. To enable multicast data flows to be switched to the new forwarding path immediately after the network topology changes, run the mld snooping send-query enable command to enable the device to send MLD general Query messages to non-router interfaces upon topology changes to learn updated router interface information. This function therefore ensures non-stop forwarding of multicast data flows. Updated interface information includes:

* Router interfaces: In the MSTP protocol networking, MLD general Query messages are sent to all non-router interfaces.
* Member interfaces: After receiving MLD general Query messages, hosts that still require multicast services reply with MLD Report messages. The device then updates information about multicast member interfaces.

Example
-------

# Enable the device to send MLD Query messages to non-router interfaces when the network topology changes.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] mld snooping send-query enable

```