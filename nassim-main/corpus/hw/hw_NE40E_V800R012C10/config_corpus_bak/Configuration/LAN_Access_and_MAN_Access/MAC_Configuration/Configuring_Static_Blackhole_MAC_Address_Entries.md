Configuring Static Blackhole MAC Address Entries
================================================

To protect a network against attacks using MAC addresses, configure static blackhole MAC address entries to discard packets with the specified destination MAC addresses.

#### Usage Scenario

To prevent invalid MAC address entries, such as those of unauthorized users, from occupying a MAC address table and prevent hackers from attacking user devices or networks using MAC addresses, configure the MAC addresses of untrusted users as blackhole MAC addresses to discard packets destined for such MAC addresses.


#### Pre-configuration Tasks

Before configuring static blackhole MAC address entries, connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mac-address blackhole**](cmdqueryname=mac-address+blackhole) *mac-address* **vlan** *vlan-id*
   
   
   
   A static blackhole MAC address entry is added.
3. Run [**mac-address blackhole**](cmdqueryname=mac-address+blackhole) *mac-address* **vsi** *vsi-name*
   
   
   
   A static blackhole MAC address entry is added.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following commands to check the previous configurations.

* Run the [**display mac-address**](cmdqueryname=display+mac-address) [ *mac-address* ] { [ **vlan** *vlan-id* ] | [ **vsi** *vsi-name* [ **ce-vlan** ] ] | [ **ce-vlan** ] } [ **verbose** ] command to check MAC address entries.
* Run the [**display mac-address blackhole**](cmdqueryname=display+mac-address+blackhole) { [ **vlan** *vlan-id* | **vsi** *vsi-name* ] } [ **verbose** ] command to check static blackhole MAC address entries.