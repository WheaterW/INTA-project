Verifying the Inter-VLAN Communication Configuration
====================================================

After inter-VLAN communication is configured, you can check whether users in different VLANs can communicate with each other and check information about VLANs to which users belong.

#### Prerequisites

The configurations of inter-VLAN communication are complete.


#### Procedure

* Run the [**ping**](cmdqueryname=ping) [ **ip** ] [ **-a** *source-ip-address* | **-c** *count* | **-d** | **-f** | **-h** *ttl-value* | **-i** *interface-type* *interface-number* | **-m** *time* | **-n** | **-p** *pattern* | **-q** | **-r** | **-s** *packetsize* | **-system-time** | **-t** *timeout* | **-tos** *tos-value* | **-v** | **-vpn-instance** *vpn-instance-name* ] \* *host* command to check whether users in different VLANs can communicate with each other.
  
  
  
  If the ping fails, you can run the following commands to locate the fault:
  
  + Run the [**display vlan**](cmdqueryname=display+vlan) [ *vlan-id* [ **verbose** ] ] command to check information about all VLANs or a specified VLAN.
  + Run the [**display interface**](cmdqueryname=display+interface) **vlanif** [ *vlan-id* ] command to check information about VLANIF interfaces.
    
    Before running this command, ensure that VLANIF interfaces have been configured.