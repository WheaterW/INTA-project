dpfr enable(System view)
========================

dpfr enable(System view)

Function
--------



The **dpfr enable** command enables DPFR globally and sets the sampling rate and aging time.

The **undo dpfr enable** command disables DPFR globally and deletes the sampling rate and aging time.



By default, DPFR is not enabled globally.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dpfr enable** [ **sampler** *random-packet-number* ] [ **aging-time** *time-value* ]

**undo dpfr enable** [ **sampler** *random-packet-number* ] [ **aging-time** *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sampler** *random-packet-number* | Specifies the number of packets between two sampled packets in packet-based random sampling mode. In this mode, one packet is randomly sampled out of packet-number packets. | The value is an integer in the range from 1 to 65535. The default value is 1024. |
| **aging-time** *time-value* | Sets the aging time of the fault table. | The value is an integer in the range from 1 to 600. The default value is 5s. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After DPFR is enabled globally, the device enables local faulty link detection, local faulty link convergence, remote faulty link notification, remote faulty link relay, and remote faulty link convergence.

**Precautions**

To enable DPFR globally, you need to load the license in advance. DPFR and NSLB are mutually exclusive.


Example
-------

# Enable DPFR globally, set the sampling rate to 1024, and set the aging time to 10s.
```
<HUAWEI> system-view
[~HUAWEI] dpfr enable sampler 1024 aging-time 10

```