Monitoring the Running Status of IGMP
=====================================

Monitoring the Running Status of IGMP

#### Context

In routine maintenance, you can run the following commands in any view to check the running status of IGMP.


#### Procedure

* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message counters** [ **interface** *interface-type interface-number* ] [ **message-type** { **query** | **report** } ] command to check IGMP message statistics.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] [**invalid-packet**](cmdqueryname=invalid-packet) [ **interface** *interface-type interface-number* | **message-type** { **leave** | **query** | **report** } ]\* command to check statistics about invalid IGMP messages.
* Run the [**display igmp**](cmdqueryname=display+igmp) [**invalid-packet**](cmdqueryname=invalid-packet) [ *packet-number* ] **verbose** command to check detailed information about recently received invalid IGMP messages.