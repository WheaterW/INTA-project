Enabling LDP-IGP Synchronization
================================

LDP-IGP synchronization needs to be enabled on interfaces on both ends of the link between the node where a primary LSP and a backup LSP diverge from each other and its LDP peer on the primary LSP. LDP-IGP synchronization can be enabled either on an interface or in an IGP process.

#### Context

LDP-IGP synchronization can be enabled in either of the following modes:

* Enable LDP-IGP synchronization in the interface view.
  
  LDP-IGP synchronization can be enabled on specified interfaces if a few interfaces need to support this function.
* Enable LDP-IGP synchronization in an IGP process.
  
  After LDP-IGP synchronization is enabled in an IGP process, it is automatically enabled on all interfaces in the process. If LDP is enabled on all IGP-enabled interfaces of a node, this configuration mode is recommended.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Choose one of the preceding modes as needed.




#### Procedure

* Enable LDP-IGP synchronization in the interface view.
  
  
  
  If OSPF is used, perform the following steps on the interfaces on both ends of the link between the node where the primary LSP and the backup LSP diverge from each other and its LDP peer on the primary LSP.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ospf ldp-sync**](cmdqueryname=ospf+ldp-sync)
     
     
     
     LDP-OSPF synchronization is enabled for the interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To enable LDP-OSPF synchronization on a multi-area adjacency interface, run the [**ospf ldp-sync**](cmdqueryname=ospf+ldp-sync+multi-area) **multi-area** *area-id* command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  If IS-IS is used, perform the following steps on the interfaces on both ends of the link between the node where the primary LSP and the backup LSP diverge from each other and its LDP peer on the primary LSP.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
     
     
     
     IS-IS is enabled on the interface.
  4. Run [**isis ldp-sync**](cmdqueryname=isis+ldp-sync)
     
     
     
     LDP-IS-IS synchronization is enabled on the interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  When LDP-IGP synchronization and LDP GTSM are configured on an interface, an LDP session needs to be established over a non-direct link. Therefore, the number of GTSM hops must be set based on the actual hop count and cannot be set to 1. If the number of GTSM hops is set to 1, the LDP session cannot be established. As a result, the route cannot be switched back or LDP-IGP synchronization fails.
* Enable LDP-IGP synchronization in an IGP process.
  
  
  
  If OSPF is used, perform the following steps on the node on which the primary LSP and the backup LSP diverge from each other and its LDP peer on the primary LSP:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF process is started, and the OSPF view is displayed.
     
     
     
     *process-id* specifies an OSPF process. If the *process-id* parameter is not specified, the default process ID 1 is used. To associate an OSPF process with a VPN instance and run OSPF in the VPN instance, run the [**ospf**](cmdqueryname=ospf+vpn-instance) [ *process-id* | **vpn-instance** *vpn-instance-name* ] \* command. If a VPN instance is specified, the OSPF process belongs to the specified instance. Otherwise, the OSPF process belongs to the global instance.
  3. Run [**area**](cmdqueryname=area) *area-id*
     
     
     
     The OSPF area view is displayed.
  4. Run [**ldp-sync enable**](cmdqueryname=ldp-sync+enable)
     
     
     
     LDP-OSPF synchronization is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  If IS-IS is used, perform the following steps on the node on which the primary LSP and the backup LSP diverge from each other and its LDP peer on the primary LSP:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The specified IS-IS process is started, and the IS-IS view is displayed.
     
     
     
     *process-id* specifies an IS-IS process ID. If the *process-id* parameter is not specified, the default process ID 1 is used. To associate an IS-IS process with a VPN instance, run the [**isis**](cmdqueryname=isis+vpn-instance) [ *process-id* ] [ **vpn-instance** *vpn-instance-name* ] command.
  3. Run [**ldp-sync enable**](cmdqueryname=ldp-sync+enable)
     
     
     
     LDP-IS-IS synchronization is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.