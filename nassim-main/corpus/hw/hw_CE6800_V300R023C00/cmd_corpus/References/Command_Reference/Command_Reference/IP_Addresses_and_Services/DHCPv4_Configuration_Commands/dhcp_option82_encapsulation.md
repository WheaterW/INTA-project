dhcp option82 encapsulation
===========================

dhcp option82 encapsulation

Function
--------



The **dhcp option82 encapsulation** command configures suboptions inserted into the DHCP Option 82 field.

The **undo dhcp option82 encapsulation** command restores the default suboptions inserted into the DHCP Option 82 field.



By default, the circuit-id (CID) suboption, remote-id (RID) suboption, subscriber-id (SID) suboption, and vendor-defined suboption in the Sub9 field are inserted into the DHCP Option 82 field.

In other views, the function of inserting suboptions into the DHCP Option 82 field is disabled by default.




Format
------

**dhcp option82 encapsulation** { **circuit-id** | **remote-id** | **vendor-specific-id** | **subscriber-id** } \*

**undo dhcp option82 encapsulation**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **circuit-id** | Inserts the circuit-id suboption. | - |
| **remote-id** | Inserts the remote-id suboption. | - |
| **vendor-specific-id** | Inserts the vendor-specific suboption in the Sub9 field. | - |
| **subscriber-id** | Inserts the subscriber-id (SID) suboption. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLAN view,Bridge domain view,Interface group view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This function is used on the DHCP relay agent. Option 82 records the location of a DHCP client. A device adds Option 82 to a DHCP request message to send the location of a DHCP client to the DHCP server. This enables the DHCP server to allocate a proper IP address and other configurations to the client based on the content of Option 82, implementing security control on the client. The administrator can run this command to configure the device to insert one or more of the circuit-id suboption, remote-id suboption, subscriber-id suboption and vendor-specific suboption in the Sub9 field into the DHCP Option 82 field. After the command is executed, if the format of the sub-option to be inserted is not configured, the sub-option is not inserted by default.The configuration in the interface view takes precedence over that in the VLAN view. The configuration in the VLAN view takes precedence over that in the BD view. The configuration in the BD view takes precedence over that in the system view. If the default configuration is used in all views, the configuration in the system view takes effect.

**Prerequisites**

The DHCP function has been enabled in the system view using the **dhcp enable** command. Enable the function of adding the Option 82 field to DHCP messages.


Example
-------

# Configure the circuit-id suboption to be inserted into the DHCP Option 82 field on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] dhcp option82 insert enable
[*HUAWEI-100GE1/0/1] dhcp option82 encapsulation circuit-id

```