(Optional) Configuring PCE to Calculate a Path Crossing Both the IP and Optical Layers
======================================================================================

A specific path calculation mode must be planned for a GMPLS UNI tunnel.

#### Context

The NE40E calculates a path for a GMPLS UNI tunnel in either of the following modes:

* Independent path calculation at IP and optical layers
* PCE path calculation for a path crossing the IP and optical layers

The independent path calculation mode is enabled by default. PCE path calculation can be configured to calculate a path crossing both the IP and optical layers.

#### Procedure

1. Configure the ingress EN to send a request to a PCE server to calculate a path crossing both the IP and optical layers.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      The MPLS view is displayed.
   3. Run [**mpls te pce**](cmdqueryname=mpls+te+pce+inter-layer+delegate) **inter-layer delegate**
      
      
      
      The ingress EN is configured to send a request to a PCE server to calculate a path crossing both the IP and optical layers.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. [Specifying Candidate PCE Servers for a PCE Client](dc_vrp_pcep_cfg_0004.html)
3. [(Optional) Configure PCEP session authentication.](dc_vrp_pcep_cfg_0005.html)
4. [(Optional) Configure timers for a PCE client.](dc_vrp_pcep_cfg_0006.html)