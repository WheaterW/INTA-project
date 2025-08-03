Configuring a BFD Session to Modify the PST
===========================================

Configuring a BFD Session to Modify the PST

#### Context

BFD for port state table (PST) associates a BFD session bound to an interface with the PST of this interface. When a link down event is detected, the BFD session modifies the interface status in the PST (modifying the corresponding bit value in the PST). Therefore, the underlying layer can learn whether the interface is faulty and switch the link according to the PST.

BFD for PST applies only to single-hop BFD sessions that are bound to outbound interfaces.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL in low latency mode does not support this function.



#### Prerequisites

Before configuring a BFD session to modify the PST, you have [configured single-hop BFD](vrp_bfd_cfg_0005.html).


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BFD session view.
   ```
   [bfd](cmdqueryname=bfd) session-name
   ```
3. Configure the BFD session to modify the PST.
   ```
   [process-pst](cmdqueryname=process-pst)
   ```
   
   By default, a BFD session does not modify the PST upon fault detection.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```