display vrrp protocol-information
=================================

display vrrp protocol-information

Function
--------



The **display vrrp protocol-information** command displays VRRP information.




Format
------

**display vrrp protocol-information**


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

The display vrrp protocol-information command displays VRRP information on the device as required.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display VRRP information.
```
<HUAWEI> display vrrp protocol-information
 VRRP protocol information is shown as below:
    VRRP protocol version : V3
    Send advertisement packet mode : send v3 only

```

**Table 1** Description of the **display vrrp protocol-information** command output
| Item | Description |
| --- | --- |
| VRRP protocol version | VRRP version:   * V2: VRRPv2. * V3: VRRPv3. |
| Send advertisement packet mode | Mode in which VRRP Advertisement packets are sent. The options are as follows:   * send v2 only: Only VRRPv2 packets are sent. * send v3 only: Only VRRPv3 packets are sent. * send v2v3 both: Both VRRPv2 and VRRPv3 packets are sent. |