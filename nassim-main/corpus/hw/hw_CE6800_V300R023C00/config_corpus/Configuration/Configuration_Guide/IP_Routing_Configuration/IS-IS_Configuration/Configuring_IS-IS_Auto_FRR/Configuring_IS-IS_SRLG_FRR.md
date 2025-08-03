Configuring IS-IS SRLG FRR
==========================

Configuring IS-IS SRLG FRR

#### Prerequisites

Before configuring IS-IS SRLG FRR, you have completed the following task:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0012.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Add the interface to an SRLG.
   
   
   ```
   [isis srlg](cmdqueryname=isis+srlg) srlg-value
   ```
   
   By default, an interface is not added to any SRLG.
5. (Optional) Set the solution of selecting a backup path for IS-IS auto FRR to SRLG-disjoint path first.
   
   
   ```
   [quit](cmdqueryname=quit)
   [isis](cmdqueryname=isis) process-id
   [frr](cmdqueryname=frr)
   [loop-free-alternate](cmdqueryname=loop-free-alternate) [ level-1 | level-2 | level-1-2 ]
   [tiebreaker](cmdqueryname=tiebreaker) srlg-disjoint preference preference [ level-1 | level-2 | level-1-2 ]
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis**](cmdqueryname=display+isis) [ *process-id* ] **srlg** { *srlgGroupId* | **all** } command to check information about SRLGs.