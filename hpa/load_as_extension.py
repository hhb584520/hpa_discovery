from __future__ import print_function

import argparse

from stevedore import extension


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--width',
        default=20,
        type=int,
        help='maximum output width for text',
    )
    parsed_args = parser.parse_args()

    flavor = ""
    extra_specs = {
        "aggregate_instance_extra_specs:storage": "local_image",
        "capabilities:cpu_info:model": "Haswell",
        "hw:cpu_policy": "dedicated",
        "hw:cpu_thread_policy": "prefer"
    }
    viminfo = ""
    data = [flavor, extra_specs, viminfo]

    mgr = extension.ExtensionManager(
        namespace='hpa.discovery',
        invoke_on_load=True,
        invoke_args=(parsed_args.width,),
    )

    def get_hpa_capabilities(ext, data):
        return (ext.name, ext.obj.get_hpa_capabilities(data))

    results = mgr.map(get_hpa_capabilities, data)
    for name, value in results:
        print(name)
        print(value)
