keepalive (Tunnel interface view)
=================================

keepalive (Tunnel interface view)

Function
--------



The **keepalive** command enables the Keepalive function for a GRE tunnel.

The **undo keepalive** command disables the Keepalive function for a GRE tunnel.



By default, the Keepalive function of a GRE tunnel is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**keepalive** [ **period** *period* [ **retry-times** *retry-times* ] ]

**undo keepalive** [ **period** *period* [ **retry-times** *retry-times* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **period** *period* | Specifies the interval for sending Keepalive messages. | The value is an integer ranging from 1 to 32767, in seconds. The default value is 5. |
| **retry-times** *retry-times* | Specifies the count of the unreachable counter. | The value is an integer ranging from 1 to 255. The default value is 3. |



Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent an unavailable GRE tunnel from being selected to transmit packets, enable the Keepalive function for GRE tunnels. Before the Keepalive function is enabled, the local tunnel interface may be Up even if the peer tunnel interface is unreachable. After the Keepalive function is enabled, the local tunnel interface goes Down if the peer tunnel interface is unreachable.After the Keepalive function is enabled on a GRE tunnel, the tunnel periodically sends Keepalive messages. The unreachable counter increases by one each time a message is sent. If no Keepalive response message is received when the value of the counter reaches the configured retry-times, the peer is considered unreachable.The Keepalive function immediately takes effect after the **keepalive** command is run on a GRE tunnel interface. The **undo keepalive** command disables this function.

**Prerequisites**

A tunnel interface has been created using the **interface tunnel** command.The tunnel encapsulation type has been set to GRE using the **tunnel-protocol gre** command.

**Configuration Impact**

If the **keepalive** command is run more than once, the latest configuration overrides the previous one.

**Follow-up Procedure**

After configuring the Keepalive function, you can run the **display keepalive packets count** command to check the numbers of Keepalive messages and Keepalive response messages sent and received by a GRE tunnel interface.

**Precautions**

The keepalive function is unidirectional. To enable the keepalive function on both ends of a tunnel, run the **keepalive** command on each end of the tunnel. The keepalive configuration takes effect on one end even if the function is disabled on the other end. However, it is recommended that you enable the keepalive function on both ends.Using the default values for the interval at which Keepalive packets are sent and the unreachability counter are recommended.


Example
-------

# Enable the Keepalive function for the GRE tunnel using default parameters.
```
<HUAWEI> system-view
[~HUAWEI] interface tunnel 100
[*HUAWEI-Tunnel100] tunnel-protocol gre
[*HUAWEI-Tunnel100] keepalive

```

# Enable the Keepalive function for the GRE tunnel. Specify the interval for sending Keepalive messages as 12 seconds and configure the unreachable counter to use default parameters.
```
<HUAWEI> system-view
[~HUAWEI] interface tunnel 100
[*HUAWEI-Tunnel100] tunnel-protocol gre
[*HUAWEI-Tunnel100] keepalive period 12

```

# Enable the Keepalive function for the GRE tunnel. Specify the interval for sending Keepalive messages as 12 seconds and set the retry-times to 4.
```
<HUAWEI> system-view
[~HUAWEI] interface tunnel 100
[*HUAWEI-Tunnel100] tunnel-protocol gre
[*HUAWEI-Tunnel100] keepalive period 12 retry-times 4

```