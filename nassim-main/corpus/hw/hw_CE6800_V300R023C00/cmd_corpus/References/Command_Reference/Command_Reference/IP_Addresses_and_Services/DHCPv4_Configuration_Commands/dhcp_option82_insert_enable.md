dhcp option82 insert enable
===========================

dhcp option82 insert enable

Function
--------



The **dhcp option82 insert enable** command enables a DHCP relay interface to insert Option 82 into DHCP packets.

The **undo dhcp option82 insert enable** command disables a DHCP relay interface from inserting Option 82 into DHCP packets.



By default, the function of inserting the Option 82 option to DHCP packets on the DHCP relay interface in inter-VPN scenarios is disabled.


Format
------

**dhcp option82** { **vss-control** | **link-selection** | **server-id-override** } **insert** **enable**

**undo dhcp option82** { **vss-control** | **link-selection** | **server-id-override** } **insert** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vss-control** | Indicates suboption 151 and suboption 152 that carry VPN information of a DHCP client. | - |
| **link-selection** | Indicates suboption 5 that carries the GiAddr address of the DHCP relay interface. | - |
| **server-id-override** | Indicates suboption 11 that carries the IP address of the DHCP relay interface. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the DHCP server and DHCP clients are in different VPNs, run the dhcp option82 command on the DHCP relay so that suboption 151, suboption 152, suboption 5, and suboption 11 can be inserted to the Option 82 field in DHCP request packets. In this manner, DHCP clients can properly obtain IP addresses from the DHCP server.The functions of the three suboptions are as follows:

* suboption151 and suboption 152: corresponds to the vss-control parameter that indicates VPN information of DHCP clients. Inserting this suboption to the Option 82 field is a proof of address allocation by the DHCP server.
* suboption5: corresponds to the link-selection parameter that indicates the GiAddr information of the DHCP relay interface. In inter-VPN scenarios, the **dhcp relay giaddr outgoing-interface-address** command is run to allow the DHCP reply packets to be properly sent to the DHCP relay. The suboption 5 allows the GiAddr information to be sent to the DHCP server. Then DHCP server then selects the desired address pool based on suboption151, suboption 152 and suboption5 and allocates IP addresses to DHCP clients.
* suboption11: corresponds to the server-id-override parameter that indicates the IP address of the DHCP relay interface. This suboption helps DHCP clients to obtain the correct destination IP address of renewal packets. Generally, when a DHCP client applies for an IP address for the first time, the DHCP reply packet sent by the DHCP server carries the Option 54 field that contains the IP address of the DHCP server. Upon receipt of the DHCP reply packet, the DHCP client uses this IP address as the destination IP address of renewal packets. Then, the DHCP client can interact with the DHCP server using unicast packets whenever it wants to renew the lease. In inter-VPN scenarios, if suboption 11 is inserted to the Option 82 field on the DHCP relay, the DHCP server encapsulates the content in suboption 11 into Option 54 in a DHCP reply packet. Upon receipt of the DHCP reply packet, the DHCP client uses the IP address of the DHCP relay interface as the destination IP address of renewal packets. In this manner, the DHCP client can properly send packets to the DHCP server through DHCP relay when it renews the lease.

**Prerequisites**

DHCP relay has been enabled on the VLANIF interface using the **dhcp select relay** command.

**Precautions**

If the DHCP server does not support suboption link-selection, configure a loopback interface on the DHCP relay agent, set the IP address of the loopback interface to the giaddr address, and bind the loopback interface to the VPN where the DHCP server resides.

This method may be time consuming when the live network is complex as this method requires the configuration of a loopback interface on each server or client. If the server supports the suboption function, you are advised to insert suboptions on the relay agent.

In inter-VPN scenarios where the server-id-override command is configured, only the first-hop DHCP request packets can be relayed. The multi-hop DHCP relay agent does not process received DHCP request packets.


Example
-------

# Enable the function of inserting suboption 5 and suboption 11 into DHCP packets on interface 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp option82 link-selection insert enable
[*HUAWEI-100GE1/0/1] dhcp option82 server-id-override insert enable

```