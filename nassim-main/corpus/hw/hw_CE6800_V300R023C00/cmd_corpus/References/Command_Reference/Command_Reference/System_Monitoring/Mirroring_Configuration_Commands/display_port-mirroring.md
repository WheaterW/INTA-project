display port-mirroring
======================

display port-mirroring

Function
--------



The **display port-mirroring** command displays the mirroring configuration on the device.




Format
------

**display port-mirroring**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After observing ports and mirrored ports are configured on the device, you can run the display port-mirroring command to check detailed mirroring configuration on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the packet mirroring configuration.
```
<HUAWEI> display port-mirroring
  Observe port mirroring:
  -----------------------------------------------------------------------------
  MirroringPort         Direction        ObservePort : Interface
  -----------------------------------------------------------------------------
  100GE1/0/2            Inbound                    1 : 100GE1/0/1
  -----------------------------------------------------------------------------
  Observe port group mirroring:
  -----------------------------------------------------------------------------
  MirroringPort         Direction        ObserveGroup
  -----------------------------------------------------------------------------
  100GE1/0/3            Inbound                     1
  -----------------------------------------------------------------------------
  Traffic mirroring:
  -----------------------------------------------------------------------------
  TrafficBehavior                        ObservePort : Interface
  -----------------------------------------------------------------------------
  b1                                               1 : 100GE1/0/1
  -----------------------------------------------------------------------------
  VLAN mirroring:
  -----------------------------------------------------------------------------
  VLAN                  Direction        ObservePort : Interface
  -----------------------------------------------------------------------------
  VLAN 10               Inbound                    1 : 100GE1/0/1
  -----------------------------------------------------------------------------

```

**Table 1** Description of the **display port-mirroring** command output
| Item | Description |
| --- | --- |
| MirroringPort | Mirrored ports. |
| Direction | Direction of mirrored packets.   * Inbound: indicates incoming packets. * Outbound: indicates outgoing packets. |
| ObservePort : Interface | Observing port that mirrored packets are sent to. |
| TrafficBehavior | Traffic behavior of traffic mirroring. |
| ObserveGroup | Observing port group that mirrored packets are sent to. |
| VLAN | VLAN ID of VLAN mirroring. |