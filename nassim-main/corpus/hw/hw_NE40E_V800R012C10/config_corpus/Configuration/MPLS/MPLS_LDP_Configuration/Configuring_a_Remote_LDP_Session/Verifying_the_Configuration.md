Verifying the Configuration
===========================

After configuring a remote MPLS LDP session, you can view information about the LDP protocol, LDP session status, LDP adjacencies, and remote peers of the LDP session.

#### Prerequisites

A remote MPLS LDP session has been established.


#### Procedure

* Run the [**display mpls ldp**](cmdqueryname=display+mpls+ldp+all+verbose) [ **all** ] [ **verbose** ] command to check LDP information.
* Run one of the following commands to check the LDP session status:
  
  
  + [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session+verbose) [ **verbose** | *peer-id* ]
  + [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session+all+verbose) [ **all** ] [ **verbose** ]
* Run the [**display mpls ldp adjacency**](cmdqueryname=display+mpls+ldp+adjacency+interface+remote+peer+verbose) [ **interface** *interface-type* *interface-number* | **remote** ] [ **peer** *peer-id* ] [ **verbose** ] command to check information about LDP adjacencies.
* Run one of the following commands to check information about the peer of an LDP session:
  
  
  + [**display mpls ldp peer**](cmdqueryname=display+mpls+ldp+peer+verbose) [ **verbose** | *peer-id* ]
  + [**display mpls ldp peer**](cmdqueryname=display+mpls+ldp+peer+all+verbose) [ **all** ] [ **verbose** ]
* Run the [**display mpls ldp remote-peer**](cmdqueryname=display+mpls+ldp+remote-peer+peer-id) [ *remote-peer-name* | **peer-id** *peer-id* ] command to check information about the remote peer of an LDP session.