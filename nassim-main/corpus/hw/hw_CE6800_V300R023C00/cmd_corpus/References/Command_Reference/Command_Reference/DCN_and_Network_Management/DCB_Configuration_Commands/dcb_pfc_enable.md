dcb pfc enable
==============

dcb pfc enable

Function
--------



The **dcb pfc enable** command applies a PFC profile to an interface.

The **undo dcb pfc enable** command deletes a PFC profile from an interface.



By default, no PFC profile is applied to an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**dcb pfc enable** [ *pfcprofile* ] [ **mode** { **auto** | **manual** } ]

**undo dcb pfc enable** [ *pfcprofile* ] [ **mode** { **auto** | **manual** } ]

For CE6885-LL (low latency mode):

**dcb pfc enable** [ *pfcprofile* ] [ **mode** **manual** ]

**undo dcb pfc enable** [ *pfcprofile* ] [ **mode** **manual** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pfcprofile* | Specifies the name of a PFC profile. | The PFC profile must already exist. |
| **mode** | PFC working mode.  If this parameter is not specified, PFC works in manual mode. | - |
| **auto** | Negotiation mode.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **manual** | Forcible mode. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In PFC, eight priority queues on the transmit interface of an uplink device correspond to eight buffers on the receive interface of a downlink device. When a receive buffer on the receive interface of the downlink device is to be congested, the downlink device sends a backpressure signal to the uplink device, requesting the uplink device to stop sending packets in the corresponding priority queue. After setting priorities for queues, run the **dcb pfc enable** command to enable PFC.The principles for setting mode { auto | manual } are as follows:

* auto: The local device and remote device exchange PFC parameters through DCBX. If PFC negotiation has succeeded, PFC takes effect. Otherwise, PFC does not work. DCB parameters of the remote device can be configured on the local device, if the remote device allows such configuration.The device does not allow DCB parameters of the remote device to be locally configured.
* manual: PFC parameters on the local and remote devices are configured manually and must be the same. If the remote device does not support DCBX, configure PFC to work in manual mode.

**Prerequisites**



PFC has been enabled globally using the **undo dcb pfc global disable** command. By default, PFC is enabled globally.A PFC profile has been created using the dcb pfc [ <pfcprofile> ] command and the PFC profile view has been displayed, or the view of an existing PFC profile has been displayed.For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ:The chip-level headroom buffer threshold has been set using the **qos buffer headroom-pool** command.



**Precautions**

If the PFC working mode is set to auto, you need to enable an interface to advertise or receive DCBX TLVs as follows:

* Run the **lldp enable** command in the system view to enable LLDP globally.
* Run the **lldp tlv-enable dcbx** command on the interface to enable the interface to advertise DCBX TLVs.When congestion occurs on an interface, the **dcb pfc enable** or **undo dcb pfc enable** command may fail to be executed. Reconfigure the PFC profile when the interface is not congested or after the interface is restarted.


Example
-------

# Apply the PFC profile default to 100GE1/0/1 and configure PFC to work in forcible mode. (CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] dcb pfc enable mode manual

```

# Apply the PFC profile default to 100GE1/0/1 and configure PFC to work in forcible mode. (CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ)
```
<HUAWEI> system-view
[~HUAWEI] qos buffer headroom-pool size 4 mbytes slot 1
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] dcb pfc enable mode manual

```