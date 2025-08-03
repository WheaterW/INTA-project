dhcp option82 vendor-specific format(interface view)
====================================================

dhcp option82 vendor-specific format(interface view)

Function
--------



The **dhcp option82 vendor-specific format** command configures a format for the Option 82 suboption 9 carried in a DHCP packet.

The **undo dhcp option82 vendor-specific format** command cancels the configuration.



By default, the format of the suboption 9 in DHCP option 82 field is not configured.


Format
------

**dhcp option82 vendor-specific format vendor-sub-option** *sub-option-num* **source-ip-address** *ip-address*

**undo dhcp option82 vendor-specific format vendor-sub-option** *sub-option-num* **source-ip-address** *ip-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-ip-address** *ip-address* | Specifies an IP address to be inserted into the Vendor-Specific suboption (suboption 9). | The value is in dotted decimal notation. |
| **vendor-sub-option** *sub-option-num* | Specifies a value for the Vendor-Specific suboption (suboption 9). | The value is an integer ranging from 1 to 255. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

DHCP users obtain IP addresses from DHCP servers on different subnets through the DHCP relay agent deployed on the gateway. Users on the same subnet have the same gateway address. If the DHCP server uses the gateway address as the destination address of response packets, the response packets cannot be sent to the gateway to which the users belong. As a result, the users fail to go online. In this case, you can run this command on the DHCP relay agent to configure the DHCP relay agent to insert the Sub9 suboption (vendor-specific) into Option 82 and run the dhcp relay information enable command to enable the DHCP relay agent to support Option 82. The DHCP relay agent encapsulates the IP address that uniquely identifies the gateway location into a DHCP Request packet and sends the packet to the DHCP server. The DHCP server that supports Option 82 reserves Option 82 in the response packet. If the response packet is sent back to another gateway, the DHCP relay agent on the gateway forwards the packet to the correct gateway based on the IP address carried in the Sub9 suboption of Option 82.

**Precautions**

If the Vendor-Specific suboption (suboption 9) is configured in both the system view and interface view, the configuration in the interface view takes effect.The length of the Option 82 suboption 9 is subject to the configuration in the interface view and that in the system view. If the Option 82 field is too long after the suboption 9 is inserted, the suboption 9 will not be carried in the Option 82 field.When this command is run to deploy gateways functioning as a DHCP relay, set the <sub-option-num> parameter to the same value for different gateways.


Example
-------

# Configure the Vendor-Specific suboption (suboption 9) as 10 and insert the source IP address 10.1.1.1 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp relay information enable
[*HUAWEI-100GE1/0/1] dhcp option82 vendor-specific format vendor-sub-option 10 source-ip-address 10.1.1.1

```