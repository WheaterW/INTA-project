Configuration Validation
========================

Configuration Validation

#### Basic Operations

1. Construct the data to be configured, for example, the interface MTU. The corresponding XPath is /ifm/interfaces/interface.
   
   
   ```
   CREATE_INTERFACE = '''<config>
               <ifm xmlns="urn:huawei:yang:huawei-ifm">
                   <interfaces>
                     <interface>
                       <name></name>  
                       <mtu>1300</mtu>
                     </interface>
                   </interfaces>
                 </ifm>
   </config>'''
   ```
2. Deliver an <edit-config> message in which the value of <test-option> is set.
   
   
   ```
   rpc_obj = m.edit_config(target='candidate', config=CREATE_INTERFACE, test_option='set')
   _check_response(rpc_obj, 'CREATE_INTERFACE')
   ```
3. Deliver a validate message.
   
   
   ```
   m.validate(source="candidate")
   ```
   In the preceding example, "m" indicates the following:
   ```
   with huawei_connect(host, port=port, user=user, password=password) as m:
   ```

#### Example

This example shows how to configure a simple Python script to connect to the device and implement configuration.
```
# test_validate.py
import sys
import logging 
from ncclient import manager
from ncclient import operations

log = logging.getLogger(__name__)
CREATE_INTERFACE = '''<config>
                 <ifm xmlns="urn:huawei:yang:huawei-ifm">
                   <interfaces>
                     <interface>
                       <name>100GE1/0/1</name>
                       <mtu>1300</mtu>
                      </interface>
                    </interfaces>
                  </ifm>
                </config>'''

#Fill the device information and establish a NETCONF session
def huawei_connect(host, port, user, password):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           hostkey_verify = False,
                           device_params={'name': "huaweiyang"},
                           allow_agent = False,
                           look_for_keys = False)

def _check_response(rpc_obj, snippet_name):
    print("RPCReply for %s is %s" % (snippet_name, rpc_obj.xml))
    xml_str = rpc_obj.xml
    if "<ok/>" in xml_str:
        print("%s successful" % snippet_name)
    else:
        print("Cannot successfully execute: %s" % snippet_name)      

def test_validate(host, port, user, password):
    #1.Create a NETCONF session
    with huawei_connect(host, port=port, user=user, password=password) as m:

        #2.Send RPC and check RPC reply
        rpc_obj = m.edit_config(target='candidate', config=CREATE_INTERFACE, test_option='set')
        _check_response(rpc_obj, 'CREATE_INTERFACE')
  
        #validate check
        m.validate(source="candidate")
        m.commit()

if __name__ == '__main__':
    test_validate(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
```