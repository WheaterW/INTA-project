Configuring the Proposal/Agreement Mechanism on an Interface
============================================================

Configuring the Proposal/Agreement Mechanism on an Interface

#### Context

The Proposal/Agreement mechanism implements rapid transition. Within this mechanism, there are two modes: enhanced mode and common mode.

When Huawei devices are connected to non-Huawei devices on a network running a spanning tree protocol, select the same Proposal/Agreement mode as that used on non-Huawei devices. If they use different Proposal/Agreement modes, they may fail to communicate with each other.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the interface to use the common Proposal/Agreement mechanism.
   
   
   ```
   [stp no-agreement-check](cmdqueryname=stp+no-agreement-check)
   ```
   
   
   
   By default, the interface uses the enhanced Proposal/Agreement mechanism.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

In the interface view, run the [**display this**](cmdqueryname=display+this) command to check its Proposal/Agreement mechanism mode.