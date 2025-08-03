Maintenance
===========

Maintenance

#### Basic Operations

1. Construct an RPC action message based on the corresponding data model. In this example, action is set to save configuration. The corresponding XPath is /save/filename.
   
   
   ```
   ACTION = '''<rpc message-id="{}" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
    <save xmlns="urn:huawei:yang:huawei-cfg">
       <filename>test.cfg</filename>
     </save>
   </rpc>'''
   ```
2. Deliver the action message.
   
   
   ```
   # Set the message-id for the rpc
   msgId = 1001
   ```
   ```
   rpc = ACTION.format(msgId)
   # Send RPC
   m._session.send(rpc)
   ```

#### Example

This example shows how to configure a simple Python program to connect to the device and implement maintenance.

```
# test_action.py
import sys
import logging
import time
from ncclient import manager
from ncclient import operations
log = logging.getLogger(__name__) 

ACTION = '''<rpc message-id="{}" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <save xmlns="urn:huawei:yang:huawei-cfg">
    <filename>test.cfg</filename>
  </save>
</rpc>'''

def test_action(host, port, user, password):
    #Fill the device information and establish a NETCONF session
    with manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           hostkey_verify = False,
                           device_params={'name': "huaweiyang"},
                           allow_agent = False,
                           look_for_keys = False) as m:

        #Set the message-id for the rpc
        msgId = 1001
        rpc = ACTION.format(msgId)
        #Send RPC
        m._session.send(rpc)
        time.sleep(2)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test_action(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
```