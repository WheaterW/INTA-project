dhcp relay information strategy
===============================

dhcp relay information strategy

Function
--------



The **dhcp relay information strategy** command configures the strategies used by a DHCP relay agent to process Option 82 information.

The **undo dhcp relay information strategy** command restores the default setting.



By default, the strategy used by a DHCP relay agent to process Option 82 information is replace.


Format
------

**dhcp relay information strategy** { **drop** | **keep** | **replace** }

**undo dhcp relay information strategy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **drop** | Configures the DHCP relay agent to drop Option 82 information. | - |
| **keep** | Configures the DHCP relay agent to keep Option 82 information. | - |
| **replace** | Configures the DHCP relay agent to replace Option 82 information. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to the DHCP relay agent. When DHCP Request messages carry Option 82 information, the DHCP server can locate user positions accurately and assign IP addresses to users using different policies. When a DHCP relay agent receives DHCP Request messages, it uses one of the following strategies to process Option 82 information:

* Drop:
* If the received DHCP message does not carry an Option 82 field, the DHCP relay agent forwards the message directly without processing it.
* If the received DHCP message carries an Option 82 field, the DHCP relay agent drops the Option 82 field and forwards the message.
* Keep:
* If the received DHCP message does not carry an Option 82 field, the DHCP relay agent forwards the message directly without processing it.
* If the received DHCP message carries an Option 82 field, the DHCP relay agent keeps the Option 82 field and forwards the message.
* Replace:
* If the received DHCP message does not carry an Option 82 field, the DHCP relay agent inserts an Option 82 field configured by the administrator into the received message and forwards the message.
* If the received DHCP message carries an Option 82 field, the DHCP relay agent replaces it with the Option 82 field configured by the administrator and forwards the message.

**Prerequisites**

DHCP relay has been enabled by running the **dhcp select relay** command in the interface view.The Option 82 function has been enabled for the DHCP relay agent by using the **dhcp relay information enable** command.


Example
-------

# Configure the DHCP relay agent to drop Option 82 information on the 100GE1/0/1 interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp select relay
[*HUAWEI-100GE1/0/1] dhcp relay information enable
[*HUAWEI-100GE1/0/1] dhcp relay information strategy drop

```