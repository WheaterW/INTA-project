pim bfd
=======

pim bfd

Function
--------



The **pim bfd** command enables BFD for IPv4 PIM on an interface and adjusts PIM BFD parameters on the interface.

The **undo pim bfd** command disables BFD for IPv4 PIM on an interface and restores the default PIM BFD parameter settings on the interface.



By default, BFD for IPv4 PIM is not enabled on an interface.


Format
------

**pim bfd enable**

**pim bfd** { **min-tx-interval** *tx-value* | **min-rx-interval** *rx-value* | **detect-multiplier** *multiplier-value* } \*

**undo pim bfd enable**

**undo pim bfd** { **min-tx-interval** *tx-value* | **min-rx-interval** *rx-value* | **detect-multiplier** *multiplier-value* } \*

**undo pim bfd** { **min-tx-interval** | **min-rx-interval** | **detect-multiplier** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-tx-interval** *tx-value* | Specifies the minimum interval for transmitting BFD packets. | The value is an integer ranging from 3 to 1000. The default value is 1000. |
| **min-rx-interval** *rx-value* | Specifies the minimum interval for receiving BFD packets. | The value is an integer ranging from 3 to 1000. The default value is 1000. |
| **detect-multiplier** *multiplier-value* | Specifies the local multiplier of BFD packets. | The value is an integer ranging from 3 to 50. The default value is 3. |
| **enable** | Enables BFD for IPv4 PIM. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When using the **pim bfd enable** command, note the following:

* This command applies to non-broadcast multiple access (NBMA) interfaces and broadcast interfaces, not point-to-point (P2P) interfaces.
* Before configuring this command on an interface, you must run the **pim sm** command on the interface to enable PIM-SM. Running the **undo pim sm** command also disables BFD for IPv4 PIM on an interface.
* BFD for IPv4 PIM depends on the BFD protocol. If the **bfd** command is not run to enable global BFD, the session status is BFD global disable though PIM BFD sessions can be set up.NOTE:The **pim bfd enable** command is mutually exclusive with the **pim silent** command.

**Configuration Impact**

You can configure one or more parameters. Parameters that are not configured use their original values.

**Precautions**

Two PIM BFD ends negotiate the sending interval, receiving interval, and detection period for BFD packets based on the following mechanism:

* Actual sending interval and receiving interval for PIM BFD packets:
* Actual sending interval = max (local min-tx-interval, remote min-rx-interval)
* Actual receiving interval = max (remote min-tx-interval, local min-rx-interval)Actual detection period = remote detect-multiplier x max (remote min-tx-interval, local min-rx-interval)
* PIM BFD parameters can be configured on both the receive and transmit ends, and the configurations on the two ends are both effective.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Adjust the minimum interval for sending PIM BFD messages on Vlanif1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim bfd min-tx-interval 200

```

# Enable BFD for IPv4 PIM on Vlanif1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim sm
[*HUAWEI-Vlanif1] pim bfd enable

```