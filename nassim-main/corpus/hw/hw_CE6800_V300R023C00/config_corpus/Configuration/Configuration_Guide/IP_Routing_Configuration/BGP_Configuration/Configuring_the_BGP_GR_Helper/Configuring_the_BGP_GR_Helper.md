Configuring the BGP GR Helper
=============================

Configuring the BGP GR Helper

#### Context

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
3. Configure BGP GR.
   
   
   ```
   [graceful-restart](cmdqueryname=graceful-restart)
   ```
   
   By default, BGP GR is disabled.
4. Configure the wait time for End-of-RIB messages on the restarting speaker and receiving speaker.
   
   
   ```
   [graceful-restart timer wait-for-rib](cmdqueryname=graceful-restart+timer+wait-for-rib) time
   ```
   
   By default, the wait time for End-of-RIB messages is 600 seconds.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can adjust the GR parameters of a BGP session as required. In normal cases, however, the default values are recommended.
5. (Optional) Configure the BGP device to reset the BGP connection in GR mode.
   
   
   ```
   [graceful-restart peer-reset](cmdqueryname=graceful-restart+peer-reset)
   ```
   
   Currently, BGP does not support dynamic capability negotiation. Therefore, a change in a BGP capability causes peer relationship re-establishment. If a BGP capability changes when BGP IPv4 unicast peer relationships have been established and IPv4 services are running properly, the BGP IPv4 unicast peer relationships will be reestablished, affecting the ongoing IPv4 services. To resolve this problem, run the **graceful-restart peer-reset** command to enable the BGP device to reset a BGP connection in GR mode.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the BGP GR helper, check the configurations.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) **verbose** command to check the BGP GR status.
* Run the [**display bgp graceful-restart status**](cmdqueryname=display+bgp+graceful-restart+status) command to check the BGP speaker's GR information.