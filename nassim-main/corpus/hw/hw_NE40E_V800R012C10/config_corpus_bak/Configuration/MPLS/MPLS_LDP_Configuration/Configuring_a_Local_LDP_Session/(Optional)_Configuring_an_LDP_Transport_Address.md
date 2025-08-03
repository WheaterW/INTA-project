(Optional) Configuring an LDP Transport Address
===============================================

Before establishing an LDP session, two LSRs confirm each other's LDP transport address and set up a TCP connection.

#### Context

An LDP transport address is used to set up a TCP connection between peers. A route to the LDP transport address must be reachable on each peer. An LSR ID, which is the loopback interface address, serves as the LDP transport address.![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The LDP sessions over multiple links between two LSRs can be established using the same pair of transport addresses.
* A change in an LDP transport address will terminate the associated LDP session. Exercise caution when configuring an LDP transport address.
* The default LDP transport address is recommended.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which an LDP session is to be established is displayed.
3. Run [**mpls ldp transport-address**](cmdqueryname=mpls+ldp+transport-address+interface) { *interface-type* *interface-number* | **interface** }
   
   
   
   The IP address of a specified interface is configured as an LDP transport address.
   
   
   
   * *interface-type* *interface-number*: specifies the type and number of an interface. This parameter configures LDP to use the address of the specified interface as the TCP transport address.
   * **interface**: configures LDP to use the IP address of the current interface as the TCP transport address.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.