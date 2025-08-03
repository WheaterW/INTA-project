application priority
====================

application priority

Function
--------



The **application priority** command specifies the service priority in the APP TLV of DCB packets.

The **undo application priority** command cancels the configuration.



By default, no service priority is configured for the APP TLV in DCB.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**application** { **fcoe** | **fip** | **iscsi** | { **ethtype** *ethtype-value* } | { [ **tcp** | **udp** ] **port** *port* } } **priority** *priority-value*

**undo application** { **fcoe** | **fip** | **iscsi** | { **ethtype** *ethtype-value* } | { [ **tcp** | **udp** ] **port** *port* } } **priority** *priority-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **fcoe** | Specifies the FCoE service priority. | - |
| **fip** | Specifies the FIP service priority. | - |
| **iscsi** | Specifies the ISCSI service priority. | - |
| **ethtype** *ethtype-value* | Specifies the Ethernet frame type service priority. | The value ranges from 0 to ffff in hexadecimal notation. |
| **tcp** | Specifies the TCP service priority. | - |
| **udp** | Specifies the UDP service priority. | - |
| **port** *port* | Specifies the TCP or UDP service priority of the port number. | The value is an integer that ranges from 0 to 65535. |
| **priority** *priority-value* | Specifies a service priority. | The value is an integer that ranges from 0 to 7. |



Views
-----

DCB app-profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable the DCB-enabled device to interwork with a non-Huawei device, create an APP profile, specify a service priority in the APP TLV in the APP profile, and apply the APP profile to an interface. To specify the service priority in the APP TLV, run this command.


Example
-------

# Set the FCoE service priority in the APP TLV to 4.
```
<HUAWEI> system-view
[~HUAWEI] dcb app-profile myapp
[*HUAWEI-dcb-app-myapp] application fcoe priority 4

```