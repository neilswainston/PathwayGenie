'''
PathwayGenie (c) University of Manchester 2017

PathwayGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
# pylint: disable=invalid-name
import sys

from scripts.writer import write


def do_write(filename, ice_url, ice_username, ice_password,
             group_name=None):
    '''Write.'''
    comp_columns = ['part', 'vector']
    typ = 'PLASMID'
    write(filename, ice_url, ice_username, ice_password, typ, comp_columns,
          group_name)


def main(args):
    '''main method.'''
    do_write(*args)


if __name__ == '__main__':
    main(sys.argv[1:])
