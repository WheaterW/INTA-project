Resetting LDP
=============

Resetting LDP makes new configurations take effect.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Resetting LDP affects the establishment of an LSP. Exercise caution when performing this operation.



#### Procedure

* To reset all LDP peers in global LDP instances, run the [**reset mpls ldp**](cmdqueryname=reset+mpls+ldp) command in the user view to make new configurations take effect.
* To reset a specified LDP peer, run the [**reset mpls ldp**](cmdqueryname=reset+mpls+ldp+peer) **peer** *peer-id* command in the user view to make new configurations take effect.
* To reset all GR-capable LDP peers in global LDP instances, run the [**reset mpls ldp**](cmdqueryname=reset+mpls+ldp+graceful) **graceful** command in the user view to make new configurations take effect, which implements uninterrupted service transmission during a restart.
* To reset a specified GR-capable LDP peer, run the [**reset mpls ldp**](cmdqueryname=reset+mpls+ldp+peer+graceful) **peer** *peer-id* **graceful** command in the user view to make new configurations take effect, which implements uninterrupted service transmission during a restart.