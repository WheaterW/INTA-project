Configuring TCP FlexBuffer
==========================

Configuring TCP FlexBuffer

#### Prerequisites

Before configuring TCP FlexBuffer, [configure differentiated flow scheduling](galaxy_ai_dpp_cfg_0013.html).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
3. Enter the mice-elephant-flow view.
   
   
   ```
   [mice-elephant-flow](cmdqueryname=mice-elephant-flow)
   ```
4. Enable TCP FlexBuffer.
   
   
   ```
   [flex-buffer enable](cmdqueryname=flex-buffer+enable)
   ```
   
   By default, TCP FlexBuffer is disabled.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
   
   When TCP FlexBuffer is enabled, you need to set the dynamic threshold of the queue-level service buffer for the elephant-flow queue on an interface to 9 using the **[**qos buffer queue**](cmdqueryname=qos+buffer+queue)** *queue-index* **shared-threshold dynamic** *dynamic-value* command.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **[**display flex-buffer state**](cmdqueryname=display+flex-buffer+state)** [ **interface** *interface-type interface-number* ] command to check the status of TCP FlexBuffer.