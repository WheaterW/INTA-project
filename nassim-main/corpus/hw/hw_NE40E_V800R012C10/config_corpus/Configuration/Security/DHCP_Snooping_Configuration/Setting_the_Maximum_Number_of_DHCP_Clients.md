Setting the Maximum Number of DHCP Clients
==========================================

This section describes how to configure the maximum number of DHCP snooping users on an interface.

#### Usage Scenario

After the number of login users reaches the maximum number, no users can obtain IP addresses. To prevent malicious IP address application, configure the maximum number of DHCP snooping users.

When the number of access users on a DHCP snooping device reaches the maximum, the device checks whether the IP address in the DHCP ACK packet exists in the binding table to determine whether the user is a new user. In this case, you can configure strict MAC address check for DHCP snooping. DHCP snooping can determine whether the user is a new user based on the MAC address in the DHCP Discover packet sent by the user. If the MAC address of the user does not exist in the DHCP snooping binding table, the user is not allowed to go online and packets are not sent to the DHCP server. This reduces the impact of excessive users on the DHCP server.


#### Pre-configuration Tasks

Before configuring the maximum number of DHCP snooping users, enable DHCP snooping and configure trusted interfaces.


#### Procedure

* Configure the maximum number of DHCP snooping users in a VLAN.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**dhcp snooping strict-check mac-address**](cmdqueryname=dhcp+snooping+strict-check+mac-address)
     
     DHCP snooping is enabled to strictly check the MAC addresses of login users.
  3. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     The VLAN view is displayed.
  4. Run [**dhcp snooping max-user-number**](cmdqueryname=dhcp+snooping+max-user-number) *max-user-number* [ **interface** *interface-type* *interface-number* ]
     
     The maximum number of DHCP snooping users is configured in the VLAN.
  5. (Optional) Run [**dhcp snooping alarm user-limit enable**](cmdqueryname=dhcp+snooping+alarm+user-limit+enable) [ **interface** *interface-type interface-number* ]
     
     The device is enabled to generate an alarm when the number of DHCP snooping users in the VLAN reaches the maximum.
  6. (Optional) Run [**dhcp snooping alarm user-limit threshold**](cmdqueryname=dhcp+snooping+alarm+user-limit+threshold) *threshold* [ **interface** *interface-type* *interface-number* ]
     
     The maximum number of DHCP snooping users is configured in the VLAN.
  7. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure the maximum number of DHCP snooping users for an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. (Optional) Run [**dhcp snooping strict-check mac-address**](cmdqueryname=dhcp+snooping+strict-check+mac-address)
     
     DHCP snooping is enabled to strictly check the MAC addresses of login users.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  4. Run [**dhcp snooping max-user-number**](cmdqueryname=dhcp+snooping+max-user-number) *max-user-number*
     
     The maximum number of DHCP snooping users is configured for the interface.
  5. (Optional) Run [**dhcp snooping alarm user-limit enable**](cmdqueryname=dhcp+snooping+alarm+user-limit+enable)
     
     The device is enabled to generate an alarm when the number of DHCP snooping users on the interface reaches the maximum.
  6. (Optional) Run [**dhcp snooping alarm user-limit threshold**](cmdqueryname=dhcp+snooping+alarm+user-limit+threshold) *threshold-value*
     
     The maximum number of DHCP snooping users is configured for the interface.
  7. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure the maximum number of DHCP snooping users for a BD.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     The BD view is displayed.
  3. Run [**dhcp snooping max-user-number**](cmdqueryname=dhcp+snooping+max-user-number) *max-user-number*
     
     The maximum number of DHCP snooping users is configured for the BD.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display dhcp snooping**](cmdqueryname=display+dhcp+snooping) { **interface** *interface-type* *interface-number* | **vlan** *vlan-id* [ **interface** *interface-type* *interface-number* ] | **bridge-domain** *bd-id* } command to check the maximum number of DHCP snooping users.