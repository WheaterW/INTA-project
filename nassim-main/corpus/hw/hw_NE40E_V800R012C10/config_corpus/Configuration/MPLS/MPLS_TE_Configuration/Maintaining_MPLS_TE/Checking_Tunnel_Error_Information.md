Checking Tunnel Error Information
=================================

If an RSVP-TE tunnel interface is Down, run display commands to view information about faults.

#### Context

Run the [**display mpls te tunnel-interface last-error**](cmdqueryname=display+mpls+te+tunnel-interface+last-error) command on the ingress to check errors that occurred on the local node or errors in PathErr messages sent by the downstream node. The errors include:

* CSPF computation failures
* Errors that occurred when RSVP signaling was triggered
* Errors carried in received RSVP PathErr messages

This command shows the last five recorded errors that occurred on a TE tunnel.

#### Procedure

1. Run the [**display mpls te tunnel-interface last-error**](cmdqueryname=display+mpls+te+tunnel-interface+last-error) [ *tunnel-name* ] command to check error information on a tunnel interface.