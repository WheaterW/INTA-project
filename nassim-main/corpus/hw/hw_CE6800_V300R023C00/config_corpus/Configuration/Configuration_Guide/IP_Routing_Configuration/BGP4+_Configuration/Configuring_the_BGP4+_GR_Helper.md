Configuring the BGP4+ GR Helper
===============================

Configuring the BGP4+ GR Helper

#### Prerequisites

Before configuring the BGP4+ GR helper, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

When BGP4+ restarts, peer relationships are re-established and traffic forwarding is interrupted. Configuring Graceful restart (GR) can prevent such traffic interruptions.

BGP4+ GR needs to be enabled to prevent traffic interruptions in the event of BGP4+ restart. A GR restarter and its BGP4+ peer negotiate to establish a GR-capable BGP4+ session.

Configuring or disabling GR may delete and re-establish all sessions and instances.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Configure BGP4+ GR.
   
   
   ```
   [graceful-restart](cmdqueryname=graceful-restart)
   ```
   
   By default, BGP4+ GR is disabled.
4. (Optional) Set the wait time for EOR messages on the restarting speaker and receiving speaker.
   
   
   ```
   [graceful-restart timer wait-for-rib](cmdqueryname=graceful-restart+timer+wait-for-rib) time
   ```
   
   By default, the wait time for EOR messages is 600 seconds.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can adjust BGP4+ GR session parameter as required. However, using the default parameter values is recommended.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the BGP4+ GR helper, check the configurations.

* Run the [**display bgp**](cmdqueryname=display+bgp) **ipv6** [**peer**](cmdqueryname=peer) **verbose** command to check the BGP4+ GR status.
* Run the [**display bgp graceful-restart status**](cmdqueryname=display+bgp+graceful-restart+status) command to check BGP4+ speaker's GR information.