display interface troubleshooting
=================================

display interface troubleshooting

Function
--------



The **display interface troubleshooting** command displays interface diagnostic information, including alarms and causes of interface Down events, Up/Down transitions, and error packets, to rapidly locate the fault.




Format
------

**display interface troubleshooting** [ *interface-type* *interface-number* | *interface-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface type. | The value must be set according to the device configuration. |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |



Views
-----

User view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When an interface is faulty, you can run this command to view diagnostic information about the faulty interface to quickly locate the fault.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display diagnostic information about a specified interface.
```
<HUAWEI> display interface troubleshooting 10GE1/0/1
Note: Speed:value(Mbit/s) (negotiation status, configuration, port type, transceiver type)

Current state: DOWN(2020-06-18 10:47:14)
Speed: AUTO (force, -, 10GE, -)

```

# Display diagnostic information about all interfaces.
```
<HUAWEI> display interface troubleshooting
Note: Speed:value(Mbit/s) (negotiation status, configuration, port type, transceiver type)

10GE0/0/0 :
Current state: DOWN()
Speed: 10000 (force, -, 10GE, -)
Port exception information:
----------------------------------------------------------
Description               Time
----------------------------------------------------------
optical los               2021-07-31 02:49:01
----------------------------------------------------------

10GE1/0/1 :
Current state: DOWN()
Speed: 10000 (force, -, 10GE, -)

GE0/0/0 :
Current state: DOWN()
Speed: 1000 (auto, -, GE, -)
Negotiation: ENABLE

GE1/0/1 :
Current state: UP()
Speed: 1000 (auto, -, GE, -)
Loopback: INTERNAL
Negotiation: DISABLE

  ---- More ----

```

**Table 1** Description of the **display interface troubleshooting** command output
| Item | Description |
| --- | --- |
| Current state | Physical status of the interface. |
| Port exception information | Exception information about a specified interface. |
| Description | Symptom:   * link-flap: link flapping. * crc-error: CRC error. * non-huawei opt: An optical module that is not certified for is installed. * optical los: The optical module does not receive optical signals. * tx power high: The transmit optical power is too high. * tx power low: The transmit optical power is too low. * rx power high: The receive optical power is too high. * rx power low: The receive optical power is too low. * voltage high: The voltage of the optical module is too high. * voltage low: The voltage of the optical module is too low. * current high: The current of the optical module is too high. * current low: The current of the optical module is too low. * temper high: The temperature of the optical module is too high. * temper low: The temperature of the optical module is too low. * optType mismatch: optical module type mismatch. * transceiver loose: The optical module is not securely installed. |
| Time | Time when the fault occurred. |
| Speed | Interface rate information:   * value(Mbit/s): Current rate of the interface, in Mbit/s. * negotiation status: Rate auto-negotiation status. * force: forced rate. * auto: auto-negotiated rate. * configuration: Rate configuration. * port type: Actual interface type. * transceiver type: Optical module type. |
| Negotiation | Auto-negotiation mode of the interface.  This field is displayed only when the interface supports the auto-negotiation function. |
| Fec | FEC status of an interface.  This field is displayed only when the interface supports the FEC function. |
| Loopback | Loopback status of an interface.  This field is displayed only when the loopback command is configured on the interface. |
| Fault | Fault status of an interface:   * LOCAL FAULT: Signal receiving on the local interface is abnormal. * REMOTE FAULT: Signal receiving on the remote interface is abnormal.   This item is displayed only when exceptions including the optical signal fluctuation and signal interference occur. |