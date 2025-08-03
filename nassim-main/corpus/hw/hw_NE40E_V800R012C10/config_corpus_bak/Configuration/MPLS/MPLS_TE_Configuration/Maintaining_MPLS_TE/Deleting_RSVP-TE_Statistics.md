Deleting RSVP-TE Statistics
===========================

A reset command is used to delete RSVP-TE statistics.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

RSVP-TE statistics are deleted if you reset RSVP-TE statistics using the [**reset**](cmdqueryname=reset) command. Exercise caution when running the reset command.

To delete RSVP-TE statistics, run the [**reset**](cmdqueryname=reset) command in the user view.


#### Procedure

1. Run the [**reset mpls rsvp-te statistics**](cmdqueryname=reset+mpls+rsvp-te+statistics) { **global** | **interface** { *interface-type* *interface-number* | *interface-name* } } command in the user view to delete RSVP-TE statistics.