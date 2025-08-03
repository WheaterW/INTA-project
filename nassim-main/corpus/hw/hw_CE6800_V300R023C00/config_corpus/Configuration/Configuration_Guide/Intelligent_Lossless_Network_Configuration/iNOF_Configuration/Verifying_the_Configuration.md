Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display inof peer connection**](cmdqueryname=display+inof+peer+connection) command to check information about the iNOF connection established between the local and peer devices after the iNOF reflector function is configured.
* Run the [**display inof configuration zone**](cmdqueryname=display+inof+configuration+zone) [ *zone-name* ] [ **inconsistent** ] command to check the configuration of iNOF zones on the device.
* Run the [**display inof configuration host**](cmdqueryname=display+inof+configuration+host) [ **inconsistent** ] command to check the configuration of iNOF zone members.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The **inconsistent** parameter is used to display the zone member configuration that exists only on one iNOF reflector. If there are two reflectors on the iNOF network, you can run this command to check inconsistent zone configurations. If inconsistencies exist, you need to change the zone configurations on both reflectors to be the same.
* Run the [**display inof information host**](cmdqueryname=display+inof+information+host) [ **local** | **remote** | { *ip-address* | **ipv6-address** } ] command to check information about hosts managed by devices on the iNOF network.
* Run the [**display inof bfd session**](cmdqueryname=display+inof+bfd+session) command to check information about BFD sessions in the iNOF system.
* Run the [**display inof configuration status**](cmdqueryname=display+inof+configuration+status) command to check the configuration status on the iNOF network.
* Run the [**display inof rpfr connection information**](cmdqueryname=display+inof+rpfr+connection+information) command to check RoCE connection information of RPFR. (RPFR takes effect only on the following device models: CE6860-SAN, CE8850-SAN, CE6885-SAN.)
* Run the [**display inof rpfr history information**](cmdqueryname=display+inof+rpfr+history+information) [ **slot** *slot-id* ] command to check RoCE connection information of RPFR. (RPFR takes effect only on the following device models: CE6860-SAN, CE8850-SAN, CE6885-SAN.)