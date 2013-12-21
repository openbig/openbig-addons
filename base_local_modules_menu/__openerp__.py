# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
#    Module base_apps_menu_invisible for OpenERP                                #
#    Copyrigt (C) 2013 OpenGLOBE Grzegorz Grzelak (www.openglobe.pl)            #
#                       and big-consulting GmbH (www.openbig.de)                #
#                                                                               #
#    This program is free software: you can redistribute it and/or modify       #
#    it under the terms of the GNU Affero General Public License as             #
#    published by the Free Software Foundation, either version 3 of the         #
#    License, or (at your option) any later version.                            #
#                                                                               #
#    This program is distributed in the hope that it will be useful,            #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#    GNU Affero General Public License for more details.                        #
#                                                                               #
#    You should have received a copy of the GNU Affero General Public License   #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                               #
#################################################################################
{
    'name': 'Modules Menu Reordering',
    'version': '0.02 (7.0)',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """The Module changes Modules menu to see Local Modules as first.
""",
    'author': 'Thorsten Vocks/Grzegorz Grzelak for OpenBIG.org',
    'website': 'http://www.openbig.org',
    'depends': ['base', 'mail'], 
    'data': [
#           'security/base_apps_security.xml',
           'base_modules_menu_order.xml',
#           'installer.xml',
    ],
    
    'js': [
        'static/src/js/announcement.js',
    ],
    'demo_xml': [],
    'installable': True,
    'auto_install': True,
#    'active': True,
    'application': False,
}

