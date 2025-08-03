Defining Traffic Behaviors
==========================

This section describes traffic behaviors and how to configure them.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
   
   
   
   A traffic behavior is defined and the traffic behavior view is displayed.
3. Run one of the following commands as required.
   
   
   * To allow packets to pass the device, run:
     
     ```
     [permit](cmdqueryname=permit)
     ```
   * To discard matched packets, run:
     
     ```
     [deny](cmdqueryname=deny)
     ```
   * To configure CAR actions, run:
     
     ```
     [car](cmdqueryname=car) { cir cir-value [ pir pir-value] } [ cbs cbs-value [ pbs pbs-value ] ] [ green { discard | pass [ remark dscp dscp-value | service-class class color color ] } | yellow { remark dscp dscp-value | discard | pass [ service-class class color color ] } | red { discard | pass [ remark dscp dscp-value | service-class class color color ] } ]* [ summary ] [ color-aware ] [ limit-type pps ]
     ```
   * To re-configure the IP precedence of an IP packet, run:
     
     ```
     [remark ip-precedence](cmdqueryname=remark+ip-precedence) ip-precedence
     ```
   * To re-configure the DSCP value of an IP packet, run:
     
     ```
     [remark dscp](cmdqueryname=remark+dscp) dscp-value
     ```
   * To re-configure the priority of an MPLS packet, run:
     
     ```
     [remark mpls-exp](cmdqueryname=remark+mpls-exp) exp
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**remark mpls-exp**](cmdqueryname=remark+mpls-exp) command can be applied to only upstream traffic on a device.
   * To configure the Class of Service (CoS) of packets, run:
     
     ```
     [service-class](cmdqueryname=service-class) service-class color color [ no-remark ]
     ```
   * To configure a load-balancing mode (per flow or per packet) of packets, run:
     
     ```
     [load-balance](cmdqueryname=load-balance) { flow | packet }
     ```
   * To configure redirecting of packets to a single next hop device, run:
     
     ```
     [redirect ip-nexthop](cmdqueryname=redirect+ip-nexthop) ip-address vpn vpn-instance-name
     ```
   * To redirect IP packets to a target LSP on the public network, run:
     
     ```
     [redirect lsp public](cmdqueryname=redirect+lsp+public) dest-ipv4-address [ nexthop-address | interface interface-type interface-number | secondary ]
     ```