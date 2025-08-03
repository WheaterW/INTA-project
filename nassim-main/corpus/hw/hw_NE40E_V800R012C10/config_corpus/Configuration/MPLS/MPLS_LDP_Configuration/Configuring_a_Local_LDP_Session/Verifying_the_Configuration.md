Verifying the Configuration
===========================

After configuring a local MPLS LDP session, you can view information about interfaces with MPLS and MPLS LDP enabled, the LDP protocol, LDP session status, LDP adjacencies, and peers of the LDP session.

#### Prerequisites

The local MPLS LDP session has been established.


#### Procedure

* Run the [**display mpls ldp**](cmdqueryname=display+mpls+ldp+all+verbose) [ **all** ] [**verbose** ] command to check LDP information.
* Run the [**display mpls ldp interface**](cmdqueryname=display+mpls+ldp+interface+verbose+all) [ *interface-type* *interface-number* | **verbose** | **all** ] command to check information about LDP-enabled interfaces.
* Run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session+verbose+all) [ **verbose** | *peer-id* | **all** ] command to check the status of an LDP session.
* Run the [**display mpls ldp adjacency**](cmdqueryname=display+mpls+ldp+adjacency+interface+remote+peer+verbose) [ **interface** *interface-type* *interface-number* | **remote** ] [ **peer** *peer-id* ] [ **verbose** ] command to check information about LDP adjacencies.
* Run the [**display mpls ldp peer**](cmdqueryname=display+mpls+ldp+peer+verbose+all) [ **verbose** | *peer-id* | **all** ] command to check the peers of an LDP session.
* Run the [**display mpls interface**](cmdqueryname=display+mpls+interface+verbose) [ *interface-type* *interface-number* ] [ **verbose** ] command to check information about an MPLS-enabled interface.