Configuring DHCP Binding Table Update
=====================================

The Dynamic Host Configuration Protocol (DHCP) binding table update function contains the client online status detection function and the DHCP snooping binding entry deletion function.

#### Usage Scenario

* If a client obtains an IP address and gets offline abnormally, the client cannot release its IP address by sending a DHCP release packet. To resolve this problem, you can configure client online status detection. The system periodically performs ARP probe on the IP address. If a user cannot be detected for the specified number of probes, the system will delete the DHCP binding entry corresponding to the user and construct a DHCP release packet to notify the DHCP server of releasing the user's IP address.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  This function can be configured only when DHCP snooping is enabled on a Layer 3 device.
* A DHCP snooping binding entry can be deleted manually if required. You can configure the client to send a release packet to the DHCP server to release the client's IP address.
  
  In client online status detection, the DHCP snooping binding table can be dynamically maintained and release packets can be constructed to instruct the server to release IP addresses. In DHCP snooping binding entry deletion, you can delete binding entries based on a VLAN, interface, BD, and IP address. You can also configure a device to construct release packets to instruct the server to release IP addresses.

#### Procedure

* Configure client online status detection.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**arp dhcp-snooping-detect enable**](cmdqueryname=arp+dhcp-snooping-detect+enable) command to enable client online status detection.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure dynamic DHCP snooping binding entry deletion.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**reset dhcp snooping bind-table**](cmdqueryname=reset+dhcp+snooping+bind-table) [ **vlan** *vlan-id* [ **interface** *interface-type* *interface-number* ] | **bridge-domain** *bd-id* | **interface** *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **public-net** | **ip-address** *ip-address* [ **interface** *interface-type* *interface-number* ] | **vsi** *vsi-name* ] [ **release** ] command to configure dynamic DHCP snooping binding entry deletion.
     
     If **release** is specified, you can configure the device to construct release packets to instruct the server to release IP addresses.
* Configure static DHCP snooping binding entry deletion.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**undo dhcp snooping bind-table static**](cmdqueryname=undo+dhcp+snooping+bind-table+static) [ **vlan** *vlan-id* [ **interface** *interface-type* *interface-number* ] | **interface** *interface-type* *interface-number* | **vsi** *vsi-name* | **ip-address** *ip-address* | **bridge-domain** *bd-id* ] command to configure static DHCP snooping binding entry deletion.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.