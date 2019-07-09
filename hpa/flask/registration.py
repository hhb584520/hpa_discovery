from flask import Flask, jsonify, request
from stevedore import extension

registration = Flask(__name__)

flavor = {
    "vcpus": 2,
    "ram": "2048",
    "disk": "2G",
    "swap": False,
    "OS-FLV-EXT-DATA:ephemeral": False
}

# Add cloud_extra_info in convert_vim_info
viminfo = {
    "createTime": "2017-04-01 02:22:27",
    "domain": "Default",
    "name": "TiS_R4",
    "password": "admin",
    "tenant": "admin",
    "type": "openstack",
    "url": "http://128.224.180.14:5000/v3",
    "userName": "admin",
    "vendor": "WindRiver",
    "version": "newton",
    "vimId": "windriver-hudson-dc_RegionOne",
    'cloud_owner': 'windriver-hudson-dc',
    'cloud_region_id': 'RegionOne',
    'cloud_extra_info': '{ \
        "ovsDpdk": { \
            "version": "v1", \
            "arch": "Intel64", \
            "libname": "dataProcessingAccelerationLibrary", \
            "libversion": "v12.1" \
        } \
    }',
    'insecure': 'True'
}

extraResp = {
    "aggregate_instance_extra_specs:sriov_nic": "sriov-nic-intel-8086-15b3-physnet-1:1",
    "capabilities:cpu_info:model": "Haswell"
}

hpa_capabilities = []

@registration.route('/hpa', methods=['GET'])
def get_hpa():
    print hpa_capabilities
    return jsonify({'hpa_capabilities': hpa_capabilities})

@registration.route('/hpa', methods=['POST'])
def create_hpa():

    def get_hpa_capabilities(ext, data):
        return (ext.name, ext.obj.get_hpa_capabilities(data))

    # call extension plugin start
    params = [flavor, extraResp, viminfo]
    mgr = extension.ExtensionManager(
        namespace='hpa.discovery',
        invoke_on_load=True,
    )
    results = mgr.map(get_hpa_capabilities, params)
    for name, value in results:
        for hpa_capability in value:
            hpa_capabilities.append(hpa_capability)

    return jsonify({'post': hpa_capabilities})

@registration.route('/hpa/<string:feature_name>', methods=['DELETE'])
def delete_hpa(feature_name):
    if len(feature_name) == 0:
        abort(404)
    for index in range(len(hpa_capabilities)):
        if hpa_capabilities[index]["hpa-feature"] == feature_name:
            del hpa_capabilities[index]
            break
    return jsonify({'result': True})

if __name__ == '__main__':
    registration.run()
