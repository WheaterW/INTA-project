pim timer dr-switch-delay
=========================

pim timer dr-switch-delay

Function
--------



The **pim timer dr-switch-delay** command enables the PIM designated router (DR) switching delay function and configures a switching delay on an interface.

The **undo pim timer dr-switch-delay** command disables the PIM DR switching delay function on an interface.



By default, the PIM DR switching delay function is disabled on an interface.


Format
------

**pim timer dr-switch-delay** *interval*

**undo pim timer dr-switch-delay**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a DR switching delay. | The value is an integer ranging from 10 to 3600, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Without the PIM DR switching delay function, when the system triggers a PIM DR switchover, the switchover takes effect immediately, and therefore data forwarding will be interrupted during the switchover period. If the network is unstable, frequent switchovers occur, affecting the multicast forwarding performance. To address this issue, run the **pim timer dr-switch-delay** command to configure a PIM DR switching delay to implement non-stop service forwarding during the switchover.

**Configuration Impact**

After an outbound interface changes from a DR to a non-DR, the PIM DR switching delay function enables the interface to continue to forward data before the delay expires.

**Precautions**

The configuration of deleting or changing a DR switching delay takes effect only after the current switching delay expires.The **pim timer dr-switch-delay** command is mutually exclusive with the **pim silent** command.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Enable PIM DR switching delay on VLANIF 1 and set the delay to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim timer dr-switch-delay 20

```