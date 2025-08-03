Adding a Port to a VLAN
=======================

Adding a port to a VLAN associates the port with the VLAN.

#### Context

* A port connecting a switch to a PC must be configured as an access or a hybrid port.
  
  The [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) command is invalid on access ports.
* A port connecting one switch to another must be configured as a trunk or hybrid port.
  
  The [**port default vlan**](cmdqueryname=port+default+vlan) command cannot be used on trunk ports.

#### Procedure

* For access ports or QinQ ports: 
  
  
  1. Run the [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id* command to add a port to a specified VLAN.
     
     To add ports to a VLAN in batches, run the [**port**](cmdqueryname=port) *porttype* { *portbegin* [ **to** *iportend* ] } &<1-10> command in the VLAN view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The input port format must be correct. The port number following **to** must be greater than the port number before **to**. If a group of ports are specified, ensure that these ports are of the same type and all specified ports exist.
     
     In one [**port**](cmdqueryname=port) command, a maximum of 10 groups of ports can be specified by using **to**.
  2. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* For trunk ports: 
  
  
  1. Run the [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** } command to add ports to specified VLANs.
  2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.