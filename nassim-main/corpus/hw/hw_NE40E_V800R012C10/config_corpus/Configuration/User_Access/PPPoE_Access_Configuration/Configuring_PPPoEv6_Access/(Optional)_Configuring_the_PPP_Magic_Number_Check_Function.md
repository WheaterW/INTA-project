(Optional) Configuring the PPP Magic Number Check Function
==========================================================

You can configure the PPP magic number check function to
check whether a PPPoE user stays online after the user logs in.

#### Context

After a PPPoE user goes online, the device periodically
sends Echo Request packets to the user.

After receiving an Echo
Reply packet from the user, the device compares the magic number carried
in the packet with that learned during LCP negotiation. If the two
magic numbers are the same, the user is considered online. If they
are different, the user is considered offline.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ppp keepalive
   strict-check magic-number**](cmdqueryname=ppp+keepalive+strict-check+magic-number)
   
   
   
   The PPP magic number check function is enabled so that the
   device compares the magic number in a received Echo Reply packet with
   that learned during LCP negotiation.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.