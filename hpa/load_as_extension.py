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

    data = {
        'a': 'A',
        'B': 'BBB',
        'long': 'word ' * 80,
    }

    mgr = extension.ExtensionManager(
        namespace='hpa_discovery.formatter',
        invoke_on_load=1,
        invoke_args=(parsed_args.width,),
    )

    def hformat_data(ext, data):
        return (ext.name, ext.obj.hformat(data))

    def tformat_data(ext, data):
        return (ext.name, ext.obj.tformat(data))

    arr_format = [hformat_data, tformat_data]    

    for index in range(len(arr_format)):
        results = mgr.map(arr_format[index], data)
        for name, result in results:
            print('Formatter: {0}'.format(name))
            for chunk in result:
                print(chunk, end='')
            print('')
